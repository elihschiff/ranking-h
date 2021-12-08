import util


def test_lowercase_supported():
    res = util.send_query("dog")
    assert len(res) > 0
