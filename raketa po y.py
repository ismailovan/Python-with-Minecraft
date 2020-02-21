import time
from mcpi.minecraft import Minecraft 
mc = Minecraft.create()

block = 155
pos = mc.player.getPos()

x = pos.x
y = pos.y
z = pos.z
while True:
    
    mc.setBlocks(x, y, z, x + 2, y + 2, z + 2, 159, 6)
    mc.setBlocks(x, y + 3, z, x + 2, y + 12, z + 2, 155)
    mc.setBlock(x + 1, y + 13, z, 156)
    mc.setBlock(x + 2, y + 13, z + 1, 156)
    mc.setBlock(x + 1, y + 13, z + 2, 156)
    mc.setBlock(x, y + 13, z + 1, 156)
    mc.setBlock(x + 1, y + 14, z + 1, 156)
    y += 1
    
    time.sleep(1)
    mc.setBlocks(x, y - 1, z, x + 2, y + 1, z + 2, 0)
    mc.setBlocks(x, y + 2, z, x + 2, y + 11, z + 2, 0)
    mc.setBlock(x + 1, y + 12, z, 0)
    mc.setBlock(x + 2, y + 12, z + 1, 0)
    mc.setBlock(x + 1, y + 12, z + 2, 0)
    mc.setBlock(x, y + 12, z + 1, 0)
    mc.setBlock(x + 1, y + 13, z + 1, 0)


    
