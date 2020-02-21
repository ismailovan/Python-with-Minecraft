from mcpi.minecraft import Minecraft 
mc = Minecraft.create() 
pos = mc.player.getPos()
x = pos.x 
y = pos.y 
z = pos.z 
width = 13
height = 13
length = 13

block = 35
air = 0

mc.setBlocks(x, y, z, x + width, y + height, z + length, block)


width = 9
height = 9
length = 9
mc.setBlocks(x + 2, y + 14, z + 2, x + width + 2, y + height + 14, z + length + 2, block)

width = 5
height = 5
length = 5
mc.setBlocks(x + 4, y + 24, z + 4, x + width + 4, y + height + 24, z + length + 4, block)
