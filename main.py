import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from prompt import PERSONA  # Assuming PERSONA is a string containing the persona instructions

load_dotenv()

def main():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY environment variable is not set.")
        return
    
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)

    print("Gemini Chatbot (type 'exit' to quit)")
    print(f"Persona: {PERSONA}") 
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        try:
            prompt = f"{PERSONA}\n\nUser: {user_input}"
            response = llm.invoke(prompt)
            print("Bot:", response.content)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
