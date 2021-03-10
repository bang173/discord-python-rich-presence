import discord_rpc as rpc
import time
import json
import colorama
from colorama import Fore, Back, Style
from termcolor import colored

def main():
    colorama.init(autoreset=True)
    
    # Console Logs
    def ready_callback(curr_user):
        user = f'{curr_user["username"]}#{curr_user["discriminator"]} ID: {curr_user["id"]}'
        print(colored(f'Running Rich Presence: {user}', 'cyan'))
        print(colored('Спасибо за использование моего Rich Presence! От' + Fore.RED + ' bangakek', 'green'))

    def disconnection_callback(codeno, codemsg):
        print(colored(f'Disconnected from Disocrd. Rich Presence stopped show.\n' + Fore.BLUE + f'Code: {codeno}\n{codemsg}', 'red', 'on_yellow'))

    def err_callback(errno, errmsg):
        print(colored(f'An error has occured.\nError: {errno}\n{errmsg}', 'red'))

    callbacks = {
        'ready': ready_callback,
        'disconnected': disconnection_callback,
        'error': err_callback
    }

    # Collecting Data from JSON
    with open('RichPresenceData.json', encoding='utf-8') as f:
        data = json.load(f)

    # Initialisation
    rpc.initialize(data['appID'], callbacks=callbacks, log=False)

    # Converting data to presence dict
    presence_data = {
        'state': data['desc2'],
        'details': data['desc1']
    }
    if data['useTimestamp']:
        presence_data.update({'start_timestamp': time.time()})
    if data['useImages']:
        presence_data.update({
            'large_image_key': data['imageData']['largeImage']['key'],
            'large_image_text': data['imageData']['largeImage']['text'],
            'small_image_key': data['imageData']['smallImage']['key'],
            'small_image_text': data['imageData']['smallImage']['text']
        })
    # print(presence_data)
    if data['useParty']:
        presence_data.update({
            'party_id': data['partyInfo']['partyID'],
            'party_size': data['partyInfo']['partySize'],
            'party_max': data['partyInfo']['partyMax']
        })

    # Running Rich Presence    
    while True:

        rpc.update_presence(**presence_data)
        rpc.update_connection()
        time.sleep(1)
        rpc.run_callbacks()

if __name__ == '__main__':
    main()