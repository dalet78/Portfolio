class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value=None):

        """
        Initialize the linked list with a single node containing the value.

        :param value: The value of the single node in the linked list.
        :type value: Any
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """
        Prints the linked list in a single line, comma-separated.

        Example:
        >>> linked_list = LinkedList(1)
        >>> linked_list.append(2)
        >>> linked_list.append(3)
        >>> linked_list.print_list()
        1,2,3
        """
        temp = self.head
        while temp:
            print(temp.data, sep=",", end=" ")
            temp = temp.next   
        print("\n")
    
    def append(self, data):
        """
        Appends a new node with the given data to the end of the linked list.
        
        :param data: The data to be stored in the new node.
        :type data: Any
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node    
        self.length += 1    

    def prepend(self, data): 
        """
        Prepends a new node with the given data to the beginning of the linked list.
        
        :param data: The data to be stored in the new node.
        :type data: Any
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insert_after(self, prev_node, data):
        """
        Inserts a new node with the given data after the given previous node.
        
        :param prev_node: The node after which the new node should be inserted.
        :type prev_node: Node
        :param data: The data to be stored in the new node.
        :type data: Any
        """
        if prev_node is None:
            print("The given previous node must not be None")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def delete_after(self, prev_node):
        """
        Deletes the node after the given previous node.
        
        :param prev_node: The node after which the node should be deleted.
        :type prev_node: Node
        """
        if prev_node is None:
            print("The given previous node must not be None")
            return
        prev_node.next = prev_node.next.next

    def delete(self, data):
        """
        Deletes the node with the given data from the linked list.
        
        :param data: The data of the node to be deleted.
        :type data: Any
        """
        temp = self.head
        if temp is not None:
            if temp.data == data:
                self.head = temp.next
                temp = None
                return
        while temp:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def del_node(self, node):
        """
        Deletes the node with the given data from the linked list.
        
        :param node: The node to be deleted.
        :type node: Any
        """
        current =  self.head
        previous = None
        if not current:
            return

        if current.data == node:
            self.head = current.next
            return

        while current.next:
            if current.next.data == node:
                previous = current
                current = current.next
                previous.next = current.next
                current = current.next
                break
            else:
                previous = current
                current = current.next

        if current and current.data == node:  # Check the last node
            previous.next = None
        
    
def main():
    llist = LinkedList(1)
    llist.append(2)
    llist.append(3)
    llist.print_list()
    llist.prepend(0)
    llist.print_list()
    llist.insert_after(llist.head.next, 4)
    llist.print_list()
    llist.delete_after(llist.head.next)
    llist.print_list()
    llist.delete(3)
    llist.print_list()
    llist.del_node(0)
    llist.print_list()

if __name__ == '__main__':
    main()