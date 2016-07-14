# call pdfparser first
#call wordcloud
# print

import pdfparser
import cloud

def main():
    path = 'constitution_of_india.pdf'
    start_pg = 28
    end_pg = 446
    constitutionOfIndia = pdfparser.get_string_from_pdf(path,start_pg,end_pg)
    WIDTH = 1280
    HEIGHT = 720
    NUM_OF_WORDS = 250
    cloud.makecloud(constitutionOfIndia,WIDTH,HEIGHT,NUM_OF_WORDS)



if __name__ == '__main__':
    main()
