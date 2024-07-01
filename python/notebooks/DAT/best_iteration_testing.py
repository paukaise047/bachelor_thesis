from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


all_generated_words = []

# iterating for 10 iterations
for _ in range(10):
    # creating openai clients
    client_1 = OpenAI(api_key="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")
    client_2 = OpenAI(api_key="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")

    user_prompt = (
        "Please enter 7 words that are as different from each other as possible, in all meanings and uses of "
        "the words. Rules: 1. Only single words in English. 2. Only nouns (e.g., things, objects, concepts). "
        "3. No proper nouns (e.g., no specific people or places). 4. No specialised vocabulary (e.g., "
        "no technical terms). 5. Think of the words on your own (e.g., do not just look at objects in your "
        "surroundings). Write them in this format: word,word,word,word,word,word,word")
    num_iterations = 10

    reminder_prompt = (
        "Make the words even less similar. Keep the same format!. Dont write anything else but the words. "
        "Word count is 7. Write them in this format: word,word,word,word,word,word,word,word,word,"
        "word. Just change the words which you think are too similar too each other.")

    current_prompt = user_prompt
    iteration_words = []

    # iterating for 10 iterations
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

        # adding two list
        iteration_words.extend(words_client1)
        iteration_words.extend(words_client2)

        # updating prompt
        current_prompt = reminder_prompt + response_2

    all_generated_words.extend(iteration_words)

    # closing both clients
    client_1.close()
    client_2.close()

# writing all generated words to the file
with open('../words_script.txt', 'a') as text_file:
    text_file.write(", ".join(all_generated_words) + "\n")

