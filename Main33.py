import openai

openai.api_key = "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"

def chat_with_gpt(prompt, max_tokens= 30):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages =[{"role": "system", "content": "You are a helpful assitant for trslating words"},
        {"role":"user", "content": prompt},
        ],

        max_tokens= max_tokens
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        print(" Hi! I am a word trasnlater: You can ask any unknown word to know the meaning")
        user_input = input("You: ")
        if user_input.lower() in ["quit", "bye", "exit", "stop"]:
            print("Good bye ! If you have any qestions feel free to ask")
            break

        response = chat_with_gpt(user_input)
        print("Vika: ",response)

