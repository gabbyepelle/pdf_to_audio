from tkinter import *
import pyttsx3
import PyPDF3
import pdfplumber
from tkinter import filedialog, messagebox
import os
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfile, askopenfilename


# -----------------------------------OPEN AND READ PDF-----------------------------------#

def open_pdf():
    filetypes = (
        ("PDF Files", "*.pdf"),
        ("All Files", "*.*"))
    global file
    file = filedialog.askopenfilename(filetypes=filetypes)
    if file:
        # Open the PDF File
        global pdf_file
        pdf_file = PyPDF3.PdfFileReader(file)
        pages = pdf_file.numPages
        information = pdf_file.getDocumentInfo()
        title_label = Label(text=f"Title: {information.title}")
        title_label.pack()
        author_label = Label(text=f"Author: {information.author}")
        author_label.pack()
        pages = Label(text=f"Number of pages: {pages}")
        pages.pack()


def read_pdf():
    pages = pdf_file.numPages

    with pdfplumber.open(file) as pdf:
        for i in range(0, pages):
            page = pdf.pages[i]
            text = page.extract_text()
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()

#Not working. Not sure if M1 is the problem.
def save_audio():
    pages = pdf_file.numPages
    text = ""
    with pdfplumber.open(file) as pdf:
        for i in range(0, pages):
            page = pdf.pages[i]
            text += page.extract_text()
    print(text)
    engine = pyttsx3.init()
    #filename = filedialog.asksaveasfile(mode='w', defaultextension=".aiff")
    engine.save_to_file(text, "audio.aiff")
    engine.runAndWait()


# ---------------------UI SETUP------------------------#
window = Tk()
window.title("PDF to Audio")
# window.geometry("625x450")
title_label = Label(text="PDF 2 Audio", font='Courier 30 ', pady=20, padx=20)
title_label.pack()

upload_button = Button(text="Upload PDF", fg="blue", bg="blue", command=open_pdf)
upload_button.pack()
upload_button.config(height=2, width=10)

play_button = Button(text="Play Audio", fg="green", bg="green", command=read_pdf)
play_button.pack()
play_button.config(height=2, width=10)

# save_button = Button(text="Save MP3", command=save_audio)
# save_button.pack()
# save_button.config(height=2, width=10)

window.mainloop()
