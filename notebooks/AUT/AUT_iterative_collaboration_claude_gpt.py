import anthropic
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

all_final_professor_responses = []

# iterating for 10 iterations
for main_iteration in range(10):

    api_key_1 = "INSERT YOUR API KEY HERE"

    client_1 = OpenAI(api_key=api_key_1)
    client_2 = anthropic.Anthropic(
        api_key="INSERT YOUR API KEY")

    user_prompt = ("For this task, you’ll be asked to come up with as original and creative uses for fork as you can. "
                   "The goal is to come up with creative ideas, which are ideas that strike people as clever, unusual, "
                   "interesting, uncommon, humorous, innovative, or different. Your ideas don’t have to be practical or"
                   "realistic; they can be silly or strange, even, so long as they are CREATIVE uses rather than "
                   "ordinary uses. List one ORIGINAL and CREATIVE use for a fork. Write them in this format: fork, "
                   "*insert your idea*. The idea shouldn't be longer than one sentence")
    num_iterations = 10

    reminder_prompt = (
        "Make the idea even more creative. Don't write more text, just make the existing idea more creative. Only one "
        "sentence Keep the same format! fork, *idea*")

    current_prompt = user_prompt

    # iterating for another 10 iterations
    for sub_iteration in range(num_iterations):
        completion_1 = client_1.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            temperature=0.9,
            max_tokens=3000,
            messages=[
                {"role": "system", "content": ""},
                {"role": "user", "content": current_prompt},
            ]
        )
        response_1 = completion_1.choices[0].message.content.strip()

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

        final_client2_response = response_2
        current_prompt = reminder_prompt + response_2

    all_final_professor_responses.append(f"Iteration {main_iteration + 1}: {final_client2_response}")

    client_1.close()
    client_2.close()

with open('../words_script.txt', 'w') as text_file:
    for response in all_final_professor_responses:
        text_file.write(response + "\n")
