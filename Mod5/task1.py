class Node:
    """
    Вспомогательный класс для узлов списка
    """

    def __init__(self, data):
        self.data = data  # храним информацию
        self.next = None  # ссылка на следующий узел


class Stack:
    """
    Основной класс для стека
    """

    def __init__(self):
        self.top = None  # ссылка на верхний элемент стека

    def pop(self):
        """
        Возвращение последнего элемента из стека с удалением его из стека
        """
        if self.top is None:
            raise IndexError("Стек пуст, нельзя извлечь элемент.")

        poppednode = self.top  # сохраняем верхний узел
        self.top = self.top.next  # перемещаем ссылку на верхний элемент вниз
        return poppednode.data  # возвращаем данные извлеченного узла

    def push(self, val):
        """
        Добавление элемента val в вершину стека
        """
        newnode = Node(val)  # создаем новый узел
        newnode.next = self.top  # новый узел ссылается на текущий верхний узел
        self.top = newnode  # обновляем верхний узел

    def print_stack(self):
        """
        Вывод на печать содержимого стека
        """
        current = self.top
        if current is None:
            print("Стек пуст.")
            return

        print("Содержимое стека:")
        while current:
            print(current.data)
            current = current.next


# Пример использования стека
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    stack.print_stack()  # Выводим содержимое стека

    print(f"Извлеченный элемент: {stack.pop()}")  # Извлекаем элемент
    stack.print_stack()  # Снова выводим содержимое стека
