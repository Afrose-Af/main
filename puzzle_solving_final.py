"""
This is a puzzle solving program  as follows.
We are solving a Puzzle which involves us in making selections between numbers 1-9.
The selection should be made in such a way that, the numbers we selected and distinct/unique i.e. without any repitations.
This process involves, two mathematical operations such as, Multiplication and Addition as follows.
n1n2*n3=(o/p1[1]+o/p[2])+(n4+n5)=(o/p[3]+o/p[4])

Initial Version:     Afrose Unissa
                    Salwa Sayeedul Hasan,    Date: 6th of December, 2021 
 

"""




class Puzzle_Solve:
    #https://www.hackerearth.com/practice/python/object-oriented-programming/classes-and-objects-i/tutorial/  read it
    def __init__(self, givenlist):
        self.givenlist = givenlist

    
    def print_givenlist(self):
        print("Constructor init has the list")
        print(self.givenlist)

    def puzzle_response(self,final_list,no1,no2,no3,prod,sum_):
        """
        via this method, we print our final list after our evaluation
        """
        if (final_list== []):
            print("The solution for the given Puzzle is found")
            print("the numbers are: ")
            print(no1)
            print(no2)
            print(no3)
            print("product=", prod)
            print("sum=",sum_)
            print(no1,"*",no2,"=",prod,"+",no3,"=",sum_)
            print("final list:",final_list)
    
    def chksum_fromprocessedlist(self, remaining_remaining_list, no1, no2, prod):
        #print ("call this method in the chkprod method")
        """
        using this method, based on the condition of sum values >/<99 we perform the addition satisfy the condition and give result
        """
        for m in remaining_remaining_list:
            for n in remaining_remaining_list:
                if (m!=n):
                    no3 = (10*m)+n
                    sum_ = prod + no3
                    if (sum_ <=99):
                        next_chosen_list = [m,n]
                        left_list =[x for x in remaining_remaining_list if x not in next_chosen_list]
                        #print("left_list:",left_list)
                        digit3 = sum_%10
                        digit4 = sum_//10
                        if (digit3 in left_list) and (digit4 in left_list):
                            #print("digit3:",digit3,"digit4:",digit4)
                            sum_values = [digit3, digit4]
                            final_list = [x for x in left_list if x not in sum_values]
                            #print("final_list:",final_list)
                            self.puzzle_response(final_list,no1,no2,no3,prod,sum_)
    
    def chkprod_fromgivenlist(self):
        #print("check three combinations first")
        """
        using this method, based on the condition of product values >/<99 we perform the multiplication, satisfy the condition and give result
        """
        templist = self.givenlist
        for i in templist:
            for j in templist:
                for k in templist:
                    if (i!=j!=k!=i):
                        no1 = (10*i)+j
                        no2 = k
                        prod = no1*no2
                        if (prod <= 99):
                            chosen_list = [i,j,k]
                            remaining_list=[]
                            remaining_list =[x for x in templist if x not in chosen_list]
                            #print("selected list=", chosen_list, "no1=", no1, "no2=", no2, "prod=", prod, "remaining_list=", remaining_list)
                            digit1 = prod%10
                            digit2 = prod//10
                            # so add a logic here, if the prod digits are not there in the remaiing list  then yo dont that combination 
                            # so there will be an if statement  again 
                            # do that and update your remaing_list  by taking out two numbers if they are there.
                            if (digit1 in remaining_list) and (digit2 in remaining_list):
                                #print("digit1",digit1,"digit2",digit2)
                                prod_values = [digit1, digit2]
                                remaining_remaining_list =[x for x in remaining_list if x not in prod_values]
                                self.chksum_fromprocessedlist(remaining_remaining_list, no1, no2, prod)
                                


         
    
    def solve_puzzle(self):
        print("solution of the puzzle starts")
        self.print_givenlist()
        self.chkprod_fromgivenlist()




#Main Program Starts Here

#Initialiaze the Class first with passing the constructor
givenlist = [1,2,3,4,5,6,7,8,9]

puzzle_solve= Puzzle_Solve(givenlist)
puzzle_solve.solve_puzzle()





