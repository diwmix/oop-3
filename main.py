import random
import sys

students = []
topics = []
distributedTopics = []
def clearFile():
    with open('AssignedTopics.txt', 'w', encoding='utf-8') as file:
        file.write('')

clearFile()

def getFile(fileName, arr):
    try:
        with open(fileName, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                arr.append(line.strip())
        return arr
    except FileNotFoundError:
        print(f'Файл {fileName} не знайдено')
        sys.exit()

def assignTopics():
    if len(students)!=0 and len(topics)!=0:
        student = random.choice(students)
        topic = random.choice(topics)
        
        print("Студент: {}".format(student))
        print("Тема: {}".format(topic))
        
        topics.remove(topic)
        students.remove(student)
        distributedTopics.append((student, topic))
        with open('AssignedTopics.txt', 'a', encoding='utf-8') as file:
            file.write(f"Студент: {student}\n")
            file.write(f"Тема: {topic}\n")
            file.write("\n")
        print(f"Залишилось студентів без теми: {len(students)}" + '\n')
    else:
        print("Немає наявних студентів або тем.")
    


getFile('Students.txt', students)
getFile('Topics.txt', topics)

while True:
    input("Нажмите Enter для выбора студента и темы: \n")
    assignTopics()
    if not topics:
        print("Нема доступних тем.")
        break
    if not students:
        print("Нема доступних студентів.")
        break



