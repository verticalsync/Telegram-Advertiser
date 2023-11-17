# The code in this sucks, and is not maintained, and is relatively difficult to use as it could be simplified. I don't suggest using this, find a different one instead.
# There is a possibility of where I re-code this, but it's not high.
# -
# Telegram Advertiser

## Installation
1. Download the repository.
2. Install [Python](https://python.org/) (3.8-3.10 should work, make sure to include to PATH)
3. In the directory of the repository run `pip install -r requirements.txt` to install all the required libraries.
4. Move onto [usage](#usage).

## Usage
1. Head over to [telegram's developer tools](https://my.telegram.org/auth) and login.
2. After logging in, head over to your [telegram apps](https://my.telegram.org/apps), and create one, enter any information you want.
3. After the app is created copy the api_id and api_hash, and head over to the `config.txt` and replace api_id:api_hash with your information.
4. After your config is setup, head over to the `groups.txt` and add the groups you want to send to. (the name after url on invite.)
5. After you setup the groups you want to send to head over to the `message.txt` and set your message to send to all the groups.
6. After all of that is done, you can simply run advertiser.py by either opening it, or running in cmd `python advertiser.py`.
