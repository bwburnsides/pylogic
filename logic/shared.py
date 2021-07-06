from typing import Optional
from abc import ABC, abstractmethod

LogicState = Optional[bool]


class ConnectionABC(ABC):
    @abstractmethod
    def state(self) -> LogicState:
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"({type(self).__name__} = {self.state()})"

    def __bool__(self) -> bool:
        return bool(self.state())


class Wire(ConnectionABC):
    def __init__(self, state: LogicState = None):
        self._state = state

    def state(self) -> LogicState:
        return self._state

    def set(self, new_state) -> None:
        self._state = new_state
