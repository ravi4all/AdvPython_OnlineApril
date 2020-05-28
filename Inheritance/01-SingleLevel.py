import random
class Bank:
    def __init__(self):
        self.bank = "HDFC"
        self.branch = 'HDFC, Rohini'
        self.ifsc = 101010
        self.accNo = random.randint(1000,1000000)
        self.customer = []

    def storeCustomer(self):
        self.customer.append([self.accNo, self.branch, self.ifsc])

class Customer(Bank):

    def __init__(self, name, age, occ):
        self.cust_name = name
        self.cust_age = age
        self.cust_occ = occ
        super().__init__() # calling parent class constructor

    def show(self):
        print("Welcome to {} bank".format(self.bank))
        print("Branch is",self.branch)
        print("Details of Customer : ")
        self.customer.append([self.cust_name, self.cust_age, self.cust_occ])
        print(self.customer)
        print("=============================")

obj = Customer('Ram',40,'Emp')
obj.storeCustomer()
obj.show()

obj_2 = Customer('Shyam',20,'Student')
obj_2.storeCustomer()
obj_2.show()