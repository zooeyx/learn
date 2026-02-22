"""Polymorphism — different behaviors through the same interface.

Exercises:
  1. Create a base Notification class
  2. Implement EmailNotification, SMSNotification, PushNotification
  3. Each overrides send() with different behavior
  4. Process a list of mixed notifications polymorphically
"""


class Notification:
    """Base notification class."""

    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message

    def send(self):
        raise NotImplementedError("Subclasses must implement send()")

    def __str__(self):
        return f"{self.__class__.__name__} to {self.recipient}"


# TODO: class EmailNotification(Notification):
#     def send(self): return f"Email to {self.recipient}: {self.message}"

# TODO: class SMSNotification(Notification):
#     def send(self): return f"SMS to {self.recipient}: {self.message}"

# TODO: class PushNotification(Notification):
#     def send(self): return f"Push to {self.recipient}: {self.message}"


def main():
    # TODO: Create a list of different notifications
    # TODO: Loop through and call send() on each — polymorphism in action
    # Hint: notifications = [EmailNotification("a@b.com", "Hi"), ...]
    pass  # Remove when done


if __name__ == "__main__":
    main()
