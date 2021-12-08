import util


def test_non_alphanumeric_supported():
    res = util.send_query("&& ||")
    assert len(res) > 0
