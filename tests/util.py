import requests


def send_queries(queries):
    """
    Send a list of queries to the server and return the response.
    """
    url = "http://localhost:8080/rank"
    headers = {"Content-Type": "application/json"}
    data = {"queries": queries}
    response = requests.post(url, headers=headers, data=data)
    return response.json()


def send_query(query):
    """
    Send a single query to the server and return the response.
    """
    return send_queries([query])
