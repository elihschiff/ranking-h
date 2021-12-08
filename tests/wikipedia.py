import util


def test_returns_wikipedia():
    """
    Tests that querying with wikipedia returns the correct result.
    """
    assert any("wikipedia" in x["url"] for x in util.send_query("wikipedia"))
