import random

ans=True
a=100
b=8000
fortunes = ["What we think we become",
			"Waste Not Want Not",
			"Do not dwell in the past, do not dream of the future, concentrate the mind on the present",
			"Plant something today",
			"Good things come to those who wait.",
            "Patience is a virtue.",
            "The early bird gets the worm.",
            "A wise man once said, everything in its own time and place.",
            "Fortune cookies rarely share fortunes.",
            "We are shaped by our thoughts",
            "money, it is stupid"]

while ans:
    print ("""
    1. Happy
    2. Sadness
    3. Anger
    4. Don't know
    """)
    ans=raw_input("What are you feeling now? ") 
    if ans>"1":
    	print "\n\n"
	print random.choice(fortunes)
    if ans=="1": 
      print("\n Get exercise and get to nirvana by helping others") 
    elif ans=="2":
      print("\n You are about to get to the next stage of your sadness and you are very close to the end of your suffering") 
    elif ans=="3":
      print("\n Get lot's of ecercise. Anger is simply mischanneled energy and is a normal part of life. Do not let your anger provoke negative actions or thoughts or messages. \n\n End the cycle by running this many steps ")
      print random.randrange(a, b)
    elif ans=="4":
      print("\n Good, being happy is so close so be happy. Here is something you should try. Do something you love or get a new hoby to try. ") 
    elif ans !="":
      print("\n Not Valid Choice Try again") 

