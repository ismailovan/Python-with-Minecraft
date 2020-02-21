import time
from mcpi.minecraft import Minecraft 
mc = Minecraft.create()

count = 0


while count <= 20:
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    mc.setBlocks(pos.x, pos.y - 1, pos.z, pos.x + 2, pos.y - 1, pos.z + 2, 41)
    time.sleep(1)
