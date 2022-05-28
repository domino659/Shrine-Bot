import os, json
from pathlib import Path
from unidecode import unidecode

# This programme will react to any word contained in a json file in data/
CUR_DIR = Path(__file__).parent.parent
DATA_FILE = os.path.join(CUR_DIR, "data", "key_words.json")

def get_key_words():
    with open(DATA_FILE, "r") as f:
        key_words = json.load(f)

    words = [key_word for key_word in key_words]
    return(words)

def watcher(message):
    string = unidecode(message.content).lower()
    decomposed_string = string.split()
    for word in decomposed_string:
        if word in get_key_words():
            return True