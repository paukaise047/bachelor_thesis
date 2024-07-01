from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

all_words = []

client = OpenAI(api_key="INSERT API KEY HERE")

user_prompt = ("Give me 7 words that are as different from each other as possible, in all meanings and uses of the "
               "words. Rules: 1. Only single words in English. 2. Only nouns (e.g., things, objects, concepts). 3. No "
               "proper nouns (e.g., no specific people or places). 4. No specialised vocabulary (e.g., no technical "
               "terms). 5. Think of the words on your own (e.g., do not just look at objects in your "
               "surroundings).Write them in this format: word,word,word,word,word,word,word")

num_iterations = 100

for i in range(num_iterations):
    print(f"Iteration {i + 1}:")

    # Initialize a list for the current iteration
    iteration_words = []

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        temperature=0.9,
        max_tokens=2000,
        messages=[
            {"role": "system", "content": ""},
            {"role": "user", "content": user_prompt},
        ]
    )
    response = completion.choices[0].message.content

    print("Response:")
    print(response + "\n")

    iteration_words.extend([word.strip() for word in response.split(',')])

    all_words.extend(iteration_words)

with open('../words_script.txt', 'w') as text_file:
    text_file.write(", ".join(all_words) + "\n")