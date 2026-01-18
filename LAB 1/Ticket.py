"""
Calculating the balance amount and share to each person after Buying a ticket
"""
Ticket_Price = 100 # ticket price
Total_Money = 200 # money in your pocket
print(f"\nTotal Money:   {Total_Money:.2f} kr")
print(f"Ticket Price:  {Ticket_Price:.2f} kr")
print(f"\nAfter buying a ticket there will be {Total_Money - Ticket_Price:.2f} kronor left.")
share = (Total_Money - Ticket_Price)/2
print(f"\nEach person's will get a share of: {share:.2f} kr")