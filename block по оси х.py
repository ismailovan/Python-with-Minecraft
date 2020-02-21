from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

block = 47
pos = mc.player.getPos()
x = pos.x - 1
while True:
    
    mc.setBlock(x, pos.y, pos.z, block)
    x += 1
    
    time.sleep(1)
    mc.setBlock(x - 1, pos.y, pos.z, 0)
