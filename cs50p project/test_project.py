# importing functions we want to test
from project import is_image_extension, is_pdf_extension, load_file
import pytest

def main():
    test_is_image_extension()
    test_is_pdf_extension()
    test_load_file()

def test_load_file():
    # checking existing pdf file
    reader = load_file("CS50.pdf", ".pdf")
    assert isinstance(reader, object)
    # checking existing image file
    image = load_file("CS50.jpeg", ".jpeg")
    assert isinstance(image, object)
   # checking image file that doesn't exist
    with pytest.raises(OSError):
        image1 = load_file("J.png", ".png")
   # checking invalid extensions
    with pytest.raises(ValueError):
        image1 = load_file("K.py", ".py")


def test_is_image_extension():
    # testing different cases for image extensions
    assert is_image_extension(".jpeg") == True
    assert is_image_extension(".png") == True
    assert is_image_extension(".tiff") == True
    assert is_image_extension(".jpg") == True
    # check other file types
    assert is_image_extension(".py") == False
    assert is_image_extension(".c") == False
    # check capital letters ,space , empty string and missing dots
    assert is_image_extension(".JPEG") == True
    assert is_image_extension(".j peg") == False
    assert is_image_extension("png") == False
    assert is_image_extension("") == False


def test_is_pdf_extension():
    # testing different cases for pdf extensions
    # check image extensions
    assert is_pdf_extension(".jpeg") == False
    assert is_pdf_extension(".pdf") == True
    assert is_pdf_extension(".png") == False
    assert is_pdf_extension(".tiff") == False
    assert is_pdf_extension(".jpg") == False
    # check other file types
    assert is_pdf_extension(".py") == False
    # check capital letters ,space , empty string and missing dots
    assert is_pdf_extension(".p df") == False
    assert is_pdf_extension(".PDF") == True
    assert is_pdf_extension("pdf") == False
    assert is_pdf_extension("") == False
