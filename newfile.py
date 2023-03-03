import discord
from keep_alive import keep_alive
from discord.ext import commands,tasks
#from itertools import cycle

intents=discord.Intents.all()
intents.typing = False
intents.presences = False
intents.guilds=True
intents.guild_messages=True
intents.guilds=True
intents.dm_messages=True


client=discord.Client(intents=intents)

@client.event
async def on_ready():
	for guild in client.guilds:
		if guild.name == "GUILD":
			print(f"{client.user} is in {guild.name}: {guild.id}")
	print(f"Active, {client.user}")
	print("\n".join([member.name for member in guild.members]))



@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!')


@client.event
async def on_message(message):
	if message.author != client.user:
		return f"message received {message.content}"
	if message.content:
		response="Hi"
		await message.channel.send(response)

keep_alive()
token = "MTA0NTExMzMzOTg5MTY5NTc0OA.GAmFY8.U1ihoea1ZHRD0HHgrwWi6rlyhF7RR3TlHCKk_w"
client.run(token)
