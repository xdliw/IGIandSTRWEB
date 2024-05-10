# Lab work 3
# Author: Kryshalovich Dmitry
# Date: 22.04.24



from tools import conditional_input as ci
import my_decorator
import task1
import task2
import task3
import task4
import task5

@my_decorator.my_decorator("IGI Labwork 3")
def main():
	

	task = ci(int,lambda x: 0 <= x <= 5,"choose task to execute\n1 - 5 tasks\n0 to exit\n")

	while task:
		match task:
			case 0:
				break
			case 1:
				task1.task1()
			case 2:
				task2.task2()
			case 3:
				task3.task3()
			case 4:
				task4.task4()
			case 5:
				task5.task5()
		
		task = ci(int,lambda x: 0 <= x <= 5,"choose task to execute\n1 - 5 tasks\n0 to exit\n")

			





if __name__ == "__main__":
	main()

