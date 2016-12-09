from operator import itemgetter
############
#Definitions of the Functions that will be used
############
#This will print out all the players scored after each of the rounds of play
def pScores():
	p1Printout="\n\n"+p1N + "\'s score is: \t" + str(p1S)
	p2Printout=p2N + "\'s score is: \t" + str(p2S)
	p3Printout=p3N + "\'s score is: \t" + str(p3S)
	p4Printout=p4N + "\'s score is: \t" + str(p4S)
	print (p1Printout)
	print (p2Printout)
	print (p3Printout)
	print (p4Printout)
	return 

k = 4 
#########
#Start of the Actual Program
#########
#start by setting global variables
print("\n\n\n\n\nWelcome to the \"Hearts\" scorekeeper!\n\n")
p1N = raw_input("What is Player 1's name?   ")
p1N = p1N.capitalize()
p1S = 0
p2N = raw_input("What is Player 2's name?   ")
p2N = p2N.capitalize()
p2S = 0
p3N = raw_input("What is Player 3's name?   ")
p3N = p3N.capitalize()
p3S = 0
p4N = raw_input("What is Player 4's name?   ")
p4N = p4N.capitalize()
p4S = 0
h = 13
pScores()
#make sure no one has scored over 100
while (p1S<99 and p2S<99 and p3S<99 and p4S<99):
	#counter to make sure everyone is passing in the correct direction
	if (k%4==0):
		passDirections = "\n\nPass 3 cards to the player to your right.\n"
	elif (k%4==1):
		passDirections = "\n\nPass 3 cards to the player to your left.\n"
	elif (k%4==0):
		passDirections = "\n\nPass 3 cards to the player across from you.\n"
	elif (k%4==0):
		passDirections = "\n\nDo not pass any cards. Keep all cards that you were dealt.\n"
	print (passDirections)
	#Wait for the round to be played before you ask for the point cards
	nothing = raw_input("Press any key to score this round...")
	#ask about the queen
	x=0
	while (x==0):
		queen = raw_input("Who picked up the Queen of spades?\t")
		queen = queen.capitalize()
		if (queen!=p1N and queen!=p2N and queen!=p3N and queen!=p4N):
			print("I am sorry but you did not identify a player currently in this game.\nPlease try again...\n")
			x = 0
		else:
			x = 1
	#ask for the heart count of each player
	#check to make sure there were 13 hearts taken
	h = 13
	while (h > 0):
		p1Q = "How many hearts did " + p1N + " pick up this round?\t"
		p1H = raw_input(p1Q)
		p1H = int(p1H)
		h = h-p1H
		p2Q = "How many hearts did " + p2N + " pick up this round?\t"
		p2H = raw_input(p2Q)
		p2H = int(p2H)
		h = h-p2H
		p3Q = "How many hearts did " + p3N + " pick up this round?\t"
		p3H = raw_input(p3Q)
		p3H = int(p3H)
		h = h-p3H
		p4Q = "How many hearts did " + p4N + " pick up this round?\t"
		p4H = raw_input(p4Q)
		p4H = int(p4H)
		h = h-p4H
		if (h != 0):
			print "Someone didn't count all of the hearts in their deck, please recount..."
			h = 13
	#check to see if someone shot the moon.
	if queen == p1N:
		p1H = p1H+13
	elif queen == p2N:
		p2H = p2H+13
	elif queen == p3N:
		p3H = p3H+13
	else:
		p4H = p4H+13
	if (p1H ==26):
		p1H = 0
		p2H = 26
		p3H = 26
		p4H = 26
	elif (p2H ==26):
		p1H = 26
		p2H = 0
		p3H = 26
		p4H = 26
	elif (p3H ==26):
		p1H = 26
		p2H = 26
		p3H = 0
		p4H = 26
	elif (p4H ==26):
		p1H = 26
		p2H = 26
		p3H = 26
		p4H = 0
	p1S = p1S+p1H
	p2S = p2S+p2H
	p3S = p3S+p3H
	p4S = p4S+p4H
	#display the scores
	pScores()
	k = k+1
#display the final scores	
final = []
p1final = []
p2final = []
p3final = []
p4final = []
p1final.append(p1N)
p1final.append(p1S)
p2final.append(p2N)
p2final.append(p2S)
p3final.append(p3N)
p3final.append(p3S)
p4final.append(p4N)
p4final.append(p4S)
final.append(p1final)
final.append(p2final)
final.append(p3final)
final.append(p4final)
final.sort(key=itemgetter(1), reverse=False)
#Create the string variable's for the places everyone is in
firstplace = "\n\nIn FIRST PLACE is "+final[0][0]+" with a score of "+ str(final[0][1])
secondplace = "\nIn SECOND PLACE is "+final[1][0]+" with a score of "+str(final[1][1])
thirdplace = "\nIn THIRD PLACE is "+final[2][0]+" with a score of "+str(final[2][1])
forthplace = "\nIn FOURTH PLACE is "+final[3][0]+" with a score of "+str(final[3][1])+"\n\n"
#Print out the final places
print (firstplace)
print (secondplace)
print (thirdplace)
print (forthplace)
