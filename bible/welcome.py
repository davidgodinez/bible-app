import os
import pythonbible as bible
from gtts import gTTS
from playsound import playsound

os.chdir('./bible')

def welcome_message(message: str, name: str):
    """Generate any type of welcome message you like. This converts the text you enter to be saved as an mp3 file.

    Args:
        message (_str_): The message you would like
        name (_str_): the name of the message
    """
    text = message
    language = 'en'
    my_obj = gTTS(text, lang=language)
    my_obj.save(f"{name}.mp3")
    return playsound(f"{name}.mp3")


if __name__ == '__main__':
    message = input('Enter welcome message: ')
    name = input('Enter name of the file (e.g. "welcome"): ')
    welcome_message(message=message, name=name)