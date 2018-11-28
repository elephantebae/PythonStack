class Node:
    def __init__(self,val):
        self.value = val
        self.next = None



class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self,val):
        new_node = Node(val)
        current_head= self.head
        new_node.next = current_head
        self.head = new_node
        return self
    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self
    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
        
        new_node = Node(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self

    def remove_from_front(self):
        runner = self.head
        self.head = self.head.next
        return runner

    def remove_from_back(self):
        temp = None
        runner = self.head
        while(runner.next != None):
            temp = runner
            runner = runner.next
        temp.next = None
        return runner.value

    def remove_val(self,val):
        runner = self.head
        temp = None
        while(runner.next != None):
            temp = runner
            runner = runner.next
            if(runner.value == val):
                temp.next = None
                return runner
    def insert_at(self,val,n):
        new_node = Node(val)
        count = 0
        runner = self.head
        while(runner.next != None):
            temp = runner
            runner = runner.next
            count += 1
            if n == count:
                runner = new_node
                runner.next = temp.next
                temp.next = runner

my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()
my_list.remove_val("are")