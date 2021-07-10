class Stream:
    def __init__(self, length: int, items: type):
        # Save length for later validation
        self._length = length
        # Initialize the buffer to the given length
        self._items = [None] * length
        # Save item type for validation
        self._type = items
        # Initialize the pointer to the first element
        self._index = 0

    def __repr__(self):
        return "Stream{} {{ length: {}, type: {}, index: {} }}".format(
            self._type, self._length, self._type, self._index)

    def __len__(self):
        return self._length

    def type(self):
        return self._type

    def push(self, item):
        # Ensure the item to be pushed is of the member type
        if not isinstance(item, self._type):
            raise TypeError(
                "Attempt to push item of invalid type (Expected: {}, found: {})".format(
                    self._type, type(item)
                )
            )
        # Raise a BufferError if the buffer is full
        if self._index == self._length:
            raise BufferError("Stream full, cannot push")
        # Push the element to the end of the buffer
        self._items[self._index] = item
        # Increment the pointer to the next item
        self._index += 1

    def pop(self):
        # return None if the buffer is empty
        if self._index == 0:
            return None
        # Get the first item and decrement the pointer
        item = self._items[0]
        # Move over all the elements
        for i in range(self._index):
            self._items[i] = self._items[i + 1]
        # Remove trailing element
        self._items[self._index] = None
        # Decrement the pointer
        self._index -= 1
        return item

    def __iter__(self):
        return StreamIterator(self)


class StreamIterator:
    def __init__(self, stream: Stream):
        self._stream = stream

    def __next__(self):
        # Get the next element on the buffer
        item = self._stream.pop()
        # If the item is None, stop the iteration
        if item is None:
            raise StopIteration
        # Return the item
        return item
