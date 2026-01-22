"""
Sport Results- Version- 1
Tottenham are playing Liverpool in the Champions League.
Write a program that asks the user how many goals each team scored, and tells which team won.
"""
print("************* Champions League ******************")
print("********* Tottenham VS Liverpool ****************\n")
Tottenham_score = int(input("What's the total score of Tottenham?: "))
Liverpool_score = int(input("What's the total score of Liverpool?: "))

if Tottenham_score > Liverpool_score:
    print("\nTottenham Won!!!!")
else:
    print("\nLiverpool Won!!!!")

# The problem here is if both the teams get same score then it will show the team in else block as Winner