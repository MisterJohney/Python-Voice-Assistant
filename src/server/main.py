import logging

import whisper
from langchain_ollama import OllamaLLM
import edge_tts
from playsound3 import playsound

INPUT_FILE = "../tests/recording.wav"
OUTPUT_FILE = "../tests/compleation.mp3"

def transcribe(input_audio_file):
    model = whisper.load_model("base")
    result = model.transcribe(input_audio_file)
    return result["text"]


def prompt(input_text):
    model = OllamaLLM(model="llama3.2")
    result = model.invoke(input=input_text)
    return result

def tts(input_text):
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

    # NOTE: on the desktop for me the audio isn't playing
    logging.info("playing")
    playsound(OUTPUT_FILE)
