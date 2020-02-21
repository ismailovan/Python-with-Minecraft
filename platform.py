from mcpi.minecraft import Minecraft 
mc = Minecraft.create() 
pos = mc.player.getPos()
x = pos.x 
y = pos.y 
z = pos.z 
width = 999
height = 0
length = 2

block = 152
air = 0

mc.setBlocks(x, y, z, x + width, y + height, z + length, block)

block = 27

mc.setBlocks(x, y + 1, z + 1, x + width, y + 1, z + 1, block)
