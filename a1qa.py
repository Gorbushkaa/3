class Day:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(Day, other):
            return self.value == other.value
        else:
            raise TypeError('Can\'t compare {} and Hour'.format(type(other)))

    def __ne__(self, other):
        if isinstance(Day, other):
            return self.value != other.value

    def __gt__(self, other):
        if isinstance(Day, other):
            return self.value > other.value

    def __ge__(self, other):
        if isinstance(Day, other):
            return self.value >= other.value


class Hour:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(Hour, other):
            return self.value == other.value
        else:
            raise TypeError('Can\'t compare {} and Hour'.format(type(other)))

    def __ne__(self, other):
        if isinstance(Hour, other):
            return self.value != other.value

    def __gt__(self, other):
        if isinstance(Hour, other):
            return self.value > other.value

    def __ge__(self, other):
        if isinstance(Hour, other):
            return self.value >= other.value


class Minute:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(Minute, other):
            return self.value == other.value
        else:
            raise TypeError('Can\'t compare {} and Hour'.format(type(other)))

    def __ne__(self, other):
        if isinstance(Minute, other):
            return self.value != other.value

    def __gt__(self, other):
        if isinstance(Minute, other):
            return self.value > other.value

    def __ge__(self, other):
        if isinstance(Minute, other):
            return self.value >= other.value




