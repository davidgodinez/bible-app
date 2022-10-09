import os
import pythonbible as bible
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr 
from pydub.silence import split_on_silence

#create docker file to test out 
# TODO need to account for ranges of bible verses, can use regex splicing to do this

#os.chdir('./bible')


def welcome():
    playsound('./welcome.mp3')


def main():
    welcome()

    # Speech input
    r = sr.Recognizer()
    with sr.Microphone(device_index=0,sample_rate=44100) as source:
        # record the audio data from the default microphone
        print("Recognizing...")
        r.adjust_for_ambient_noise(source)
        audio_data = r.record(source, duration=5)
        print('Done')
        # convert speech to text
        user_input = r.recognize_google(audio_data)
        print(user_input)

    normalized_reference = bible.normalize_reference(user_input)
    converted_reference = bible.convert_references_to_verse_ids(normalized_reference)
    language = 'en'

    if len(converted_reference) == 1:
        verse_text = bible.get_verse_text(converted_reference[0])
        print(f"The verse is: \n{verse_text}")
        my_obj = gTTS(verse_text, lang=language)
        my_obj.save(f"{user_input}.mp3")
        playsound(f"{user_input}.mp3")
    elif len(converted_reference) > 1:
        verse_list = []
        for verse in converted_reference:
            verse_list.append(bible.get_verse_text(verse))
        verse_texts = ' '.join(verse_list)
        print(f'The verses are:\n{verse_texts}')
        my_obj = gTTS(verse_texts, lang=language)
        my_obj.save(f"{user_input}.mp3")
        playsound(f"{user_input}.mp3")


if __name__ == '__main__':
    main()







