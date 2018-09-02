import os
import sys

result = ""
final_epi=""
dir_listing = []
base_listing = []

os.system("cls")
print("Specify First Split Point")
first_split = str(input())

os.system("cls")
print("Specify Second Split Point")
second_split = str(input())

os.system("cls")
print("Specify Series Name")
series_name = str(input())

os.system("cls")
print("Specify Path (Be sure to escape special characters!!)")
dir_listing.append(input())
while result != "N" or result != "n":
	os.system("cls")
	print("Another path? (Be sure to escape special characters!!)(N to end)")
	result = input()
	if result != "N" and result != "n":
		dir_listing.append(result)
		print(result)
	else:
		break

os.system("cls")
if len(dir_listing) == 1:
	print("Specify final episode")
	final_epi = int(input())

os.system("cls")
base_listing.append(0)
os.system("cls")
print("Specify where to cut the episodes")
while result != "N" or result != "n":
	print("Another episode cut? (N to end)")
	result = input()
	os.system("cls")
	if result.isnumeric():
		base_listing.append(int(result))
	elif result.isnumeric() == False or result == "N" or result == "n":
		break

os.system("cls")
print("First Spilt : \"" + first_split + "\"")
print("Second Spilt : \"" + second_split + "\"")
print("Series Name : \"" + series_name + "\"")
print("Directory lists is/are :")
for j in range(len(dir_listing)):
	print ("{number}. \"{path}\"".format(number=j+1, path=dir_listing[j]))
if len(dir_listing) == 1:
	print("Final Episode number : \"{episode_num}\"".format(episode_num=final_epi))
	print("")
	print("Single directory processing")
	single_dir = True
	staticdirectory = dir_listing[0]
else:
	single_dir = False
print("")
list=values = ','.join(str(v) for v in base_listing)
print("Episodes are separated at these episodes numbers : \"" + list + "\"")
print("Are these values correct?")
result = input()
if result == "N" or result == "n":
	os.system("cls")
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

def degenerate_rename(dest, baselist, series, final):
	os.chdir(dest)
	dictionary_rename = {}
	baselist.append(final)
	for j in range(len(baselist)-1):
		for k in range(int(baselist[j+1])-int(baselist[j])):
			dictionary_rename[str(baselist[j]+k+1)] = ("S"+str(j+1).zfill(2)+"E"+str(k+1).zfill(2))
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
	snum = i+1
	if single_dir: 
		degenerate_rename(staticdirectory, base_listing, series_name, final_epi)
		os.system("cls")
		print("Done renaming")
	else: 
		rename(dest, base, snum, series_name)
		os.system("cls")
		print("Done renaming")



