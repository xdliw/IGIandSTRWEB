#Kryshalovich Dmitry
#Lab4
#23.05.24
#main.py
#Version 1.0

from tools.tools import conditional_input as ci
import task1.task1 as task1
import task2.task2 as task2
import task3.task3 as task3
import task4.task4 as task4
import task5.task5 as task5

def main():

	task_number = ci(int,lambda x: 0 <= x <= 5,"choose task to execute\n1 - 5 tasks\n0 to exit\n")

	while task_number:
		match task_number:
			case 0:
				break
			case 1:
				task1.task1_Class.Execute()
		
		task_number = ci(int,lambda x: 0 <= x <= 5,"choose task to execute\n1 - 5 tasks\n0 to exit\n")


			

if __name__ == "__main__":
	main()

