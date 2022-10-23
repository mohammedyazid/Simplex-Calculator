from simplex import *

Obj_Table=[40,30]
Const_Table=[1,2,2,1]
Results=[12,16]
Eq_Type=['<=','<=']
N_Variables=2
N_Constraints=2

Show_Data(N_Variables,Obj_Table,Const_Table,Results,Eq_Type)
Constraint,Obj_Table=Preliminary_stage(N_Variables,Obj_Table,Const_Table,Results,Eq_Type)
Obj_Table=ToInt(Obj_Table);Constraint=ToIntMatrix(Constraint);Results=ToInt(Results)
print(f"Max Z = {round(calculation(Constraint,Results,N_Variables+1,Obj_Table),2)}")
