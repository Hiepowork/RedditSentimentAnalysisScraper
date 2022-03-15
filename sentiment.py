from pathlib import Path
from textblob import TextBlob

fileName = input("Enter the file name: ")
txt = Path(fileName).read_text()
txt = txt.replace('##############################################################################################', '')
txt = txt.replace('\n', '')
blob = TextBlob(txt)
sentiment = blob.sentiment.polarity
print(sentiment)