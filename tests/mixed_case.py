import util


def test_mixedcase_supported():
    res = util.send_query("DoG")
    assert len(res) > 0
