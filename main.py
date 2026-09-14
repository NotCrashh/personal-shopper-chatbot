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

    print("Welcome to your new personal shopper!")
    while True:
        try:
            query = input("What are you looking for today? (ex. Laptop, Desktop, Monitor, Phone)\nEnter request: ")
            if query.lower() == 'exit':
                print("Thanks. Have a great day!")
                exit()
            if "laptop" in query.lower():
                laptopQuery = input("List your wants and needs (ex. College laptop under $400): ")
                interaction = client.interactions.create(
                    model="gemini-3.8-flash",
                    input=f"Customer is looking for a laptop. Give them three options (make, model, cpu, ram, gpu, and price) from bestbuy without any more questions. Query: {laptopQuery}",
                )
                print(interaction.output_text)

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