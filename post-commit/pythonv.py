import os
 
command = "python --version" #command to be executed
 
res = os.system(command)
#the method returns the exit status

print("Xavi eres un monstruo")
print(os.environ.get('DEVELOPER')) 
print("Returned Value: ", res)
