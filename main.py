from dotenv import load_dotenv
from google import genai
import os

load_dotenv()  # reads .env into the environment

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)