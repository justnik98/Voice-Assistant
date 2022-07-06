import os
import time
from vacore import VACore
import utils.num_to_text_ru as num_to_text
modname = os.path.basename(__file__)[:-3] # calculating modname
def start(core:VACore):
    manifest = {
        "name": "Помощь Игоря",
        "version": "1.0",
        "require_online": False,

        "default_options": {
            "wavRepeatTimes": 1, # число повторений WAV-файла таймера
            "wavPath": 'media/igor1.wav', # путь к звуковому файлу
        },

        "commands": {
            "спроси у игоря|спроси": ask_igor,
        }
    }
    return manifest

def start_with_options(core:VACore, manifest:dict):
    pass

def ask_igor(core:VACore, phrase:str):
    options = core.plugin_options(modname)
    core.play_wav(options["wavPath"])
    time.sleep(0.2)