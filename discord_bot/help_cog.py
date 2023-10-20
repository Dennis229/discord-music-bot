import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        self.help_message = """

```
General commands:
!help - displays all the avaiable commands
!p <keywords> - finds the song on youtube and plays it in your current channel.
!q - displays the queue
!skip - skips the current song
!clear - clears the queue and stops the music
!leave - disconnects the bot from the channel
!pause - pauses the music
!resume - resumes the music

```



"""




        self.text_channel_text = []

        @commands.Cog.listener()
        async def on_ready(self):
            for guild in self.bot.guilds:
                for channel in guild.text_channels:
                    self.text_channel_text.append(channel)

            await self.send_to_all(self.help_message)

        async def send_to_all(self, msg):
         for text_channel in self.text_channel_text:
           await text_channel.send(msg)

        @commands.command(name="help", help="Displays all the avaiable commands")
        async def help(self, ctx):
           await ctx.send(self.help_message)

        
        
    




