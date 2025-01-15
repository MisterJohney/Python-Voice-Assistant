import logging

import whisper
from langchain_ollama import OllamaLLM
import edge_tts

import sql_helper

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
    con, cur = sql_helper.init()

    logging.info("Transcribing")
    prompt_prepend = "Do not use * or - to beautify the answer. No yapping and use no more than 100 words to answer the following question: "
    recorded_text = transcribe(audio_file_path)

    logging.info("Prompting")
    answer_text = prompt(prompt_prepend + recorded_text)

    sql_helper.add_log_entry(con, cur, prompt_prepend + recorded_text, answer_text)

    logging.info("Ttsing")
    tts(answer_text, output_path)
