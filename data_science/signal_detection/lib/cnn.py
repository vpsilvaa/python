import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time
import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split

# Função para treinar e salvar o modelo
def treinar_modelo():
    diretorio = 'images'
    imagens = []
    rotulos = []

    for letra in os.listdir(diretorio):
        if os.path.isdir(os.path.join(diretorio, letra)):
            for imagem_nome in os.listdir(os.path.join(diretorio, letra)):
                imagem_path = os.path.join(diretorio, letra, imagem_nome)
                imagem = cv2.imread(imagem_path)
                imagem = cv2.resize(imagem, (300, 300))
                imagens.append(imagem)
                rotulos.append(letra)

    dados = pd.DataFrame({'Imagem': imagens, 'Label': rotulos})
    print(dados)

    label_encoder = LabelEncoder()
    dados['Label'] = label_encoder.fit_transform(dados['Label'])

    train_data, test_data = train_test_split(dados, test_size=0.25, random_state=42)
    print("Tamanho dos dados de treinamento:", len(train_data))
    print("Tamanho dos dados de teste:", len(test_data))
    train_images = np.array(train_data['Imagem'].tolist())
    train_labels = np.array(train_data['Label'].tolist())
    test_images = np.array(test_data['Imagem'].tolist())
    test_labels = np.array(test_data['Label'].tolist())

    train_images = train_images / 255.0
    test_images = test_images / 255.0

    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(300, 300, 3)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(512, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(26, activation='softmax')
    ])

    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    history = model.fit(train_images, train_labels, epochs=30, 
                        validation_data=(test_images, test_labels))

    test_loss, test_acc = model.evaluate(test_images, test_labels)
    print("Acurácia do modelo:", test_acc)

    # Salvar o modelo treinado
    model.save('model_att.h5')

# Função para carregar o modelo e fazer o teste
def testar_modelo():
    # Carregar o modelo salvo
    model = tf.keras.models.load_model('model_att.h5')

    cap = cv2.VideoCapture(0)
    detector = HandDetector(maxHands=1)
    offset = 20
    imgSize = 300

    def preprocess_image(image):
        resized_image = cv2.resize(image, (imgSize, imgSize))
        normalized_image = resized_image / 255.0
        return normalized_image

    label_encoder = LabelEncoder()
    labels = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    label_encoder.fit(labels)
    
    while True:
        success, img = cap.read()
        if not success:
            break
        imgOutput = img.copy()
        hands, img = detector.findHands(img)
        if hands:
            hand = hands[0]
            x, y, w, h = hand['bbox']
            imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
            imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
            imgCropShape = imgCrop.shape
            aspectRatio = h / w

            if aspectRatio > 1:
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                wGap = math.ceil((imgSize - wCal) / 2)
                imgWhite[:, wGap:wCal + wGap] = imgResize
            else:
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                hGap = math.ceil((imgSize - hCal) / 2)
                imgWhite[hGap:hCal + hGap, :] = imgResize

            processed_img = preprocess_image(imgWhite)
            predictions = model.predict(np.expand_dims(processed_img, axis=0))
            index = np.argmax(predictions)
            predicted_letter = label_encoder.inverse_transform([index])[0]

            cv2.rectangle(imgOutput, (x - offset, y - offset - 50),
                          (x - offset + 90, y - offset - 50 + 50), (255, 0, 255), cv2.FILLED)
            cv2.putText(imgOutput, predicted_letter, (x, y - 26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
            cv2.rectangle(imgOutput, (x - offset, y - offset),
                          (x + w + offset, y + h + offset), (255, 0, 255), 4)
            cv2.imshow("ImageWhite", imgWhite)
        cv2.imshow("Image", imgOutput)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

#treinar_modelo()
testar_modelo()
