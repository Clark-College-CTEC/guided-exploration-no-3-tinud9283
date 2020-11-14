# Guided Exploration No. 3
# Johnathan Gibert
'''this allows the python random library to be used'''
import random
'''this is creating a variable that is an empty list'''
possible_names = []
'''this stores the names created into a text file for later'''
outputFile = open('rap-names-output.txt', 'w')
with open('rap-names.txt', 'r') as dataFile:
    '''this creates a loop'''
    for name in dataFile:
        '''this is appending names into the empty list we created earlier'''
        possible_names.append(name.rstrip())
'''this code is asking the user how many names they would like to create and assigning it to a variable'''
count = int(input('How many rap names would you like to create? '))
'''this is asking how many parts to the name they want and then assigning it to a variable'''
parts = int(input('How many parts should the name contain? '))
for i in range(count):
    '''this code creates an empty variable to be manipulated (used to store names)'''
    name_parts = []
    '''this code creates a loop to actually stitch together the names'''
    for j in range(parts):
        '''this pieces the names together depending on how many parts you want'''
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])
        '''this joins the random parts brought in to the name and writes them piece by piece'''
        outputFile.write(f"{' '.join(name_parts)}\n")
        '''this prints out the name being created when a new part is added'''
        print(f"{' '.join(name_parts)}")
outputFile.close()
