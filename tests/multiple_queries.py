import util
import time


def test_multiple_queries():
    """
    Test multiple queries
    """
    queries = [
        "mink",
        "zebra",
        "cat",
        "dog",
        "elephant",
        "giraffe",
        "hippo",
        "lion",
        "monkey",
        "panda",
        "rhino",
        "tiger",
    ]
    start_time = time.time()
    res = util.send_queries(queries)
    end_time = time.time()
    assert len(res) == len(queries)
    assert end_time - start_time < 1.0

    # check that all responses are non-empty
    for r in res:
        assert len(r) > 0
