from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

result = generator("I love pizza bicause", max_length=50)

print(result[0]["generated_text"])