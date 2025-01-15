import pyaudio
import wave
import time
from speech_recognition import Recognizer, Microphone

# Function to check for silence
def is_silent(audio_chunk, threshold=500):
    """Check if the audio_chunk is silent based on a threshold."""
    return max(audio_chunk) < threshold

# Record audio after detecting a keyword
def record_audio_until_silence(output_filename, silence_duration=2):
    """Record audio until a specific silence duration is detected."""
    CHUNK = 1024  # Number of frames per buffer
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100  # Sampling rate

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    print("Recording...")
    frames = []

    silent_chunks = 0  # Counter for silent chunks
    silent_threshold = RATE // CHUNK * silence_duration  # Convert silence duration to chunks

    while True:
        data = stream.read(CHUNK)
        frames.append(data)

        # Check for silence
        audio_data = list(int.from_bytes(data[i:i+2], 'little', signed=True) for i in range(0, len(data), 2))
        if is_silent(audio_data):
            silent_chunks += 1
        else:
            silent_chunks = 0

        # Stop recording if silence exceeds threshold
        if silent_chunks >= silent_threshold:
            print("Silence detected, stopping recording.")
            break

    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio to a file
    with wave.open(output_filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    print(f"Audio saved as {output_filename}")

# Listen for a specific keyword
def listen_for_keyword(keyword):
    """Listen for a specific keyword using speech recognition."""
    recognizer = Recognizer()
    with Microphone() as source:
        print(f"Listening for keyword: '{keyword}'")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Calibrate for background noise
        while True:
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)
                print(f"Detected text: {text}")
                if keyword.lower() in text.lower():
                    print("Keyword detected!")
                    return
            except Exception as e:
                print("Could not recognize audio, please try again.")
