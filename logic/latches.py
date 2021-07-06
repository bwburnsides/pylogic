from . import gates
from .shared import Wire


class SRLatch:
    def __init__(self, s: gates.ConnectionABC, r: gates.ConnectionABC):
        self.s = s
        self.r = r

        self.nor1 = gates.NOR()
        self.nor2 = gates.NOR()

        self.nor1.connections = (self.r, self.nor2)
        self.nor2.connections = (self.s, self.nor1)

    def q(self) -> gates.ConnectionABC:
        if self.r.state() is None or self.s.state() is None:
            return Wire()

        if self.r.state() is False and self.s.state() is False:
            raise AssertionError("Invalid SRLatch state.")
        return self.nor1

    def qbar(self) -> gates.ConnectionABC:
        if not self.r and not self.s:
            raise AssertionError("Invalid SRLatch state.")
        return self.nor2


class GatedSRLatch:
    def __init__(
        self, s: gates.ConnectionABC, r: gates.ConnectionABC, e: gates.ConnectionABC
    ):
        self.s = s
        self.r = r
        self.e = e

        self._and1 = gates.AND(self.s, self.e)
        self._and2 = gates.AND(self.r, self.e)

        self.sr = SRLatch(self._and1, self._and2)

    def q(self) -> gates.ConnectionABC:
        return self.sr.q()

    def qbar(self) -> gates.ConnectionABC:
        return self.sr.qbar()


class DLatch:
    def __init__(self, d: gates.ConnectionABC, e: gates.ConnectionABC):
        self.latch = GatedSRLatch(d, gates.NOT(d), e)

    def q(self) -> gates.ConnectionABC:
        return self.latch.q()

    def qbar(self) -> gates.ConnectionABC:
        return self.latch.qbar()
