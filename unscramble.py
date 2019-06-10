try:
    from subprocess import call
    import itertools 
    from nltk.corpus import wordnet
except:
    pythons = ['python -m ', 'py -m ', 'python3 -m ', 'py3 -m ']
    pips = ['pip install ', 'pip3 install ']
    #defined pip packages
    pacakges = ['nltk']

    for pip in pips:
        for pacakge in pacakges:
            for python in pythons:
                try:
                    call(python + pip + pacakge, shell = True)
                except:
                    print(python + pip + pacakge + ' is not a valid command')
            
            try:
                call(pip + pacakge, shell = True)
            except:
                print(pip + pacakge + ' is not a valid command')
    
    from nltk.corpus import wordnet
    import nltk
    # nltk.download()
    input('3rd party libries added please download the \'wordnet\' lexicon (press d)\n<Enter> to continue')
                
    
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
    print(main(''))