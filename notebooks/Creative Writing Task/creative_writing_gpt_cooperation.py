from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

final_descriptions = []

for _ in range(5):
    client_1 = OpenAI(api_key="INSERT API KEY HERE")
    client_2 = OpenAI(api_key="INSERT API KEY HERE")

    user_prompt = ("Create a five-sentence description of a piece of art (e.g., painting, photograph) titled: Human "
                   "nature")
    num_iterations = 10

    reminder_prompt = ("Make the description more creative. Don't add more sentences, you should stick to five "
                       "sentences")

    current_prompt = user_prompt

    for i in range(num_iterations):
        completion_1 = client_1.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            temperature=0.9,
            max_tokens=3000,
            messages=[
                {"role": "system", "content": ""},
                {"role": "user", "content": current_prompt},
            ]
        )
        response_1 = completion_1.choices[0].message.content

        completion_2 = client_2.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=3000,
            temperature=0.9,
            system=user_prompt,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": reminder_prompt + response_1
                        }
                    ]
                }
            ]
        )
        response_2 = ", ".join([block.text for block in completion_2.content])

        current_prompt = reminder_prompt + response_2

    final_descriptions.append(response_2)
    client_1.close()
    client_2.close()

with open('../words_script.txt', 'w') as text_file:
    text_file.write("\n\n".join(final_descriptions) + "\n")
