import pyttsx3
import pytesseract
import pypdf
from PIL import Image
import os


def main():
    path = get_path()
    root, ext = os.path.splitext(path)  # spliting extension and root
    reader = load_file(path, ext)  # getting an image/pdf object
    text = file_to_text(reader, ext)  # extracting text
    text_to_audio(text)  # displaying audio


def get_path():
    while True:
        try:
            path = input("File path: ")
            root, ext = os.path.splitext(
                path
            )  # spliting extention and root to check extensions
        except ValueError:  # reprompiting if it isn't a string
            continue
        # checking file type and reprompitting if not valid extensions given
        if not (is_image_extension(ext)) and not (is_pdf_extension(ext)):
            continue
        if not (os.path.exists(path)):  # little help from CS50 duck debugger
            continue
        else:
            break
    return path


def load_file(File, ext):
    """
    Reading image/pdf files.
    :param File: file path
    :param ext: extension of file
    :type File: string
    :type ext: string
    :return: Pdfreader object if file is pdf or Image object if file is image
    """
    if is_pdf_extension(ext):
        try:
            reader = pypdf.PdfReader(File)
        except pypdf.errors.PdfReadError:
            raise pypdf.errors.PdfReadError("Can't read pdf")
        return reader
    elif is_image_extension(ext):
        try:
            image = Image.open(File)
        except OSError:
            raise OSError("Can't read image")
        return image
    else:
        raise ValueError("Invalid file")


def file_to_text(f, ext):
    """
    Extracting text from pdf or image files.
    :param f: reader/image object
    :param ext: extension of file
    :type f: object
    :type ext: string
    :return: text extracted from pdfs or images
    :rtype: str
    """
    pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
    if is_pdf_extension(ext):
        text = ""
        for page in f.pages:
            text += page.extract_text()
    elif is_image_extension(ext):
        text = pytesseract.image_to_string(f)
    else:
        raise Exception("Invalid file")
    if text == "":
        raise Exception("your image have no text or the program can't read it")
    return text


def text_to_audio(txt):
    """
    Converting text to audio.
    :param txt: text
    :type txt: string
    :return: Audio reading text provided to the function
    :rtype: audio
    """
    engine = pyttsx3.init()
    try:
        engine.say(txt)
        engine.save_to_file(txt, "output.wav")
        engine.runAndWait()
    except:
        engine.say("Failed to convert to audio")


def is_image_extension(ext):
    """
    Checking valid image extentions(.png, .jpg, .jpeg, .tiff).
    :param ext: file extension
    :type ext: string
    :return: True if it is an image, False if it isn't.
    :rtype: bool
    """
    ext = ext.lower()
    img_extensions = [".jpeg", ".jpg", ".png", ".tiff"]
    return ext in img_extensions


def is_pdf_extension(ext):
    """
    Checking valid pdf extentions(.pdf).
    :param ext: file extension
    :type ext: string
    :return: True if it is a pdf, False if it isn't.
    :rtype: bool
    """
    ext = ext.lower()
    return ".pdf" == ext


if __name__ == "__main__":
    main()
