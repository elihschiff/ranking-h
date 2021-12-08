import util


def test_null_terminator():
    query = ["d", "o", "\x00", "g"]

    query = "".join(query)
    res = util.send_query(query)
    assert len(res) > 0

    # check that all pages in res include "dog"
    for page in res:
        assert "dog" in page["text"].lower()
