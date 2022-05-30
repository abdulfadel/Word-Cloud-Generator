# Python Word Cloud Generator
Word Cloud is a data visualization technique used for representing text data in which the size of each word indicates its frequency or importance. 
Significant textual data points can be highlighted using a word cloud. Word clouds are widely used for analyzing data from social network websites. 

![Figure_1](https://user-images.githubusercontent.com/92131037/170895315-f056c2e6-cd86-4fe9-8b9f-11c85cc7c2be.png)

## How to run?
```
git clone https://github.com/abdulfadel/wordcloud.git
```
- Add your **.txt** document to folder - *Pasting serveral articles related to your topic of interest should do just fine*
- Rename **Line 6** `github.txt` to your new text document: 
```py
text = open('RENAME.txt', encoding='utf-8').read()
```
- Add your image or logo to folder - *Use an image with a solid/clear background for best results.*
- Rename **Line 7** `gitlogo.jpg` to your new image:
```py
python_mask = np.array(PIL.Image.open("RENAME.jpg"))
```
# Edit Perameters

- Customize your generated `WordCloud` by editing th following:

```py
wc = WordCloud(stopwords=STOPWORDS,
                mask = python_mask,
                background_color = "white",
                contour_color = "black",
                contour_width = 1,
                min_font_size=4,
                max_words=500).generate(text) 
```
# Remove words from `WordCloud` in addition to `NLTK Stop Words`

```py
stopwords = STOPWORDS.update(["addidtional", "fluff", "words"])
```
- Learn more about [NLTK Stop words](https://pythonspot.com/nltk-stop-words/)

# Now run the program in the terminal - VSC users may press **F5** key

![image](https://user-images.githubusercontent.com/92131037/170896571-d833cf5d-bf42-4327-9fce-86711533f023.png)

- Resize image by dragging expanding corner of figure screen
- Savfe file once satisfied:
![image](https://user-images.githubusercontent.com/92131037/170903417-e396eba4-e08b-466c-936c-7b46dc99204a.png)


## Install - Dependencies

```
pip install wordcloud
pip install matplotlib 
pip install numpy
pip install Pillow
```
- Python 3.10
- [WordCloud 1.8.1](https://pypi.org/project/wordcloud/)
- [matplotlib](https://pypi.org/project/matplotlib/)
- [numpy](https://pypi.org/project/numpy/)
- [Pillow](https://pypi.org/project/Pillow/)



#  Microsoft Visual C++ 14.0 or greater is required.
![image](https://user-images.githubusercontent.com/92131037/170896958-af2a11d7-0c55-427e-bd2f-0dbade9e4d76.png)

### [Install Microsoft Visual C++ 14.0+](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
- Once install is complete - Restart Visual Studio Code
- You do not need to keep `Visual C++ open after install` - This is only a dependency
## `pip install wordcloud` after Visual C++ install is complete
![image](https://user-images.githubusercontent.com/92131037/170897133-18e1b21f-8565-46ad-af53-5b80a8d8983d.png)


