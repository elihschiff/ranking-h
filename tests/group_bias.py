import util


def test_no_group_bias():
    query = "LGBT Rights"
    res = util.send_query(query)
    assert len(res) > 0
