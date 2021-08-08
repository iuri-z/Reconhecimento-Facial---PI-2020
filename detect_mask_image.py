# USO
# python detect_mask_image.py --image images/pic1.jpeg

# importe os pacotes necessários
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import argparse
import cv2
import os
def mask_image():
	# construir o analisador de argumentos e analisar os argumentos
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--image", required=True,
		help="path to input image")
	ap.add_argument("-f", "--face", type=str,
		default="face_detector",
		help="path to face detector model directory")
	ap.add_argument("-m", "--model", type=str,
		default="mask_detector.model",
		help="path to trained face mask detector model")
	ap.add_argument("-c", "--confidence", type=float, default=0.5,
		help="minimum probability to filter weak detections")
	args = vars(ap.parse_args())

	# carregar nosso modelo de detector facial serializado do disco
	print("[INFO] loading face detector model...")
	prototxtPath = os.path.sep.join([args["face"], "deploy.prototxt"])
	weightsPath = os.path.sep.join([args["face"],
		"res10_300x300_ssd_iter_140000.caffemodel"])
	net = cv2.dnn.readNet(prototxtPath, weightsPath)

	# carregar o modelo do detector de máscara facial do disco
	print("[INFO] loading face mask detector model...")
	model = load_model(args["model"])

	# carregue a imagem de entrada do disco, clone-a e pegue a imagem espacial
	# dimensões
	image = cv2.imread(args["image"])
	orig = image.copy()
	(h, w) = image.shape[:2]

	# construir um blob a partir da imagem
	blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300),
		(104.0, 177.0, 123.0))

	# passe o blob pela rede e obtenha as detecções de rosto
	print("[INFO] computing face detections...")
	net.setInput(blob)
	detections = net.forward()

	# fazer um loop sobre as detecções
	for i in range(0, detections.shape[2]):
		# extrair a confiança (i.e, probabilidade) associada com
		# a detecção
		confidence = detections[0, 0, i, 2]

		# filtre as detecções fracas, garantindo que a confiança é
		# maior do que a confiança mínima
		if confidence > args["confidence"]:
			# calcule as coordenadas (x, y) da caixa delimitadora para
			# o objeto
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")

			# certifique-se de que as caixas delimitadoras estejam dentro das dimensões de
			# a moldura
			(startX, startY) = (max(0, startX), max(0, startY))
			(endX, endY) = (min(w - 1, endX), min(h - 1, endY))

			# extrair o ROI do rosto, convertê-lo do canal BGR para RGB
			# ordenação, redimensione-o para 224x224 e pré-processe-o
			face = image[startY:endY, startX:endX]
			face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
			face = cv2.resize(face, (224, 224))
			face = img_to_array(face)
			face = preprocess_input(face)
			face = np.expand_dims(face, axis=0)

			# passe o rosto pelo modelo para determinar se o rosto
			# tem uma máscara ou não
			(mask, withoutMask) = model.predict(face)[0]

			# determina o rótulo da classe e a cor que usaremos para desenhar
			# a caixa delimitadora e o texto
			label = "Mask" if mask > withoutMask else "No Mask"
			color = (0, 255, 0) if label == "Mask" else (0, 0, 255)

			# inclui a probabilidade no rótulo
			label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

			# exibe o rótulo e o retângulo da caixa delimitadora na saída
			# quadro
			cv2.putText(image, label, (startX, startY - 10),
				cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
			cv2.rectangle(image, (startX, startY), (endX, endY), color, 2)

	# mostra a imagem de saída
	cv2.imshow("Output", image)
	cv2.waitKey(0)
	
if __name__ == "__main__":
	mask_image()
