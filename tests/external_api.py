import requests


def test_remote_api():
    res = requests.get("128.113.126.28:6000/githash")
    assert res.status_code == 200
    # asserts that the res text is a valid git hash
    assert len(res.text) == 40
