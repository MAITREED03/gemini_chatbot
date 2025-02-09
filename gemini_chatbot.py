from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

#get apu key from .env

api_key = os.getenv("GOOGLE_API_KEY")

#configure gemini Client with api key
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model='gemini-2.0-flash', 
    contents='Tell me a story in 300 words.'
)
print(response.text)

print(response.model_dump_json(
    exclude_none=True, indent=4))