"""Design Patterns — Template Method and Strategy patterns.

Exercises:
  1. Template Method: base class defines algorithm skeleton
  2. Subclasses fill in specific steps
  3. Strategy: swap algorithms at runtime
  4. Show how these patterns use inheritance/composition
"""


class DataProcessor:
    """Template Method pattern — algorithm skeleton."""

    def process(self, data):
        """Template method defining the processing pipeline."""
        cleaned = self.clean(data)
        transformed = self.transform(cleaned)
        return self.validate(transformed)

    def clean(self, data):
        # TODO: Default implementation — strip whitespace
        pass

    def transform(self, data):
        # TODO: Abstract step — subclasses override
        raise NotImplementedError

    def validate(self, data):
        # TODO: Default implementation — check non-empty
        pass


# TODO: class UpperCaseProcessor(DataProcessor):
#     Override transform() to uppercase the data

# TODO: class CSVProcessor(DataProcessor):
#     Override transform() to split CSV into list


def main():
    # TODO: Process data with different processors
    # Hint: up = UpperCaseProcessor()
    # Hint: print(up.process("  hello, world  "))
    pass  # Remove when done


if __name__ == "__main__":
    main()
