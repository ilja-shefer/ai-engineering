from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-5-mini",
    input="Explain what an API is in one sentence.",
)

print(response.output_text)


