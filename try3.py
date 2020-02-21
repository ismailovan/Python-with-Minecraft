from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 10 
y = 11 
z = 12 
gift = mc.getBlock(x, y, z)
if gift == 57:
    mc.postToChat("Almaz")
elif gift == 41:
    mc.postToChat("Zoloto")

elif gift == 42:
    mc.postToChat("Zhelezo")

elif gift == 22:
    mc.postToChat("Lazurit")


else: 
	mc.postToChat("Ty nichego ne podarish?")
