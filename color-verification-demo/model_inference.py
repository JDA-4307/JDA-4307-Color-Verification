import tensorflow as tf
import numpy as np
import zipfile
import os

COMPRESSED_MODEL_PATH = "color_detection_model.zip"  
EXTRACTED_MODEL_PATH = "color_detection_model.h5"  

COLOR_LABELS = ["Medium Cherry", "Desert Oak", "Graphite Walnut"]

def unzip_model(zip_path, output_path):
    """
    Unzips the model file if it hasn't been extracted yet.
    
    Args:
        zip_path (str): Path to the ZIP file.
        output_path (str): Path where the model should be extracted.
    """
    if not os.path.exists(output_path):  
        print(f"Extracting model from {zip_path}...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(".")  
        print(f"Model extracted to {output_path}")
    else:
        print(f"Model already extracted at {output_path}")


unzip_model(COMPRESSED_MODEL_PATH, EXTRACTED_MODEL_PATH)

print("Loading model...")
model = tf.keras.models.load_model(EXTRACTED_MODEL_PATH)
print("Model loaded successfully!")

def predict(image_path):
    """
    Predict the color label for the given image.
    
    Args:
        image_path (str): Path to the image file.
    
    Returns:
        str: Predicted color label.
    """
    img = tf.keras.utils.load_img(image_path, target_size=(224, 224))
    img_array = tf.keras.utils.img_to_array(img) / 255.0
    img_array = tf.expand_dims(img_array, axis=0)


    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions[0])  
    predicted_color = COLOR_LABELS[predicted_index]
    return predicted_color

