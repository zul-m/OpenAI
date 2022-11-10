import openai
openai.api_key = "sk-xxx"

engines = openai.Engine.list()

print(engines.data[0].id)

completion = openai.Completion.create(engine = "ada", prompt = "Hello world!")

print(completion.choices[0].text)