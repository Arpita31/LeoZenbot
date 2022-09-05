# motivationalbot

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
  ```
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
*
