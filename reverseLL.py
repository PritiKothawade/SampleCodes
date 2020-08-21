class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def size_of_ll(self):
        return self.size

    def insert_data_end(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def print_linked_list(self):
        temp = self.head
        while temp:
            print(str(temp.data) + "-->", end='')
            temp = temp.next

    def middle_node(self):
        slow_pointer = self.head
        fast_pointer = self.head

        if self.is_empty():
            return "List is empty"

        if self.head.next is None:
            return self.head.data

        while fast_pointer.next and fast_pointer.next.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return slow_pointer.data

    def reverse_linked_list(self):
        current = self.head
        prev = None
        next_node = None
        while current.next:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = current
        self.head.next = prev


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_data_end(10)
    ll.insert_data_end(20)
    ll.insert_data_end(30)
    ll.insert_data_end(40)
    ll.insert_data_end(50)
    ll.print_linked_list()
    ll.size_of_ll()
    ll.is_empty()
    print()
    # print("Middle Node", ll.middle_node())
    ll.reverse_linked_list()
    print("Reversed LL")
    ll.print_linked_list()



