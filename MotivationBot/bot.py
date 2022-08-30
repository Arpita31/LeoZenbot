'''
    Building MotivationBot 1.0
'''

from email.quoprimime import quote
import discord
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_GUILD = os.getenv("DISCORD_GUILD")


# intents = discord.Intents.default() # To show sensitive information as all the members list
# intents.members = True

client = discord.Client()

def get_quotes(types: str):
    ''' 
        Finds an appropriate quote according to user's mood and posts.

        Args:
            types: Mood detection keywords
        Returns:
            the quote to post.
    '''
    url = "https://zenquotes.io/api/"+types
    print(url)
    response = requests.get(url)
    # print(response.text)
    json_data = json.loads(response.text)
    # print(json_data)
    quote = json_data[0]['a'] + " quotes : \n\t" +json_data[0]['q'] 
    return quote

@client.event
async def on_ready():
    '''
        Event listener when the bot turned Online from Offline.
        Prints the guild name and memebers names.
    '''
    print(f"{client.user} has connected to discord!")

    # 3 ways to find the guild
    # for guild in client.guilds:
        # if guild.name == DISCORD_GUILD:
        #     break

    # guild = discord.utils.find(lambda g: g.name == DISCORD_GUILD, client.guilds)
    guild = discord.utils.get(client.guilds, name = DISCORD_GUILD)
            
    print(f"{client.user} is connected to the following guild:\n"
        f"{guild.name} \t id = {guild.id}"
        )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_member_join(member):
    '''
        Sending Direct messages to the user.
        When a member joins our server, a welcome dm is sent 

        Args:
            member : New user information
    '''
    await member.create_dm()
    await member.dm_channel.send(f"Hi, {member.name}, Welcome to Speak out server!")

@client.event
async def on_message(message):
    '''
        when user messages - this def takes input posts the appropriate responds. 
        
        Args:
            message : Users message 
    '''
    if message.author == client.user:
        return

    
    # if 'inspire' in message.content.lower():
    #     print("inside inspire")
    #     await message.channel.send(get_quotes("right"))

    greetings = ["hello", "hi", "yo", "wat's up", "hey", "howdy", "bonjour", "ahoj"]

    moods_dict = {"happiness" : ["sad", "not good", "depressed", "disappointed", "unhappy"],
                "anxity": ["anxious", "stressed"],
                "courage": ["scared", "afraid", "nervous", "fearful"]
                }
    posted = False
    msg = message.content.lower()
    
    for word in greetings:
        if word in msg:
            posted = True
            await message.channel.send("Bonjour! This is Leo.\n How are you feeling?")
            break

    if not posted:
        for i in moods_dict.keys():
            if any(word in msg for word in moods_dict[i]):
                posted = True
                if i == "happiness":
                    await message.channel.send(f"Dearest {message.author} every cloud has a silver lining.")# \n{get_quotes(i)}")
                elif i == "anxity":
                    await message.channel.send(f"Hush! don't panic our beloved {message.author}.")# \n{get_quotes(i)}")
                else:
                    await message.channel.send(f"Don't worry dear {message.author}.")#\n{get_quotes(i)}")
        if not posted:
            await message.channel.send(f"Hey buddy {message.author} You are amazing.") #\n{get_quotes('random')}")


    
client.run(DISCORD_TOKEN)
