from PyPDF2 import PdfReader
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Location of the PDF document
file_path = r"C:\Users\YourName\Documents\file.pdf"

# Reading the PDF file
reader = PdfReader(file_path)

text = ""
for page in reader.pages:
    text += page.extract_text() or ""

# Creating the word Cloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

plt.imshow(wordcloud)
plt.axis("off")
plt.show()
