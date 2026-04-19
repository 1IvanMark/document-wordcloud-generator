from docx import Document
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Location of the word document
file_path =r"C:\Users\YourName\Documents\file.docx"

doc = Document(file_path)

# Fetching the text
text = ""
for para in doc.paragraphs:
    text += para.text + " "

# Creating the word cloud itself
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

plt.imshow(wordcloud)
plt.axis("off")
plt.show()
