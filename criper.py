from mcpi.minecraft import Minecraft 
mc = Minecraft.create() 
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

width = 7
height = 4
length = 2

block = 168
ident = 1

mc.setBlocks(x, y, z, x + 7, y + 4, z + 3, block, ident)
mc.setBlocks(x, y + 5, z + 4, x + 7, y + 17, z + 4 + 3, block, ident)
mc.setBlocks(x, y, z + 8, x + 7, y + 4, z + 3 + 8, block, ident)
mc.setBlocks(x, y + 18, z + 2, x + 7, y + 25, z + 9, block, ident)
