# Predict the output
class SafeStorage:
    __data = None
    def get(self):
        return self.__data
    def put(self, data):
        self.__data = data

safe = SafeStorage()    # Creating instance of class SafeStorage and store it in object safe
safe.put("Anakonda")    # call the put function of safe object at assign __data to 'Anaconda'
x = safe.get()          # call get to get the value of __data('Anaconda') and assign it to x
safe.put("Boaorm")  # Now calling put function with 'Boaorm' that assigns __data to 'Boaorm'
y = safe.get()      # Here call get() function to get the value of __data that is 'Boaorm' now
print(x, y)         # display x & y, x is 'Anaconda' and y is 'Boaorm'

# Run the code to see output
# The output appeared at terminal
# Anakonda Boaorm