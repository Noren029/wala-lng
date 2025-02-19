import requests

def getPokemon(pokeNameOrID):

    #converts passed param to lowercase and strips the whitespace before and after it
    print("Converting name or id given to string and formating...")
    pokeNameOrID = str(pokeNameOrID).strip().lower()
    print("The formated argument passed is:", pokeNameOrID)

    #http get reqest to get the info of pokemon passed
    print("Getting data of pokemon specified...")
    pokeData = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokeNameOrID}/")

    #if program runs return the pokemon data as a dictionary else say there was an error and return code
    if (pokeData.status_code == requests.codes.ok):
        print("Recived data okay returning dictionary...")
        return pokeData.json()
    else:
        print("Recived error when communicating with page. Ending script...")
        print("error code: ", pokeData.status_code)
        return 0

if __name__ == "__main__":
    print("please import this as a module to your main code")

