from mcpi.minecraft import Minecraft 
mc = Minecraft.create() 

block = 35
ident = 3

x = 79
y = 150
z = 207
mc.player.setPos(79, 100, 207)

mc.setBlock(x, y, z, block, ident)
mc.setBlock(x, y - 1, z, block, ident)
mc.setBlock(x, y - 1, z + 1, block, ident)
mc.setBlock(x + 1, y - 1, z, block, ident)
mc.setBlock(x, y - 2, z, block, ident)
mc.setBlock(x + 1, y - 2, z, block, ident)
mc.setBlock(x + 2, y - 2, z, block, ident)
mc.setBlock(x, y - 2, z + 1, block, ident)
mc.setBlock(x, y - 2, z + 2, block, ident)
mc.setBlock(x + 1, y - 2, z + 1, block, ident)
mc.setBlock(x, y - 3, z, block, ident)
mc.setBlock(x + 1, y - 3, z, block, ident)
mc.setBlock(x, y - 3, z + 1, block, ident)
mc.setBlock(x, y - 4, z, block, ident)

