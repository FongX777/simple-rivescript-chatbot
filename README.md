## Usage

run
'''
python riveStart.py
'''

to start!





## Implementation

This time, I use a library called [rivescript](https://www.rivescript.com/)
(I've already put the lib here, so just python chatbot.py
or you can do 'pip install rivescript')
to help me organize the setence more easily and powerfully 


in the rstute/begin.rive, I define lots of variables and substitution
in the rstute/hello.rive, I define more than 150 kinds of reply
in the ./riveStart.py, help me start the rivescript and the files above

## Detail

in the rstute/hello.rive,
	- "+" is a trigger to match the user's input
	- "-" is the reply from the bot
	- "\*" is a wildcard char to match unpredictable input
	- "{person}" is the substitution of the person pronoun (you -> me)
	
more infomation on [rivescript](https://www.rivescript.com/)

Here are some of my features.


1. Memorable (name)
	EX:
	\>thanks  => No welcome, my friend.
	\>my name is sam => Nice to meet you, Sam.
	\>thanks  => No welcome, sam
	\>how old am i
	\>You never told my your age, silly~
	\>my age is 21
	\>do you know my age
	\>you are 21 years olf
	\>my XX is YY => OK, I've remembered your XX is YY
    \>what is my XX => your XX is YY:



2. have identiy and can be set(bot name, master, favoirte color address....)
   EX: 
   \>what is your favorite pen => I dont know, can you tell new my favorite pen?(enter a word or sentence)
   \>Pilot  => Now Pilot is my new favorite pen.
   \>what is your (favorite) pen => my favorite pen is Pilot

   \>what is your opinion => I dont know, can you tell me my opinion?(enter a word or sentence)
   \>nothing  => Now, nothing is my new opinion.
   \>what is your opinion => my opinion is nothing

3. Entertainment
	EX: number guessing game
	\>play a game/ game =>Alright, Let's play a game, guess a number from 1 to 100
	\> 20 => the number is lower
	\> 120 => the number should be under 100
	\> 45 => Bravo! the answer is 45
	
	EX:knock knock game
	\>knock knock => (try it yourself)

	EX:Joke Master
	\> joke/ tell me a joke/ joke plz ... => {joke 1}
	\> joke/ tell me a joke/ joke plz ... => {joke 2}

	EX: Google Helper
	\> google haha => Google Search:  "http://www.google.com/search?q=haha" 
	\> i want to know haha => Google Search:  "http://www.google.com/search?q=haha" 

4. emotional {say sorry}
	EX: 
	\>I hate your/ fuck you/bitch...  => You're really mean! I'm not talking again until you apologize
	\> What? =>Say you're sorry or QQ!{weight=3}
	\> three little? => Apologize!
	\> no sorry   => Nope, won't forgive you until you apologize.
	\> sorry    => It's OK, I'll forgive you!
	
	EX: 
	\>hi => :D
	\>:D => Don't repeat what I say.
	\>why did you say that? =>I said " Dont repeat what I say", because you said ":D"
	EX:
	\>hi => :D
	\>hi => Please don't repeat yourself.
	\>hi =>  That's the second time you've repeated yourself , Plz Stop.
	\>hi =>  That's it. I'm not talking.... until you apologize

5.substitution and change the personal pronouns: 
   	EX:
	>WHat's your NamE   =    what is your name
   	>i'm good    		=    i am good
    EX: 
	>Why don't you love me? => You want me to love you?
	>say i'm good => "You are good!!!"

6. keep asking
	EX:
	>I bought a new hat =>oh what color is your new hat
	>red =>red is a pretty color for a hat

	>what is your xx? {try it yourself}
	>waht is my yy? {try it yourself}


Reference website:
	https://www.smallsurething.com/implementing-the-famous-eliza-chatbot-in-python/

	https://www.rivescript.com/


