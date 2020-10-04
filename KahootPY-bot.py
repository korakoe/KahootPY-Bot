#imports

from kahoot import client

#inputs required for functions

print('enter game id')
ID=input('')
print('enter name')
name=input('')
print('enter amount of bots')
amount=input()

#joining functions are below, this uses the Kahoot! API to connect

count = 0
while count < int(amount):
    bot = client()
    bot.join(ID, name + str(count))
    def joinHandle():
        pass
    bot.on("joined",joinHandle)
    count += 1
    print(name + str(count) + ' has joined!')