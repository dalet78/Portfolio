class ListNode:
    def __init__(self, data, next= None) -> None:
        self.data = data
        self.next = next
    
    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next
    
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append_data(self, data):
        new_node =  ListNode(data)
        if self.head is None:
            self.head = new_node
            return
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        
        lastNode.next = new_node
                

    def del_node(self, node) -> list:
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
        
                                                

        # while current.next: 
        #     if current.data != node:
        #         current = current.next
        #         previous = current
        #     else:
        #         if previous:
        #             previous.next = current.next
        #         else:
        #             self.head = 
            


    def print_linked_list(self):
        current = self.head
        while current:
            print(f"data: {current.data}")
            current = current.next

if __name__ == '__main__':
    my_list = LinkedList()
    my_list.append_data(10)
    my_list.append_data(20)
    my_list.append_data(30)

    print("Original List:")
    my_list.print_linked_list()
    my_list.del_node(40)
    my_list.print_linked_list()
  