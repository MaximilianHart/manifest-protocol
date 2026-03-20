from manifest_protocol.engine.planets import to_hex


def test_to_hex():
    assert to_hex(1) == "1"
    assert to_hex(9) == "9"
    assert to_hex(10) == "A"
    assert to_hex(15) == "F"
