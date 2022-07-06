from vacore import VACore


# функция на старте
def start(core: VACore):
    manifest = {  # возвращаем настройки плагина - словарь
        "name": "Подсказка по всем актуальным командам",  # короткое описание
        "version": "1.0",  # версия
        "require_online": False,  # требует ли онлайн?

        "commands": {  # набор скиллов. Фразы скилла разделены | . Если найдены - вызывается функция
            "функционал|что|что умеешь|что можешь|что ты умеешь": help_start,
        }
    }
    return manifest


def help_start(core: VACore,
               phrase: str):  # в phrase находится остаток фразы после названия скилла, если юзер сказал больше
    core.say("Расказать кратко, подробно или отмена")
    core.context_set(menu_main)  # меню - набор фраз и правил, в конце файла


def help_cancel(core: VACore, phrase: str):
    core.say("хорошо")
    return


def help_short(core: VACore, phrase: str):
    help_cmd(core, phrase, "short")
    return


def help_desc(core: VACore, phrase: str):
    help_cmd(core, phrase, "desc")
    return


menu_main = {"кратко|коротко": help_short, "подробно": help_desc, "отмена": help_cancel}


def help_cmd(core: VACore, phrase: str, mode_help: str):
    for manifs in core.plugin_manifests.keys():
        commands = core.plugin_manifests[manifs].get('commands')
        name = core.plugin_manifests[manifs].get('name')
        if commands != None:
            for keyall in commands.keys():
                keys = keyall.split("|")
                msg = keys[0]
                if msg == "что умеешь":
                    continue

                if mode_help == 'desc':
                    msg = msg + ' - ' + name

                print(msg)
                core.say(msg)
    return
