import vlc
import os
import pythonbible as bible
from gtts import gTTS
#from playsound import playsound
import speech_recognition as sr 
from pydub.silence import split_on_silence
import time

# instance = vlc.Instance('--aout=alsa')
# p = instance.media_player_new()
# m = instance.media_new('welcome.mp3')
# p.set_media(m)
# p.play()
# vlc.libvlc_audio_set_volume(p,80)
# print('audio played')

# media = vlc.MediaPlayer('welcome.mp3')
# media.play()
# print('audio played')
# time.sleep(1.5)
# duration = player.get_length() / 1000
# time.sleep(duration)

def Sound(sound):
    vlc_instance = vlc.Instance()
    player = vlc_instance.media_player_new()
    media = vlc_instance.media_new(sound)
    player.set_media(media)
    player.play()
    time.sleep(1.5)
    duration = player.get_length() / 1000
    time.sleep(duration)

Sound('welcome.mp3')
print('done')
