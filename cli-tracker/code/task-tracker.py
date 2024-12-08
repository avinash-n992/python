import os
import re 
import random
import string 
import datetime
import json


class TaskTracker:

    # task structure - 
    
    # id: A unique identifier for the task
    # description: A short description of the task
    # status: The status of the task (todo, in-progress, done)
    # createdAt: The date and time when the task was created
    # updatedAt: The date and time when the task was last updated

    current_time = datetime.datetime.now() 
    # Printing attributes of now().
    print("The attributes of now() are :")

    print("Year :", current_time.year)

    print("Month : ", current_time.month)

    print("Day : ", current_time.day)

    print("Hour : ", current_time.hour)

    print("Minute : ", current_time.minute)

    print("Second :", current_time.second)

    print("Microsecond :", current_time.microsecond)

    time_value = (str(current_time.year),"_",str(current_time.month),"_",str(current_time.day),"_",str(current_time.hour),str(current_time.minute),str(current_time.second))
    new_curr_time = "".join(time_value)
    print(new_curr_time)

    def add_task(self):
        pass

    def update_task(self):
        pass

    def delete_task(self):
        pass
    
    def push_task_to_json(self,task_dict):
        parent_folder = os.path.dirname(os.path.realpath(os.getcwd()))
        op_file = os.path.join(parent_folder,"output","task.json")
        with open(op_file, "a") as outfile: 
            json.dump(task_dict, outfile)
    
    def extract_task_from_json(self,t_id):
        parent_folder = os.path.dirname(os.path.realpath(os.getcwd()))
        op_file = os.path.join(parent_folder,"output","task.json")
        t_json = open(op_file)
        data = json.load(t_json)
        print(data) 
        
    def __init__(self):
        u_input = input('''Enter below number codes to execute specific commands of task tracker : \n 
                         - Do you want to create a new task ? --> 1 
                         - Do you want to update an existing task ? --> 2 
                         - Do you want to delete an existing task ? --> 3
                        Enter your response (numbers only) --> ''')
        
        # regex to check if only 1,2 and 3 were pressed by users 
        input_pattern = "[1-3]"
        
        #create 
        if u_input == "1":
            t_desc = input("enter the description of the task  ")
            i_status = input('''enter the option number of status of the task \n 
                             1 - To Do
                             2 - In Progress
                             3 - Done
                             Enter your choice --> ''')
            if i_status == "1":
                t_status = "ToDo"
            elif i_status == "2":
                t_status = "InProgress"
            elif -i_status == "3":
                t_status = "Done"

            chars = string.ascii_uppercase + string.digits
            t_id = ''.join(random.choice(chars) for _ in range(6))
            print("Id generated is", t_id, "and status is ", t_status )

            task = {
                'id': t_id,
                'desc': t_desc,
                'status' : t_status,
                'createdAt': self.new_curr_time,
                'updatedAt': "NA"
            }
            print(task)

            self.push_task_to_json(task)
            print("Task created successfully in json")

        # update 
        elif u_input == "2":
            t_id = input("Enter the ID of the task -->")

        # delete 
        elif u_input == "3":
            pass
        elif u_input == "4":
            self.extract_task_from_json("4r")

obj = TaskTracker()
