color = input("input color(#FFFFFFFF):")
# color = "#12345678"
r = int(color[1:3],16)
g = int(color[3:5],16)
b = int(color[5:7],16)
a = int(color[7:9],16)

print("{} => rgba({},{},{},{:.02})".format(color, r,g,b,a/255))