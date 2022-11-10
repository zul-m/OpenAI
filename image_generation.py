import openai
openai.api_key = "sk-xxx"

image_resp = openai.Image.create(
    prompt = "two dogs playing chess, oil painting",
    n = 4,
    size = "512x512"
)