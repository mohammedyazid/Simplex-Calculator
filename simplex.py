# objective_function=[5,4]
# constraints=[1,3,5,8,9,10]
# results=[25,83,50]
# N_Variables=2

def Get_Data(Message):
    Number=int(input(Message))
    return Number
    # N_Variables=int(input("How many variables are there? *ps only accept 2 or more*\n"))
    # for i in range(0,N_Variables):
    #     objective_function.append(input(f"Enter the coefficient of the variable {str(i+1)} of the objective function :"))
    # for i in range(0,N_constraint):
    #     for j in range(0,N_Variables):
    #         constraints.append(input("Enter the coefficient of the variable X"+str(j+1)+" of the constraint number "+str(i+1)+" :"))
    #     results.append(input("Enter the result of the constraint number "+str(i+1)+" :"))
    
def Fill_Tables(Number,Message,Table_Type):
    Table=[];j=0
    for i in range(0,Number):
        if Table_Type=="Objective_or_results":
            Table.append(input(Message%str(i+1)))
        elif Table_Type=="Constraints":
            Table.append(input(Message%(str(i+1),str(j+1))))
            j+=1
    print("____________________\n")
    return Table

def Show_Data(objective_function,constraints,results,N_Variables):
    Result_Index=0
    print("Objective function :",end=" ")
    print("Max Z = ",end="")
    for i in range(0,len(objective_function)):
        print(str(objective_function[i])+" X"+str(i+1),end="")
        if(i<len(objective_function)-1):
            print(" + ",end="")
    print("\n====================\nConstraints :\n")
    for i in range(0,len(constraints)):
        print(str(constraints[i])+" X"+str(i+1),end="")
        if((i+1)%N_Variables==0):
            print(" <= "+str(results[Result_Index])+"\n")
            Result_Index+=1
        else:
            print(" + ",end="")
# Get_Data()
# Show_Data()