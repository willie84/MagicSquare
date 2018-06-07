# Magic square for odd numbers
#
userNumber=eval(input("Enter the number of the magic square to generate:\n"))
 
def CreateSquare(oddnum):
 
    matrix=[]
    two=[]
      #Create a two by two matrix by intializing everything by zero
    for i in range(0,oddnum):
        for j in range(0,oddnum):
            two.append(0)
        matrix.append(two)
        two=[]
 
    # initialize position of 1
    row = oddnum//2
    col = oddnum-1
     
    #Initialise 1 at middle row at the last column 
    num = 1
     
    #The loop will run from 1 to number squared
    while num <= (oddnum**2):
        if row == -1 and col == oddnum: # This is the condition where the calculated values 
            col = oddnum-2
            row = 0
        else:
            #When the column number is the same as the number . Modify due to index out of range error 
            if col == oddnum:
                col= 0
            # next number goes out of upper side
            if row < 0:
                row = oddnum-1
                 
        if matrix[row][col]>0: # This is when the box calculated is calculated
            col = col-2
            row = row+1
            continue
        else:
            matrix[row][col] = num
            num = num+1
                 
        col = col+1
        row = row-1
    return matrix
def sumofNumbers(h):
    sum=0
    if type(h)==list:
        for i in h:
            sum=sum+i
    return sum
     
         
 
#Check if the number is odd number
if userNumber%2==1:
    print("..........................Generating the magicSquare.............")
    m=CreateSquare(userNumber)
    for i in m:
        for k in i:
            print(k,end=" ")
        print()
    #getting the sum of the first row
    p=sumofNumbers(m[0])
    boolean=True
    for i in m:
        boolean*=(sumofNumbers(i)==p)
    if(boolean==True):
        print("The MagicSquare is correct and okay")
        print("The sum of each row is :",sumofNumbers(m[0]))
    else:
        ("Magic Square is not correct")
else:
    print("Kindly enter an odd number please")