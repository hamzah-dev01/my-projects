from openai import OpenAI

client = OpenAI(api_key=("Add Your OpenAi-APi key here"))

def chat_with_bot(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    print("Type 'exit', 'bye' or 'quit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        response = chat_with_bot(user_input)
        print("Chatbot:", response)

#NotE: code could be updated according to the syntax provided by the openai libarary, check docs for Openai at github!
