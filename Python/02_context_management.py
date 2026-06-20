# Context Manager
# class Server:
#     def __enter__(self):
#         print("Startup")
    
#     def __exit__(self, exc_type, exc, tb):
#         print(exc_type is ValueError)
#         print(exc)
#         print("Shutdown")
#         return True

# with Server() as s:
#     # print("Start")
#     raise ValueError("Value Error")

from contextlib import contextmanager

@contextmanager
def my_context():
    print("Start")
    yield
    print("End")

with my_context():
    print("Hello")