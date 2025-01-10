from sender import send_file

import logging

from playsound3 import playsound

INPUT_FILE = "./recording.wav"
OUTPUT_FILE = "./output.mp3"

if __name__ == "__main__":
    logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

    logging.info("Sending file")
    send_file(INPUT_FILE)

    # NOTE: on the desktop for me the audio isn't playing
    logging.info("Playing")
    playsound(OUTPUT_FILE)
