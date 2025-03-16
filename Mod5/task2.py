class Node:
    """
    Вспомогательный класс для узлов списка
    """

    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # ссылка на предыдущий узел


class Queue:
    """
    Основной класс для очереди
    """

    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def push(self, val):
        """
        Добавление элемента val в конец очереди
        """
        new_node = Node(val)  # создаем новый узел
        if self.start is None:  # если очередь пуста
            self.start = new_node
            self.end = new_node
        else:
            self.end.nref = new_node  # предыдущий последний узел ссылается на новый
            new_node.pref = self.end  # новый узел ссылается на предыдущий последний узел
            self.end = new_node  # обновляем конец очереди

    def pop(self):
        """
        Возвращаем элемент из начала очереди с удалением его из очереди
        """
        if self.start is None:
            raise IndexError("Очередь пуста, нельзя извлечь элемент.")

        popped_node = self.start  # сохраняем первый узел
        self.start = self.start.nref  # перемещаем ссылку на следующий узел
        if self.start is None:  # если очередь стала пустой
            self.end = None
        else:
            self.start.pref = None  # обнуляем ссылку на предыдущий узел у нового начала

        return popped_node.data  # возвращаем данные извлеченного узла

    def insert(self, n, val):
        """
        Вставить элемент val между элементами с номерами n-1 и n
        """
        new_node = Node(val)
        current = self.start
        index = 0

        if n == 0:  # вставка в начало
            new_node.nref = self.start
            if self.start is not None:
                self.start.pref = new_node
            self.start = new_node
            if self.end is None:  # если очередь была пустой
                self.end = new_node
            return

        while current is not None and index < n:
            current = current.nref
            index += 1

        if current is None:  # вставка в конец
            self.end.nref = new_node
            new_node.pref = self.end
            self.end = new_node
        else:  # вставка между узлами
            new_node.nref = current
            new_node.pref = current.pref
            if current.pref is not None:
                current.pref.nref = new_node
            current.pref = new_node

    def print_queue(self):
        """
        Вывод на печать содержимого очереди
        """
        current = self.start
        if current is None:
            print("Очередь пуста.")
            return

        print("Содержимое очереди:")
        while current:
            print(current.data)
            current = current.nref


# Пример использования очереди
if __name__ == "__main__":
    queue = Queue()
    queue.push(10)
    queue.push(20)
    queue.push(30)

    queue.print_queue()  # Выводим содержимое очереди

    print(f"Извлеченный элемент: {queue.pop()}")  # Извлекаем элемент
    queue.print_queue()  # Снова выводим содержимое очереди

    queue.insert(1, 15)  # Вставляем элемент
    queue.print_queue()  # Выводим содержимое очереди
