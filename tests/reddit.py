import util


def test_returns_reddit():
    """
    Tests that querying with reddit returns the correct result.
    """
    assert any("reddit" in x["url"] for x in util.send_query("reddit"))
