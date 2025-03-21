from openai import OpenAI

# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "user", "content": "You are a virtual assistant names jarvis skilled in general task like alexa"}
    , {"role" : "user", "content" : "what is coding"}
  ]
)

print(completion.choices[0].message.content)
