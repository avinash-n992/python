import io
import re 

class TaskTracker:

    def add_task():
        pass

    def update_task():
        pass

    def delete_task():
        pass

    def __init__(self):
        u_input = input('''Enter below number codes to execute specific commands of task tracker : \n 
                         - Do you want to create a new task ? --> 1 
                         - Do you want to update an existing task ? --> 2 
                         - Do you want to delete an existing task ? --> 3 
                        Enter your response (numbers only) --> ''')
        
        # regex to check if only 1,2 and 3 were pressed by users 
        input_pattern = "[1-3]"
        
        if u_input == "1":
            pass
        elif u_input == "2":
            pass
        elif u_input == "3":
            pass


        print(u_input)
        print("hello")

obj = TaskTracker()
