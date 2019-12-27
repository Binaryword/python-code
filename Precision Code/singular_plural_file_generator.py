from pattern.en import singularize
import enchant
from nltk.corpus import WordNetLemmatizer



## creating singular and plural method


## helper method to create singular and plural file

## program initialization goes here 
singular_list = []
plural_list = []
diction = enchant.Dict("en_Us")

def creatPluralSingularFile(word):
    if word == singularize(word):
        singular_list.append(word)
    else:
        plural_list.append(word)


def spellChecker(word):
     if diction.check(word):
        print("Spelt Correctly\n")
        return True
     else:
        print("Spelt Incorrectly")
        print("Do you mean->> " , diction.suggest(word) , "\n")
        return False


def wordInflationDetector():
    print("inflection function")
    # An helper function to detect inflection routing
    # 1. pass user input into routing..
    # 2. get meaning and neccessary details if singular ..
    # 3. if plural stemmatize user input and get meaning ..
    # 4. if incorect word check lema ..
    # 5. if lema exit enter inflation detection ...
    # 6. loop through each word and cut off last index [knivesss]..
    # 7. check new list if word is correct [knives]..
    # 8. create list of inflected words [ssn]..
    # 9. pass user input into routing..
    # 10. pass user input into routing..

    
def printWordSemantic():
    print("print ... word meaning...")
    

raw_file = open("words_alpha.txt" , "r")

word_file = raw_file.readlines()
p_word = []
words = word_file[:]


for word in words:
    p_word.append(word[:-1])
    creatPluralSingularFile(word[:-1])
else:
    print("loop completed")
    print(len(p_word))


print(singular_list[:10])
print(plural_list[:10])
print(len(singular_list))
print(len(plural_list))

runProgram = True
foundInSingular = False
foundInPlural = False 
 

while runProgram == True:

    foundInSingular = True
    foundInPlural = True

    text = input("Enter a word to search for :")
    user_input = text.lower()
    
    if user_input == "_exit":
        break

    # check which file i.e (singular or plural file) word can be find....
    isSingular = False

    for word in singular_list:
        if word == user_input:
            print("Word is singular")
            if spellChecker(user_input):
                # call the helper method to display data..
                pass
            else:
                # call the word inflation algorithm
                pass
            isSingular = True
            break
    else:
        foundInSingular = False
       # print("\t Word not found in sugular file")

            

    # check for plurality if word not found in singular file....
    for word in plural_list:
        if not isSingular:
            if word == user_input:
                print("Word is plural")
                if spellChecker(user_input):
                    # call the helper method to display data..
                    pass
                else:
                    # call the word inflation algorithm
                    pass
                break
    else:
        foundInPlural = False
       # print("\t Word not found in plural file")


    #second word validation
   

    if not foundInSingular and  not foundInPlural:
        
        if not diction.check(user_input):
           print("Incorrect spelling : do you mean->> " , diction.suggest(user_input))
           


print("\n\n********* program terminated *********")

