
import openai
from config import api_key

openai.api_key = api_key
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write a email to boss for resignation",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response["choices"][0]["text"])

