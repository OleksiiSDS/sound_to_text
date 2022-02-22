import speech_recognition as sr
from os import path


def microphone_say_recognize():
    """Розпізнавання аудіо з мікрофону ПК"""

    mic = sr.Microphone(device_index=0)

    """
    list_mic = sp.Microphone.list_microphone_names()

    for some_mic in range(0, len(list_mic)):
        print(f"{some_mic}  {list_mic[some_mic]}")
    """

    r = sr.Recognizer()
    with mic as source:
        print("Говоріть...")
        audio = r.listen(source)

    # Використовуючи Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        you_say = r.recognize_google(audio, language='ru-RU')
        print("Ви сказали: " + you_say)
    except sr.UnknownValueError:
        print("Програма не змогла розпізнати текст")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


#microphone_say_recognize()

def audio_file_say_recognize():
    """Розпізнавання тексту з аудіофайлу"""
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "test_2.wav")

    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)

    try:
        print("Текст з аудіо: " + r.recognize_google(audio, language='ru-RU'))
    except sr.UnknownValueError:
        print("Програма не змогла розпізнати текст")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


audio_file_say_recognize()