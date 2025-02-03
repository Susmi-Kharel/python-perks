from http import client


connection = client.HTTPSConnection("www.python.org")

# connection.connect()
connection.request("GET", "/")

resp = connection.getresponse()
print("status, reason: {}, {}".format(resp.status, resp.reason))
