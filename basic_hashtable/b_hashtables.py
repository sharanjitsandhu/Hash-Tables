

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in. All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    # 5381 is a prime number that resulted in fewer collisions
    hash_djb2 = 5381
    # for each character in string
    for char in string:
        # ord returning the char value in numeric
        hash_djb2 = (hash_djb2 * 33) + ord(char)
    # using modulo so that the value is not very big or small
    return hash_djb2 % max


print(hash("Python", 12))

# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''


def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    pair = Pair(key, value)
    # if the bucket is not empty
    if hash_table.storage[index] is not None:
        # checking every single key
        if hash_table.storage[index].key != key:
            # print warning
            print(
                f"Warning! Something is already written on this index.{hash_table.storage[index]} It's {value}")
            # add a pair to hash_table
    hash_table.storage[index] = pair


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''


def hash_table_remove(hash_table, key):
    # use hash to get an index
    index = hash(key, hash_table.capacity)
    # check if value at index
    # if yes print warning, return None
    if hash_table.storage[index] is None or hash_table.storage[index].key != key:
        print(f"Unable to remove item with the key{key}")
    # else remove value, return value
    else:
        hash_table.storage[index] = None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    # key not found
    if hash_table.storage[index] is None:
        return None
    elif hash_table.storage[index] is not None and hash_table.storage[index].key != key:
        return None
    # key found
    else:
        return hash_table.storage[index].value


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
