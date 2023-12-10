# prediction_script.py

from tensorflow.keras.models import load_model
import librosa
import numpy as np

# Load the saved model
loaded_model = load_model("music_genre_classifier.h5")

# Function to extract features from audio files
def extract_features(file_path):
    try:
        audio, _ = librosa.load(file_path, res_type='kaiser_fast')
        mfccs = librosa.feature.mfcc(y=audio, sr=22050, n_mfcc=13)
        return np.mean(mfccs.T, axis=0)
    except Exception as e:
        print(f"Error while processing {file_path}: {e}")
        return None

# Function to predict the genre of a song
def predict_genre(file_path):
    features = extract_features(file_path)
    if features is not None:
        # Reshape the features to match the input shape of the model
        features = np.reshape(features, (1, features.shape[0]))

        # Make the prediction
        prediction = loaded_model.predict(features)

        # Get the predicted genre label
        predicted_genre_label = np.argmax(prediction)

        # Map the label to the genre name
        genre_mapping = {0: 'hiphop', 1: 'rock', 2: 'pop'}
        predicted_genre = genre_mapping[predicted_genre_label]

        return predicted_genre
    else:
        return None

# Example usage
file_to_predict = "../rock.00088.wav"
predicted_genre = predict_genre(file_to_predict)

if predicted_genre is not None:
    print(f"The predicted genre for the input song is: {predicted_genre}")
