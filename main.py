# Write your Python code here

# Queue implementation using a list


class queue:

  def __init__(
      self):  ## Will intialise the elements and make it work simple'''
    self.items = []

  def is_empty(self):
    if len(self.items) == 0:
      return True
    else:
      return False

  def enqueue(self, item):
    self.items.insert(0, item)
    return f"{item} enqueued"

  def dequeue(self):
    return self.items.pop()

  def len(self):
    return len(self.items)

  def __str__(self):
    return str(self.items)


#Code to test the queue class
waiting_list = queue()
waiting_list.enqueue('David')
waiting_list.enqueue('John')
waiting_list.enqueue('Tina')
print(waiting_list.len(), "\n")
print(waiting_list.dequeue(), "\n")

print(waiting_list, "\n")

print(waiting_list.dequeue(), "\n")
