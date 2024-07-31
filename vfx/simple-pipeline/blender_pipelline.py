import bpy

# Using factory startup settings (start with an empty scene)
bpy.ops.wm.read_factory_settings(use_empty=True)

# Add a cube
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0))

# Add a camera
bpy.ops.object.camera_add(location=(10, -10, 10))
camera = bpy.context.object
camera.rotation_euler = (1.1, 0, 0.7854)  # Rotate camera for better view
bpy.context.scene.camera = camera

# Add a light
bpy.ops.object.light_add(type='SUN', location=(10, -10, 10))
light = bpy.context.object
light.data.energy = 10  # Set the light intensity

# Add a plane (background) and store the plane object
bpy.ops.mesh.primitive_plane_add(size=10, location=(0, 0, -1))
plane = bpy.context.object

# Create a new material
material = bpy.data.materials.new(name="PlaneMaterial")
material.use_nodes = True

# Get the principled shader node
bsdf = material.node_tree.nodes["Principled BSDF"]

# Set the base color
bsdf.inputs['Base Color'].default_value = (0.1, 0.8, 0.1, 1)  # RGBA, green color

# Assign the material to the plane
if plane.data.materials:
    plane.data.materials[0] = material
else:
    plane.data.materials.append(material)

# Set rendering output properties
bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080
bpy.context.scene.render.filepath = '/before/render.png'

# Set color management to Standard
bpy.context.scene.display_settings.display_device = 'sRGB'
bpy.context.scene.view_settings.view_transform = 'Standard'

# Render the before scene
bpy.ops.render.render(write_still=True)

# Change the camera rotation
camera.rotation_euler = (1.1, 0, 0.7854)  # Rotate camera for better view
bpy.context.scene.camera = camera

# Set the light intensity
light.data.energy = 10  

# Change the plane color

# Set rendering output properties
bpy.context.scene.render.filepath = '/after/render.png'
# Render the after scene
bpy.ops.render.render(write_still=True)
