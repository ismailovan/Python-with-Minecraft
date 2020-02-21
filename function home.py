from mcpi.minecraft import Minecraft
mc = Minecraft.create()




height = input("Enter a height: ")


pos = mc.player.getTilePos()
mc.setBlocks(pos.x, pos.y, pos.z, pos.x +  15, pos.y + (int) (height), pos.z + 15, 5)
