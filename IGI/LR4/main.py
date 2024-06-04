#Kryshalovich Dmitry
#Lab4
#23.05.24
#main.py
#Version 1.0

from tools.tools import conditional_input as cin
from task1_directory.task1 import task1
from task2_directory.task2 import task2
from task3_directory.task3 import task3
from task4_directory.task4 import task4
from task5_directory.task5 import task5


def main():

	while True:
		task_number = cin(int,lambda x: 0 <= x <= 5,"choose task to execute\n1 - 5 tasks\n0 to exit\n")
		match task_number:
			case 0:
				break
			case 1:
				task1()
			case 2:
				task2()
			case 3:
				task3()
			case 4:
				task4()
			case 5:
				task5()


			

if __name__ == "__main__":
	main()
	