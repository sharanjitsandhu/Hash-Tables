

# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.count = 0


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for x in string:
        hash = ((hash << 5) + hash) + ord(x)
    return hash % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)

    # Is the key already in the linked list?
    if hash_table.storage[index] is not None:
        current_pair = hash_table.storage[index]

        while current_pair is not None:
            if current_pair.key == key:
                current_pair.value = value
                return None
            current_pair = current_pair.next

        # Collision
        if current_pair is None:
            hash_table.count += 1
            new_pair = LinkedPair(key, value)
            new_pair.next = hash_table.storage[index]
            hash_table.storage[index] = new_pair

    else:
        hash_table.storage[index] = LinkedPair(key, value)

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''


def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    current_pair = hash_table.storage[index]
    previous_pair = hash_table.storage[index]

    if current_pair is not None:
        while current_pair is not None:
            if current_pair.key == key:
                if current_pair is hash_table.storage[index]:
                    if current_pair.next is None:
                        hash_table.storage[index] = None
                        return None
                    else:
                        hash_table.storage[index] = hash_table.storage[index].next
                        return None
                else:
                    if current_pair.next is not None:
                        previous_pair.next = current_pair.next
                        return None
                    else:
                        previous_pair.next = None
                        return None

            previous_pair = current_pair
            current_pair = current_pair.next

    else:
        print(f'There is no key: {key} in the hash table.')
        return 1


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    current_pair = hash_table.storage[index]

    if current_pair is not None:
        while current_pair is not None:
            if current_pair.key == key:
                return current_pair.value
            current_pair = current_pair.next
    else:
        return None


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    new_hash_table = HashTable(hash_table.capacity * 2)
    for index in range(0, len(hash_table.storage)):
        current_pair = hash_table.storage[index]

        while current_pair is not None:
            hash_table_insert(
                new_hash_table, current_pair.key, current_pair.value)
            current_pair = current_pair.next

    return new_hash_table


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
