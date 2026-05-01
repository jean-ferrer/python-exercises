# 2026-04-20

import threading

class Foo:
    def __init__(self):
        self.done_first = threading.Event()
        self.done_second = threading.Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.done_first.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.done_first.wait()
        printSecond()
        self.done_second.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self.done_second.wait()
        printThird()