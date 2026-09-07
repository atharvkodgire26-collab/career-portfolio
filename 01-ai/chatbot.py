import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

print("AI Chatbot - Type 'quit' to exit")
print("-" * 40)

messages = [{"role": "system", "content": "You are a helpful assistant. Keep answers short and clear."}]

while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    assistant_message = response.choices[0].message.content
    print(f"\nAI: {assistant_message}")

    messages.append({"role": "assistant", "content": assistant_message})
