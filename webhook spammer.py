try:
    import time
    import os
    import fade
    import colorama
    from colorama import Fore
    import keyboard
    import requests
    import webbrowser
    import json
    from datetime import datetime

except ModuleNotFoundError:
    print("Module not found error. Installing the Requirements")
    os.system("pip install requests")
    os.system("pip install keyboard")
    os.system("pip install colorama")
    os.system("pip install fade")

    webbrowser.open("https://www.youtube.com/channel/therealdisaster")

faded_text = fade.purplepink("""
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗    ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝     ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗     ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗    ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                        made by kenjixoxo on khord""")
print(faded_text)


try:
    webhook = input("\n put your webhook here: ")
    message = input("enter the message to send: ")

    while True:
      requests.post(webhook, json={'username': 'Spammer', 'content': message})
      print("\n sending message")
      
except KeyboardInterrupt:
    print('\n[~] Deteniendo spam...')
    time.sleep(1)
    quit()
