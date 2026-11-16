import bpy
import os
import shutil

bpy.ops.wm.read_factory_settings(use_empty=True)

stl_path = r"d:\GitHub\BLENDER\Rama_6inch_PrintReady.stl"
bpy.ops.import_mesh.stl(filepath=stl_path)

obj = bpy.context.selected_objects[0]

# Decimate to 70% (~1.54M triangles)
mod = obj.modifiers.new("Decimate", 'DECIMATE')
mod.ratio = 0.70
bpy.ops.object.modifier_apply(modifier="Decimate")

out_stl = r"d:\GitHub\BLENDER\Rama_6inch_PrintReady_DirectSTL.stl"
bpy.ops.export_mesh.stl(
    filepath=out_stl,
    check_existing=False,
    use_selection=True,
    global_scale=1.0,
    use_scene_unit=False,
    ascii=False,
    axis_forward='Y',
    axis_up='Z'
)

desktop_stl = r"C:\Users\divya\Desktop\Rama_6inch_PrintReady_DirectSTL.stl"
shutil.copyfile(out_stl, desktop_stl)

size_mb = os.path.getsize(out_stl) / (1024 * 1024)
print(f"Direct STL size: {size_mb:.2f} MB")
