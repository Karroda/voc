import java.lang
import java.util

class SpyingHashMap(extends=java.util.HashMap):
    def __init__(self):
        self.counter = 0

    def put(self, key: java.lang.Object, value: java.lang.Object) -> java.lang.Object:
        print('Putting %s in key %s' % (value, key))
        return super().put(key, value)


m = SpyingHashMap()
m.put("hello", "it's me")
m.put("from where?", "the other side")
print('map entries are:', m.entrySet())