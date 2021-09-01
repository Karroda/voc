from java.lang import Math


class MyThread(extends=java.lang.Thread):
    def __init__(self, id):
        self.id = id
        self.counter = 0

    def run(self) -> void:
        print('Starting thread %d' % self.id)
        for i in range(10):
            self.sleep(Math.random() * 1000)
            self.counter += 1
            print('Thread %d executed %d times' % (self.id, self.counter))


MyThread(1).start()
MyThread(2).start()
MyThread(3).start()