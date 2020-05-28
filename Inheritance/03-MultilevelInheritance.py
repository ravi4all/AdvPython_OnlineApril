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

class Employees(Customer):

    def __init__(self,name,age,acc_type,sal,company):
        self.name = name
        self.age = age
        self.occ = "Emp"
        self.acc_type = acc_type
        self.sal = sal
        self.company = company
        # super(Employees, self).__init__()
        super().__init__(self.name,self.age,self.occ)

    def storeEmp(self):
        self.currentUser['salary'] = self.sal
        self.currentUser['company'] = self.company
        self.currentUser['acc_type'] = self.acc_type

    # override
    def showCurrentCustomer(self):
        print("Welcome to {} bank".format(self.bank))
        print("Branch is", self.branch)
        print("Details of Customer : ")
        print(self.currentUser)
        print("=============================")
        self.checkLoanAvail()

    def checkLoanAvail(self):
        print("Loan option available for employees...")
        if self.sal >= 45000:
            print("Loan Available upto 50 Lac")
        elif self.sal >= 30000 and self.sal < 45000:
            print("Loan Available upto 30 Lac")
        else:
            print("Loan Available upto 10 Lac Only")

obj = Employees('Ram',34,'Saving',45000,'TCS')
obj.storeDefault()
obj.storeCustomer()
obj.storeEmp()
obj.showCurrentCustomer()

