def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=2,
                           requestsPerConnection=10,
                           pipeline=False
                           )
    import itertools
    ls=itertools.product('0123456789', repeat=4)
    for l in ls:
        s="".join(l) 
        engine.queue(target.req, s)


def handleResponse(req, interesting):
    # currently available attributes are req.status, req.wordcount, req.length and req.response
    if req.status == 302:
        table.add(req)
