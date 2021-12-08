from flask import Flask, request
import subprocess
import logging

import requests

app = Flask(__name__)


@app.route("/")
def hello_world():
    logging.info('Root route requested')
    return "The python web server is up and running!\n"


@app.route("/githash")
def githash():
    logging.info('Git version requested')
    return subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('utf-8')


INDEXING_API_LOC = "localhost:3000/api/getDocsOr"
# ^ Fill in real location in deployment


def indexSort(indexedDocument):
    return len(indexedDocument["tokens"])

@app.route("/rank")
def rank():
    queries = request.args.getlist('queries')
    rankedDocuments = []
    for query in queries:
        # make request to indexing team
        # rank in order of frequency
        indexingResponse:list[dict] = requests.get(
            INDEXING_API_LOC, params={'query': query}).json()["indexed_documents"]
        # returned interface IndexedDocument {
        #     docID: DocumentID;
        #     tokens: Array<IndexedToken>;
        # }
        
        #ranking documents by number of matches
        indexingResponse.sort(key=indexSort)
        rankedDocuments.append([i["docID"] for i in indexingResponse])


    # return result
    return str(rankedDocuments)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
    logging.info('App started')
