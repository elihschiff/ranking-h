import util


def test_numeric_supported():
    res = util.send_query("123")
    assert len(res) > 0
