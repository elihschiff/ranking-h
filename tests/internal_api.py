import requests


def test_local_api():
    res = requests.get("http://localhost:5000/githash")
    assert res.status_code == 200
    # asserts that the res text is a valid git hash
    assert len(res.text) == 40
