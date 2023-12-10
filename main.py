import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
from model import predict_genre

def record_audio(duration=30, fs=44100, filename='output.wav'):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
    sd.wait()  # Wait until recording is finished
    print("Recording finished, saving file...")
    write(filename, fs, np.int16(audio * 32767))  # Convert to 16-bit data and save as WAV file
    print(f"File saved as {filename}")

def model_response_final(audio_duration=30, record=True):
  # Record a 30-second audio clip and save it as output.wav
  if record:
    record_audio(duration=audio_duration)
  try:
    audio = "output.wav"
  except:
    pass
  result = predict_genre(audio, audio_duration=audio_duration)

  title = result[0]['label']

  # Assuming result is a list of dictionaries with 'label' keys
  result = [{'label': result[0]['label']}, {'label': result[1]['label']}, {'label': result[2]['label']}]

  # Extracting the first part before the "-" and creating a list
  out_l = [result[0]['label'].split("-", 1)[0], result[1]['label'].split("-", 1)[0], result[2]['label'].split("-", 1)[0]]
  
  # Creating a set to hold unique values
  out = set(out_l)
  out = list(out)

  # for genre in out:
  #   print(f"Predicted genre: ** {genre} **")

  return [title, out]
