from mcpi.minecraft import Minecraft 
mc = Minecraft.create() 

block = 35
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

ident = 10
mc.setBlock(x + 1, y, z, block, ident)
mc.setBlock(x + 1, y + 1, z, block, ident)
mc.setBlock(x - 1, y, z, block, ident)
mc.setBlock(x - 1, y + 1, z, block, ident)
mc.setBlock(x, y + 2, z, block, ident)

ident = 11
mc.setBlock(x + 2, y, z, block, ident)
mc.setBlock(x + 2, y + 1, z, block, ident)
mc.setBlock(x + 1, y + 2, z, block, ident)
mc.setBlock(x, y + 3, z, block, ident)
mc.setBlock(x - 1, y + 2, z, block, ident)
mc.setBlock(x - 2, y + 1, z, block, ident)
mc.setBlock(x - 2, y, z, block, ident)

ident = 3
mc.setBlock(x + 3, y, z, block, ident)
mc.setBlock(x + 3, y + 1, z, block, ident)
mc.setBlock(x + 2, y + 2, z, block, ident)
mc.setBlock(x + 1, y + 3, z, block, ident)
mc.setBlock(x, y + 4, z, block, ident)
mc.setBlock(x - 1, y + 3, z, block, ident)
mc.setBlock(x - 2, y + 2, z, block, ident)
mc.setBlock(x - 3, y + 1, z, block, ident)
mc.setBlock(x - 3, y, z, block, ident)

ident = 5
mc.setBlock(x + 4, y, z, block, ident)
mc.setBlock(x + 4, y + 1, z, block, ident)
mc.setBlock(x + 3, y + 2, z, block, ident)
mc.setBlock(x + 2, y + 3, z, block, ident)
mc.setBlock(x + 1, y + 4, z, block, ident)
mc.setBlock(x, y + 5, z, block, ident)
mc.setBlock(x - 1, y + 4, z, block, ident)
mc.setBlock(x - 2, y + 3, z, block, ident)
mc.setBlock(x - 3, y + 2, z, block, ident)
mc.setBlock(x - 4, y + 1, z, block, ident)
mc.setBlock(x - 4, y, z, block, ident)

ident = 4
mc.setBlock(x + 5, y, z, block, ident)
mc.setBlock(x + 5, y + 1, z, block, ident)
mc.setBlock(x + 4, y + 2, z, block, ident)
mc.setBlock(x + 3, y + 3, z, block, ident)
mc.setBlock(x + 2, y + 4, z, block, ident)
mc.setBlock(x + 1, y + 5, z, block, ident)
mc.setBlock(x, y + 6, z, block, ident)
mc.setBlock(x - 1, y + 5, z, block, ident)
mc.setBlock(x - 2, y + 4, z, block, ident)
mc.setBlock(x - 3, y + 3, z, block, ident)
mc.setBlock(x - 4, y + 2, z, block, ident)
mc.setBlock(x - 5, y + 1, z, block, ident)
mc.setBlock(x - 5, y, z, block, ident)

ident = 1
mc.setBlock(x + 6, y, z, block, ident)
mc.setBlock(x + 6, y + 1, z, block, ident)
mc.setBlock(x + 5, y + 2, z, block, ident)
mc.setBlock(x + 4, y + 3, z, block, ident)
mc.setBlock(x + 3, y + 4, z, block, ident)
mc.setBlock(x + 2, y + 5, z, block, ident)
mc.setBlock(x + 1, y + 6, z, block, ident)
mc.setBlock(x, y + 7, z, block, ident)
mc.setBlock(x - 1, y + 6, z, block, ident)
mc.setBlock(x - 2, y + 5, z, block, ident)
mc.setBlock(x - 3, y + 4, z, block, ident)
mc.setBlock(x - 4, y + 3, z, block, ident)
mc.setBlock(x - 5, y + 2, z, block, ident)
mc.setBlock(x - 6, y + 1, z, block, ident)
mc.setBlock(x - 6, y, z, block, ident)

ident = 14
mc.setBlock(x + 7, y, z, block, ident)
mc.setBlock(x + 7, y + 1, z, block, ident)
mc.setBlock(x + 6, y + 2, z, block, ident)
mc.setBlock(x + 5, y + 3, z, block, ident)
mc.setBlock(x + 4, y + 4, z, block, ident)
mc.setBlock(x + 3, y + 5, z, block, ident)
mc.setBlock(x + 2, y + 6, z, block, ident)
mc.setBlock(x + 1, y + 7, z, block, ident)
mc.setBlock(x, y + 8, z, block, ident)
mc.setBlock(x - 1, y + 7, z, block, ident)
mc.setBlock(x - 2, y + 6, z, block, ident)
mc.setBlock(x - 3, y + 5, z, block, ident)
mc.setBlock(x - 4, y + 4, z, block, ident)
mc.setBlock(x - 5, y + 3, z, block, ident)
mc.setBlock(x - 6, y + 2, z, block, ident)
mc.setBlock(x - 7, y + 1, z, block, ident)
mc.setBlock(x - 7, y, z, block, ident)













