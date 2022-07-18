import twitchio
import threading
import time
import IpRemove
from twitchio.ext import commands
import subprocess
import json
from datetime import datetime
import requests
class Bot(commands.Bot):
    urls = "test"
    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token='<twitch oarth>', prefix='!', initial_channels=['<twitch channel>'])
    async def event_ready(self):
        def run_background():
            subprocess.run(['nginx.exe'], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
        bg_thread = threading.Thread(target=run_background)
        bg_thread.start()
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
        IpRemove.NewPoll()
        IpRemove.IpRemove()
        print(IpRemove.urltest)
        global x
        global hopvote
        hopvote =0
        global stayvote
        global votearr
        stayvote = 0
        x = 0
        
    async def event_message(self, message):
        global x
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return
        # Print the contents of our message to console...
        print(message.content)
        ip = 'https://strawpoll.com/polls/' + IpRemove.idval
        print(ip)
        x = x + 1
        if x > 6:
            x = 0
            ip = 'https://strawpoll.com/polls/' + IpRemove.idval
            print(ip)
            connect = 'https://api.strawpoll.com/v3/polls/' + IpRemove.idval + '/results'
            print(connect)
            headers = {'Content-Type': 'application/json','X-API-Key': '<strawpoll api key> ',}
            response = requests.get(connect, headers=headers)
            response_dict= json.loads(response.text)
            if int(response_dict.get("participant_count")) >0 :
                for i in response_dict:
                    if i == "poll_options":
                        text= response_dict.get(i)[-1]
                        text = str(text)
                        text = text.split(' ').pop()
                print(((text[:-1])))
                totalint = int(response_dict.get("participant_count"))
                textint = int(text[:-1])
                pernhop = round((textint/totalint)*100,2)
                if pernhop < 25 :
                    if totalint > 10:
                        print("vote test")
            print()

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)
    @commands.command()
    async def cum(self, ctx: commands.Context):
        await ctx.send("I wish I would be able to magically make cum appear. In a non-gay way, I just think that the taste is pretty good and it would break the social stigma around drinking cum.")
    @commands.command()
    async def vote(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # e.g ?hello
        ip = 'https://strawpoll.com/polls/' + IpRemove.idval
        print(ip)
        connect = 'https://api.strawpoll.com/v3/polls/' + IpRemove.idval + '/results'
        print(connect)
        headers = {'Content-Type': 'application/json','X-API-Key': '<strawpoll api key>',}
        response = requests.get(connect, headers=headers)
        response_dict= json.loads(response.text)
        if int(response_dict.get("participant_count")) >0 :
            for i in response_dict:
                    if i == "poll_options":
                        text= response_dict.get(i)[-1]
                        text = str(text)
                        text = text.split(' ').pop()
            print(((text[:-1])))
            totalint = int(response_dict.get("participant_count"))
            textint = int(text[:-1])
            pernhop = round((textint/totalint)*100,2)
            if pernhop < 40 :
                if totalint > 10:
                    channel = bot.get_channel('everytwo_experiment')
                    await channel.send(f' Goodbye cruel world!')
                    subprocess.call(['python','end.py'])
                    time.sleep(5)
                    IpRemove.IpRemove()
                    subprocess.call(['python','start.py'])
                print("hello")
            print()
            await ctx.send(f'This stream currently has {pernhop} %  of people not wanting to kick and a total of {totalint} votes || you wanna vote {ip}')
        else:
            await ctx.send(f'Straw poll is currently down err0rz is triyng to fix thing atm so sorry for any schananigans !hop and !stay are in place temporarly')
        

    @commands.command()
    async def ohyeah(self, ctx: commands.Context):
            # Here we have a command hello, we can invoke our command with our prefix and command names
            # e.g ?hello
            # We can also give our commands aliases (different names) to invoke with.
            await ctx.send(f"'oh yeah you think you're a real intellectual huh? I bet you still think rats are real you corporate shill. I bet you don't even know about the RATS government program back in '88. I bet you don't even realize they can control your TV. why do you think they crawl into the walls THEY ARE LISTENING IN!'")
    @commands.command()
    async def kick(self, ctx: commands.Context):
                accounts = [<mod accounts>]
                print(ctx.author.name)
                if ctx.author.name in accounts:
                    subprocess.call(['python','end.py'])
                    time.sleep(2)
                    IpRemove.IpRemove()
                    subprocess.call(['python','start.py'])
                    await ctx.send(f'smited ...')
    @commands.command()
    async def newpoll(self, ctx: commands.Context):
                accounts = [<mod accounts>]
                print(ctx.author.name)
                if ctx.author.name in accounts:
                    IpRemove.NewPoll()
                    ip = 'https://strawpoll.com/polls/' + IpRemove.idval
                    print(ip)
                    await ctx.send(f'This is a new poll {ip}')
    @commands.command()
    async def PuttPutt(self, ctx: commands.Context):
            # Here we have a command hello, we can invoke our command with our prefix and command name
            # e.g ?hello
            # We can also give our commands aliases (different names) to invoke with.
            await ctx.send(f'HOT ZIGGITY https://www.youtube.com/watch?v=Q_hQ1h1Arl4')
    @commands.command()
    async def votekick(self, ctx: commands.Context):
            # Here we have a command hello, we can invoke our command with our prefix and command name
            # e.g ?hello
            # We can also give our commands aliases (different names) to invoke with.
            await ctx.send(f'Use !vote to start an anonymous hop strawpoll.')
    @commands.command()
    async def Hop(self, ctx: commands.Context):

            await ctx.send(f'Use !vote to start an anonymous hop strawpoll.')
    @commands.command()
    async def Stay(self, ctx: commands.Context):

            # Here we have a command hello, we can invoke our command with our prefix and command name
            # e.g ?hello
            # We can also give our commands aliases (different names) to invoke with.
            await ctx.send(f'Use !vote to start an anonymous hop strawpoll.')
    @commands.command()
    async def tick(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # e.g ?hello
        # We can also give our commands aliases (different names) to invoke with.
        await ctx.send(
            f"SOMEONE SAID THIS WAS GENUINELY UNWATCHABLE??? MY MAN HASN'T MISSED A SINGLE TICK SINCE THE START OF THE STREAM")
    @commands.command()
    async def help(self, ctx: commands.Context):
            # Here we have a command hello, we can invoke our command with our prefix and command name
            # e.g ?hello
            # We can also give our commands aliases (different names) to invoke with.
            await ctx.send(f'Anyone can stream to the Everyone Experiment.  To connect, see explanation and stream key in the description.')
    @commands.command()
    async def Dev(self, ctx: commands.Context):
            # Here we have a command hello, we can invoke our command with our prefix and command name
            # e.g ?hello
            # We can also give our commands aliases (different names) to invoke with.
            await ctx.send(f'The Dev for this channel is Err0rz For the server and the botand Johhnnay is helping maintain it with bot ')

while True:
    bot = Bot()
    bot.run()
# bot.run() is blocking and will stop execution of any below code here until stopped or closed.
