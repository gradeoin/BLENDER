import bpy
import math
import shutil
import os

bpy.ops.wm.read_factory_settings(use_empty=True)

# Import STL
stl_path = r"d:\GitHub\BLENDER\Rama_6inch_PrintReady.stl"
bpy.ops.import_mesh.stl(filepath=stl_path)

obj = bpy.context.selected_objects[0]
obj.name = "Rama_Sculpt"
bpy.ops.object.shade_smooth()

# Material - Premium warm marble clay
mat = bpy.data.materials.new(name="Idol_Marble")
mat.use_nodes = True
nodes = mat.node_tree.nodes
bsdf = nodes.get("Principled BSDF")
if bsdf:
    bsdf.inputs["Base Color"].default_value = (0.94, 0.92, 0.89, 1.0)
    bsdf.inputs["Roughness"].default_value = 0.25
    if "Subsurface Weight" in bsdf.inputs:
        bsdf.inputs["Subsurface Weight"].default_value = 0.15
        bsdf.inputs["Subsurface Radius"].default_value = (1.0, 0.6, 0.4)
    elif "Subsurface" in bsdf.inputs:
        bsdf.inputs["Subsurface"].default_value = 0.15
obj.data.materials.append(mat)

# Scene & Render
scene = bpy.context.scene
scene.render.engine = 'BLENDER_EEVEE'
scene.render.resolution_x = 1280
scene.render.resolution_y = 720
scene.eevee.use_gtao = True
scene.eevee.gtao_distance = 20.0

# World Background - Elegant dark studio
world = bpy.data.worlds.new("Studio_World")
world.use_nodes = True
wn = world.node_tree.nodes
wn.clear()
bg = wn.new(type='ShaderNodeBackground')
bg.inputs['Color'].default_value = (0.05, 0.06, 0.08, 1.0)
bg.inputs['Strength'].default_value = 1.0
wout = wn.new(type='ShaderNodeOutputWorld')
world.node_tree.links.new(bg.outputs['Background'], wout.inputs['Surface'])
scene.world = world

# Lights
# 1. Key Sun (front-right warm)
sun1 = bpy.data.lights.new(name="Key_Sun", type='SUN')
sun1.energy = 4.8
sun1.color = (1.0, 0.97, 0.92)
sun1_obj = bpy.data.objects.new("Key_Sun", sun1)
sun1_obj.rotation_euler = (math.radians(50), math.radians(20), math.radians(-30))
scene.collection.objects.link(sun1_obj)

# 2. Fill Sun (left soft cool)
sun2 = bpy.data.lights.new(name="Fill_Sun", type='SUN')
sun2.energy = 2.4
sun2.color = (0.86, 0.92, 1.0)
sun2_obj = bpy.data.objects.new("Fill_Sun", sun2)
sun2_obj.rotation_euler = (math.radians(45), math.radians(-25), math.radians(55))
scene.collection.objects.link(sun2_obj)

# 3. Rim Sun (back highlight)
sun3 = bpy.data.lights.new(name="Rim_Sun", type='SUN')
sun3.energy = 3.8
sun3.color = (1.0, 0.95, 0.88)
sun3_obj = bpy.data.objects.new("Rim_Sun", sun3)
sun3_obj.rotation_euler = (math.radians(-45), math.radians(10), math.radians(150))
scene.collection.objects.link(sun3_obj)

# Floor plane shadow catcher
bpy.ops.mesh.primitive_circle_add(radius=200, fill_type='NGON', location=(0, 0, -0.2))
disc = bpy.context.active_object
disc_mat = bpy.data.materials.new(name="Disc_Mat")
disc_mat.use_nodes = True
d_bsdf = disc_mat.node_tree.nodes.get("Principled BSDF")
d_bsdf.inputs["Base Color"].default_value = (0.03, 0.04, 0.05, 1.0)
d_bsdf.inputs["Roughness"].default_value = 0.5
disc.data.materials.append(disc_mat)

# Camera - Framed to capture full 6-inch figure with headroom and base
cam = bpy.data.cameras.new("Main_Camera")
cam.lens = 52 # 52mm portrait
cam_obj = bpy.data.objects.new("Main_Camera", cam)
# Slightly 3/4 angle: X = -35, Y = -440, Z = 78
cam_obj.location = (-35, -440, 78)
scene.collection.objects.link(cam_obj)
scene.camera = cam_obj

focus = bpy.data.objects.new("Focus_Target", None)
focus.location = (0, 0, 76.2) # Exact midpoint of 152.4mm model
scene.collection.objects.link(focus)

tr = cam_obj.constraints.new(type='TRACK_TO')
tr.target = focus
tr.track_axis = 'TRACK_NEGATIVE_Z'
tr.up_axis = 'UP_Y'

out_path = r"d:\GitHub\BLENDER\SuperProfile_Cover_1280x720.png"
scene.render.filepath = out_path
bpy.ops.render.render(write_still=True)

# Also copy to Desktop for instant convenience
desktop_dir = os.path.join(os.environ.get("USERPROFILE", r"C:\Users\divya"), "Desktop")
desktop_path = os.path.join(desktop_dir, "SuperProfile_Cover_1280x720.png")
try:
    shutil.copyfile(out_path, desktop_path)
    print("Copied to Desktop:", desktop_path)
except Exception as e:
    print("Desktop copy skipped:", e)

print("Rendered successfully:", out_path)
