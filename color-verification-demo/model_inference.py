import tensorflow as tf

# Load your trained model
model = tf.keras.models.load_model('model.h5')

def predict(image_path):
    # Preprocess the image
    img = tf.keras.utils.load_img(image_path, target_size=(224, 224))
    img_array = tf.keras.utils.img_to_array(img) / 255.0
    img_array = tf.expand_dims(img_array, axis=0)

    # Make predictions
    predictions = model.predict(img_array)
    accuracy = predictions[0][0]  # Adjust based on your model's output
    return accuracy
