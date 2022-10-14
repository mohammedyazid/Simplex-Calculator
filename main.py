from unittest import result
from simplexe import *

objective_function=[]
constraints=[]
results=[]


N_Variables=Get_Data("How many variables are there? *ps only accept 2 or more*\n")

N_constraints=Get_Data("How many constraints are there?\n")

objective_function=Fill_Tables(N_Variables,"Enter the coefficient of the variable X%s of the objective function :","Objective_or_results")

constraints=Fill_Tables(N_constraints,"Enter the coefficient of the variable X%s of the constraint number %s :","Constraints")

results=Fill_Tables(N_constraints,"Enter the result of the constraint number %s :","Objective_or_results")
print("====================\n")
Show_Data(objective_function,constraints,results,N_Variables)

# print(objective_function)
# print(constraints)
# print(results)
# Show_Data()