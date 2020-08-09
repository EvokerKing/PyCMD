from os import system
import os.path
from termcolor import colored
import colorama

colorama.init()

def clear():
	system("cls")
def cp(text, col):
    print(colored(text, col))

if os.path.isdir("files") == False:
	system("md files")
clear()
cp("PyCMD V1.0", "yellow")
print()
cp("Use the HELP command for a list of commands and what they do.", "yellow")
print()
while True:
	query = input(colored(">>>  ", "magenta"))
	if query.lower() == "cls":
		clear()
	elif query.lower() == "cmd" or query.lower() == "exit":
		system("cmd")
	elif query.lower() == "date":
		mystr = system('date')
		print(str(mystr))
	elif query.lower() == "del":
		delquery = input("del:  ")
		system("cd files & del {}".format(delquery))
	elif query.lower() == "dir":
		dirquery = input("dir:  ")
		system("cd files & dir {}".format(dirquery))
	elif query.lower() == "help":
		cp("Use command HELP <command> for help with a certain command\n", "yellow")
		cp("cls     Clears the screen", "cyan")
		cp("cmd     Exits PyCMD", "cyan")
		cp("exit    Exits PyCMD", "cyan")
		cp("date    Displays or sets the date", "cyan")
		cp("del     Deletes one or more files", "cyan")
		cp("dir     Shows all files and subdirectories in a directory", "cyan")
		cp("help    Lists all commands and what they do", "cyan")
		cp("md      Creates a directory", "cyan")
		cp("move    Moves a directory or file", "cyan")
		cp("mkdir   Creates a directory", "cyan")
		cp("rd      Deletes a directory", "cyan")
		cp("ren     Renames a file", "cyan")
		cp("rename  Renames a file", "cyan")
		cp("rmdir   Deletes a directory", "cyan")
		cp("time    Displays or sets the time", "cyan")
		cp("title   Sets the title of the window", "cyan")
		cp("type    Displays the contents of a text file", "cyan")
		cp("ver     Displays the PyCMD version", "cyan")
		cp("edit    Used for editing text files", "cyan")
	elif query.lower() == "md" or query.lower() == "mkdir":
		mdquery = input("md:  ")
		system("cd files & md {}".format(mdquery))
	elif query.lower() == "move":
		movequeryfrom = input("from:  ")
		movequeryto = input("to:  ")
		system("cd files & move {0} {1}".format(movequeryfrom, movequeryto))
	elif query.lower() == "rd" or query.lower() == "rmdir":
		rdquery = input("rd:  ")
		system("cd files & rd {}".format(rdquery))
	elif query.lower() == "ren" or query.lower() == "rename":
		renfrom = input("from:  ")
		rento = input("to:  ")
		system("cd files & ren {0} {1}".format(renfrom, rento))
	elif query.lower() == "time":
		system("time")
	elif query.lower() == "title":
		titlequery = input("title:  ")
		system("title {}".format(titlequery))
	elif query.lower() == "type":
		typequery = input("type:  ")
		system("cd files & type {}".format(typequery))
	elif query.lower() == "ver":
		cp("PyCMD V1.0", "yellow")
	elif query.lower() == "edit":
		editquery = input("edit:  ")
		try:
			system("cd files & notepad {}".format(editquery))
		except:
			cp("Notepad is not installed on this device.", "red")
	elif query.lower() == "help cls":
		cp("cls", "cyan")
		cp("\nClears the sreen", "cyan")
	elif query.lower() == "help cmd" or query.lower() == "help exit":
		cp("cmd", "cyan")
		cp("exit", "cyan")
		cp("\nExits PyCMD", "cyan")
	elif query.lower() == "help date":
		cp("date", "cyan")
		cp("\nDisplays or sets the date", "cyan")
		cp("\nResult:", "cyan")
		cp("\nThe current date is: <weekday> <month>/<day>/<year>", "cyan")
		cp("Enter the new date: (mm-dd-yy) <[input]>", "cyan")
	elif query.lower() == "help del":
		cp("del", "cyan")
		cp("\nDeletes one or more files", "cyan")
		cp("\nResult:", "cyan")
		cp("\ndel:  <[input]>", "cyan")
	elif query.lower() == "help dir":
		cp("dir", "cyan")
		cp("\nShows all files and subdirectories in a directory", "cyan")
		cp("\nResult:", "cyan")
		cp("\ndir: <[input]>", "cyan")
	elif query.lower() == "help md" or query.lower() == "help mkdir":
		cp("md", "cyan")
		cp("mkdir", "cyan")
		cp("\nCreates a directory", "cyan")
		cp("\nResult:", "cyan")
		cp("\nmd:  <[input]>", "cyan")
	elif query.lower() == "help move":
		cp("move", "cyan")
		cp("\nMoves a directory or file", "cyan")
		cp("\nResult:", "cyan")
		cp("\nfrom:  <[input]>", "cyan")
		cp("to:  <[input]>", "cyan")
	elif query.lower() == "help rd":
		cp("rd", "cyan")
		cp("\nDeletes a directory", "cyan")
		cp("\nResults:", "cyan")
		cp("\nrd:  <[input]>", "cyan")
	elif query.lower() == "help ren" or query.lower() == "help rename":
		cp("ren", "cyan")
		cp("rename", "cyan")
		cp("\nRenames a file", "cyan")
		cp("\nResults:", "cyan")
		cp("\nfrom:  <[input]>", "cyan")
		cp("\nto:  <[input]>", "cyan")
	elif query.lower() == "help rmdir":
		cp("rmdir", "cyan")
		cp("\nDeletes a directory", "cyan")
		cp("\nResults:", "cyan")
		cp("rmdir:  <[input]>", "cyan")
	elif query.lower() == "help time":
		cp("time", "cyan")
		cp("\nDisplays or sets the time", "cyan")
		cp("\nResults:", "cyan")
		cp("\nThe current time is: <hour>:<minute>:<second>", "cyan")
		cp("Enter the new time: <[input]>", "cyan")
	elif query.lower() == "help title":
		cp("title", "cyan")
		cp("\nSets the title of the window", "cyan")
		cp("\nResult:", "cyan")
		cp("\ntitle:  <[input]>", "cyan")
	elif query.lower() == "help type":
		cp("title", "cyan")
		cp("\nDisplays the contents of a text file", "cyan")
	elif query.lower() == "help ver":
		cp("ver", "cyan")
		cp("\nDisplays the PyCMD version", "cyan")
	elif query.lower() == "help edit":
		cp("edit", "cyan")
		cp("\nUsed for editing text files", "cyan")
		cp("\nNotes:", "cyan")
		cp("\nYou can enter a file that is not real and it will create it for you.", "cyan")
	else:
		print("\""+query+"\" is not a valid command.")
