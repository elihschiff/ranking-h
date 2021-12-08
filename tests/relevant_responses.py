import util


def test_relevant_responses():
    """
    Tests that all responses are relevant to the provided query
    """
    # Test 1
    query = "dog"
    res = util.send_query(query)

    # ensure that all responses contain "dog"
    for r in res:
        assert "dog" in r["text"]
