import PyPDF2


def get_string_from_pdf(pdf_path, start_page, end_page):
    content = ""
    p = open(pdf_path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(p)
    #print (pdfReader.numPages)
    for pageNum in range(start_page,end_page):
        page = pdfReader.getPage(pageNum)
        if page.extractText() is not None:
            pageContents = page.extractText()
            content += pageContents

    return content
