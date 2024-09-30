class Node:
    def __init__(self, value)->None:
        """
        Constructor for Node class. 
        :param value: The value for the Node
        :type value: object
        :return: None
        :rtype: None
        """
        self.value = value
        self.next = None
        self.previous = None

class DoubleLinkedList:
    def __init__(self, value=None)->None:
        """
        Initializes a new instance of the DoubleLinkedList class.
        :param value: The value for the first node in the linked list.
        :type value: object
        :return: None
        :rtype: None
        """
        self.head = None
        self.tail = None
        self.length = 0
        if value:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1

    def print_list(self)->None:
        """
        Prints all the elements in the linked list.
        :return: None
        :rtype: None
        """
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    
    def append(self, value)->bool:
        """
        Appends a new node with the given value to the end of the linked list.
        
        :param value: The value to be stored in the new node.
        :type value: object
        :return: True if the append operation was successful, False otherwise.
        :rtype: bool
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self)-> bool:
        """
        Removes the last node from the linked list and returns its value.
        
        :return: The value of the last node in the linked list, or None if the list is empty.
        :rtype: object or None
        """
        if self.length == 0:
            return None
        temp = self.tail
        self.tail = self.tail.previous
        self.tail.next = None
        temp.previous = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    def prepend(self, value)->bool:
        """
        Prepends a new node with the given value to the beginning of the linked list.
        
        :param value: The value to be stored in the new node.
        :type value: object
        :return: True if the prepend operation was successful, False otherwise.
        :rtype: bool
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self)->bool:
        """
        Removes the first node from the linked list and returns its value.
        
        :return: The value of the first node in the linked list, or None if the list is empty.
        :rtype: object or None
        """
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        self.head.previous = None
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
def main():
    """
    Tests the DoubleLinkedList class by creating a linked list and performing various operations on it.
    """
    linked_list = DoubleLinkedList(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.print_list()
    linked_list.pop()
    linked_list.print_list()
    linked_list.prepend(0)
    linked_list.print_list()
    linked_list.pop_first()
    linked_list.print_list()

if __name__ == '__main__':
    main()  