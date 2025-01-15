import threading

def startThread(func):
    thread = Thread(target = threaded_function, args = (10, ))
    thread.start()
    thread.join()

    return thread