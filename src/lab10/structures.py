from collections import deque
from typing import Any


class Stack:
    """Структура данных типа стек (LIFO), основанная на списке.."""  # «стек»

    def __init__(self):
        self._data: list[Any] = []

    def push(self, item: Any) -> None:
        """Add an element to the top of the stack."""
        self._data.append(item)

    def pop(self) -> Any:
        """Удаляет верхний элемент стека и возвращает его.."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> Any | None:
        """Возвращает верхний элемент, не удаляя его. Возвращает None, если стек пуст."""
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        """Возвращает True, если стек пуст, в противном случае — False.."""
        return len(self._data) == 0

    def __len__(self) -> int:
        """Количество элементов в стеке."""
        return len(self._data)


class Queue:
    """Структура данных FIFO, основанная на collections.deque.."""  # «очередь»

    def __init__(self):
        self._data: deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        """Добавить элемент в конец очереди."""
        self._data.append(item)

    def dequeue(self) -> Any:
        """
       Удаляет левый элемент из начала очереди и возвращает его.

Если очередь пуста, возвращает исключение IndexError..
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self) -> Any | None:
        """Возвращает первый элемент, не удаляя его. Возвращает None, если очередь пуста.."""
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        """Возвращает True, если очередь пуста.."""
        return len(self._data) == 0

    def __len__(self) -> int:
        """Количество элементов в очереди."""
        return len(self._data)


                            #--Test all--#



if __name__ == "__main__":
                                     #LIFO-#
    stack = Stack()
    print("\n===================================================================")
    print(f"1. Stack created: {stack}")
    print("===================================================================")

    print(f"   Empty? {stack.is_empty()}, Length: {len(stack)}, Top: {stack.peek()}")

    elements = [20, 10, 2, "Author", ["Domingos", "Sebastião"]]
    for elem in elements:
        # Выполнение LIFO
        stack.push(elem)  # Добавление новых элементов в начало списка
        print(f"2. Added {elem}: {stack}")  # Отображение добавленного элемента
        print(f"   Upper: {stack.peek()}, Length: {len(stack)}")  # Элемент сверху

    print(f"\n   Empty? {stack.is_empty()}, Length: {len(stack)}, Top: {stack.peek()}")

    print("\n3. Extract (LIFO order):")
    while not stack.is_empty():  # Извлечение элементов из верхней части списка
        item = stack.pop()  # Экстракция
        print(f"   Extracted: {item}, Remaining: {len(stack)}, Top: {stack.peek()}")

    print(f"\n4. Result: {stack}, Empty? {stack.is_empty()}")

                                     # -Fifo-#
    q = Queue()

    # Fifo Инициализация
    print("\n===================================================================")
    print(f"1. Queue created: {q}")
    print("===================================================================")
    print(f"\n   Empty? {q.is_empty()}, Length: {len(q)}, First: {q.peek()}")

    # Добавление элементов
    elements = ["first", "second", "third", 0, 1, 2]
    for element in elements:
        q.enqueue(element)
        print(f"2. Added {element}: {q}")
        print(f"   Last in: {q.peek()}, Length: {len(q)}")

    # Извлечение элементов
    print("\n3. Extract (FIFO order):")
    while not q.is_empty():
        item = q.dequeue()
        print(f"   Extracted: {item}, Remaining: {len(q)}, First: {q.peek()}")

    # Результат
    print(f"\n4. Result: {q}, Empty? {q.is_empty()}")