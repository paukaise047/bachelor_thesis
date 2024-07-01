from dotenv import load_dotenv
import anthropic

load_dotenv()

all_words = []

client = anthropic.Anthropic(
    api_key="INSERT YOUR API KEY HERE")

user_prompt = ("For this task, you’ll be asked to come up with as original and creative uses for fork as you can. "
               "The goal is to come up with creative ideas, which are ideas that strike people as clever, unusual, "
               "interesting, uncommon, humorous, innovative, or different. Your ideas don’t have to be practical or "
               "realistic; they can be silly or strange, even, so long as they are CREATIVE uses rather than ordinary "
               "uses. List one ORIGINAL and CREATIVE uses for a fork. Write them in this format: fork, *insert your "
               "idea*")

num_iterations = 100

for i in range(num_iterations):
    print(f"Iteration {i + 1}:")

    completion = client.messages.create(
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
                        "text": user_prompt
                    }
                ]
            }
        ]
    )
    response = ", ".join([block.text for block in completion.content])

    iteration_words = [word.strip() for word in response.split(',')]

    all_words.extend(iteration_words)

with open('../words_script.txt', 'w') as text_file:
    for word in all_words:
        text_file.write(word + "\n")
