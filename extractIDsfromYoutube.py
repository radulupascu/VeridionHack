import re

def extract_video_id(youtube_link):
    # Use regex to find the video ID
    match = re.search(r'(?<=v=)[^&]+', youtube_link)
    if match:
        return match.group(0)
    else:
        return None

def read_links_from_file(file_path):
    with open(file_path, 'r') as file:
        links = file.readlines()
    return [link.strip() for link in links]

def save_video_ids_to_file(video_ids, file_path):
    with open(file_path, 'w') as file:
        for video_id in video_ids:
            file.write(video_id + '\n')

# Replace 'pop_links.txt' with the actual file name
file_name = '../pop_links'

# Read links from the file
youtube_links = read_links_from_file(file_name)

# Extract video IDs
video_ids = [extract_video_id(link) for link in youtube_links]

# Save video IDs to a separate file
output_file = 'song_ids.txt'
save_video_ids_to_file(video_ids, output_file)

# Display the extracted video IDs
print("Extracted Video IDs:")
print(video_ids)
print(f"Video IDs saved to {output_file}")
