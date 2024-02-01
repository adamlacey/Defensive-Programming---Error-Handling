def simpson_character(character_name):                  # Define Simpson character with Simpsons names below which is the family.
    simpson_family = ["Homer", "Marge", "Bart", "Lisa", "Maggie"]
    
    if character_name in simpson_family: 
        return True
    else:
        return "False"                                  # Incorrect return value for Simpsons characters who are not in the family.
    
def main():
    print("The Simpsons Family")
    
    character_name = input("Enter a character name: ")  # User inputs a member of The Simpsons family
    
    if simpson_character(character_name):               # To see if the character is in The Simpsons family. Statement prints either is in family or is not.
        print(f"{character_name} is a member of The Simpsons family.")
    else:
        print(f"{character_name} is not a member of The Simpsons family.")

main()
        
