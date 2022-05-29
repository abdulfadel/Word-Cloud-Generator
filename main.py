from wordcloud import WordCloud, STOPWORDS
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image

text = open('github.txt', encoding='utf-8').read()
python_mask = np.array(PIL.Image.open("gitlogo.jpg"))

wc = WordCloud(stopwords=STOPWORDS,
                mask = python_mask,
                background_color = "white",
                contour_color = "black",
                contour_width = 1,
                min_font_size=4,
                max_words=500).generate(text)

plt.imshow(wc)
plt.axis("off")
plt.show()
