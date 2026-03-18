# TO DO APPLICATION

msg = '''
TYPE 1 TO ADD A TASK
TYPE 2 TO VIEW ALL TASK
TYPE 3 TO REMOVE A TASK
TYPE 4 TO MARK A TASK COMPLETED
TYPE 5 TO VIEW COMPLETED TASK
TYPE 6 TO QUIT
'''

tasks = []
complete_task = []
OPTIONS = ['1','2','3','4','5','6']
def getOption():
    while True:
        option = input('1,2,3,4: ')
        if option.isdigit() and option in OPTIONS:
            option = int(option)
            break
        else:
            print('OPTION MUST BE A DIGIT FROM 1 TO 4')
    return option

def addTask():
    while True:
        task = input('ADD A TASK: ')
        if task:
            tasks.append(task)
            break
        else:
            print('TASK CANNOT BE EMPTY OR NULL')
    return task

def removeTask():
    while True:
        task_to_remove = input('ENTER INDEX OF TASK TO DELETE: ')
        if task_to_remove.isdigit():
            task_to_remove = int(task_to_remove)
            if task_to_remove <= len(tasks):
                tasks.pop(task_to_remove)
                break
            else:
                print('TASK DOES NOT EXISTS...')
        else:
            print('TASK INDEX SHOULD BE A DIGIT...')
    return task_to_remove

def completeTask():
    while True:
        completed_task = input('ENTER INDEX OF COMPLETED TASK: ')
        if completed_task.isdigit():
            completed_task = int(completed_task)
            if completed_task <= len(tasks):
                complete_task.append(completed_task)
                break
            else:
                print('TASK NOT FOUND...')
        else:
            print('TASK INDEX MUST BE A DIGIT...')

def main():
    while True:
        print(msg)
        option = getOption()
        if option == 1:
            task = addTask()
        elif option == 2:
            if tasks != []:
                for i,task in enumerate(tasks):
                    print(f'\n\tTASK {i}: {task}\n')
            else:
                print('NO TASK ADDED YET....')
        elif option == 3:
            for i,task in enumerate(tasks):
                    print(f'\n\tTASK {i}: {task}')
            task_to_remove = removeTask()
        elif option == 4:
            for i,task in enumerate(tasks):
                print(f'\n\tTASK {i}: {task}')
            completed_task = complete_task()
        elif option == 5:
            for completed_task in complete_task:
                print(completed_task)
        elif option == 6:
            exit()

if __name__ == '__main__':
    main()
