import util


def test_empty_query():
    res = util.send_query("")
    assert res["status"] == "error"
    assert res["err"] == "No query provided"
