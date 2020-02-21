from mcpi.minecraft import Minecraft 
mc = Minecraft.create()
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
block = 49

mc.setBlock(x, y, z, block)
mc.setBlock(x + 1, y, z, block)
mc.setBlock(x + 2, y, z, block)
mc.setBlock(x + 3, y, z, block)

mc.setBlock(x + 3, y + 1, z, block)
mc.setBlock(x + 3, y + 2, z, block)
mc.setBlock(x + 3, y + 3, z, block)
mc.setBlock(x + 3, y + 4, z, block)


mc.setBlock(x, y + 1, z, block)
mc.setBlock(x, y + 2, z, block)
mc.setBlock(x, y + 3, z, block)
mc.setBlock(x, y + 4, z, block)


mc.setBlock(x + 1, y + 4, z, block)
mc.setBlock(x + 2, y + 4, z, block)
mc.setBlock(x + 3, y + 4, z, block)


