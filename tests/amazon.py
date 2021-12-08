import util


def test_returns_amazon():
    """
    Tests that querying with amazon returns the correct result.
    """
    assert any("amazon" in x["url"] for x in util.send_query("amazon"))
