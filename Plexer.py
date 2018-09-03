import os
import sys
from os import name

result = ""
final_epi=""
dir_listing = []
base_listing = [0]
snum = ""

def clear():
	if name == 'nt': 
		_ = os.system('cls') 
	else: 
		_ = os.system('clear') 

clear()
print("Specify First Split Point")
first_split = str(input())

clear()
print("Specify Second Split Point")
second_split = str(input())

clear()
print("Specify Series Name")
series_name = str(input())

clear()
print("Specify Path (Be sure to escape special characters!!)")
dir_listing.append(input())
while result != "N" or result != "n":
	clear()
	print("Current Directory lists is/are :")
	for j in range(len(dir_listing)):
		print ("{number}. \"{path}\"".format(number=j+1, path=dir_listing[j]))
	print("\nAdd another path? (Be sure to escape special characters!!)(N to end)")
	result = input()
	if result != "N" and result != "n":
		dir_listing.append(result)
	else:
		break

clear()
if len(dir_listing) == 1:
	print("Specify final episode")
	final_epi = int(input())

clear()
while result != "N" or result != "n":
	print("Specify where to cut the episodes")
	list= ','.join(str(v) for v in base_listing)
	print("\nEpisodes are separated at these episodes numbers : \"" + list + "\"\n")
	print("Add another episode cut? (N to end)")
	result = input()
	clear()
	if result.isnumeric():
		base_listing.append(int(result))
	elif result.isnumeric() == False:
		break

clear()
print("Specify Starting Season Number\n (Default is S00)")
snum = str(input())
if snum == "":
	snum = 0
else:
	snum = int(snum)

clear()
print("First Spilt : \"" + first_split + "\"")
print("Second Spilt : \"" + second_split + "\"")
print("Series Name : \"" + series_name + "\"\n")
print("Directory lists is/are :")
for j in range(len(dir_listing)):
	print ("{number}. \"{path}\"".format(number=j+1, path=dir_listing[j]))
if len(dir_listing) == 1:
	print("\nFinal Episode number : \"{episode_num}\"\n".format(episode_num=final_epi))
	print("Single directory processing")
	single_dir = True
	staticdirectory = dir_listing[0]
else:
	single_dir = False
print("\nStaring Season Number : \"S{snum}\"".format(snum=str(snum).zfill(2)))
list= ','.join(str(v) for v in base_listing)
print("\nEpisodes are separated at these episodes numbers : \"" + list + "\"")
print("Are these values correct?")
result = input()
if result == "N" or result == "n":
	clear()
	sys.exit("User cancelled")

def rename(dest, base, snum, series):
	os.chdir(dest)
	filenames = os.listdir(os.getcwd())
	for file in filenames:
		ep = file.split(first_split)[1].split(second_split)[0]
		suffix = ""
		if ep[-1:].isalpha():
			suffix = ep[-1:]
			ep = ep[:-1]
		ep = int(ep)-base
		os.rename(file, series + " - S" + str(snum).zfill(2) + "E" + str(ep).zfill(2) + suffix + ".mkv")

def degenerate_rename(dest, baselist, series, final, snum):
	os.chdir(dest)
	dictionary_rename = {}
	baselist.append(final)
	for j in range(len(baselist)-1):
		for k in range(int(baselist[j+1])-int(baselist[j])):
			dictionary_rename[str(baselist[j]+k+1)] = ("S"+str(snum).zfill(2)+"E"+str(k+1).zfill(2))
		snum=snum+1
	filenames = os.listdir(os.getcwd())
	for file in filenames:
		ep = file.split(first_split)[1].split(second_split)[0]
		suffix = ""
		if ep[-1:].isalpha():
			suffix = ep[-1:]
			ep = ep[:-1]
		ep_str = dictionary_rename[str(int(ep))] + suffix
		os.rename(file, series + " - " + ep_str + ".mkv")


for i in range(len(dir_listing)):
	if len(dir_listing) != len(base_listing) and len(dir_listing) != 1: break # Soft check for bad config
	dest = dir_listing[i]
	base = base_listing[i]
	snum = snum+i
	if single_dir: 
		degenerate_rename(staticdirectory, base_listing, series_name, final_epi,snum)
	else: 
		rename(dest, base, snum, series_name)
	clear()
	print("Done renaming")



