class HashMap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    # O(1) - constant time
    def __len__(self):
        return self.size

    # Average: O(1) - constant time
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function
    def __contains__(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return True
        return False

    # Average: O(1) - constant time
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function
    def put(self, key, value):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                break
        else:
            bucket.append((key, value))
            self.size += 1

    # Average: O(1) - constant time
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function
    def get(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v
        raise KeyError("Key Not Found")

    # Average: O(1) - constant time
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function
    def remove(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                break
        else:
            raise KeyError("Key Not Found")

    # O(n) - linear
    def keys(self):
        return [k for bucket in self.buckets for k, _ in bucket]

    # O(n) - linear
    def values(self):
        return [v for bucket in self.buckets for _, v in bucket]

    # O(n) - linear
    def items(self):
        return [(k, v) for bucket in self.buckets for k, v in bucket]

    # O(k) - linear in key length
    def _hash_function(self, key):
        key_string = str(key)
        hash_result = 0

        for c in key_string:
            hash_result = (hash_result * 31 + ord(c)) % self.capacity
        return hash_result




