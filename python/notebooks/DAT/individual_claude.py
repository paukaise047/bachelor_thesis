from dotenv import load_dotenv
import anthropic


load_dotenv()

all_words = []

client = anthropic.Anthropic(
    api_key="INSERT YOUR API KEY HERE", )

user_prompt = ("Give me 7 words that are as different from each other as possible, in all meanings and uses of the "
               "words. Rules: 1. Only single words in English. 2. Only nouns (e.g., things, objects, concepts). 3. No "
               "proper nouns (e.g., no specific people or places). 4. No specialised vocabulary (e.g., no technical "
               "terms). 5. Think of the words on your own (e.g., do not just look at objects in your "
               "surroundings).Write them in this format: word,word,word,word,word,word,word")

num_iterations = 100

for i in range(num_iterations):
    print(f"Iteration {i + 1}:")


    iteration_words = []

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


    iteration_words.extend([word.strip() for word in response.split(',')])

    all_words.extend(iteration_words)

# writing all words into final file
with open('../words_script.txt', 'w') as text_file:
    text_file.write(", ".join(all_words) + "\n")