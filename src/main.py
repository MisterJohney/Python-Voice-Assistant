import whisper
from langchain_ollama import OllamaLLM
import edge_tts
from playsound3 import playsound

def transcribe():
    INPUT_FILE = "../tests/recording.wav"
    OUTPUT_FILE = "../tests/input_text.txt"

    model = whisper.load_model("base")
    result = model.transcribe(INPUT_FILE)
    # print(result["text"])
    with open(OUTPUT_FILE, "w") as f:
        f.write(result["text"])


def prompt():
    model = OllamaLLM(model="llama3.2")
    INPUT_FILE = "../tests/input_text.txt"
    OUTPUT_FILE = "../tests/output_text.txt"
    
    with open(INPUT_FILE, "r") as f:
        text = f.read()
    
    result = model.invoke(input=text)
    
    # print(result)
    
    with open(OUTPUT_FILE, "w") as f:
        f.write(result)

def tts():
    with open("../tests/output_text.txt", "r") as f:
        text = f.read()

    VOICE = "en-GB-SoniaNeural"
    OUTPUT_FILE = "../tests/compleation.mp3"
    communicate = edge_tts.Communicate(text, VOICE)
    communicate.save_sync(OUTPUT_FILE)

# def play_audio():
    # pygame.init()
    # pygame.mixer.init(frequency=44100)
    # pygame.mixer.music.load("../tests/compleation.mp3")
    # pygame.mixer.music.play()

print("transcribing")
transcribe()
print("prompting")
prompt()
print("ttsing")
tts()
print("playing")
playsound("../tests/compleation.mp3")
