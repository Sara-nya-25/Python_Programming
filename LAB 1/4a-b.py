#Time taken to reach the destination based on the speed of the driver

distance = 470
speed = input("Enter the average speed per hour: ")
distance = float(distance)
speed = float(speed)
time_taken = distance / speed
print(f"I takes {time_taken:.2f} hours to travel from Stockholm to Gothenburg ")
print(f"I takes {time_taken * 60:.2f} hours to travel from Stockholm to Gothenburg ")

