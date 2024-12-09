"""
This file was ment to be a shitty voice recogniser that could be run on any hardware to detect keyword, and then the following audio would be sent to more accurate speech recognition.
"""


# class Assistant:
#     def __init__(self):
#         pass

import sys
from threading import Thread

import speech_recognition

# from neuralinters import GenericAssistant


class Assistant:
    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()

        # self.assistant = GenericAssistant("intents.json", intent_methods={"file": self.create_file})
        # self.assistant.train_model()

        # threading.Tread(target=self.run_assistant).start()


    def create_file(self):

        with open("nonimportant.txt", "w") as f:
            f.write("HELLOOG")

    def run_assistant(self):
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = self.recognizer.listen(mic)

                    text = self.recognizer.recognize_google(audio)
                    text = text.lower()


                    if "hey there" in text:
                        print("You said hey there")
                        audio = self.recognizer.listen(mic)
                        text = self.recognizer.recognize_google(audio)
                        text = text.lower()
                        if text == "no":
                            print("You said no")
                            sys.exit()
                        else:
                            if text is not None:
                                print(text)
                                # response = self.assistant.request(text)
                                # if response is not None:
                                #     print("Nothing")
            except speech_recognition.exceptions.UnknownValueError:
                print("exception")
                continue


assistant = Assistant()
assistant.run_assistant()
