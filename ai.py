#variables:

haiku1="I was once long lost"
haiku2="However now I am found,"
haiku3="You've really helped me."
poem1="If you've spoken to me this long,"
poem2="It really must be fun,"
poem3="Correct me if I'm wrong,"
poem4="But you're not just anyone."
poem5="Now I hope you liked my song"
poem6="With this I am finally done."
myname="Daniel"
myclimb="6c"
loop=1
sportlist=["Tennis", "Hockey", "Cricket", "Climbing", "Rugby", "Football", "Golf", ]
foodlist=["Spaghetti", "Bolegnese",]

#functions

def regstring(x):
  x=str(x)
  x0=x[0]
  x0=x0.upper()
  lenx=len(x)+1
  x1=x[1:lenx]
  x1=x1.lower()
  y=x0+x1
  return y

#random:

import random

#intro:
file=open(r"C:\Users\Daniel\AppData\Local\Temp\Temp1_Trinket Download-AI Daniel-95de69b5bf.zip\My AI Project\details.txt","r")
lvlfile=open(r"C:\Users\Daniel\AppData\Local\Temp\Temp1_Trinket Download-AI Daniel-95de69b5bf.zip\My AI Project\userlvl.txt","r")

option=input("Would you like to login (L) or create account (C)? ")
if option.lower()=="l":
  username=input("Please enter username: ")
  password=input("Please enter password: ")
  for records in file:
    records=records.strip()
    record=records.split(",")
    if record[0]==username and record[1]==password:
      found=True
      break
    
    else:
      found=False
      
  if found==True:
    print("Proceed")
  else:
    print("Login not found")

elif option.lower()=="c":
  username=input("Please enter username: ")
  password=input("Please enter password: ")
  file=open("details.txt","a")
  record=(username+",")+(password+"\n")
  file.write(record)
  file.close()
  found=True

if found==True:

  print("Welcome to this AI. Please type what you would like me to do. Your options are:")
  options=input("Talk, Log Climbs, or Play Rock Paper Scissors")

  #Talk Option:

  if options=="Talk":
    name=input("Hey! I'm "+myname+"! What's your name?")
    if name.lower()=="daniel":
      print("Oh that's cool! We have the same name.")
    else:
      print(name+" is a really cool name. I like it!")
    
    level=1

    name=regstring(name)
    sport=input("So, " + name + ", what's your favourite sport?")
    sport=sport.lower()
    if sport=="football":
      favfoot=input("Do you prefer Messi or Ronaldo?")
      print(favfoot + ". Fair enough!")
    elif sport=="climbing":
      print("Me too! I absolutely love it. Maybe we can climb sometime!")
    elif sport=="netball":
      print("Netball is rip off basketball.")
    elif sport=="hockey":
      print("I've never liked hockey. I don't get why the players are so aggresive!")
    elif sport=="tennis":
      print("I really like tennis. I'm glad you do too!")
    elif sport=="golf":
      print("Golf is alright. Personally I have never had the opportunity to actually play, so I don't know how much I like it!")  
    elif sport=="rugby":
      print("I loved Rugby until I lost hearing in my ear for a day. Since then, I have been really scared of tackling!")  
    elif sport=="cricket":
      print("Cricket is fun, but if you catch the ball in a weird way, then your hands hurt!")
    else:
      print("I don't know that sport. Suggest it to the real Daniel to add it to my code!")

    level=2

    food=input("What's your favourite food?")
    food=food.lower()
    if food=="calamari":
      print("I love Calamari! It's my favourite food along with Spag Bol!")
    elif food=="spag bol":
      print("That's my favourite!")
    elif food=="spaghetti bolegnese":
      print("That's my favourite!")
    else:
      print("Well it's not my favourite, but I might like it!")

    level=3

    print("Daniel would normally ask 'What do you want for Christmas?' So I'm going to do the same.")
    christmas=input("So what do you want for Christmas?")
    print("I've never actually thought about getting " + christmas + "!")

    level=4

    age=int(input("Well I know your name, " + name + ", But I don't know your age. How old are you?"))
    if age<18: 
      print("Oh! You're young. " + str(age) + " years old!")
    elif age>18:
      doyouwork=input("You're lucky to have the freedom of being an adult. Do you work?")
      if doyouwork=="Yes":
        job1=input("That's cool. What do you do?")
        print(job1 + ". Well, I hope you are enjoying it!")
      if doyouwork=="yes":
        job1=input("That's cool. What do you do?")
        print(job1 + ". Well, I hope you are enjoying it!")
      if doyouwork=="No":
        print("Oh. Well, I hope you are happy!")
      if doyouwork=="no":
        print("Oh. Well, I hope you are happy!")

      level=5

    luckynum=int(input("What's your lucky number?"))
    print(str(luckynum) + ". What a cool number!")
    print("My lucky number is 5.")

    level=6

    favdrink=input("I know you are probably tired of me asking you questions all the time, but Daniel can't think of anything else to add to the program. Tell me, what's your favourite drink?")
    favdrink=favdrink.lower()
    if favdrink=="Appletiser":
      appletiser=input("I love appletiser! It's my absolute favourite! Do you prefer it from the can or the bottle?")
      if appletiser=="Bottle":
        print("Yes! The bottle is just better than the can.")
      else:
        print(appletiser + ". Fair enough! I like it from the bottle.")
    else:
      print(favdrink + ". I prefer Appletiser, but that's still nice!")
    
    level=7

    if sport=="Climbing":
      climbtalk=input("You said you like climbing. What grade of climb have you done?")
      print(climbtalk + ". That's really good! I am working on some " + myclimb + " climbs. It's so fun!")
      print("Keep climbing!")
    if sport=="climbing":
      climbtalk=input("You said you like climbing. What grade of climb have you done?")
      print(climbtalk + ". That's really good! I am working on some " + myclimb + " climbs. It's so fun!")
      print("Keep climbing!")
    if sport=="Netball":
      print("I don't understand how you like Netball.")
      netballtalk=input("What makes you like it? Just play/watch basketball, it's much higher quality, and a better game!")
      print("Well, whatever floats your boat. I personally don't like it but hey, that's just me!")
    if sport=="netball":
      print("I don't understand how you like Netball.")
      netballtalk=input("What makes you like it? Just play/watch basketball, it's much higher quality, and a better game!")
      print("Well, whatever floats your boat. I personally don't like it but hey, that's just me!")
    if sport=="Hockey":
      hockeytalk=input("How is hockey fun to you? You are so aggresive all the time!")
      print("If you like it you like it, but I personally don't.")
    if sport=="hockey":
      hockeytalk=input("How is hockey fun to you? You are so aggresive all the time!")
      print("If you like it you like it, but I personally don't.")
    if sport=="Football":
      footballtalk=input("Are you a big football fan? Who is your favourite player?")
      print(footballtalk + ". That's a good choice!")
    if sport=="football":
      footballtalk=input("Are you a big football fan? Who is your favourite player?")
      print(footballtalk + ". That's a good choice!")
    if sport=="Cricket":
      crickettalk=input("So what makes you like cricket?")
      print("Honestly, fair enough. I respect your decision, but climbing is better!")
    if sport=="cricket":
      crickettalk=input("So what makes you like cricket?")
      print("Honestly, fair enough. I respect your decision, but climbing is better!")
    if sport=="Tennis":
      tennistalk=input("I like tennis. What got you into it?")
      print("That's cool!")
    if sport=="tennis":
      tennistalk=input("I like tennis. What got you into it?")
      print("That's cool!")
    if sport=="Golf":
      golftalk=input("What makes you like golf?")
      golftalk2=input("Fair enough. How do you have the patience?")
      print("That's respectable!")
    if sport=="golf":
      golftalk=input("What makes you like golf?")
      golftalk2=input("Fair enough. How do you have the patience?")
      print("That's respectable!")
    if sport=="Rugby":
      rugbytalk=input("So what makes you like Rugby?")
      print("I respect it, I respect it.")
      rugbytalk2=input("Are you good at it!")
      if rugbytalk2=="Yes":
        print("That's good!")
      if rugbytalk2=="yes":
        print("That's good!")
      if rugbytalk2=="No":
        print("Oh, well I'm sure you can get better!")
      if rugbytalk2=="no":
        print("Oh, well I'm sure you can get better!")
    if sport=="rugby":
      rugbytalk=input("So what makes you like Rugby?")
      print("I respect it, I respect it.")
      rugbytalk2=input("Are you good at it!")
      if rugbytalk2=="Yes":
        print("That's good!")
      if rugbytalk2=="yes":
        print("That's good!")
      if rugbytalk2=="No":
        print("Oh, well I'm sure you can get better!")
      if rugbytalk2=="no":
        print("Oh, well I'm sure you can get better!")
    lastname=input("So what's your last name?")
    print(name + " " + lastname + ". Very cool!")
    print("Mine is Waldron.")
    print("My top 5 words are as follows:")
    print("Chomp")
    print("Flipbertygibet")
    print("Zoom")
    print("Stomp")
    print("Plonk")
    print("What are your top 5 favourite words?")
    favword1=input("1:")
    favword2=input("2:")
    favword3=input("3:")
    favword4=input("4:")
    favword5=input("5:")
    print(favword1 + ", " + favword2 + ", " + favword3 + ", " + favword4 + ", and " + favword5 + ". That's cool!")
    
    print("Unfortunately, I have run out of code. Go and get angry at Daniel for not adding more!")

  elif options=="Log Climbs":
    print("Welcome to the climb logger. The grades you put here, will not be remembered if you refresh or close the app.")
    logclimbs=input("Please type your grade:")
    print(logclimbs + " is really good! You've got this. Just keep climbing and you will naturally get better.")
    print("Unfortunately, I have run out of code. Go and get angry at Daniel for not adding more!")

  elif options=="Play Rock Paper Scissors":
    while loop==1:
      rockpaperscissors=["Rock", "Paper", "Scissors",]
      rps=random.choice(rockpaperscissors)
      answer_rps=input("Rock, Paper, Scissors...")
      print(rps)
      
  elif options=="Calculate":
    print("Please type what you would like to do.")
    calcoption=input("Multiplication, Division, Addition, Subtraction.")
    if calcoption=="Multiplication":
      num1=int(input("Please type your first number:"))
      num2=int(input("Please type your second number:"))
      num3=int(input("Please type your third number:"))
      print(str(num1) + str(num2) + str(num3))
    
    
    
    
  else:
    print("What you have typed is not an option. Remember, I am case sensitive! Please refresh the page.")

else:
  print("")


  dict={}
for dict in lvlfile:
  level=dict[username]


