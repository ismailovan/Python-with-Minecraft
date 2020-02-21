import time
from mcpi.minecraft import Minecraft 
mc = Minecraft.create()

count = 0


while count <= 30:
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    mc.setBlock(pos.x, pos.y - 1, pos.z, 41)
    time.sleep(1)
    count += 1
