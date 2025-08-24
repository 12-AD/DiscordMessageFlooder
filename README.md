# Demo
## https://www.youtube.com/watch?v=OWt1uVz_EK8

# Discord Bot Manager & Slave Bots

This repository contains a Manager Bot to manage multiple Discord bots (slave bots) that send messages through Discord. Each slave bot automatically loads its token based on the filename and can send DMs with customizable options. (Flooding)

# Setup
## Creating a bot with Discord
Travel to the Discord Developer Portal.

Once there and logged in, click "New Application"

Select a name for your application, accept the TOS, and click create.

You can change the profile picture of your application. (Make sure to press "Save Changes" at the bottom)

Next, travel to the "Bot" Section on the left (you can also change the picture and display name there)

There, you can obtain your token, which will be required for your .env file.

If you scroll down a little further, you will see "Privileged Gateway Intents"

I recommend selecting all 3 of them. 

Make sure to press "Save Changes".

Next, travel to the "OAuth2" section 

scroll to the "OAuth2 URL Generator"

select "Bot" (3rd row, 3rd column at the time of making this)

for permissions:
- DM commands don't require any permission
- The "Exodus command" (command I made for debugging)  does require "Manage Channels" Permissions. (Only required for the manager bot)
- The **Required** Permissions for any bot: "Send messages", "View Channels"
- If you are having issues, tick the "Admin" Box (What I usually do); it gives your bot complete control of the server. If you do this, **MAKE SURE YOU DON'T LEAK YOUR TOKEN!** This is how servers get nuked.
  
Then, click "Copy" at the bottom and paste that link in any chat of the server you want to add to the bot(s) to (you must be an admin).
Then click the link, and it should prompt you to add the bot to the server. Do these stops for however many bots you want. If you want *a lot* of bots, you will need to make alts since the application limit is fairly low.

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
