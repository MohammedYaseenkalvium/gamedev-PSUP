import random

def Flames():
    n1 = input("Please enter the first name").lower()
    n2 = input("Please enter the second name").lower()
    # now we have taken input from the user

    character = []
    for char in n1:
        if char not in n2:
            character.append(char)

    for char in n2:
        if char not in n1:
            character.append(char)
        
    flames = ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Siblings"]
    index = 0

    if len(character)>0:
        index = random.randint(0,len(character)-1)  
    if len(character)==0 or index>=len(flames):
        index = 0

    return flames[index],n1,n2

res,n1,n2 = Flames()
print(f"Flames for {n1} and {n2} is:{res}")