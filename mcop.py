import argparse
import os
files_removed = 0
i = 0
parser = argparse.ArgumentParser()
parser.add_argument("path", help="File path for players folder")
parser.add_argument("initial_items", type=int, help="Number of inventory slots to be igonred, as in initial items")
args = parser.parse_args()
directory = args.path
initialItems = args.initial_items
for filename in os.listdir(directory):
    fullPath = directory + '/' + filename
    file = open(fullPath, "r")
    while(1):
        test = file.read(i)
        if test == "Empty":
            i += 1
        else:
            print("Player", file, "not cleared")

        file.close()
        if i == 43:
            print("Player", file, "deleted")
            os.remove(fullPath)
            files_removed += 1

            break




print("Player clearing process completed.", files_removed, "players deleted.")
