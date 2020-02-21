from mcpi.minecraft import Minecraft 
mc = Minecraft.create()


block = 0


while true:
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z


    blockType = mc.getBlock(272, 83, 572)

    if x == 272 and y == 80 and z == 572:
        if blockType == 8:
            mc.setBlock(272, 82, 572, 0)

    elif x != 272 or y != 80 or z != 572:
        if blockType == 8:
            mc.setBlock(272, 82, 572, 57)
