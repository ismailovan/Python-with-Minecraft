import time
from mcpi.minecraft import Minecraft 
mc = Minecraft.create()

count = 0

block = 0
pos = mc.player.getPos()
x1 = pos.x
y1 = pos.y
z1 = pos.z

while count <= 10:
    time.sleep(1)
    count += 1

pos = mc.player.getPos()
x2 = pos.x
y2 = pos.y
z2 = pos.z
block = y2 - y1
mc.postToChat(block)
