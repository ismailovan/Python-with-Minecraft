from mcpi.minecraft import Minecraft 
mc = Minecraft.create()
pos = mc.player.getPos() 
x = pos.x 
y = pos.y 
z = pos.z
blockType = mc.getBlock(x, y - 1, z) 


blockType2 = mc.getBlock(x, y + 1, z)

onTree = blockType == 17 or blockType == 18

mc.postToChat("Under water " + str(onTree))
