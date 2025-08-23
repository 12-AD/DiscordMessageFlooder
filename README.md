# Discord Bot Manager & Slave Bots

This repository contains a Manager Bot to manage multiple Discord bots (slave bots) that send messages through Discord. Each slave bot automatically loads its token based on the filename and can send DMs with customizable options. (Flooding)

#Setup

## Installation
Download the files as a zip or clone the repo 

```
pip install discord.py python-dotenv
```
## Folder Structure
Note that the bot uses its filename as an "id". If you want to change the filename, you will need to change the ID variable in each slave bot to an appropriate number. the code on each slave bot file is the exact same. Only the file names differ.
```
/bots
    manager.py         # Manager bot script
    1.py               # Slave bot 1
    2.py               # Slave bot 2
    3.py               # Slave bot 3
    #do as many as you need
.env                    # Environment variables
stop_bots.bat           # Batch script to stop all bots
stop_bots.ps1
start_bots.vbs
restart_bots.bat
```
## Environment Variables (.env)
Create a .env file in the root directory:
```
DISCORD_TOKEN=<manager_bot_token>
BOT1=<slave_bot_1_token>
BOT2=<slave_bot_2_token>
BOT3=<slave_bot_3_token>
#and so on...
PREFIX=!
OWNER_IDS=123456789012345678,987654321098765432
#change to your owner id(s)
```
## Starting the bots
run the ``` start_bots.vbs ``` file. This will prompt you to run it with or without command prompt windows (I recommend clicking "no")
Then your bots should be online
# Commands
## Manager Bot Commands

``` !exodus ```
Deletes all channels in the server and creates a single channel called Abd. Administrator only. (Mainly used when testing)

``` !spamdm <num> <user> <content> ```
Sends ``` <num> ``` DMs to the specified user. Example: !spamdm 5 @User Hello!

``` !shutdown ```
Shuts down all bots using stop_bots.bat (owner only). Requires the author’s ID to be in OWNER_IDS. You can also shut down the bots by running the file yourself.

``` !help ```
Shows a detailed help embed with all commands and running slave bots.

## Slave Bot Commands
Slave Bot (!dm) Commands

```!dm <user> <message>``` 
Sends one (or more) DM to a user with one (or more) bots.

Optional parameters (key=value format):
delay – Seconds between messages (default: 0.5)
count – Number of messages (default: 1)
number – Amount of bots to use (default: 1)
