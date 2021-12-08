import util


def test_non_ascii_supported():
    res = util.send_query("Café")
    assert len(res) > 0
