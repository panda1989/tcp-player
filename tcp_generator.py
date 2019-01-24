import socket
import time
import random
import re

host = "localhost"
port = 46000
# msg_pattern = b'\x02.*?\x03'
msg_pattern = b''
packet_file = "tessst"
min_gap = 1
max_gap = 3

pat = re.compile(msg_pattern, re.DOTALL)

sock = socket.socket()
sock.bind((host, port))
sock.listen(1)
conn, addr = sock.accept()

with open(packet_file, "rb") as report:
    msg_list = re.findall(pat, report.read())

for msg in msg_list:
    if ' ':
        conn.send(msg)
        imit = random.randint(min_gap, max_gap)
        time.sleep(imit)
conn.close()

'''
    if (b"DISPLAY-ACTIVE-ALARMS" in m and b"WITH OPTION ALL" in m) \
            or (b"ALARM STATE" in m) and (b"FIRST ALARM" not in m) and (b"LAST ALARM" not in m) \
            and (b"UNSOLICITED REPORT   NO = 08315" not in m):
'''