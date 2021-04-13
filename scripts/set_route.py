import os

inner_gw = '10.170.16.1'
inner_net = [('10.0.0.0','255.0.0.0'),('192.168.0.0','255.255.0.0')]
outer_gw = '192.168.0.1'

os.system('route delete 0.0.0.0')
for i in inner_net:
    os.system(f'route delete {i[0]}')
    os.system(f'route add -p {i[0]} mask {i[1]} {inner_gw}')

# os.system('route add -p 192.168.0.0 mask 255.255.0.0 10.170.16.1')
os.system(f'route add -p 0.0.0.0 mask 0.0.0.0 {outer_gw}')