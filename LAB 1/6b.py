# Find and display day of the week from today's date

from datetime import datetime, timedelta

print("\nPrinting Today's Date and Current time..........\n")
print(datetime.now())

# string format time method formats date object into a readable string
# and specifically extracts a value denoted, %A - extracts weekday name
day_name = datetime.now().strftime("%A")
print("Today is ", day_name)

print("\n Printing Date and time after seven days\n", datetime.now()+timedelta(days=7))