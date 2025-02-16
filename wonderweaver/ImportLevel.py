import bpy
import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse("export.xml")
root = tree.getroot()

# Create a list to store points
points = []

# Iterate through XML and extract points
for value in root.find("value/Points").findall("value"):
    x = float(value.find("Translate/value[1]").text[:-1])  # Remove the 'f' from the value and convert to float
    y = float(value.find("Translate/value[2]").text[:-1])
    z = float(value.find("Translate/value[3]").text[:-1])
    points.append((x, y, z))

# Create points and edges in Blender
mesh = bpy.data.meshes.new(name="ImportedMesh")
obj = bpy.data.objects.new("ImportedObject", mesh)
bpy.context.collection.objects.link(obj)
bpy.context.view_layer.objects.active = obj
obj.select_set(True)
bpy.context.view_layer.objects.active = obj
obj.select_set(True)

mesh = bpy.context.object.data

# Create vertices
mesh.vertices.add(len(points))
for i, coord in enumerate(points):
    mesh.vertices[i].co = coord

# Create edges
mesh.edges.add(len(points))
for i in range(len(points) - 1):
    mesh.edges[i].vertices = (i, i + 1)
mesh.edges[len(points) - 1].vertices = (len(points) - 1, 0)

# Update the mesh and scene
mesh.update()
bpy.context.view_layer.update()

print("XML data imported into Blender.")