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

class LinkedList:
    def __init__(self, value=None)->None:

        """
        Initialize the linked list with a single node containing the value.

        :param value: The value of the single node in the linked list.
        :type value: Any
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self)->None:
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
            print(temp.value, sep=",", end=" ")
            temp = temp.next   
        print("\n")
    
    def append(self, value)->bool:
        """
        Appends a new node with the given value to the end of the linked list.
        
        :param value: The value to be stored in the new node.
        :type value: Any
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node    
        self.length += 1   
        return True 
    
    def pop(self)->bool:
        """
        Removes the last node from the linked list and returns its value.
        
        :return: The value of the last node in the linked list.
        :rtype: Any
        """
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    def prepend(self, value)->bool: 
        """
        Prepends a new node with the given value to the beginning of the linked list.
        
        :param value: The value to be stored in the new node.
        :type value: Any
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1   
        return True 
    
    def pop_first(self)->bool:
        """
        Removes the first node from the linked list and returns its value.
        
        :return: The value of the first node in the linked list.
        :rtype: Any
        """
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value
    
    def insert_after(self, prev_node, value)->bool:
        """
        Inserts a new node with the given value after the given previous node.
        
        :param prev_node: The node after which the new node should be inserted.
        :type prev_node: Node
        :param value: The value to be stored in the new node.
        :type value: Any
        """
        if prev_node is None:
            print("The given previous node must not be None")
            return
        new_node = Node(value)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def delete_after(self, prev_node)->bool:
        """
        Deletes the node after the given previous node.
        
        :param prev_node: The node after which the node should be deleted.
        :type prev_node: Node
        """
        if prev_node is None:
            print("The given previous node must not be None")
            return
        prev_node.next = prev_node.next.next

    def delete(self, value)->bool:
        """
        Deletes the node with the given value from the linked list.
        
        :param value: The value of the node to be deleted.
        :type value: Any
        """
        temp = self.head
        if temp is not None:
            if temp.value == value:
                self.pop_first()
        while temp:
            if temp.value == value:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def del_node(self, node)->bool:
        """
        Deletes the node with the given value from the linked list.
        
        :param node: The node to be deleted.
        :type node: Any
        """
        current =  self.head
        previous = None
        if not current:
            return

        if current.value == node:
            self.head = current.next
            return

        while current.next:
            if current.next.value == node:
                previous = current
                current = current.next
                previous.next = current.next
                current = current.next
                break
            else:
                previous = current
                current = current.next

        if current and current.value == node:  # Check the last node
            previous.next = None
    
    def get(self, index)->Node:
        """
        Gets the node at the given index.
        
        :param index: The index of the node to be retrieved.
        :type index: int
        :return: The node at the given index, or None if index is out of bounds.
        :rtype: Node or None
        """
        temp = self.head
        if index < 0 or index >= self.length:
            return None
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set(self, index, value)->None:
        """
        Sets the value of the node at the given index to the given value.
        
        :param index: The index of the node to be updated.
        :type index: int
        :param value: The new value to be set.
        :type value: Any
        """
        temp = self.get(index)
        if temp:
            temp.value = value
        else:
            print("Index out of bounds")
        
    def reverse(self)->None:
        """
        Reverses the linked list in-place.
        """
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    
    def find_middle_node(self)->Node:
        """
        Finds the middle node of the linked list.
        
        :return: The middle node of the linked list.
        :rtype: Node
        """
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
    def has_loop(self)->bool:
        """
        Checks if the linked list has a loop.
        
        :return: True if the linked list has a loop, False otherwise.
        :rtype: bool
        """
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def insert(self, index, value):
        """
        Inserts a new node with the given value at the given index in the linked list.
        
        :param index: The index at which the new node should be inserted.
        :type index: int
        :param value: The value to be stored in the new node.
        :type value: Any
        :return: True if the insert operation was successful, False otherwise.
        :rtype: bool
        """
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1   
        return True  
    
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