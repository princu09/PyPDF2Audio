import PyPDF2
from gtts import gTTS

pdfFile = open("nameorpathof.pdf" , "rb")

pdfReader = PyPDF2.PdfFileReader(pdfFile)

myText = ""
totalPages = pdfReader.numPages

for pno in range("enter here page number for start pdf reading like 24 etc.." ,totalPages):
    page = pdfReader.getPage(pno)
    myText += page.extractText()

print(myText)
pdfFile.close()

tts = gTTS(text=myText, lang='en')
tts.save("filenameforsave.mp3")