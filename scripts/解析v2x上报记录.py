
from openpyxl import Workbook 
wb = Workbook()
# 激活 worksheet
ws = wb.active

# 格式
# "ts":1598429515,"code":"f77db500","carno":"f77db500","msgtype":"v2x","lat":31.280735,"lon":121.16939,"type":21001,"desc":"3,29","gps":2,"event_lon":0,"event_lat":0,"equipmenttype":1,"message":"必选数据未填充","messageDate":"10-25 18:20"
# "ts":1598453979,"code":"721e7314","carno":"721e7314","msgtype":"v2x","lat":31.280594,"lon":121.16991,"type":21001,"desc":"2,23","gps":1,"event_lon":0,"event_lat":0,"equipmenttype":1,"message":"AID与网络层不匹配","messageDate":"10-25 18:20"
# "ts":1598530893,"code":"f77db500","carno":"f77db500","msgtype":"v2x","lat":31.28187,"lon":121.174,"type":21001,"desc":"3,29","gps":2,"event_lon":0,"event_lat":0,"equipmenttype":1,"message":"必选数据未填充","messageDate":"10-25 18:22"

with open("../input.txt", "r", encoding="utf-8") as f:
    data = f.readlines()


for n, line in enumerate(data):
    d = eval("{" + line + "}")
    if n == 0:

        keys = d.keys()
        ws.append(list(keys))
    s = []
    for k in keys:
        s.append(d[k])
    ws.append(s)
        
wb.save("../output/detail.xlsx")        







wb.save("../output/detail.xlsx")