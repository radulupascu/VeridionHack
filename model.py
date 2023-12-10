import numpy as np
from transformers import pipeline
from audio_to_np import convert_audio_to_array

def predict_genre(audio, audio_duration=30):
  audio = convert_audio_to_array(audio, target_duration=audio_duration)
  model = "mtg-upf/discogs-maest-30s-pw-73e-ts"
  pipe = pipeline("audio-classification", model=model, trust_remote_code=True)
  result = pipe(audio)
  return result

if __name__ == '__main__':
  audio = np.random.randn(30 * 16000)
  model = "mtg-upf/discogs-maest-30s-pw-73e-ts"
  pipe = pipeline("audio-classification", model=model, trust_remote_code=True)
  result = pipe(audio)
  print(result)