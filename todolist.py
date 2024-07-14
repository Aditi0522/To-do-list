w=[]
class Create_todo():
    def __init__(self):
      z.clear()
      self.x = input("give name of the Todo list: \n")
    
      if self.x in w:
          print("This list already exists, please try again!")
          starting()
      w.append(self.x)     
      print(f"Your pending todo lists are {w}")
      print(f"Currently opening Todo list- {self.x}")
      choice_p()

class Use_todo():
    use=0
    def __init__(self):
        print(f"Which to-do list would you like to use?\n {w}")
        self.use=int(input())
        self.use=self.use-1
        print(f"Opening to do list {w[self.use]}!!")
        #z=g[self.use]
        choice_z()
        
        #double double z is getting added into g what to do
class Add_task_insert(Use_todo):
      def __init__(self):
          n = int(input("Print no. of tasks"))
          looprun_p = range(0,n)
          #z=list(g[self.use])
          for i in looprun_p:
            Task_use()    
          #g[self.use]=list(z)
          #g.join(self.use,z)
          print(g)
          print(g[self.use])
          choice_z()

class Completed_use(Use_todo):
    def __init__(self):
        self.q=input('which task did you complete? ')
        z=g[self.use]
        if self.q in z:
            print(f"congratulations on completing your task '{self.q}' \u2713 !!")
            #add tick in the list
            z.remove(self.q)  
            print(f"New list is {g[self.use]}")

def mark_as_completed_use():
    Completed_use()
    #print(f"New list is {g[self.use]}")
    choice_z()

def choice_z():
    print("choice\n1)add task\n2)remove task")
    print ('3) \u2713 mark as completed')
    print("4) quit")
    p = int(input())
    if p==1:
        Add_task_insert()
    if p==2:
        remove_task_use()
    if p==3:
        mark_as_completed_use()
    if p==4:
        starting()       


class Remove_todo():
    def __init__(self):
        print(f"Which to do list would you like to remove?\n {w}")
        removal=input()
        b= w.index(removal)
        #b=b-1
        del w[b]
        del g[b]
        print(w)
        print(f"Good going! Only a few todo lists left!!\n{w}")
        starting()

g=[]

class Task_use(Use_todo):
    def __init__(self):
        self.taskname= input('Enter Taskname: ')
        z=g[self.use]
        z.append(self.taskname)
        
        
        

class Task:
    def __init__(self):
        self.taskname= input('Enter Taskname: ')
        z.append(self.taskname)
        

class Add_task():
      def __init__(self):
          n = int(input("Print no. of tasks"))
          looprun_p = range(0,n)
          for i in looprun_p:
            Task()    
          
          g.append(list(z))
          print(g)
          print(z)
          choice_p()

class Taskr_use(Use_todo):
    def __init__(self):
            self.y=input('which word would you like to remove? ')
            z=g[self.use]
            if self.y in z:
                z.remove(self.y)
            print(g[self.use])      

class Taskr(Use_todo):
    def __init__(self):
            self.y=input('which word would you like to remove? ')
            if self.y in z:
                z.remove(self.y)
                      

class Completed(Task):
    def __init__(self):
        self.q=input('which task did you complete? ')
        if self.q in z:
            print(f"congratulations on completing your task '{self.q}' \u2713 !!")
            #add tick in the list
            z.remove(self.q)  

def remove_task_use():
    Taskr_use()
    choice_z()

def remove_task():
    Taskr()
    print(z)
    choice_p()

def mark_as_completed():
    Completed()
    print(f"New list is {z}")
    choice_p()

def choice_p():
    print("choice\n1)add task\n2)remove task")
    print ('3) \u2713 mark as completed')
    print("4) quit")
    p = int(input())
    if p==1:
        Add_task()
    if p==2:
        remove_task()
    if p==3:
        mark_as_completed()
    if p==4:
        starting()       

def ending():
    print("Hope you completed all your tasks!! Wish you luck!!")   
    quit()   

def starting():
  print("TO DO LIST")
  print("choice")
  print("1)Create todo list\n2)use todo list\n3)remove todo list\n4)quit")
  
  a=int(input("What would you like to do? "))
  if a==1:
        Create_todo()
  if a==2:
        Use_todo()
  if a==3:
        Remove_todo()
  if a==4:
      ending()
z=[]
starting()

#first check completed
#then come back to problem of creating more than one to do list.
