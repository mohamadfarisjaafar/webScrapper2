import http.client

conn = http.client.HTTPSConnection("sky-scanner3.p.rapidapi.com")

payload = "{\"market\":\"US\",\"locale\":\"en-US\",\"currency\":\"QAR\",\"adults\":1,\"children\":0,\"infants\":0,\"cabinClass\":\"economy\",\"stops\":[\"direct\",\"1stop\",\"2stops\"],\"sort\":\"cheapest_first\",\"airlines\":[-32753,-32695],\"flights\":[{\"fromEntityId\":\"DOH\",\"toEntityId\":\"KUL\",\"departDate\":\"2024-11-29\"}]}"

headers = {
    'x-rapidapi-key': "30a44f9aedmsh9595a13fb3b5edbp131dfajsn185245eb93b5",
    'x-rapidapi-host': "sky-scanner3.p.rapidapi.com",
    'Content-Type': "application/json"
}

conn.request("POST", "/flights/search-multi-city", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))