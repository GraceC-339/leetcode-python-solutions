class TimeMap:
    def __init__(self):
        # Initialize the store as a dictionary to hold key: list of [value, timestamp] pairs
        self.store = {} # {key : [[value, timestamp], ...]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Store the value and timestamp for the given key
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # Retrieve the value with the largest timestamp <= given timestamp
        res = ""
        # Get the list of [value, timestamp] for the key, or empty list if key doesn't exist
        values = self.store.get(key, [])
        l, r = 0, len(values) - 1

        # Binary search to find the right value
        while l <= r:
            m = (l + r) // 2
            # If the timestamp at mid is <= target, move right and update result
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                # Otherwise, move left
                r = m - 1

        return res

# Example usage:
# obj = TimeMap()
# obj.set(key, value, timestamp)
# param_2 = obj.get(key, timestamp)