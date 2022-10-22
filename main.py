from simplex import *
##Arrays
Obj_Table=[90,90]
Const_Table=[1,1,2,2,3,3]
Results=[25,30,35]
Eq_Type=['<=','>=','=']
N_Variables=2
N_Constraints=3

Tms=[]
Constraints=[]

# N_Variables=Get_Data("How many variables are there?\n",2,20)
# N_constraints=Get_Data("How many constraints are there?\n",1,20)
# Obj_Table,Const_Table,Results,Eq_Type=Fill_Tables(N_Variables,N_constraints,Obj_Table,Const_Table,Results,Eq_Type)
Show_Data(N_Variables,Obj_Table,Const_Table,Results,Eq_Type)
Constraint,Tms=Preliminary_stage(N_Variables,Obj_Table,Const_Table,Results,Eq_Type)
print("Constraint Table: ",Constraint)
print("Tms: ",Tms)
calculation(Constraint,Results,Tms,Obj_Table)
