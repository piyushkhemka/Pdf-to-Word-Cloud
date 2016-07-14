from wordcloud import WordCloud, STOPWORDS

def makecloud(words,width,height,num_of_words):

    excludewords = STOPWORDS.copy()
    #print ("here")

    wordcloud = WordCloud(max_words=num_of_words, width=width, height=height, stopwords=excludewords).generate(words)
    image = wordcloud.to_image()
    image.show()
    image.save('consti' + '.jpeg')
    #print ("test successful generation of image")
