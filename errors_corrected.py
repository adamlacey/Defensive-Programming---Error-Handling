                                                                        # This example program is meant to demonstrate errors.
 
                                                                        # There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")                                   # Used () at the beginning and end of statement - Syntax error
print("\n")                                                             # Deleted the spaces before print function, put () at beginning and end of statement - Syntax error

                                                                        # Variables declaring the user's age, casting the str to an int, and printing the result
age_str = 24                                                            # Removed capitalised S from string. Also removed extea = and deleted spaces before string - Runtime error. Removed "years old" along with quotation marks around 24 - Syntax error
age = age_str                                                           # Deleted spaces before string along with int and input function - Runtime error
print(f"I'm {age} years old.")                                          # Deleted spaces before print function - Runtime error. Included f statement at beginning - Syntax error

                                                                        # Variables declaring additional years and printing the total years of age
years_from_now = 3.5                                                    # Removed quotation marks around 3. Added .5 at end of 3 as total = 330. - Syntax error
total_years = (age + years_from_now)                                    # Removed spaces from beginning of line 14 + 15 - Runtime error. Also inputted brackets - Syntax error
                                                                        # Included int function and brackets for age + years_from_now - Syntax error
print("\n")                                                             # Included newline
print(f"The total number of years: {total_years}")                      # Included brackets after print function - Syntax error

                                                                        # Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12                                         # Before changing years_from_now value, this would have been a Logial error when program ran as answer was not 330.
print("\n")                                                             # Included newline
print(f"In 3 years and 6 months, I'll be {total_months} months old.")   # Included brackets after print function - Syntax error. Removed +'s - Runtime error
                                                                        # Also included f statement and {} around total_months - Syntax error

                                                                        #HINT, 330 months is the correct answer

