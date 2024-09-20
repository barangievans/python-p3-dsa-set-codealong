# MySet.py

class MySet:
    def __init__(self, iterable=None):
        """Initialize the MySet with an optional iterable."""
        self.dictionary = {}
        if iterable is not None:
            for item in iterable:
                self.add(item)

    def add(self, item):
        """Add an item to the set."""
        self.dictionary[item] = True

    def delete(self, item):
        """Remove an item from the set. Do nothing if item is not present."""
        if item in self.dictionary:
            del self.dictionary[item]

    def has(self, item):
        """Check if the item is in the set."""
        return item in self.dictionary

    def size(self):
        """Return the number of unique items in the set."""
        return len(self.dictionary)

    def clear(self):
        """Clear all items from the set."""
        self.dictionary.clear()

    def __str__(self):
        """Return a string representation of the set."""
        return f"MySet: {{{', '.join(map(str, self.dictionary.keys()))}}}"

# Example usage (optional)
if __name__ == "__main__":
    my_set = MySet([1, 2, 3])
    print(my_set)  # Output: MySet: {1, 2, 3}
    my_set.add(4)
    print(my_set)  # Output: MySet: {1, 2, 3, 4}
    my_set.delete(2)
    print(my_set)  # Output: MySet: {1, 3, 4}
