def my_decorator(message: str):
    
    
    def actual_decorator(func):
        def task():
            print("=========================================================")
            print(message)
            func()
            print("=========================================================\n")
        return task
    return actual_decorator