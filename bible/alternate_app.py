import os
import pythonbible as bible
from gtts import gTTS
from playsound import playsound

os.chdir('./bible')

def main():
    user_input = input('Enter the reference you wish to see "Book chapter:verse": ')
    normalized_reference = bible.normalize_reference(user_input)
    converted_reference = bible.convert_references_to_verse_ids(normalized_reference)
    language = 'en'

    if len(converted_reference) == 1:
        verse_text = bible.get_verse_text(converted_reference[0])
        print(f"The verse is: \n {verse_text}")
        my_obj = gTTS(verse_text, lang=language)
        my_obj.save(f"{user_input}.mp3")
        playsound(f"{user_input}.mp3")
    elif len(converted_reference) > 1:
        verse_list = []
        for verse in converted_reference:
            verse_list.append(bible.get_verse_text(verse))
        print('The verses are: ')
        verse_texts = ' '.join(verse_list)
        print(verse_texts)
        my_obj = gTTS(verse_texts, lang=language)
        my_obj.save(f"{user_input}.mp3")
        playsound(f"{user_input}.mp3")


if __name__ == '__main__':
    main()







