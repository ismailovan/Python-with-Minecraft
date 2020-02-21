from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

pos = mc.player.getPos(); 
while True:
    mc.setBlocks(pos.x, pos.y-1, pos.z, pos.x + 9, pos.y-1, pos.z + 9, 41)
    time.sleep(1)
    mc.setBlocks(pos.x, pos.y - 1, pos.z, pos.x + 9, pos.y -1, pos.z + 9, 57)
    time.sleep(1)
