from datetime import datetime
from functools import wraps

def log(func):
    @wraps(func)
    def decorator(*args,**kwargs):
        print('Function ' + func.__name__ +' has been called at ' +datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return func(*args, **kwargs)
    return decorator

@log
def add(x, y):
    return x+y

add(1,2)

print(add.__name__)
