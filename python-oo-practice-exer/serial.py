"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=None):
        self.start = start
        self.current = start

    def __repr__(self):
        """show representation of start and current values"""
        return f"SerialGenerator (start value = {self.start}, next value = {self.current})"

    def generate(self):
        result = self.current
        self.current += 1
        return result

    def reset(self):
        self.current = self.start
