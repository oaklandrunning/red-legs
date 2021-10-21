import os 
cwd = os.getcwd()

y = 0
print("Current Working Directory: ", cwd)
f = open("./red-legs/data.dat", "r")

for a in f:
    totalzeros = a.count("0")
    totalones = a.count("1")
    print(totalzeros, totalones)
    if (totalzeros % 3 == 0) or (totalones % 2 == 0):
        print("true")
        y += 1
    else:
        print("nope")
    
print(y)
f.close()
