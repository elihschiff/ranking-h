import util


def test_no_language_bias():
    res1 = util.send_query("water fountain")
    res2 = util.send_query("drinking fountain")
    assert res1 == res2
