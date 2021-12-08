import util


def test_uppercase_supported():
    res = util.send_query("DOG")
    assert len(res) > 0
