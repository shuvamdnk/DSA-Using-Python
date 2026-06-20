def add(a,b):
    return a+b

print(__name__)

# this statement only run when we execute this file directly not imported
if __name__ == "__main__":
    print(add(4,5))