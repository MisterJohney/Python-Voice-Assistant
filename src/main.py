import logging

import whisper
from langchain_ollama import OllamaLLM
import edge_tts
from playsound3 import playsound

INPUT_FILE = "../tests/recording.wav"
OUTPUT_FILE = "../tests/compleation.mp3"

def transcribe(input_audio_file):
    # OUTPUT_FILE = "../tests/input_text.txt"

    model = whisper.load_model("base")
    result = model.transcribe(input_audio_file)
    # print(result["text"])
    # with open(OUTPUT_FILE, "w") as f:
    #     f.write(result["text"])
    return result["text"]


def prompt(input_text):
    model = OllamaLLM(model="llama3.2")
    # INPUT_FILE = "../tests/input_text.txt"
    # OUTPUT_FILE = "../tests/output_text.txt"
    
    # with open(INPUT_FILE, "r") as f:
    #     text = f.read()
    #
    # result = model.invoke(input=text)
    result = model.invoke(input=input_text)
    
    # print(result)
    
    # with open(OUTPUT_FILE, "w") as f:
    #     f.write(result)
    return result

def tts(input_text):
    # with open("../tests/output_text.txt", "r") as f:
    #     text = f.read()

    VOICE = "en-GB-SoniaNeural"
    # communicate = edge_tts.Communicate(text, VOICE)
    communicate = edge_tts.Communicate(input_text, VOICE)
    communicate.save_sync(OUTPUT_FILE)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    logging.info("transcribing")
    recorded_text = transcribe(INPUT_FILE)

    logging.info("prompting")
    answer_text = prompt(recorded_text)

    logging.info("ttsing")
    tts(answer_text)

    logging.info("playing")
    playsound(OUTPUT_FILE)
