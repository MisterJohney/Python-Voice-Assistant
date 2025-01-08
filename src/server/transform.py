import logging

import whisper
from langchain_ollama import OllamaLLM
import edge_tts

def transcribe(input_path):
    model = whisper.load_model("base")
    result = model.transcribe(input_path)
    return result["text"]

def prompt(input_text):
    model = OllamaLLM(model="llama3.2")
    result = model.invoke(input=input_text)
    return result

def tts(input_text, output_path):
    VOICE = "en-GB-SoniaNeural"
    communicate = edge_tts.Communicate(input_text, VOICE)
    communicate.save_sync(output_path) # Would have loved to return audio itself, but it isn't looking plausible

def transform(audio_file_path, output_path):
    logging.info("Transcribing")
    recorded_text = "Strictly in no more than 100 words answer the following question: "
    recorded_text += transcribe(audio_file_path)

    logging.info("Prompting")
    answer_text = prompt(recorded_text)

    logging.info("Ttsing")
    tts(answer_text, output_path)


# if __name__ == "__main__":
#     recorded_text = "Strictly in no more than 100 words answer the following question: "
#     logging.basicConfig(level=logging.INFO)
#
#     INPUT_FILE = "../../tests/recording.wav"
#     OUTPUT_FILE = "./processed_audio.wav"
#
#     logging.info("transcribing")
#     recorded_text = "Strictly in no more than 100 words answer the following question: "
#     recorded_text += transcribe(INPUT_FILE)
#
#     logging.info("prompting")
#     answer_text = prompt(recorded_text)
#
#     logging.info("ttsing")
#     tts(answer_text, OUTPUT_FILE)
