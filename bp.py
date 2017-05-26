import random

ans=True
a=100
b=8000

sports = [  "cycling or running",
			"fishing or swimming or anything involving fluid but no inoxicants",
			"mountaineering, climbing or walking with an obstacle to overcome",
			"cross country or downhill skiing, snowboarding or anything with a hill involved that you must climb over and overcome",
			"tennis or something with a ball you must smash",
			"archery or something you must hit a target. dont stop until the target is hit in the sweet spot",
			"fly a kite"]

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
    5. Intoxicated
    """)
    ans=raw_input("What are you feeling now? ") 
    if ans:
    	print "\n\n"
	print "Buddha says " + random.choice(fortunes)
    if ans=="1": 
      print("\n Get exercise and get to nirvana by helping others") 
    elif ans=="2":
      print("\n You are about to get to the next stage of your sadness and you are very close to the end of your suffering") 
      print("\n Buddha says you must do a sport below or similar activity that is only if you can physically do it without injuries or sickness")
      print("\n\n Budda says you should " + random.choice(sports))
    elif ans=="3":
      print("\n Get lot's of ecercise. Anger is simply mischanneled energy and is a normal part of life. Do not let your anger provoke negative actions or thoughts or messages. \n\n End the cycle by running this many steps ")
      print random.randrange(a, b)
    elif ans=="4":
      print("\n Good, being happy is so close so be happy. Here is something you should try. Do something you love or get a new hoby to try. ") 
    elif ans=="5":
      print("\n Buddha says to keep a clear mind. You must drink water, and do more sports.")
      print("\n\n Budda says you should try " + random.choice(sports)) 
    elif ans !="":
      print("\n Not Valid Choice Try again") 

