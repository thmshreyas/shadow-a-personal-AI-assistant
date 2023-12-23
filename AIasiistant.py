import speech_recognition as sr
import openai
import datetime
import pyttsx3

openai.api_key = 'openAPI_key'

def voice_to_text_and_play(stop_word="goodbye"):
    recognizer = sr.Recognizer()
    play_text("hi i am shadow how can i help you today")

    while True:
        with sr.Microphone() as source:

            print("Say something (Press Enter to stop recording):")
            recognizer.adjust_for_ambient_noise(source)

            audio = recognizer.listen(source, timeout=3, phrase_time_limit=None)

        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)

            if text.lower() == stop_word.lower():
                play_text(f"I hope i was of some help : {stop_word}")
                break

            completion = openai.Completion.create(
                engine="text-davinci-002",
                prompt=f"You are a personal assistant, skilled in explaining everything and updated till the date 23 december 2023 . User: {text}",
                temperature=0.7,
                max_tokens=150
            )
            generated_response = completion.choices[0].text.strip()

            if generated_response:
                play_text(generated_response)

        except sr.UnknownValueError:
            play_text("Sorry"
                      "I couldn't understand "
                      "can you repeat it again?")
        except sr.RequestError as e:
            print("Error connecting to Google API: {}".format(e))

def play_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    voice_to_text_and_play()
