import random

# Get guess
def get_guess():
    return list(input("What is your guess? "))

# Generate computer code 123
def generate_code():
    digits = [str(x) for x in range(10)]

    #Shuffle the digits  and then grab the first three
    random.shuffle(digits)
    return digits[:3]

#Geneate the clues
def gen_clues(code,user_guess):
    if user_guess == code:
        return ["Code Cracked!"]

    clues = []
    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("MATCH")
        elif num in code:
            clues.append("CLOSE")
    if clues == []:
        return ["NOPE"]
    else:
        return clues

#Run game logic
print("Welcome Code Breaker!")
secret_code = generate_code()
clue_list = []
while clue_list != ["Code Cracked!"]:
    guess = get_guess()
    clue_list = gen_clues(guess,secret_code)
    print("Here's the result:")
    if clue_list == "Code Crakced!":
        print(clue_list[0])
        break
    for clue in clue_list:
        print(clue)
