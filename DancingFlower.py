import mujoco
import mujoco_viewer
import numpy as np

model = mujoco.MjModel.from_xml_path('Homework1.xml')
data = mujoco.MjData(model)

viewer = mujoco_viewer.MujocoViewer(model, data)

motors = model.nu
step = np.array([.2, -.2, .2, -0.2])
data.ctrl[:motors] = step

# Moving :D 
for i in range(10000): 
    if viewer.is_alive:
        if i%50 == 0:
            step = step*-1
        data.ctrl[:motors] = step 
        mujoco.mj_step(model, data)
        viewer.render()
    else:
        break

viewer.close 