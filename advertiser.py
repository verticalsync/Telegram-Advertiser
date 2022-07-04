import asyncio, time, os
import contextlib
from telethon import TelegramClient, errors
from telethon.tl.functions.channels import GetFullChannelRequest
from colorama import Fore

clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

clear()
os.system("title " + "Telegram Advertiser - Made by dart (more like purpl3r0se)")
print(f"""{Fore.RED}
d888888b d88888b db      d88888b  d888b  d8888b.  .d8b.  .88b  d88.    .d8b.  d8888b. db    db 
`~~88~~' 88'     88      88'     88' Y8b 88  `8D d8' `8b 88'YbdP`88   d8' `8b 88  `8D 88    88 
   88    88ooooo 88      88ooooo 88      88oobY' 88ooo88 88  88  88   88ooo88 88   88 Y8    8P 
   88    88~~~~~ 88      88~~~~~ 88  ooo 88`8b   88~~~88 88  88  88   88~~~88 88   88 `8b  d8' 
   88    88.     88booo. 88.     88. ~8~ 88 `88. 88   88 88  88  88   88   88 88  .8D  `8bd8'  
   YP    Y88888P Y88888P Y88888P  Y888P  88   YD YP   YP YP  YP  YP   YP   YP Y8888D'    YP    
                                                                                                                                                                                                                                                                                                                          
{Fore.WHITE}""")

with open("config.txt", "a+") as config:
    config.seek(0)
    cfg = config.read().strip()
    if cfg == "api_id:api_hash":
        print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.RESET} Please edit config.txt with your api id and api hash")
        time.sleep(9999)
        exit()
    else:
        try:
            api_id, api_hash = cfg.split(":")
        except ValueError:
            print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.RESET} Incorrectly formatted config, make sure your format is api_id:api_hash")
            time.sleep(9999)
            exit()
        except Exception as e:
            print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.RESET} Unknown error ({e}), make sure your config is formatted correctly")
            time.sleep(9999)
            exit()

client = TelegramClient('anon', api_id, api_hash)

groups = open("groups.txt", "r+").read().strip().split("\n")
found_groups = []
message = open("message.txt", "r+").read().strip()

wait1 = int(input(f"{Fore.WHITE}[{Fore.MAGENTA}?{Fore.WHITE}]{Fore.RESET} How long do you want to wait between each message? (seconds): "))
wait2 = int(input(f"{Fore.WHITE}[{Fore.MAGENTA}?{Fore.WHITE}]{Fore.RESET} How long do you want to wait after all groups have been messaged? (seconds): "))
print("")

async def x():
    async for dialog in client.iter_dialogs():
        if dialog.is_group:
            with contextlib.suppress(Exception):
                inv = await client(GetFullChannelRequest(dialog.id))
                for group in groups:
                        for chat in inv.chats:
                            if chat.username.lower() == group.lower():
                                found_groups.append(f"{chat.username}")

    v = [found_group.lower() for found_group in found_groups]
    for group in groups:
        if group.lower() not in v:
            print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.RESET} Group {group} not found")

    print("")

    while True:
        for found_group in found_groups:
            group = found_group
            try:
                await client.send_message(group, message)
                print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]{Fore.RESET} Message sent to {group}, Sleeping for {wait1} seconds")
                time.sleep(wait1)
            except errors.rpcerrorlist.SlowModeWaitError:
                print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.RESET} Failed to send to channel {group}, due to slowmode.")
                time.sleep(wait1)
        print(f"{Fore.WHITE}[{Fore.YELLOW}\{Fore.WHITE}]{Fore.RESET} Sleeping for {wait2} seconds, because all groups have been sent to.")
        time.sleep(wait2)


client.start()
client.loop.run_until_complete(x())
