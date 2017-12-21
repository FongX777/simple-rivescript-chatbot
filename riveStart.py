from rivescript import RiveScript

bot = RiveScript()
bot.load_directory("./rstut/")
bot.sort_replies()

def getReply(msg):	
	reply = bot.reply("localuser", msg)
	print('Bot>', reply)
	return reply


print('Say \'bye\' to exit.')
while True:
    msg = input("Client>")
    if msg == 'bye':
        break
    print(getReply(msg))
