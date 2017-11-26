import os
files_removed = 0
directory = input("Directory to clear players: ")
for filename in os.listdir(directory):
    fullPath = directory + '/' + filename
    file = open(fullPath, "r")
    line = 18
    while(line < 42):
        test = file.read(i)
        if test == "Empty":
            i += 1
        else:
            print("Player", file, "not cleared")

        file.close()
        if line == 43:
            print("Player", file, "deleted")
            os.remove(fullPath)
            files_removed += 1

            break




print("Player clearing process completed.", files_removed, "players deleted.")
