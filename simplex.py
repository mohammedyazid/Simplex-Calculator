from kiwisolver import Constraint
from simple_term_menu import TerminalMenu

options = ['=', '>=', '<=']

def Get_Data(Message,min,max):
    while True:
        try:
            Number=int(input(Message))
            if Number<min or Number>max:
                raise ValueError
            break
        except ValueError:
            print("______________________________!!!!!!!______________________________")
            print("Invalid input. Please enter a number between %s and %s."%(min,max))
            print("______________________________!!!!!!!______________________________\n")
    return Number

def Fill_Tables(Var_Number,Const_Number,Obj_Table,Const_Table,Results,Eq_Type):
    index=0;counter=0
    for i in range(0,Var_Number):
        Obj_Table.append(input(f"Enter the coefficient of the variable X{str(i+1)} of the objective function: "))
    
    for i in range(0,Var_Number):
        print(f"\n|_________________________________{counter+1}_________________________________|\n")
        for j in range (0,Const_Number):
            Const_Table.append(input(f"Enter the coefficient of the variable X{str(index+1)} of the constraint number {str(counter+1)}: "))
            index+=1;
            if index==Var_Number:
                index=0
                terminal_menu = TerminalMenu(options,title=f"Select the type of the constraint number: {str(counter+1)}")
                menu_entry_index = terminal_menu.show()
                Eq_Type.append(options[menu_entry_index])
                Results.append(input(f"Enter the result of the constraint number {str(i+1)}:"))
                counter+=1
                print(f"\n|_________________________________{counter+1}_________________________________|\n")
    return Obj_Table,Const_Table,Results,Eq_Type

def Show_Data(Var_Number,Obj_Table,Const_Table,Results,Eq_Type):
    Result_Index=0;index=0
    print("\n========================Objective Function========================")
    print("Max Z = ",end="")
    for i in range(0,len(Obj_Table)):
        print(str(Obj_Table[i])+" X"+str(i+1),end="")
        if(i<len(Obj_Table)-1):
            print(" + ",end="")
    print("\n____________________________Constraints____________________________\n")
    for i in range(0,len(Const_Table)):
        index+=1;
        print(str(Const_Table[i])+" X"+str(index) ,end="")
        if((i+1)%Var_Number==0):
            print(Eq_Type[Result_Index] + str(Results[Result_Index])+"\n")
            Result_Index+=1
        else:
            print(" + ",end="")
        if index==Var_Number:
                    index=0

def Preliminary_stage(Var_Number,Obj_Table,Const_Table,Results,Eq_Type):
    Var_counter=0;const_counter=0;Constraint=[];X_counter=0
    for i in range(0,len(Eq_Type)):
        if Eq_Type[i]==">=":
            Var_counter+=2
        elif Eq_Type[i]=="=" or Eq_Type[i]=="<=":
            Var_counter+=1
    Constraint.append([])
    for i in range(0,len(Const_Table)):
        Constraint[const_counter].append(Const_Table[i])
        if (i+1) % Var_Number == 0 and i != 0 or i == len(Const_Table)-1:
            Obj_Table.append(0)
            while X_counter<const_counter:
                Constraint[const_counter].append(0)
                X_counter+=1
            if((const_counter+1)*2==len(Const_Table)):
                Constraint[const_counter].append(0)
            if Eq_Type[const_counter]==">=":
                Constraint[const_counter].append(-1)
                Constraint[const_counter].append(1)
            elif Eq_Type[const_counter]=="=" or Eq_Type[const_counter]=="<=":
                Constraint[const_counter].append(1)
            while len(Constraint[const_counter])!=(Var_counter+Var_Number):
                Constraint[const_counter].append(0)
            X_counter=0
            const_counter+=1
            if const_counter*2!=len(Const_Table):
                Constraint.append([])
    return Constraint,Obj_Table
def calculation(Constraint,Results,Tms,Z):
    iteration=0;Hold=[]
    while any(x<0 for x in Tms) == False:
        print(f"Iteration number {iteration}:")
        Max_Tms=Tms.index(max(Tms))
        iteration+=1
        for i in range(0,len(Constraint)):
            Hold.append(Results[i]/Constraint[i][Max_Tms])
        print(Hold[Hold.index(min(Hold))])
        break