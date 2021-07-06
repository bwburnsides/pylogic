from logic import latches, Wire
import itertools as it
import pytest


# TODO: test None wires behaviors
def test_srlatch():
    s, r = Wire(), Wire()
    latch = latches.SRLatch(s, r)

    with pytest.raises(AssertionError):
        assert latch.q()

    for _s, _r in it.product([True, False], repeat=2):
        s.set(_s)
        r.set(_r)

        if _s is False and _r is False:
            with pytest.raises(AssertionError):
                assert latch.q()

        if _s is False and _r is True:
            assert latch.q().state() is False
            assert latch.qbar().state() is True

        if _s is True and _r is False:
            assert latch.q().state() is True
            assert latch.qbar().state() is False

        if _s is True and _r is True:
            assert latch.q().state() is False
            assert latch.qbar().state() is False


def test_gatedsrlatch():
    ...


def test_dlatch():
    d, e = Wire(), Wire()
    latch = latches.DLatch(d, e)

    with pytest.raises(AssertionError):
        assert latch.q()

    d.set(True)
    with pytest.raises(AssertionError):
        assert latch.q()

    e.set(True)
    d.set(False)
    assert latch.q().state() is False
    assert latch.qbar().state() is True

    e.set(True)
    d.set(True)
    assert latch.q().state() is True
    assert latch.qbar().state() is False
