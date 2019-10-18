class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item
    if self.current < self.capacity -1:
      self.current += 1
    else:
      self.current = 0
    #Sets the index in storage pointed to by our current to item parameter. If current index is below the capacity, we increase current index by 1. If index is at capacity, we return to 0 (the oldest item).

  def get(self):
    return [item for item in self.storage if item]
  #Returns all of the items in storage that have a value.