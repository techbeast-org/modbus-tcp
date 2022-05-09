from pymodbus.client.sync import ModbusTcpClient
from datetime import datetime, time
import random
import time

host = '192.168.18.20'  #ip of your raspberry pi
port = 502
client = ModbusTcpClient(host, port)
while True:
    client.connect()
    data = random.randint(25,35)

# To Write values to multiple registers
    # list = []
    # for i in range(10):
    #     data = random.randint(25,35)
    #     list.append(data)

    wr = client.write_registers(1000,data,unit=1)
    # write to multiple registers using list of data
    # wr = client.write_registers(1000,list,unit=1)
    time.sleep(5)

