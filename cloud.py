from wordcloud import WordCloud


def makecloud(words, width, height, num_of_words, image_file_name):

    excludewords = []
    f = open('stopwords.txt', 'r')
    for line in f.readlines():
        excludewords.append(line.strip())

    wordcloud = WordCloud(max_words=num_of_words, width=width, height=height,
                          stopwords=excludewords).generate(words)
    image = wordcloud.to_image()
    image.show()
    image.save(image_file_name + '.jpeg')
    # print ("test successful generation of image")
