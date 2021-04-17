from os import system
from time import sleep
from random import randrange, choice
import winsound

class bcolors:
    YELLOW = '\033[1;33'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    PURPLE = '\033[35m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Globals
user = 0
questions_answered = 0
health = 50
i = 5
dif = 1
teacher_finish = ["Stay were you belong... In my memories...", "You are dead...", "HAHAHAHAHA!!!!!!!", "DIE YOU FOOL!!! HAHAHAHAHA!!!!!!!!!"]
teacher_quote = ["I'm glad your dead... HAHAHAHAHA!!!", "Get better soon...", "Wow, you are terrible..."]
teacher_rematch = ["You want to get beat down again?", "Do you want to die again?", "Do you want to try again... And DIE!!!!!", "HAHAHAHAHA... do you want to get killed again?"]
names = ["stupid", "dumb", "bad"]
correct_qoutes = ["meh.", "Okay.", "Fine."]
wrong_quotes = ["Bang.", "Slice.", "HAHAHAHAHA...", "Easy", "You will DIE!!!", "VANISH!!!", "NOPE.", "?!?!?!", "JUST WHY!!!"]
type_error_qoutes = ["Learn HOw To tYPE A STUPID NUMBER!!!!!!!!!!!!!!!", "tHat ISn't A numBER!?!?! Why ARE yOu sO DUmB????????!!!!!", "NuMBERS ONlY!?!!? yOU SUCK aT mATH!!!"]


# Game start
system("cls")

winsound.PlaySound("groove-strings.wav", winsound.SND_ASYNC)

try:
	game = input(f"{bcolors.FAIL}{bcolors.BOLD}\tMATH-KILLER\n\n{bcolors.ENDC}[PRESS ENTER TO START GAME]\n")

	if game == "":
		winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
		system("cls")
	else:
		system("cls")
		winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
		exit()
except KeyboardInterrupt:
	system("cls")
	exit()


while True:
	try:
		problem = f"{randrange(1, i)} * {randrange(1, i)}"
		answer = eval(problem)
		
		system("cls")
		print(f"{bcolors.UNDERLINE}CURRENT PROBLEM: {questions_answered + 1} | Health: {health}{bcolors.ENDC}\n")

		try:
			user = int(input(f"{bcolors.UNDERLINE}{problem}{bcolors.ENDC} = "))
		except ValueError:
			system("cls")

			print(f"{bcolors.UNDERLINE}{bcolors.FAIL}CURRENT PROBLEM: {questions_answered + 1} | Health: DEAD{bcolors.ENDC}\n")
			print(f"{bcolors.UNDERLINE}{bcolors.FAIL}{problem} = INVALID NUMBER!!!{bcolors.ENDC}")

			winsound.PlaySound("groove-marimba.wav", winsound.SND_ASYNC)
			sleep(0.5)
			print(choice(type_error_qoutes))
			sleep(2)
			system("cls")
			print(f"{bcolors.UNDERLINE}{bcolors.FAIL}CURRENT PROBLEM: {questions_answered + 1} | Health: DEAD{bcolors.ENDC}\n")
			print("YOU LOSE...")
			print(f"Questions answered: {questions_answered}")
			input("\n[PRESS ANY KEY TO CONTINUE]")
			system("cls")
			break


		if user == answer:
			system("cls")
			print(f"CURRENT PROBLEM: {questions_answered + 1} | Health: {bcolors.UNDERLINE}{bcolors.OKGREEN}{bcolors.BOLD}{health}{bcolors.ENDC}\n")
			print(f"{bcolors.UNDERLINE}{bcolors.OKGREEN}{bcolors.BOLD}{problem} = {user}{bcolors.ENDC}")
			winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
			print(choice(correct_qoutes))
			sleep(0.5)
		else:
			health -= dif * 5
			system("cls")
			
			if health <= 0:
				print(f"{bcolors.UNDERLINE}{bcolors.FAIL}CURRENT PROBLEM: {questions_answered + 1} | Health: DEAD\n")
			else:
				print(f"CURRENT PROBLEM: {questions_answered + 1} | Health: {bcolors.FAIL}{bcolors.UNDERLINE}{health}{bcolors.ENDC}\n")
			

			print(f"{bcolors.FAIL}{bcolors.UNDERLINE}{problem} = {user}{bcolors.ENDC}")
			winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)
			
			if health <= 0:
				winsound.PlaySound("groove-marimba.wav", winsound.SND_ASYNC)
			
			sleep(0.5)
			print(f"The answer was {answer}.")
			sleep(0.5)
			print(f"{choice(wrong_quotes)}")
			sleep(0.5)
			print(f"-{dif*5}, Your health is now: {health}")

			if health <= 0:
				sleep(0.5)
				print("YOU ARE NOW DEAD...")
			sleep(2)

		dif += 1
		i += 1
		questions_answered += 1

		if health <= 0:
			system("cls")
			print(f"{bcolors.UNDERLINE}{bcolors.FAIL}CURRENT PROBLEM: {questions_answered + 1} | Health: DEAD{bcolors.ENDC}\n")
			sleep(0.5)
			print(choice(teacher_quote))
			sleep(0.5)
			print(choice(teacher_finish))
			sleep(0.5)
			rematch = input(f"{choice(teacher_rematch)}\n> ").lower()

			if "y" in rematch:
				winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
				system("cls")
				questions_answered = 0
				health = 50
				i = 5
				dif = 1
			else:
				system("cls")
				print(f"{bcolors.UNDERLINE}{bcolors.FAIL}CURRENT PROBLEM: {questions_answered + 1} | Health: DEAD{bcolors.ENDC}\n")
				print("YOU LOSE...")
				print(f"Questions answered: {questions_answered}")
				input("\n[PRESS ANY KEY TO CONTINUE]")
				system("cls")
				break
	except KeyboardInterrupt:
			system("cls")

			print(f"{bcolors.UNDERLINE}{bcolors.FAIL}CURRENT PROBLEM: {questions_answered + 1} | Health: DEAD{bcolors.ENDC}\n")
			print(f"{bcolors.UNDERLINE}{bcolors.FAIL}{problem} = ^C{bcolors.ENDC}")

			winsound.PlaySound("groove-marimba.wav", winsound.SND_ASYNC)
			sleep(0.5)
			print(choice(teacher_quote))
			sleep(2)
			system("cls")
			print(f"{bcolors.UNDERLINE}{bcolors.FAIL}CURRENT PROBLEM: {questions_answered + 1} | Health: DEAD{bcolors.ENDC}\n")
			print("YOU LOSE...")
			print(f"Questions answered: {questions_answered}")
			input("\n[PRESS ANY KEY TO CONTINUE]")
			system("cls")
			break