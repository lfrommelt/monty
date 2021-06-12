class Vector2D:
    # Include your methods from task 4 here. Only __init__ is really required.
        
    def __iter__(self):
        # YOUR CODE HERE
        
class Vector2D_Iterator:
    def __init__(self, vector):
        # Our iterator does not have to work with anything but Vector2D-objects
        if not type(vector)==Vector2D:
            raise TypeError           
        # YOUR CODE HERE
        
    def __iter__(self):
        return self
              
    def __next__(self):
        # YOUR CODE HERE
     
my_V2D=Vector2D(4,2)

#Make sure the object's values can still be accessed like before
print("x-value:", my_V2D.x)

#test the iteration
for item1 in my_V2D:
    for item2 in my_V2D:
        print(item1, item2)   

'''
Intended output:
x-value: 4
4 4
4 2
2 4
2 2
'''
