"""
Sport Results - Version 3
Tottenham are playing Liverpool in the Champions League.
Include- The Winning team won by how many runs?
"""
print("************* Champions League ******************")
print("********* Tottenham VS Liverpool ****************\n")
Tottenham_score = int(input("What's the total score of Tottenham?: "))
Liverpool_score = int(input("What's the total score of Liverpool?: "))
print('-'*50)
if Tottenham_score == Liverpool_score:
    print("\nMatch is Draw!!!!")
elif Tottenham_score > Liverpool_score:
    print(f"\nTottenham Won by {Tottenham_score-Liverpool_score} runs!!!!")
else:
    print(f"\nLiverpool Won by {Liverpool_score - Tottenham_score} runs!!!!")
"""
Test case 1: 
Input- Tottenham- 5, Liverpool - 3 
Expected Output- Tottenham Won by 2 runs!!!
Test Case 2: 
Input- Tottenham- 1, Liverpool- 5 
Expected Output- Liverpool Won by 4 runs!!!
Test Case 3: 
Input- Tottenham- 5, Liverpool- 5 
Expected Output- Match is Draw!!!
"""