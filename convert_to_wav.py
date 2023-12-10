import os
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError


def convert_mp4_to_wav(mp4_file, output_folder='wav_files'):
    try:
        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Load MP4 file
        audio = AudioSegment.from_file(mp4_file, format='mp4')

        # Remove invalid characters from the output file name
        output_file_name = os.path.splitext(os.path.basename(mp4_file))[0]
        output_file_name = ''.join(char for char in output_file_name if char.isalnum() or char in (' ', '_', '-'))

        # Define the output WAV file path
        wav_file = os.path.join(output_folder, output_file_name + '.wav')

        # Export as WAV
        audio.export(wav_file, format='wav')

        print(f"Conversion completed: {wav_file}")

    except CouldntDecodeError:
        print(f"Could not decode {mp4_file}. Skipping.")
    except Exception as e:
        print(f"Error: {e}")


# Print the current working directory
print("Current Working Directory:", os.getcwd())

# Set the input folder where the MP4 files are located
input_folder = 'C:\\Users\\ionut\\Desktop\\hackathon_veridion\\audio'

# Iterate over all files in the input folder
for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.lower().endswith('.mp4'):
            mp4_file_path = os.path.join(root, file)
            # Enclose file path in double-quotes to handle spaces
            convert_mp4_to_wav(f'"{mp4_file_path}"')
