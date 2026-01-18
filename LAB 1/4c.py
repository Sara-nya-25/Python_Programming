"""
Time taken to reach the destination based on the speed of the driver
Convert in whole hours and minutes using // and % .
"""

distance = 470
speed = input("Enter the average speed per hour: ")
distance = float(distance)
speed = float(speed)
time_mins = int((distance / speed) *60)
hours = time_mins // 60
minutes = time_mins % 60
print(f"I takes {hours} hours and {minutes} minutes to travel from Stockholm to Gothenburg ")


