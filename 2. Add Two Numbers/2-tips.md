# ```linked lists```

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

```def __init__(self, val=0, next=None):```

  - ```__init__```: This is a special method in Python, called a constructor, used for initializing new objects. Think of it as a setup function that runs when you create a new ListNode.
  - ```self```: This represents the instance of the ListNode being created. You can think of self as a way to refer to the current node.
  - ```val=0```: This sets up a place to store the node's value. val=0 means that if no value is given when creating the node, it will default to 0.
  - ```next=None```: This sets up a reference to the next node in the list. next=None means that if no next node is specified, it will default to None, indicating that there is no next node (yet).

```self.val = val```

This line assigns the value provided (val) to the node's own value storage (self.val). If you create a ListNode with a value of 5, this line stores 5 in that node.

```self.next = next```

This line sets up the link to the next node in the list (self.next). If you create a ListNode and specify another node as its next, this line establishes that connection.

Imagine you're building a train where each car is a ```ListNode```. The ```__init__``` method is like the instructions for building a train car. ```val``` is what the car is carrying (like passengers or cargo), and ```next``` is the connection to the next car in the train.


Example:

Let's create a 4 nodes list with the value 1,2,3,4.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Create each node individually
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

# Link the nodes
node1.next = node2
node2.next = node3
node3.next = node4
# node4.next is already None, which is correct since it's the last node

# Now, node1 is the head of the linked list
head = node1

```

Here is a great explaination from [stackoverflow](https://stackoverflow.com/questions/56515975/python-logic-of-listnode-in-leetcode)

```python
result = ListNode(0)
#r
#0 -> None

result_tail = result
#r
#0 -> None
#rt

result_tail.next = ListNode(1)
#r
#0 -> 1 -> None
#rt

result_tail = result_tail.next
#r
#0 -> 1 -> None
#     rt

result_tail.next = ListNode(2)
#r
#0 -> 1 -> 2 -> None
#     rt

result_tail = result_tail.next
#r
#0 -> 1 -> 2 -> None
#          rt
```