# Import necessary libraries
import os
import librosa
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras import models, layers, optimizers
from tensorflow.keras.utils import to_categorical

# Function to extract features from audio files
def extract_features(file_path):
    try:
        audio, _ = librosa.load(file_path, res_type='kaiser_fast')
        mfccs = librosa.feature.mfcc(y=audio, sr=22050, n_mfcc=13)
        return np.mean(mfccs.T, axis=0)
    except Exception as e:
        print(f"Error while processing {file_path}: {e}")
        return None

# Function to create the dataset using GTZAN dataset
def create_gtzan_dataset(data_path):
    X, y = [], []

    genres = os.listdir(data_path)
    for genre_label, genre_name in enumerate(genres):
        genre_path = os.path.join(data_path, genre_name)
        for filename in os.listdir(genre_path):
            file_path = os.path.join(genre_path, filename)
            features = extract_features(file_path)
            if features is not None:
                X.append(features)
                y.append(genre_label)

    return np.array(X), np.array(y)

# Load and preprocess the GTZAN dataset
gtzan_data_path = "C:\\Users\\ionut\Downloads\\archive\\Data\\genres_original"  # Replace with the actual path to GTZAN dataset
X, y = create_gtzan_dataset(gtzan_data_path)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert labels to categorical format
num_classes = len(np.unique(y))
y_train = to_categorical(y_train, num_classes=num_classes)
y_test = to_categorical(y_test, num_classes=num_classes)

# # Build a simple neural network model
# model = models.Sequential()
# model.add(layers.Dense(256, activation='relu', input_shape=(X_train.shape[1],)))
# model.add(layers.Dropout(0.5))
# model.add(layers.Dense(128, activation='relu'))
# model.add(layers.Dropout(0.5))
# model.add(layers.Dense(num_classes, activation='softmax'))
#
# # Compile the model
# model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
#
# # Train the model
# model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))
#
# # Evaluate the model
# loss, accuracy = model.evaluate(X_test, y_test)
# print(f"Test Loss: {loss}, Test Accuracy: {accuracy}")


model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(X_train.shape[1],)))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(num_classes, activation='softmax'))

# Compile the model with a potentially lower learning rate
model.compile(optimizer=optimizers.Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model with a potentially larger number of epochs
model.fit(X_train, y_train, epochs=200, batch_size=32, validation_data=(X_test, y_test))

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Loss: {loss}, Test Accuracy: {accuracy}")

#Save the trained model
model.save("music_genre_classifier.h5")