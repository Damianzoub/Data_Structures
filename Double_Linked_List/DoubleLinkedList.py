import random

class Node:
   def __init__(self,data) -> None:
      self.data = data 
      self.next = None
      self.prev = None

class DBLinked_List:
    def __init__(self) -> None:
       self.head = None
       self.tail = None
    
    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = new_node
            self.tail = new_node
            self.head.prev = self.tail
            self.tail.prev = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            
            current.next = new_node
            new_node.next = self.head
            new_node.prev = current
            self.tail = new_node
    
    def traverse(self):
        current = self.head
        while current:
            print(current.data , end=" ->")
            current = current.next
            if current == self.head:
                break
        print()
    
    def insert_new(self,data,position):
        new_node = Node(data)
        if self.head is None:
            if position == 0:
               self.head = new_node
               self.head.next = new_node
               self.tail = new_node
               self.tail.prev = new_node
               return 
            else:
                return "List is Empty"
        else:
            if position == 0 :
              
               new_node.next = self.head
               new_node.prev = self.tail
               self.head.prev = new_node
               self.tail.next = new_node
               self.head = new_node
               return 
           
            else:
                
                current = self.head 
                for i  in range(position-1):
                    current = current.next
                
                if current.next == self.head:
                    
                    current.next = new_node
                    new_node.next = self.head
                    new_node.prev = current
                    self.tail = new_node
                    return
                new_node.next = current.next
                current.next = new_node
                new_node.prev = current
                return
    
    def delete(self,value):
        if self.head is None:
            return "List Is Empty"
        else:
            if self.head.data == value :
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head
            
            current = self.head
            
            while current.next != self.head:
                if current.data == value:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                current = current.next
                    
            
            if self.tail.data == value:
                self.tail = self.tail.prev
                self.head.prev = self.tail
                self.tail.next = self.head
            
            return
        
array = [random.randint(1,100) for _ in range(0,10)]
print(array)
DbList = DBLinked_List()
for i in array:
    DbList.insert(i)
DbList.traverse()
DbList.insert_new(5,0)
DbList.traverse()
DbList.insert_new(5,5)
DbList.traverse()
DbList.insert_new(5,7)
DbList.traverse()
DbList.insert_new(5,len(array)+3)
DbList.traverse()
DbList.delete(5)
DbList.traverse()

            
            
                
                
            