import random
class Bank:
    customers = []
    def __init__(self):
        self.bank = "HDFC"
        self.branch = 'HDFC, Rohini'
        self.ifsc = 101010
        self.accNo = random.randint(1000,1000000)
        self.currentUser = {}

    def storeDefault(self):
        self.currentUser['account_num'] = self.accNo
        self.currentUser['branch'] = self.branch
        self.currentUser['IFSC'] = self.ifsc
        self.customers.append(self.currentUser)

    def showAll(self):
        print(self.customers)

class Customer(Bank):

    def __init__(self, name, age, occ):
        self.cust_name = name
        self.cust_age = age
        self.cust_occ = occ
        super().__init__() # calling parent class constructor

    def storeCustomer(self):
        self.currentUser['name'] = self.cust_name
        self.currentUser['age'] = self.cust_age
        self.currentUser['occupation'] = self.cust_occ

    def showCurrentCustomer(self):
        print("Welcome to {} bank".format(self.bank))
        print("Branch is",self.branch)
        print("Details of Customer : ")
        print(self.currentUser)
        print("=============================")

obj = Customer('Ram',40,'Emp')
obj.storeDefault()
obj.storeCustomer()
obj.showCurrentCustomer()

obj_2 = Customer('Shyam',20,'Student')
obj_2.storeDefault()
obj_2.storeCustomer()
obj_2.showCurrentCustomer()