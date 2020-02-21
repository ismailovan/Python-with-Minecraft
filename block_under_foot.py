from mcpi.minecraft import Minecraft 
mc = Minecraft.create() 
pos = mc.player.getPos()
x = pos.x 
y = pos.y 
z = pos.z 

mc.player.setTilePos(x + 100, y, z)
block = 17
mc.setBlock(x + 100, y - 1, z, block)
