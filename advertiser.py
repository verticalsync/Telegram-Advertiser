import time, os, contextlib
from telethon import TelegramClient, errors
from telethon.tl.functions.channels import GetFullChannelRequest
from colorama import Fore

os.system("title Telegram Advertiser ^| purpl3r0se#0001")
clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clear()

with open("config.txt", "a+") as config:
    config.seek(0)
    cfg = config.read().strip().split("\n")[0]
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

try: os.mkdir("session")
except: pass

client = TelegramClient('session/session', api_id, api_hash)

sent = 0
groups = open("groups.txt", "r+").read().strip().split("\n")
forwardgroup = int(open("forward.txt", "r+", encoding="utf8").read().strip().split("\n")[0])
found_groups = []

wait1 = int(input(f"{Fore.WHITE}[{Fore.MAGENTA}?{Fore.WHITE}]{Fore.RESET} How long do you want to wait between each message? (seconds): "))
wait2 = int(input(f"{Fore.WHITE}[{Fore.MAGENTA}?{Fore.WHITE}]{Fore.RESET} How long do you want to wait after all groups have been messaged? (seconds): "))
print("")

lefttowait = 0

def title():
    text = f"Telegram Advertiser ^| purpl3r0se#0001 ^| Groups: {len(found_groups)}, Messages Sent: {sent}"
    text += f" ^| Sleeping for {lefttowait} seconds" if lefttowait > 0 else ""
    os.system(f"title {text}")

def sleep(towait):
    global lefttowait
    for i in range(towait):
        lefttowait = towait - i
        title()
        time.sleep(1)
    lefttowait = 0
    title()

async def send(forwarded_message):
    global sent

    while True:
        for found_group in found_groups:
            group = found_group
            try:
                await client.forward_messages(group, forwarded_message)
                print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]{Fore.RESET} Message sent to {group}, Sleeping for {wait1} seconds")
                sent += 1
                title()
                sleep(wait1)
            except errors.rpcerrorlist.SlowModeWaitError:
                print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.RESET} Failed to send to channel {group}, due to slowmode.")
                title()
                sleep(wait1)
            except errors.rpcerrorlist.ChannelPrivateError:
                print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.RESET} Failed to send to channel {group}, due to it being private or you've been banned, removing it from list.")
                found_groups.remove(found_group)
                title()
                sleep(wait1)
            except Exception as e:
                print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.RESET} Failed to send to channel {group}, due to it being an unhandled exception here's the direct reason: {e}, {e.args}")
                title()
                sleep(wait1)
        print(f"{Fore.WHITE}[{Fore.YELLOW}\{Fore.WHITE}]{Fore.RESET} Sleeping for {wait2} seconds, because all groups have been sent to.")
        sleep(wait2)

async def x():
    forwarded_message = (await client.get_messages(forwardgroup, limit=50))[0]

    async for dialog in client.iter_dialogs():
        if dialog.is_group:
            with contextlib.suppress(Exception):
                inv = await client(GetFullChannelRequest(dialog.id))
                for group in groups:
                        for chat in inv.chats:
                            if chat.username.lower() == group.lower():
                                found_groups.append(f"{chat.username}")
                                title()

    v = [found_group.lower() for found_group in found_groups]
    for group in groups:
        if group.lower() not in v:
            print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.RESET} Group {group} not found")
            time.sleep(1)

    os.system("cls")
    await send(forwarded_message)

client.start()
client.loop.run_until_complete(x())