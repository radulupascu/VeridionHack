import librosa
import json
import numpy as np

def analyze_audio(file_path):
    # Load the audio file
    y, sr = librosa.load(file_path)

    # Extract features
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr).mean()
    rmse = librosa.feature.rms(y=y).mean()
    spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr).mean()

    # Convert NumPy types to native Python types for JSON serialization
    audio_features = {
        "tempo": float(tempo),
        "chroma_stft": float(chroma_stft),
        "rmse": float(rmse),
        "spectral_centroid": float(spec_cent)
    }

    return audio_features

def main():
    file_path = 'audio/Y2meta.app - Wilian Lee - Sultans of Swing [HD] (128 kbps).mp3'  # Replace with your audio file path
    features = analyze_audio(file_path)
    json_data = json.dumps(features, indent=4)
    print(json_data)

if __name__ == "__main__":
    main()
