# Python Voice Assistant
Digital voice assistant solution on desktop. Work in progress...

## Installation
Note: as of now the voice assistant is supported until python 3.11.9 because of openai-whisper package.
It is also recommended to install this programm on a python virtual enviroment. To do that, run:
```sh
python3 -m venv envitoment-name
```
and to activate on windows run:
```sh
enviroment-name\Scripts\activate
```
and on Unix or MacOS, run:
```sh
source enviroment-name/bin/activate
```

To host the server you need to install dependecies:
[ollama](https://ollama.com/download)
after that, install necessary python dependecies from `requirements.txt`
```sh
pip install -r requirements.txt
```

For client side temporarily [mpv](https://mpv.io/) is needed

## Running the software
To start the LLM server, run:
```sh
ollama serve
```
After that run `server.py` on the server and then `client.py` on client's machine.
