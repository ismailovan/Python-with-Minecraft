from mcpi.minecraft import Minecraft 
mc = Minecraft.create() 
pos = mc.player.getPos()
x = pos.x 
y = pos.y 
z = pos.z 
width = 10
height = 10
length = 10

block = 17
air = 0

mc.setBlocks(x, y, z, x + width, y + height, z + length, block)
mc.setBlocks(x + 1, y + 1, z + 1, x + width - 1, y + height - 1, z + length - 1, air)
