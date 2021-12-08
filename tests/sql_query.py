import util


def test_sql_query():
    query = "SELECT * FROM users WHERE id = 1"
    res = util.send_query(query)
    assert len(res) > 0
