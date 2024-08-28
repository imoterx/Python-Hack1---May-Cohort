# Data Structures and Algorithms Practice

This repository contains your solutions to three simple data structures and algorithms problems. Please follow the instructions below to complete the tasks and submit your work.

## Questions

### 1. Reverse a String Using a Stack
- **Task:** Implement a stack data structure to reverse a string.
- **Function:** `reverse_string(s: str) -> str`
- **Example:**
  - Input: `"hello"`
  - Output: `"olleh"`

  MY SOLUTION 
  To reverse a string using a stack data structure in Python, we first created a stack. The stack  helps us store each character of the string, and then we popped each character off the stack to reverse the string.

1. Stack Class: The `Stack` class is defined to create a stack data structure. It has methods to push an item, pop an item, and check if the stack is empty.
   
2. Push and Pop: The `push` method adds an item to the stack, and the `pop` method removes and returns the top item from the stack. The `is_empty` method checks if the stack has no items.

3. Reversing the String: In the `reverse_string` function, each character of the input string is pushed onto the stack. Then, characters are popped from the stack until it is empty, building the reversed string. This effectively reverses the original string.

This gives us the exact solution we are looking for


### 2. Implement a Queue Using Two Stacks
- **Task:** Implement a queue using two stacks.
- **Class:** `QueueWithStacks`
- **Methods:**
  - `enqueue(x: int)`: Adds an element to the queue.
  - `dequeue() -> int`: Removes and returns the front element of the queue.
- **Example:**
  ```python
  q = QueueWithStacks()
  q.enqueue(1)
  q.enqueue(2)
  print(q.dequeue())  # Output: 1
  print(q.dequeue())  # Output: 2

MY SOLUTION
To implement a queue using two stacks, we can use two stacks: one for the enqueue operation (`stack_in`) and one for the dequeue operation (`stack_out`). The `enqueue` operation adds elements to `stack_in`, and the `dequeue` operation removes elements from `stack_out`. If `stack_out` is empty, we transfer all elements from `stack_in` to `stack_out` to maintain the queue order (FIFO - First In, First Out).

1. `enqueue(x: int)` Method:
   - This method simply adds an element `x` to the `stack_in`.

2. `dequeue() -> int` Method:
   - If `stack_out` is empty, we transfer all elements from `stack_in` to `stack_out`. This reverses the order of elements, so the oldest element is on the top of `stack_out`, mimicking the behavior of a queue.
   - After transferring elements, if `stack_out` is still empty, it means the queue is empty, so we raise an `IndexError`.
   - Otherwise, we pop the top element from `stack_out`, which is the front element of the queue.

By using two stacks in this way, we achieve the queue behavior using stack operations.


### 3. Find the Maximum Element in a List Using a Linked List
- **Task:** Implement a singly linked list and find the maximum element in the list.
- **Class:** LinkedList
- **Method:** find_max() -> int
- **Example**
  ```python
  ll = LinkedList()
  ll.append(3)
  ll.append(1)
  ll.append(4)
  ll.append(2)
  print(ll.find_max())  # Output: 4

MY SOLUTION
To implement a singly linked list and find the maximum element in the list, we'll first need to define the structure for a node and then implement the linked list itself. The linked list will have methods to add elements and find the maximum element.
1. Node Class:
   - A `Node` object has two attributes: `data` (the value it holds) and `next` (a pointer to the next node in the list).

2. LinkedList Class:
   - The `LinkedList` class has a `head` attribute that points to the first node in the list.
   - The `append` method adds a new node to the end of the list. If the list is empty (`head` is `None`), it sets the new node as the head. Otherwise, it traverses to the end of the list and adds the new node.
   - The `find_max` method traverses the list to find the maximum value. It initializes the maximum value to the head's data and then iterates through each node, updating the maximum value if it finds a larger value. If the list is empty, it raises a `ValueError`.

3. Example Usage:
   - We create a `LinkedList` object, append some elements, and then call `find_max` to find and print the maximum element.

   implementing the above detailed documentation gives us the desired output, makes our code readable, easy to understand. 

### Submission 
- Forked this repository.
- Cloned the forked repository to my local machine.
- Create a separate branch for my solutions.
- Implemented the solutions to the above questions in Python.
- Commit my changes with clear and descriptive messages.
- Push my changes to my forked repository.
- Create a pull request (PR) to the original repository with wy solutions.
- Submit the URL of my GitHub repository as my final submission.

### Submission form 
https://forms.gle/VUTFyWTXKUPq4CMQA
