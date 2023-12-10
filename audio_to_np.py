import librosa
import numpy as np

import numpy as np
import librosa

def convert_audio_to_array(file_path, target_duration=30, sr=16000):
    #resample
    audio, _ = librosa.load(file_path, sr=sr)

    target_samples = target_duration * sr

    # pad for shorter audio
    if len(audio) < target_samples:
        padding = target_samples - len(audio)
        audio = np.pad(audio, (0, padding), mode='constant')
    else:
        # truncate if longer
        audio = audio[:target_samples]

    return audio

if __name__ == '__main__':
    file_path = 'path_to_your_audio_file.wav'  
    audio_array = convert_audio_to_array(file_path)
    print(audio_array)
