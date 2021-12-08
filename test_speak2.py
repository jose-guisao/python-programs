import pyttsx3
import PyPDF2
book = open('oopt.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(8)
text = page.extractText()
print(text)
speaker.say(text)
speaker.runAndWait()
