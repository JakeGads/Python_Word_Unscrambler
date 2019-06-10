import itertools 
                    
def load_dictonary():
    dictonary = []
    with open('english.txt', 'r') as file:
        for line in file:
            line = line.replace('\n', '').lower()
            dictonary.append(line)
    
    return dictonary

def main(word = 'ewlloh'):
    word = word.lower()
    matches = []
    lettersList = []
    for i in word:
        lettersList.append(i.lower())

    dictonary = load_dictonary()

    perm = []

    for i in range(len(lettersList)):
        perm.append(itertools.permutations(lettersList, i + 1))

    file = open('unscrambled.txt', 'w+')
    
    for i in perm:
        for h in list(i):
            string = ''

            for j in h:
                string += j
            
            if string not in matches:
                if string in dictonary:
                    file.write(string + '\n')
                    matches.append(string)
        

    file.close()
    return matches



if __name__ == "__main__":
    print(main())