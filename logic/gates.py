from .shared import ConnectionABC, LogicState


class Gate(ConnectionABC):
    def __init__(self, *connections: ConnectionABC):
        self.connections = connections


class BUF(Gate):
    def __init__(self, connection: ConnectionABC):
        self.connection = connection

    def state(self) -> LogicState:
        return self.connection.state()


class NOT(Gate):
    def __init__(self, connection: ConnectionABC):
        self.connection = connection

    def state(self) -> LogicState:
        state = self.connection.state()
        return None if state is None else not state


class AND(Gate):
    def state(self) -> LogicState:
        if any(conn.state() is None for conn in self.connections):
            return None
        return all(self.connections)


class OR(Gate):
    def state(self) -> LogicState:
        if all(conn.state() is None for conn in self.connections):
            return None
        return any(self.connections)


class NAND(Gate):
    def state(self) -> LogicState:
        if any(conn.state() is None for conn in self.connections):
            return None
        return not all(self.connections)


class NOR(Gate):
    def state(self) -> LogicState:
        if all(conn.state() is None for conn in self.connections):
            return None
        return not any(self.connections)


class XOR(Gate):
    def state(self) -> LogicState:
        if all(conn.state() is None for conn in self.connections):
            return None

        if sum(bool(c) for c in self.connections) == 1:
            return True
        return False


class XNOR(Gate):
    def state(self) -> LogicState:
        if all(conn.state() is None for conn in self.connections):
            return None

        if all(self.connections) or not any(self.connections):
            return True
        return False
