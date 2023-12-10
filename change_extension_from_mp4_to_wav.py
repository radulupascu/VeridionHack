import os

audio_folder = 'C:\\Users\\ionut\\Desktop\\hackathon_veridion\\audio'

for filename in os.listdir(audio_folder):
    if filename.endswith('.mp4'):
        # Construct new .wav filename
        new_filename = os.path.splitext(filename)[0] + '.wav'

        # Construct full file paths
        old_filepath = os.path.join(audio_folder, filename)
        new_filepath = os.path.join(audio_folder, new_filename)

        # Rename the file
        os.rename(old_filepath, new_filepath)

        print(f"Renamed: {filename} -> {new_filename}")
