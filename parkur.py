from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
kvarc = 155
mc.setBlocks(x, y, z, x + 30, y + 12, z + 10, kvarc)
mc.setBlocks(x + 1, y + 1, z + 1, x + 29, y + 11, z + 9, 0)
mc.setBlocks(x, y + 1, z, x, y + 12, z + 10, 0)
red = 152
mc.setBlocks(x, y, z, x + 30, y, z + 10, red)
mc.setBlocks(x + 3, y + 1, z + 5, x + 3, y + 4, z + 9, kvarc)
mc.setBlocks(x + 6, y + 1, z + 5, x + 6, y + 4, z + 5, kvarc)
mc.setBlocks(x + 10, y + 1, z + 1, x + 11, y + 4, z + 9, kvarc)
mc.setBlocks(x + 12, y + 1, z + 4, x + 12, y + 4, z + 4, kvarc)
mc.setBlocks(x + 14, y + 1, z + 7, x + 14, y + 4, z + 7, kvarc)
mc.setBlocks(x + 15, y + 1, z + 1, x + 16, y + 4, z + 9, kvarc)
mc.setBlocks(x + 15, y + 1, z + 2, x + 14, y + 4, z + 2, kvarc)
mc.setBlocks(x + 22, y + 1, z + 1, x + 23, y + 4, z + 9, kvarc)
mc.setBlocks(x + 25, y + 1, z + 4, x + 25, y + 4, z + 4, kvarc)
mc.setBlocks(x + 29, y + 1, z + 1, x + 30, y + 4, z + 9, kvarc)
