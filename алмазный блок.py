from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

while True:
    pos = mc.player.getPos()
    block = mc.getBlock(pos.x, pos.y - 1, pos.z)
    if block != 0:
        mc.setBlock(pos.x, pos.y-1, pos.z, 57)
