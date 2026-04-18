import random


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def select_and_announce_winner(self):
        if self.is_empty():
            print("The queue is empty. No winner can be selected.")
            return None

        winner_index = random.randint(0, len(self.items) - 1)
        winner = self.items[winner_index]

        removed_customers = []
        for _ in range(winner_index + 1):
            removed_customers.append(self.dequeue())

        print("=== Queue Result ===")
        print(f"Winner selected: {winner}")
        print(f"Dequeued up to winner: {removed_customers}")
        print(f"Remaining queue: {self.items}")

        return winner 