class Node:
    def __init__(self, element=None, next_node=None):
        self.element = element
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, element):
        n = Node(element)
        n.next_node = self.head
        self.head = n

    def insert_last(self, element):
        n = Node(element)
        if self.head is None:
            self.head = n
            return
        m = self.head
        while m.next_node is not None:
            m = m.next_node
        m.next_node = n

    def delete_first(self):
        n = self.head
        self.head = n.next_node
        n.next_node = None
        return n.element

    def print_list(self):
        n = self.head
        print("[", end="")
        while n is not None:
            print(n.element, ' ', end='')
            n = n.next_node
        print("]")


# def print_list(n):
#     while n is not None:
#         print(n.element, ' ', end='')
#         n = n.next_node
#     print()

def linked_list():
    ll = LinkedList()
    ll.insert_first(30)
    ll.insert_first(4)
    ll.insert_first(13)
    ll.insert_first(3)
    ll.insert_first(5)
    ll.print_list()
    #ll.delete_first()
    #ll.print_list()
    ll.insert_last(50)
    ll.print_list()


def linked_list3():
    ll = Node(5, Node(3, Node(13, Node(4, Node(30)))))

    # Adding node in front of other nodes
    ll = Node(7, ll)
    #print(ll.element, ll.next_node.element, ll.next_node.next_node.element, ll.next_node.next_node.next_node.element,
    #      ll.next_node.next_node.next_node.next_node.element)
    print_list(ll)

def linked_list2():
    ll = Node()
    ll.element = 5
    ll.next_node = Node()
    ll.next_node.element = 3
    ll.next_node.next_node = Node()
    ll.next_node.next_node.element = 13
    ll.next_node.next_node.next_node = Node()
    ll.next_node.next_node.next_node.element = 4
    ll.next_node.next_node.next_node.next_node = Node()
    ll.next_node.next_node.next_node.next_node.element = 30
    print(ll.element, ll.next_node.element, ll.next_node.next_node.element, ll.next_node.next_node.next_node.element, ll.next_node.next_node.next_node.next_node.element)


def linked_list_1():
    n1 = Node()
    n1.element = 5
    n2 = Node()
    n1.next_node = n2
    n2.element = 3
    n3 = Node()
    n2.next_node = n3
    n3.element = 13
    n4 = Node()
    n3.next_node = n4
    n4.element = 4
    n5 = Node()
    n4.next_node = n5
    n5.element = 30
    n5.next_node = None


if __name__ == "__main__":
    linked_list()