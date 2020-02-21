from mcpi.minecraft import Minecraft 
mc = Minecraft.create()



home_x = 399
home_y = 100
home_z = 366

current_pos = mc.player.getPos() 
x = current_pos.x 
y = current_pos.y 
z = current_pos.z

far_x = home_x > x + 40
far_y = home_y > y + 40
far_z = home_z > z + 40

mc.postToChat("Far from home by x " + str(far_x))
mc.postToChat("Far from home by y " + str(far_y))
mc.postToChat("Far from home by z " + str(far_z))

