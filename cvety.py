import time
from mcpi.minecraft import Minecraft 
mc = Minecraft.create()

count = 0
while count <= 10:
    pos = mc.player.getPos()
    mc.setBlock(pos.x, pos.y, pos.z, 38, 8)
    count += 1
    time.sleep(1)
