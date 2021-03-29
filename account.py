# Alireza Bagherinia
# Student No : 960201110013

import datetime


class Account:

    __min_amount = 10
    __total_amount = 0
    __acc_num = 1020

    def __init__(self, Name, amount=__min_amount):
        self.setAccNo(Account.__acc_num)
        Account.__acc_num += 1
        self.__amount = amount
        self.setStatus(amount)
        Account.__total_amount += amount
        self.transList = []
        self.name = name 

    def setAccNo(self, accNo):
        self.__accNo = accNo

    def getAccNo(self):
        return self.__accNo

    def getAmount(self):
        return self.__amount

    def setStatus(self, m):
        if m >= Account.getMin_amount():
            self.__status = "Active"

        elif m == Account.getMin_amount() - 1:
            self.__status = "suspend"
        else:
            self.__status = "inactive"

    def getStatus(self):
        return self.__status

    def getRecord(self):
        return self.transList

    @staticmethod
    def getMin_amount():
        return Account.__min_amount

    @staticmethod
    def setMin_amount(m):
        if m > Account.__min_amount:
            Account.__min_amount = m

    @staticmethod
    def getTotal_Amount():
        return Account.__total_amount

    def deposit(self, m):
        if self.getStatus() == "inactive":
            return False
        self.__amount += m
        Account.__total_amount +=m
        tran = Transaction(self.getAccNo(), "deposit", m)
        self.transList.append(tran.get_trans())
        return self.__amount

    def withdraw(self, m):
        if self.getStatus() != "Active":
            return False
        if (self.__amount - m) >= Account.__min_amount:
            self.__amount -= m
            Account.__total_amount -= m
            tran = Transaction(self.getAccNo(), "withdraw", m)
            self.transList.append(tran.get_trans())
            return True
        else:
            return False

    @staticmethod
    def transfer(sourceA, destA, m):
        res = sourceA.withdraw(m)
        if res:
            destA.deposit(m)
            sourceA.transList.pop()
            tran = Transaction(sourceA.getAccNo(), "transfer", m, destA.getAccNo())
            sourceA.transList.append(tran.get_trans())
            return res
        else:
            return res

    def Transfer(self, d, m):
        res = self.withdraw(m)
        if res:
            d.deposit(m)
            self.transList.pop()
            tran = Transaction(self.getAccNo(), "transfer", m, d.getAccNo())
            self.transList.append(tran.get_trans())
            return res
        else:
            return res
    @staticmethod
    def Ban(a):
        a.__amount = 0
        a.setStatus(0)
        return a.getStatus()


class Transaction:
    def __init__(self, accNo, type, amount, dest=None):
        self.accNo = accNo
        self.t_type = type
        self.t_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.amount = amount
        if dest:
            self.t_dest = dest

    def get_trans(self):
        if self.t_type == "transfer":
            trans = [self.name ,self.t_type, "from " + str(self.accNo), "to " + str(self.t_dest), "amount: "+str(self.amount), self.t_time]
        elif self.t_type == "deposit":
            trans = [self.name, self.t_type,"to " + str(self.accNo), "amount: " + str(self.amount), self.t_time]
        else:
            trans = [self.name, self.t_type, "from " + str(self.accNo), "amount: " + str(self.amount), self.t_time]
        return trans


def main():
    action = "100"
    while action != "0":
        print("#Bank Account#")
        print("please enter the number you desire:")
        print("1.Create an account")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Transfer")
        print("5.Get records")
        print("6.Get amount")
        print("7.i am an Admin\n\n")
        print("press 0 to EXIT\n")
        action = input("Action Number:\n")
        if action == "1":
            accNo = input("please insert an account number with 6 digits: ")
            acc_amount = input("if you want to open account whit more than min amount enter the vlaue otherwise enter 0: ")
            if int(acc_amount) >= 10:
                a = Account(int(accNo), int(acc_amount))
            else:
                a = Account(int(accNo))
            print("account created successfully\n")
            input("press a key to go back")
        elif action == "2":
            m = input("Enter the amount:")
            if m == '0':
                continue
            try:
                a.deposit(int(m))
            except:
                print("no account exist please create one first!")
                input()
                continue
            print("successful!")
            print(a.getAmount())
            input("press a key to go back")
        elif action == "3":
            m = input("Enter the amount:")
            if m == '0':
                continue
            try:
                a.withdraw(int(m))
            except:
                print("no account exist please create one first!")
                input()
                continue
            print("successful!")
            print(a.getAmount())
            input("press a key to go back")
        elif action == "4":
            dest = input("enter the destination account number:")
            b = Account(int(dest))
            m = input("Enter the amount:")
            if m == '0':
                continue
            try:
                a.Transfer(b, int(m))
            except:
                print("no account exist please create one first!")
                input()
                continue
            print("successful!")
            print(a.getAmount())
            input("press a key to go back")
        elif action == "5":
            try:
                print("your account's records are:")
                print(a.getRecord())
            except:
                print("no account exist please create one first!")
                input()
                continue
            input("press a key to go back")
        elif action == "6":
            try:
                print("your account's amount is:")
                print(a.getAmount())
            except:
                print("no account exist please create one first!")
                input()
                continue
            input("press a key to go back")
        elif action == "7":
            print("1.set Min Amount")
            print("2.Transfer Money")
            print("3.Get total amount")
            print("4.Ban an Account")
            action2 = input("your choice")
            if action2 == "1":
                m = input("set new min amount")
                Account.setMin_amount(int(m))
                print("DONE!")
                input("press any key to go back")
            elif action2 == "2":
                source = input("source Account:")
                destinatoin = input("destination Account:")
                m = input("amount:")
                # creating fake accounts with fake amounts
                # this step is just for test
                s = Account(int(source), int(m) + 10)
                d = Account(int(destinatoin))
                Account.transfer(s, d, int(m))
                print("DONE!")
                input("press any key to go back")
            elif action2 == "3":
                print("your Total amount is:")
                print(Account.getTotal_Amount())
                input("press a key to go back")
            elif action2 == "4":
                print("banning account A")
                try:
                    Account.Ban(a)
                except:
                    print("no account exist please create one first!")
                    input()
                    continue
                print(a.getStatus())
                input("press a key to go back")
    return 0


if __name__ == "__main__":

    main()
