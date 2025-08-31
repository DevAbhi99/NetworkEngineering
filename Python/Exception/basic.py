try:
    100/0
except Exception:   #Exception handles all kind of exceptions like zerodivisionerror, value error and type error
    print('Something went wrong')
finally:
    print('Resolved')