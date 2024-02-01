                                                                                            # This example program is meant to demonstrate errors.
 
                                                                                            # There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "lion"                                                                             # Included "" around lion - Syntax error
animal_type = "cub"
number_of_teeth = "16"

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth." # Included f statement at beginning of string so variables above would print - Runtime error
print(full_spec)                                                                             # Included brackets after print function - Syntax error


