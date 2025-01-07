# Python Voice Assistant
This project does what the title says. Work in progress...

## Installation
Note: as of now the voice assistant is supported on python 3.11.9 because of openai-whisper package.
It is recommended to install this programm on a python virtual enviroment. To do that, run:
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

To use the programm you need to install dependecies:
[ollama](https://ollama.com/download)
after that, install necessary python dependecies from `requirements.txt`
```sh
pip install -r requirements.txt
```

## Running the software
To start the LLM server, run:
```sh
ollama serve
```
~~After that run `server.py` on the server and then `client.py` on client's machine.~~

To execute the assistant, run `main.py` file.
