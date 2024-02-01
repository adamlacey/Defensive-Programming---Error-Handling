name = Input("Is your name Adam?: ")    # Syntax error 1: Capital I before "input"

if name == {"Yes", "yes"}               # Syntax error 2: Missing colon after "Yes"
print("Hello Adam!")                    # Logical error: indentation is not correct
elif name == "Maybe": 
    print(name_string("Who is this?"))  # Runtime error: inputted an unidentified variable (name_string
else:
    print("Sorry this program is for Adam only.")
