# class Line(object):
    
#     def __init__(self,coord1,coord2):
#         self.coor1 = coord1
#         self.coor2 = coord2
    
#     def distance(self):
#         x1,y1 = self.coord1
#         x2,y2 = self.coord2
#         return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
#     def slope(self):
#         x1,y1 = self.coord1
#         x2,y2 = self.coord2
#         return (y2-y1)/(x2-x1)

# coordinate1 = (3,2)
# coordinate2 = (8,10)

# li = Line(coordinate1,coordinate2)
# print(li.distance(),li.slope())




# class Cylinder:
    
#     def __init__(self,height=1,radius=1):
#         self.height = height
#         self.radius = radius
        
#     def volume(self):
#         return self.height*3.14*(self.radius)**2
    
#     def surface_area(self):
#         top = 3.14 * (self.radius)**2
#         return (2*top) + (2*3.14*self.radius*self.height)
# c = Cylinder(2,3)
# print(c.volume(),c.surface_area())


class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'
        
    def deposit(self,dep_amt):
        self.balance += dep_amt
        print('Deposit Accepted')
        
    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')

acct1 = Account('Jose',100)

print(acct1)

print(acct1.owner,acct1.balance)