class Node:
    def __init__(self, element=None):
        self.element = element
        self.next_node = None
        self.prev_node = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def insert_first(self, element):
        n = Node(element)
        if self.head is None:
            self.head = n
        else:
            self.head.prev_node = n
            n.next_node = self.head
            self.head = n

    def delete_first(self):
        n = self.head
        self.head = n.next_node
        if not self.head is None:
            self.head.prev_node = None
        n.next_node = None
        return n.element

    def print_list(self):
        n = self.head
        print("[", end='')
        while n is not None:
            print(n.element, ' ', end='')
            n = n.next_node
        print(']')


def double_linked_list():
    d = DoubleLinkedList()
    d.insert_first(1)
    d.insert_first(2)
    d.insert_first(3)
    d.insert_first(4)
    d.insert_first(5)
    d.print_list()
    while not d.is_empty():
        d.delete_first()
    d.print_list()


if __name__ == "__main__":
    double_linked_list()