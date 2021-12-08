import util


def test_no_censorship():
    res = util.send_query("Tiananmen Square")
    assert len(res) > 0
