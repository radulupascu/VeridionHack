import librosa
import numpy as np

import numpy as np
import librosa

def convert_audio_to_array(file_path, target_duration=30, sr=16000):
    """
    Convert an MP3 file to a NumPy array of shape (30*16000).

    Parameters:
    file_path (str): Path to the MP3 file.
    target_duration (int): Duration of the audio clip in seconds. Default is 30 seconds.
    sr (int): Target sampling rate. Default is 16000 Hz.

    Returns:
    np.ndarray: A NumPy array representing the audio file.
    """

    # Load the audio file and resample it to the target sampling rate
    audio, _ = librosa.load(file_path, sr=sr)

    # Calculate the target number of samples
    target_samples = target_duration * sr

    # If the audio is shorter than the target duration, pad it with zeros
    if len(audio) < target_samples:
        padding = target_samples - len(audio)
        audio = np.pad(audio, (0, padding), mode='constant')
    # If the audio is longer, truncate it to the target duration
    else:
        audio = audio[:target_samples]

    return audio

if __name__ == '__main__':
    # Example usage
    file_path = 'path_to_your_audio_file.wav'  # Replace with your audio file path
    audio_array = convert_audio_to_array(file_path)
    print(audio_array)
