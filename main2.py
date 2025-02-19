#for finding the command line arg
from sys import argv

#the two modules for this to work
import pastebinapi2
import pokeapi2

#finds and verifys commandline arg
def getPokeName():

    if (len(argv) > 1):
        return argv[1]
    else:
        print("Please provide a pokemon name in commandline")
        return 0
    
def main():

    pokeNameOrID = getPokeName()

    #returns a dictionary from the pokeapi function where we get the data about a pokemon
    pokeData = pokeapi2.getPokemon(pokeNameOrID)

    #creates all the arguments passed to the paste api fuinction
    pasteTitle = f"{pokeData['name'].capitalize()}'s Abilities" 
    pasteText = ""
    for ability in pokeData['abilities']:
        pasteText += f'~ {ability['ability']['name']}\n'
    pasteExpiration = '1M' 
    pasteListed=False
    pasteURL = pastebinapi2.postNewPaste(pasteTitle, pasteText, pasteExpiration, pasteListed)
    #prints paste url returned
    print(pasteURL)
    
    return



if __name__ == "__main__":
    main()