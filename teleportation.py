from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 500
y = 100
z = 870

mc.player.setPos(x, y, z)

x = 45
y = 100
z = 234
mc.player.setPos(x, y, x)
