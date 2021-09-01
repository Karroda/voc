from java.lang import Math, Thread


class MyThread(implements=java.lang.Runnable):
    def __init__(self, id):
        self.id = id
        self.counter = 0

    def run(self) -> void:
        print('Starting thread %d' % self.id)
        for i in range(10):
            Thread.sleep(Math.random() * 1000)
            self.counter += 1
            print('Thread %d executed %d times' % (self.id, self.counter))


Thread(MyThread(1)).start()
Thread(MyThread(2)).start()
Thread(MyThread(3)).start()