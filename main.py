from simplex import *
# Arrays
Obj_Table=[3,2]
Const_Table=[2,1,2,3,3,1]
Results=[18,42,24]
Eq_Type=['<=','<=','<=']
N_Variables=2
N_Constraints=3

# Obj_Table=[4000,5000]
# Const_Table=[40,30,20,30]
# Results=[360,480]
# Eq_Type=['<=','<=']
# N_Variables=2
# N_Constraints=2

Tms=[]
Constraints=[]
Z=[]

# N_Variables=Get_Data("How many variables are there?\n",2,20)
# N_constraints=Get_Data("How many constraints are there?\n",1,20)
# Obj_Table,Const_Table,Results,Eq_Type=Fill_Tables(N_Variables,N_constraints,Obj_Table,Const_Table,Results,Eq_Type)
Show_Data(N_Variables,Obj_Table,Const_Table,Results,Eq_Type)
Constraint,Tms,X_counter=Preliminary_stage(N_Variables,Obj_Table,Const_Table,Results,Eq_Type)
print("Constraint Table: ",Constraint)
print("Tms: ",Tms)
print(calculation(Constraint,Results,Tms,X_counter,Obj_Table))
