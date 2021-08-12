# USAGE
# python detect_mask_video.py

# importando os pacotes necessarios
# keras eh a biblioteca de rede neural aliada ao tensorflow
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input # suporta entrada de imagens de dimensao >=32x32
from tensorflow.keras.preprocessing.image import img_to_array # transforma uma imagem PIL em um array numpy de float32
from tensorflow.keras.models import load_model # irah servir para treinar os modelos de mascara
from imutils.video import VideoStream # suporta entrada de transmissao do video 
import numpy as np # biblioteca que realiza calculos em arrays multidimensionais
import alerta_sonoro # classe criada para chamar funcoes relacionadas ao alerta
import argparse # usado para facilitar a interacao com a interface command-line
import imutils # permite executar funcoes basicas de processamento de imagem 
import time # usado para o comando sleep
import cv2 # open cv, para visao computacional
import os # modulo usado para ter acesso a informacoes do sistema operacional da maquina

def detect_and_predict_mask(frame, faceNet, maskNet):
	# coleta as dimensões do fram e constroi um blob a partir disso
	(h, w) = frame.shape[:2]	#altura e largura, respectivamente, em pixels
	blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0))

	# passa o blob pela rede e obtem a detecção facial
	faceNet.setInput(blob)
	detections = faceNet.forward()

	# inicializa as listas de rostos, suas localizacoes correspondentes
	# e a lista de previsões da nossa rede de máscara
	faces = []
	locs = []
	preds = []

	# loop sobre as detecções
	for i in range(0, detections.shape[2]):
		# extrai a confiança (ou seja, probabilidade) associada com
                # a detecção
		confidence = detections[0, 0, i, 2]

		# filtre as detecções fracas, isso garante que o programa consiga detectar o rosto da pessoa
		if confidence > args["confidence"]:
			# calcule as coordenadas (x, y) do retângulo verde/vermelho presente no programa
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")

			# faz com que o retângulo sempre esteja dentro das margens da tela
			(startX, startY) = (max(0, startX), max(0, startY))
			(endX, endY) = (min(w - 1, endX), min(h - 1, endY))

			# extrai o ROI do rosto, converte ele do canal BGR para RGB, encaminha, redimensiona a imagem para 224x224 e faz o pré-processamento
			face = frame[startY:endY, startX:endX]
			face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
			face = cv2.resize(face, (224, 224))
			face = img_to_array(face)
			face = preprocess_input(face)

			# adicione a faces e o retângulos a suas respectivas listas
			faces.append(face)
			locs.append((startX, startY, endX, endY))

	# faz a previsao apenas se pelo menos um rosto for detectado
	if len(faces) > 0:
		# para uma inferência mais rápida, faremos previsões em lote em * todos *
		# faces ao mesmo tempo, em vez de previsões uma a uma
		# no loop `for` acima
		faces = np.array(faces, dtype="float32")
		preds = maskNet.predict(faces, batch_size=32)

	# retorna uma 2-tuple das localizações das faces e suas localizações correspondentes
	return (locs, preds)

# constrói o analisador de argumentos e analisa os argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", type=str,
	default="face_detector",
	help="path to face detector model directory")
ap.add_argument("-m", "--model", type=str,
	default="mask_detector.model",
	help="path to trained face mask detector model")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
	help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

# carregue nosso modelo de detector facial serializado do disco
print("[INFO] loading face detector model...")
prototxtPath = os.path.sep.join([args["face"], "deploy.prototxt"])
weightsPath = os.path.sep.join([args["face"],
	"res10_300x300_ssd_iter_140000.caffemodel"])
faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

# carregue o modelo do detector de máscara facial do disco
print("[INFO] loading face mask detector model...")
maskNet = load_model(args["model"])

# inicializar o stream de vídeo e permitir que o sensor da câmera aqueça
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

# Variavel auxiliar para congelar o tempo
congelaTempo = False

# faz um loop sobre os frames do stream de vídeo
while True:

	# Mecanismo para adicionar o tempo entre cada alerta sonoro
	if not congelaTempo:
		# O alerta ocorre a cada três segundos
		tempo = time.time() + 3
		congelaTempo = True

	# pegue o frame do stream de vídeo redimensione-o para ter uma largura máxima de 720 pixels
	frame = vs.read()
	frame = imutils.resize(frame, width=720)

	# detecta rostos no enquadramento e determina se eles estão usando uma máscara facial ou não
	(locs, preds) = detect_and_predict_mask(frame, faceNet, maskNet)

	# loop nos locais de rosto detectados e seus locais correspondentes	
	for (box, pred) in zip(locs, preds):
		# desempacota o retângulo e a predictions
		(startX, startY, endX, endY) = box
		(mask, withoutMask) = pred
		
		# determina qual label e cor será apresentada
		# caso a pessoa esteja de máscara o retângulo será verde e a mensagem será "Mask"
		# caso a pessoa não estaja de máscara o retângulo será vermelho e mensagem será "No mask"
		label = "Mask" if mask > withoutMask else "No Mask"
		color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
		
		# chama a biblioteca time
		tempoAtual = time.time()
		
		# Implementando o alerta sonoro
		if label == "Mask" and tempoAtual > tempo: 
			alerta_sonoro.getAlerta()
			congelaTempo = False
		
		# inclui a probabilidade de acerto no label "Mask" ou "No mask"
		label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

		# exibe o label e o retângulo no frame
		cv2.putText(frame, label, (startX, startY - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
		cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)

	# mostra o frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# se a tecla "q" foi pressionada, o loop acaba
	if key == ord("q"):
		break
	
# fecha o programa
cv2.destroyAllWindows()
vs.stop()
