import matplotlib.pyplot as pPlot
from wordcloud import WordCloud, STOPWORDS
import numpy as npy
from PIL import Image
dataset = open("cyberbullying.txt", "r").read()
def create_word_cloud(dataset):
   maskArray = npy.array(Image.open("cyber1.jpg"))
   cloud = WordCloud(background_color = "white", max_words = 200, mask = maskArray, stopwords = set(STOPWORDS))
   cloud.generate(dataset)
   cloud.to_file("cyber2.png")
dataset = dataset.lower()
create_word_cloud(dataset)