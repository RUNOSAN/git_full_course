from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="koheiduck/bert-japanese-finetuned-sentiment")

result = classifier("お前が嫌いだ！")

print(result)