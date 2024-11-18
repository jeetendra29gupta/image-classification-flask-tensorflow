import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

model = MobileNetV2(weights='imagenet')


def prepare_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array


def classify_image(img_path):
    img_array = prepare_image(img_path)
    predictions = model.predict(img_array)
    decoded_preds = decode_predictions(predictions, top=3)[0]

    return decoded_preds
