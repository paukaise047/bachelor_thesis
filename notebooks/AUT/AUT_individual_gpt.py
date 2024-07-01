from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

all_words = []

client = OpenAI(api_key="INSERT API KEY HERE")

user_prompt = ("For this task, you’ll be asked to come up with as original and creative uses for fork as you can. "
               "The goal is to come up with creative ideas, which are ideas that strike people as clever, unusual, "
               "interesting, uncommon, humorous, innovative, or different. Your ideas don’t have to be practical or "
               "realistic; they can be silly or strange, even, so long as they are CREATIVE uses rather than ordinary "
               "uses. List one ORIGINAL and CREATIVE uses for a fork. Write them in this format: fork, *insert your "
               "idea*")

num_iterations = 100

csv_output = "Iteration,Words\n"

for i in range(num_iterations):
    #print(f"Iteration {i + 1}:")
    iteration_words = []

    completion = client.chat.completions.create(
        model="gpt-4",
        temperature=0.9,
        max_tokens=3000,
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

    csv_output += f"{', '.join(iteration_words)}\n"

with open('../words_script.csv', 'w') as csv_file:
    csv_file.write(csv_output)
