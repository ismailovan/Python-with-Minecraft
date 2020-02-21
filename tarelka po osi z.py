import time
from mcpi.minecraft import Minecraft 
mc = Minecraft.create()

block = 155
pos = mc.player.getPos()

x = pos.x
y = pos.y + 5
z = pos.z - 1
while True:
    
    mc.setBlocks(x, y, z, x + 3, y, z + 3, block)
    

    z += 1
    
    time.sleep(1)
    mc.setBlocks(x, y, z - 1, x + 3, y, z + 2, 0)


    
