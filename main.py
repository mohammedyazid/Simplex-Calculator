from simplex import *

Obj_Table=[];Const_Table=[];Results=[];Eq_Type=[];N_Variables=0;N_Constraints=0
Constraints=[]

N_Variables=Get_Data("How many variables are there?\n",2,20)
N_constraints=Get_Data("How many constraints are there?\n",1,20)
Obj_Table,Const_Table,Results,Eq_Type=Fill_Tables(N_Variables,N_constraints,Obj_Table,Const_Table,Results,Eq_Type)
Show_Data(N_Variables,Obj_Table,Const_Table,Results,Eq_Type)
Constraint,Obj_Table=Preliminary_stage(N_Variables,Obj_Table,Const_Table,Results,Eq_Type)

print(f"Max Z = {round(calculation(Constraint,Results,N_Variables+1,Obj_Table),2)}")
