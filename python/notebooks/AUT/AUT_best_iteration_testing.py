from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()



all_generated_words = []

for _ in range(10):
    client_1 = OpenAI(api_key="INSERT API KEY HERE")
    client_2 = OpenAI(api_key="INSERT API KEY HERE")

    user_prompt = ("For this task, you’ll be asked to come up with as original and creative uses for fork as you can. "
                   "The goal is to come up with creative ideas, which are ideas that strike people as clever, unusual, "
                   "interesting, uncommon, humorous, innovative, or different. Your ideas don’t have to be practical or"
                   "realistic; they can be silly or strange, even, so long as they are CREATIVE uses rather than "
                   "ordinary"
                   "uses. List one ORIGINAL and CREATIVE use for a fork. Write them in this format: fork, "
                   "*insert your idea*")
    num_iterations = 10

    reminder_prompt = (
        "Make the idea even more creative. Keep the same format!. Dont write anything else but the words. "
        "Word count is 7. Write them in this format: word,word,word,word,word,word,word,word,word,"
        "word. Just change the words which you think are too similar too each other.")

    current_prompt = user_prompt
    iteration_words = []

    for _ in range(num_iterations):
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

        completion_2 = client_2.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            temperature=0.9,
            max_tokens=3000,
            messages=[
                {"role": "system", "content": ""},
                {"role": "user",
                 "content": reminder_prompt + response_1}
            ]
        )
        response_2 = completion_2.choices[0].message.content

        words_client1 = response_1.split(",")
        words_client2 = response_2.split(",")

        iteration_words.extend(words_client1)
        iteration_words.extend(words_client2)

        current_prompt = reminder_prompt + response_2
    all_generated_words.extend(iteration_words)

    client_1.close()
    client_2.close()

with open('../words_script.txt', 'a') as text_file:
    text_file.write(", ".join(all_generated_words) + "\n")
