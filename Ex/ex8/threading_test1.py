import threading

def hello(name):
    print('chile thread: {}'.format(threading.get_ident()))
    print('Hello ' + name)

def main():
    t = threading.Thread(target=hello, args=('shiyanlou',))
    t.start()
    t.join()
    print('main thread: {}'.format(threading.get_ident()))

if __name__=='__main__':
    main()
