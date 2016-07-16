import pdfparser
import cloud


def main():

    # specify the name of the pdf. Ensure pdf is in same folder
    path = 'constitution_of_india.pdf'

    # starting page. In this example, I am not considering the indices of
    # the book. Please remember this is zero indexed. So subtract 1 from the
    # actual start page.
    start_pg = 28

    # last page. Not considering the appendix in this example
    end_pg = 446

    # width of the picture
    WIDTH = 1280

    # height of the picture
    HEIGHT = 720

    # Number of words in the cloud
    NUM_OF_WORDS = 250

    # Name of the image
    image_file_name = 'constitution_example'

    # If you want to exclude certain words from the cloud,
    # you can add them as a new line to the file stopwords.txt
    # Currently stopwords.txt only contain Stop Words

    pdf_to_word = pdfparser.get_string_from_pdf(path, start_pg, end_pg)
    cloud.makecloud(pdf_to_word, WIDTH,
                    HEIGHT, NUM_OF_WORDS, image_file_name)

if __name__ == '__main__':
    main()
