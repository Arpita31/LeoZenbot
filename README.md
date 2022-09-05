# LeoZen bot



https://user-images.githubusercontent.com/6211637/188425418-892723fb-1553-483d-94f6-3f215f1fa158.mov



A Discord Bot

* To greet members in a discord server.
* Sends welcome texts in DM to the new users.
* Greets the existing users in the discord server.

## Process on developer portal :-

1. open developer portal home page in discord.
2. Create a New Application
3. Add Bot in application
4. Build a guild or server
5. Add the Bot details to OAuth2 in developer portal
6. Select the Guild on the OAuth2 generated URL


## Process on Python and discord.py api :-

* Install discord.py and dotenv
  ```
    $ pip install -U discord.py
    $ pip install python-dotenv
  ```
* Create a Client instance to connect with discord api
  ```python
      import os
      import discord
      from dotenv import load_dotenv

      load_dotenv()
      TOKEN = os.getenv('DISCORD_TOKEN')

      client = discord.Client()

      @client.event
      async def on_ready():
          print(f'{client.user} has connected to Discord!')

      client.run(TOKEN)
  ```
* Sending DM to new members
  ```python
       await member.create_dm()
       await member.dm_channel.send(f"Hi, {member.name}, Welcome to Speak out server!")
  ```
* Respond to messages
  ```python
       msg = message.content.lower()
       await message.channel.send(f"Hey buddy {author}!")
  ```

## Python libraries used:

* discord
* python-dotenv

