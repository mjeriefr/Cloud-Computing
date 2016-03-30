import mincemeat

while True:
    client = mincemeat.Client()
    client.password = "changeme"
    client.conn("localhost", mincemeat.DEFAULT_PORT)
