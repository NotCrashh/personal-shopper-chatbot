from dotenv import load_dotenv
from google import genai
import os


def main():
    load_dotenv()  # reads .env into the environment

    gemini_api_key = os.getenv("GEMINI_API_KEY")

    if not gemini_api_key:
        print("GEMINI API KEY NOT FOUND")
        exit()

    client = genai.Client(api_key=gemini_api_key)

    print("Welcome to your new personal shopper bot!")
    while True:
        try:
            query = input("Enter request: ")
            if query.lower() == 'exit':
                print("Thanks. Have a great day!")
                exit()
            else:
                interaction = client.interactions.create(
                    model="gemini-3.8-flash",
                    input=query
                )
                print(interaction.output_text)
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
            print("Please try again.")

if __name__ == "__main__":
    main()