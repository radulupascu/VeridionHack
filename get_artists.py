import openai

def get_gpt_response_content(user_message):
  # Get GPT responses to messages
  response = openai.ChatCompletion.create(
    model = "gpt-4",
    messages = 
      user_message
  )
  return response["choices"][0]["message"]["content"]

def parse_gpt_response(response):
  # Parse GPT response
  response = response.strip("\n").strip()
  return response

def get_artists(genre, labels):
    openai.api_key = "API_KEY"

    print(labels)

    chat_log = []
    chat_log.append({"role": "system", "content": 
                       f"Analyze this list of {genre} artists from {labels} and rank them based on popularity: \n"})

    response = get_gpt_response_content(chat_log)

    print(parse_gpt_response(response)) # Replace with output on website
    chat_log.append({"role": "assistant",
                    "content": response.strip("\n").strip()})

    # Split the response into lines and take the first five lines
    top_five_artists = response.choices[0].text.strip().split('\n')[:5]

    # Remove numbers and extra spaces from each artist's name
    artists = [artist.split('. ', 1)[-1].strip() for artist in top_five_artists]

    return artists

# Example usage
# print(get_artists("Hip-Hop", "Some Label"))
