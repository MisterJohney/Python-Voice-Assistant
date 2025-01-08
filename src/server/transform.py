import logging

import whisper
from langchain_ollama import OllamaLLM
import edge_tts

def transcribe(audio_file_path):
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

def transform(audio_file_path):
    recorded_text = "Strictly in no more than 100 words answer the following question: "
    recorded_text += transcribe(audio_file_path)

    answer_text = prompt(recorded_text)

    tts(answer_text)


if __name__ == "__main__":
    recorded_text = "Strictly in no more than 100 words answer the following question: "
    logging.basicConfig(level=logging.INFO)

    INPUT_FILE = "../../tests/recording.wav"
    OUTPUT_FILE = "../../tests/compleation.mp3"

    logging.info("transcribing")
    recorded_text = "Strictly in no more than 100 words answer the following question: "
    recorded_text += transcribe(INPUT_FILE)

    logging.info("prompting")
    answer_text = prompt(recorded_text)

    logging.info("ttsing")
    tts(answer_text)
