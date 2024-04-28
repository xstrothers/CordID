import os
import sys
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
import numpy as np

#D:\Python\CableID\cable_photos\HDMI\IMG_2053.JPG
def predict_class(img_path):
    # Step 1: Load the pre-trained model
    model = load_model('model.keras')  # Load your pre-trained model

    # Step 2: Load and preprocess the image
    img = image.load_img(img_path, target_size=(225, 225))  # Resize image to match model input size
    x = image.img_to_array(img)  # Convert image to numpy array
    x = np.expand_dims(x, axis=0)  # Add batch dimension
    x = preprocess_input(x)  # Preprocess the input data

    # Step 3: Use the loaded model to make predictions
    predictions = model.predict(x, verbose=0)  # Make predictions
    class_names = ['AUDIO', 'ELECTRICAL', 'ETHERNET', 'HDMI',  'USB A', 'USB C']

    # Assuming predictions is a 2D array with shape (1, num_classes)
    predicted_class_index = np.argmax(predictions, axis=1)[0]  # Get the index of the class with the highest probability
    predicted_class_label = class_names[predicted_class_index]  # Map the class index to the class name
    print(predicted_class_label)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <image_path>")
        sys.exit(1)

    img_path = sys.argv[1]
    predict_class(img_path)
