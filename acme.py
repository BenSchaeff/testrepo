#Ben Schaeffer
#Jamf Internship Assessment


#imports
import requests
from art import text2art
import json


#FUNCTIONS
def getAnimal(chosenAnimal):
    #set chosen animal as query paramater
    queryParam = {
    "animal" : chosenAnimal
    }

    #get chosen animal using query paramater
    response = requests.get("https://mcxlmpfy3k.execute-api.us-east-1.amazonaws.com/dev/animals", params=queryParam)



    #if given bad input, tell user 
    if (response.status_code == 404):
        print("Animal not recognized! Please try again!")
     
    else: #on good input
        #turn response into string and prepare for .loads()
        string = json.dumps(response.json())

        #load string containing animal AND detail info into responseDict 
        responseDict = json.loads(string)

        #grab animal variable and print it to user 
        animal = responseDict["animal"]
        print("Showing details for " + animal)
        print("----------")
        
        #get ONLY detail info and put it in new dictionary called detailDict
        detailsDict = responseDict["details"]
 
        #iterate through detail list and print to user
        for attribute in detailsDict:
            print(attribute + " : " + detailsDict[attribute])

        #printing space for user clarity and ease of use
        print("----------")
        #print("Press 'Enter' to continue!")
        temp = input("Press 'Enter' to continue!")




#function to display all animals
def getAllAnimals():
    #get all animals from api
    response = requests.get("https://mcxlmpfy3k.execute-api.us-east-1.amazonaws.com/dev/animals")
    
    #turn the response into a string and prepare for .loads()
    string = json.dumps(response.json())

    #use .loads() to load string into a dictionary
    animalDict = json.loads(string)

    #get list of all animals under "animals" key in dict
    animalList = animalDict["animals"]

    #print out all animals to user 
    for animal in animalList:
        print(animal)


#MAIN
art = text2art("Acme.com")
print(art)

selectedAnimal = ""
while(selectedAnimal != "quit"):


    #display list of current animals
    print("Our current animals are:")
    print("---------")
    getAllAnimals()
    print("---------")

    #get user input
    print("What animal would you like to learn about? (Type 'quit' to exit application)")
    selectedAnimal = input()

    #conver to lowercase to avoid human typing errors
    selectedAnimal = selectedAnimal.lower()
    
    #only fetch animal on valid animal input
    if (selectedAnimal != "quit"):
        getAnimal(selectedAnimal)
    

