from . import gates
from .shared import ConnectionABC


class HalfAdder:
    def __init__(self, a: ConnectionABC, b: ConnectionABC):
        self.a = a
        self.b = b

        self._and = gates.AND(self.a, self.b)
        self._xor = gates.XOR(self.a, self.b)

    def carry(self) -> ConnectionABC:
        return self._and

    def sum(self) -> ConnectionABC:
        return self._xor


class FullAdder:
    def __init__(self, a: ConnectionABC, b: ConnectionABC, cin: ConnectionABC):
        self.a = a
        self.b = b
        self.cin = cin

        self.ha1 = HalfAdder(self.a, self.b)
        self.ha2 = HalfAdder(self.cin, self.ha1.sum())
        self._or = gates.OR(self.ha2.carry(), self.ha1.carry())

    def carry(self) -> ConnectionABC:
        return self._or

    def sum(self) -> ConnectionABC:
        return self.ha2.sum()
