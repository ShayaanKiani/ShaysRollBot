This bot is a work in progress.

Installation
-------------
Install dependancies use 'pip install -r requirements.txt'.
If you want to run this locally you will need to create a secrets.py file within the main directory.
Inside secrets.py you will need a varaible called 'bot_token' which is equal to your created bot token.

Pre Commit Checks
-------------
Before commiting run 'python -m black .', this will format your code.

Bot Commands
-------------
!rollcharacter - Rolls a character using 4d6d1.
!ls - Manually set last session time in format '01-01-2021-00:00'
!ns - Manually set last session time in format '01-01-2021-00:00', you can add an additional parameter auto-ls after the time to set the last session time to the previos sessions time.