
#DETECT BOLD VALUES
# This is for a word document.

from docx import *
#INSERT PRINTED MEDICAL REPORT (WORD FORMAT) IN THE FOLLOWING LINE (MAKE SURE YOU KEEP THE PATH SAME)
document = Document('exampleDOC.docx')
bolds=[]
italics=[]
for para in document.paragraphs:
    for run in para.runs:
        if run.italic :
            italics.append(run.text)
        if run.bold :
            bolds.append(run.text)

boltalic_Dict={'bold_phrases':bolds,
              'italic_phrases':italics}

# For PDF - Convert PDF to Word and then use the same procedure
import requests
import io
import json

endpoint = "https://api2.docconversionapi.com/jobs/create"
headers = {
    'X-ApplicationID': '0945bb14-9fd4-4a93-9009-cb99f463a792',
    'X-SecretKey': '48e9c3a2-cb30-4a97-8b72-db2977e397d4'
}
file = open("examplePDF.pdf", "rb")
data = {
    'outputFormat': 'docx',
    'async': 'false',
    'conversionParameters': '{}'
}
files = {
    'inputFile': ('example.pdf', file.read())
}

r = requests.post(url=endpoint, data=data, headers=headers, files = files)


response = r.text
print(response)
y = json.loads(response)
url = y["fileDownloadUrl"]

import requests
def save_link(book_link, book_name):
    the_book = requests.get(book_link, stream=True)
    with open(book_name, 'wb') as f:
      for chunk in the_book.iter_content(1024 * 1024 * 2):  # 2 MB chunks
        f.write(chunk)


filename =  'example.docx'
save_link(url,filename)

