import discord
from functions import latency_FUNC, c_latency
client = discord.Client()

@client.event
async def on_message(message): # makes a asyncronus function that runs when the bot recieves a message(on_message)
    global latency # makes the variable global(makes it accessible outside the function)
    latency = client.latency # gives latency the value of (client.latency)
    latency_FUNC(latency) # calls the function latency_FUNC and gives it the value of latency a.k.a (client.latency)
    ping = c_latency() # makes ping the value of c_latency(output from latency_FUNC)
    print(ping) # prints(in the console) the value of ping
    if message.content.find("!PP") != -1: # searches for !PP in all of the messages it recieves (!= -1:) ! is the whole message so if (find) finds the message its greater then -1 and = means greather then so if !PP is found then it makes if true so it runs the code below it
        await message.channel.send(ping) # send a back message with the value of ping



client.run("YOUR_BOT_SECRET")