from openai import OpenAI

# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="<YOUR_API_KEY>"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "user", "content": "You are a virtual assistant names jarvis skilled in general task like alexa"}
    , {"role" : "user", "content" : "what is coding"}
  ]
)

print(completion.choices[0].message.content)
