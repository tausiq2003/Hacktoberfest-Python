import random

answers=['It is certain','It is decidedly so','Without a doubt','Yes-definitely',
         'You may rely on it','As I see it,yes','Most likely','Outlook good'
          ,'Yes Signs point to yes','Reply hazy','try again','Ask again later','Better not tell you',
          'Cannot predict now','Concentrate and ask again','Dont count on it','My reply is no','My sources say no',
          'Outlook not so good','Very doubtful']
def replay():
    print("Want to ask another question? [y/n]")
    ans=input()
    magic_ball()if ans == 'y' else exit()

def magic_ball():
    print("Hello! Enter your question")
    input()
    print(random.choice(answers))
    replay()

magic_ball()


