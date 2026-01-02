# Text-to-Speech File Reader
### Video Demo: <https://youtu.be/dVbrAuCAgFA?feature=shared>
### Description:
This is a simple project designed to convert text to speech. It takes a PDF or image file and converts it to an audio that will be displayed automatically and saved into a WAV file on your device.
### Purpose:
Just a little attempt to design a program helping people with eyesight diffculities.

> [!IMPORTANT]
> Ensure that all library requirements are met to run the code smoothly.

### Libraries:
* `pyttsx3` is a Text to Speech (TTS) library for Python 3. Works without internet connection or delay. Supports multiple TTS engines, including Sapi5, nsss, and espeak.

   [PyPI package](https://pypi.org/project/pyttsx3/).
* `pytesseract` is an optical character recognition (OCR) tool for python. That is, it will recognize and “read” the text embedded in images.

  [PyPI package](https://pypi.org/project/pytesseract/).
* `pypdf` is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. Pypdf can retrieve text and metadata from PDFs as well.

   [PyPI package](https://pypi.org/project/pypdf/).
* `PIL` is Python Imaging Library (Fork) known as pillow.

   [PyPI package](https://pypi.org/project/pillow/).

* `os` is a module that provides a portable way of using operating system dependent functionality. If you just want to read or write a file, see open(), if you want to manipulate paths, see the os.path module, and if you want to read all the lines in all the files on the command line, see the fileinput module. For creating temporary files and directories, see the tempfile module, and for high-level file and directory handling, see the shutil module.

   [Documentation](https://docs.python.org/3/library/os.html).

  ### Steps:
  * first function is `get_path` which check the validity of a file path and if it exists or not then returns the correct path.
  * the second function is `load_file` and this function is simply taking a file path and a file extension, checking if the file is not corrupted, then returns image or pdf reader object. Pypdf and PIL were used to read files based on file extension then return an object.
  * third function is `file_to_text`, this function takes an object and an extension, and it simply extracts text from PDFs or images and returns it. I used pytesseract to extract text from images and pypdf to extract text from PDFs.
  * The fourth function is `text_to_audio`. In that one, we take the text we extracted and then convert it to an audio coming out of your speakers, with an additional feature of saving that audio in a WAV file on your device using the pyttsx3 library.
  * By raising exceptions and allowing flexible input methods, the program is more user-friendly. The program prompts the user again if the file doesn't exists, if the file extension is neither an image type nor a PDF and if it's not a valid string input (`e.g.: user entered 1234568`).
  * `test_project.py` is a file that uses `pytest` to test three functions `is_pdf_extension`, `is_image_extension` and `load_file` with different cases (negative and positive).
  * `requirements.txt` is a text file containing all essential libraries to run the program, you can install these libraries via `pip install "library name"` command in your terminal.
  * Other files in the directory are testing samples.
  ### Features:
  * Accepting PDFs and images.
  * Handling errors in a user-friendly way.
  * Ability to save audio file locally to listen to it later if you want.
  * Offline implementation.
  ### Limitations:
  This program only supports image and PDF files. It doesn't support any languages other than English and doesn’t support scanned PDFs without OCR. OCR may be affected by photo quality.
  ### Conclusion
  This program reflects the basic idea behind text-to-speech tools found in browsers and operating systems. I hope to enhance it further to make it more helpful.

  And this was  Text_to_speech File Reader project!
