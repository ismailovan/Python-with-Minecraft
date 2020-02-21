from mcpi.minecraft import Minecraft 
mc = Minecraft.create() 

block = 17


x = 82
y = 70
z = 208

mc.player.setPos(82, 90, 208)

mc.setBlock(x, y, z, block)
mc.setBlock(x, y + 1, z, block)
mc.setBlock(x, y + 2, z, block)
mc.setBlock(x, y + 3, z, block)

block = 18
mc.setBlock(x, y + 4, z, block)
mc.setBlock(x + 1, y + 3, z, block)
mc.setBlock(x - 1, y + 3, z, block)
mc.setBlock(x, y + 3, z + 1, block)
mc.setBlock(x, y + 3, z - 1, block)
