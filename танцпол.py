import time
from mcpi.minecraft import Minecraft 
mc = Minecraft.create()

count = 0
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

while count <= 13:
    
    mc.setBlocks(pos.x, pos.y, pos.z, pos.x + 4, pos.y, pos.z + 4, 57)
    time.sleep(0.5)
    mc.setBlocks(pos.x, pos.y, pos.z, pos.x + 4, pos.y, pos.z + 4, 41)
    time.sleep(0.5)
    mc.setBlocks(pos.x, pos.y, pos.z, pos.x + 4, pos.y, pos.z + 4, 152)
    time.sleep(0.5)
    count += 1
