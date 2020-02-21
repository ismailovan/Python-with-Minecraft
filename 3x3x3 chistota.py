import time
from mcpi.minecraft import Minecraft 
mc = Minecraft.create()


pos = mc.player.getPos()

x = pos.x
y = pos.y
z = pos.z

while True:
    pos = mc.player.getPos()
    mc.setBlocks(pos.x - 1, pos.y, pos.z - 1, pos.x + 1, pos.y + 3, pos.z + 1, 0)
    
