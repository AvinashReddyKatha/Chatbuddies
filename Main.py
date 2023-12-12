import openai

openai.api_key = "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"

def chat_with_gpt(prompt, max_tokens= 30):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages =[{"role": "system", "content":"You are helpful for making friendly convsesations"},
       {"role":"user", "content": prompt}],
        max_tokens= max_tokens
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        print("HI! I am VIKA! How can I help YOU ")
        user_input = input("You: ")
        if user_input.lower() in ["quit", "bye", "exit", "stop"]:
            break

        response = chat_with_gpt(user_input)
        print("Vika: ",response)

