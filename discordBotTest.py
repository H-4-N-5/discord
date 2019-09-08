import discord

commands = ['$command1','$command2','$command3','$command4','$command5'] 
# still setting up commands
# $command1 --> does something
# $command2 --> does something
# $command3 --> does something
# $command4 --> does something
# $command5 --> does something

class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged on as', self.user) # print login success in terminal

	async def on_message(self, message):
		
		if message.author == self.user: # if message author is the bot...
			return 						# then don't let bot respond to itself

		if message.content == '$botCommands': # setting up commands
			await message.channel.send(str(commands)) # respong with the list of commands formatted as string
	
		if 'beer' in message.content.lower(): # if any message contains the word beer
			await message.channel.send('Drink a beer for me {0.author.mention}!'.format(message)) # respond and mention the author who said beer

client = MyClient()
client.run('PUT MY TOKEN HERE') #token generated on Bot page of my App @ discordapp.com/developers/applications