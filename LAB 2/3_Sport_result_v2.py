"""
Sport Results- version-2
Tottenham are playing Liverpool in the Champions League.
 Find and Specify if the match is a Draw
"""
print("************* Champions League ******************")
print("********* Tottenham VS Liverpool ****************\n")
Tottenham_score = int(input("What's the total score of Tottenham?: "))
Liverpool_score = int(input("What's the total score of Liverpool?: "))
print('-'*50)
if Tottenham_score == Liverpool_score:  # this code fixes the logic error of previous code
    print("\nMatch is Draw!!!!")
elif Tottenham_score > Liverpool_score:
    print("\nTottenham Won!!!!")
else:
    print("\nLiverpool Won!!!!")
"""
Test case 1: 
Input- Tottenham- 5, Liverpool - 3 
Expected Output- Tottenham Won!!!
Test Case 2: 
Input- Tottenham- 1, Liverpool- 5 
Expected Output- Liverpool Won!!!
Test Case 3: 
Input- Tottenham- 5, Liverpool- 5 
Expected Output- Match is Draw!!!
"""