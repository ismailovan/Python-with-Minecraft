import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

count = 0
while count <= 15:
    pos = mc.player.getPos()
    mc.setBlock(pos.x, pos.y, pos.z, 8)
    count += 1
    time.sleep(0.5)
