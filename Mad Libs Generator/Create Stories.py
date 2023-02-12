def check_input(input_value):
    try:
        input_value = int(input_value)
        if input_value > 0:
            return True
        else:
            print("The input must be an integer greater than zero.")
            return False
    except ValueError:
        print("The input must be an integer.")
        return False

n = input("Enter an integer greater than zero: ")

while (check_input(n) == False):
    n = input("Enter an integer greater than zero: ")
else:
    n = int(n)


loop = 1

while (loop < n):
#All the questions that the program asks the user
    noun = input("Choose a noun: ")
    p_noun = input("Choose a plural noun: ")
    noun2 = input("Choose a noun: ")
    place = input("Name a place: ")
    adjective = input("Choose an adjective (Describing word): ")
    noun3 = input("Choose a noun: ")
#Displays the story based on the users input
    print("------------------------------------------")
    print("Be kind to your",noun,"- footed", p_noun)
    print("For a duck may be somebody's", noun2,",")
    print("Be kind to your",p_noun,"in",place)
    print("Where the weather is always",adjective,".")
    print()
    print("You may think that is this the",noun3,",")
    print("Well it is.")
    print("------------------------------------------")

    loop = loop + 1