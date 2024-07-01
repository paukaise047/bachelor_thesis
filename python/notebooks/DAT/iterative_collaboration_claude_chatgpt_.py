from openai import OpenAI
from dotenv import load_dotenv
import anthropic


load_dotenv()



all_generated_words = []

for _ in range(10):
    client_1 = OpenAI(api_key="INSERT YOUR API KEY HERE")
    client_2 = anthropic.Anthropic(
        api_key="INSERT YOUR API KEY",)

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
                            "text": "Make the words even less similar. Keep the same format!. Dont write anything else "
                                    "but the words. Word count is 7. Write them in this format: word,word,word,word,"
                                    "word,word,word." + response_1
                        }
                    ]
                }
            ]
        )
        response_2 = ", ".join([block.text for block in completion_2.content])

        words_client1 = response_1.split(",")
        words_client2 = response_2.split(",")

        iteration_words.extend(words_client1)
        #iteration_words.extend(words_client2)

        current_prompt = reminder_prompt + response_2

    all_generated_words.extend(iteration_words)

    client_1.close()
    client_2.close()
    with open('../words_script.txt', 'a') as text_file:
        text_file.write(", ".join(all_generated_words[-7:]) + "\n")
