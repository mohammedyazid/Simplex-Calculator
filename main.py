from simplex import *

Obj_Table=[]
Const_Table=[]
Results=[]
Eq_Type=[]
Tms=[]
Constraints=[]


N_Variables=Get_Data("How many variables are there?\n",2,20)
N_constraints=Get_Data("How many constraints are there?\n",1,20)
Obj_Table,Const_Table,Results,Eq_Type=Fill_Tables(N_Variables,N_constraints,Obj_Table,Const_Table,Results,Eq_Type)
Show_Data(N_Variables,Obj_Table,Const_Table,Results,Eq_Type)
