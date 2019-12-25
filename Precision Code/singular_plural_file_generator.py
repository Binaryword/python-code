from pattern.en import singularize

## creating singular and plural method


## helper method to create singular and plural file

singular_list = []
plural_list = []

def creatPluralSingularFile(word):
    if word == singularize(word):
        singular_list.append(word)
    else:
        plural_list.append(word)



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

    user_input = input("Enter a word to search for :")

    if user_input == "_exit":
        break

    # check which file i.e (singular or plural file) word can be find....
    isSingular = False

    for word in singular_list:
        if word == user_input:
            print("\nWord is singular")
            isSingular = True
            break
    else:
        foundInSingular = False
        print("\t Word not found in sugular file")

            

    # check for plurality if word not found in singular file....
    for word in plural_list:
        if not isSingular:
            if word == user_input:
                print("Word is plural")
                break
    else:
        foundInPlural = False
        print("\t Word not found in plural file")


    if not foundInSingular and  not foundInPlural:
        print("\n\nword do not exit....")
        print("seggestion algo goes here")


print("program terminated")

