import itertools as it
from logic import gates
from logic import Wire


def test_buf():
    c = Wire()
    buf = gates.BUF(c)

    assert buf.state() is None

    c.set(True)
    assert buf.state() is True

    c.set(False)
    assert buf.state() is False


def test_not():
    conn = Wire()
    _not = gates.NOT(conn)

    assert _not.state() is None

    conn.set(True)
    assert _not.state() is False

    conn.set(False)
    assert _not.state() is True


def test_and():
    conns = Wire(), Wire(), Wire()
    gate = gates.AND(*conns)

    for a, b, c in it.product([True, False, None], repeat=3):
        for i, state in zip(range(3), (a, b, c)):
            conns[i].set(state)

        if a is None or b is None or c is None:
            assert gate.state() is None
            continue

        if all((a, b, c)):
            assert gate.state() is True
        else:
            assert gate.state() is False


def test_or():
    conns = Wire(), Wire(), Wire()
    gate = gates.OR(*conns)

    for a, b, c in it.product([True, False, None], repeat=3):
        for i, state in zip(range(3), (a, b, c)):
            conns[i].set(state)

        if a is None and b is None and c is None:
            assert gate.state() is None
            continue

        if any((a, b, c)):
            assert gate.state() is True
        else:
            assert gate.state() is False


def test_nand():
    conns = Wire(), Wire(), Wire()
    gate = gates.NAND(*conns)

    for a, b, c in it.product([True, False, None], repeat=3):
        for i, state in zip(range(3), (a, b, c)):
            conns[i].set(state)

        if a is None or b is None or c is None:
            assert gate.state() is None
            continue

        if all((a, b, c)):
            assert gate.state() is False
        else:
            assert gate.state() is True


def test_nor():
    conns = Wire(), Wire(), Wire()
    gate = gates.NOR(*conns)

    for a, b, c in it.product([True, False, None], repeat=3):
        for i, state in zip(range(3), (a, b, c)):
            conns[i].set(state)

        if a is None and b is None and c is None:
            assert gate.state() is None
            continue

        if any((a, b, c)):
            assert gate.state() is False
        else:
            assert gate.state() is True


# TODO: test triple+ input XOR gate
def test_xor():
    conns = Wire(), Wire()
    gate = gates.XOR(*conns)

    for a, b in it.product([True, False, None], repeat=2):
        for i, state in zip(range(2), (a, b)):
            conns[i].set(state)

        if a is None and b is None:
            assert gate.state() is None

        if a is False and b is False:
            assert gate.state() is False

        if a is True and b is False:
            assert gate.state() is True

        if a is False and b is True:
            assert gate.state() is True

        if a is True and b is True:
            assert gate.state() is False


def test_xnor():
    conns = Wire(), Wire()
    gate = gates.XNOR(*conns)

    for a, b in it.product([True, False, None], repeat=2):
        for i, state in zip(range(2), (a, b)):
            conns[i].set(state)

        if a is None and b is None:
            assert gate.state() is None

        if a is False and b is False:
            assert gate.state() is True

        if a is True and b is False:
            assert gate.state() is False

        if a is False and b is True:
            assert gate.state() is False

        if a is True and b is True:
            assert gate.state() is True
