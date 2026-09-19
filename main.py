from dotenv import load_dotenv
from google import genai
import os


def main():
    load_dotenv()  # Reads .env into the environment

    gemini_api_key = os.getenv("GEMINI_API_KEY") # Gets the api key from .env

    if not gemini_api_key:
        print("GEMINI API KEY NOT FOUND") # Prints when the api key doesnt exist
        exit()

    client = genai.Client(api_key=gemini_api_key) # Sets the api key

    print("Welcome to your new personal shopper!")
    while True:
        try:
            query = input("What are you looking for today? (ex. Laptop, Desktop, Monitor, Phone)\nEnter request: ") # Gets input from the user to figure out what they need
            if query.lower() == 'exit': # Lets the user escape the loop when prompted
                print("Thanks. Have a great day!")
                exit()
            if "laptop" in query.lower(): # Happens when the users prompt includes "laptop"
                laptopQuery = input("List your wants and needs (ex. College laptop under $400): ")
                interaction = client.interactions.create(
                    model="gemini-3.8-flash",
                    input=f"Customer is looking for a laptop. Give them three options (make, model, cpu, ram, gpu, and price) from bestbuy without any more questions. Query: {laptopQuery}",
                )
                print(interaction.output_text)
            if "desktop" in query.lower(): # Happens when the users prompt includes "desktop"
                laptopQuery = input("List your wants and needs (ex. Gaming desktop under $800): ")
                interaction = client.interactions.create(
                    model="gemini-3.8-flash",
                    input=f"Customer is looking for a desktop. Give them three options (make, model, cpu, ram, gpu, and price) from bestbuy without any more questions. Query: {laptopQuery}",
                )
                print(interaction.output_text)
            if "monitor" in query.lower(): # Happens when the users prompt includes "monitor"
                laptopQuery = input("List your wants and needs (ex. Gaming monitor under $300): ")
                interaction = client.interactions.create(
                    model="gemini-3.8-flash",
                    input=f"Customer is looking for a monitor. Give them three options (make, model, resolution (ex. 1080p, 1440p, 4k), refresh rate (ex. 60hz), response time (ex. 1ms), and price) from bestbuy without any more questions. Query: {laptopQuery}",
                )
                print(interaction.output_text)
            if "phone" in query.lower(): # Happens when the users prompt includes "phone"
                laptopQuery = input("List your wants and needs (ex. Best phone under $800): ")
                interaction = client.interactions.create(
                    model="gemini-3.8-flash",
                    input=f"Customer is looking for a phone. Give them three options (make, model, cpu, ram, screen resolution, and price) from bestbuy without any more questions. Query: {laptopQuery}",
                )
                print(interaction.output_text)

            else: # If the user doesnt have a request listed. Then it just asks the ai the users question
                interaction = client.interactions.create(
                    model="gemini-3.8-flash",
                    input=query
                )
                print(interaction.output_text)
        except Exception as e: # Prints if there's an error
            print(f"\nAn error occurred: {str(e)}")
            print("Please try again.")

if __name__ == "__main__":
    main()