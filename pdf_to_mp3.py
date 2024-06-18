import PyPDF2
from pyttsx3 import init

pdfreader = PyPDF2.PdfReader(open('Ivetta1.pdf', 'rb'))

speaker = init()

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
print(clean_text)

speaker.save_to_file(clean_text, 'Ivetta1.mp3')
speaker.runAndWait()
# speaker.stop()
