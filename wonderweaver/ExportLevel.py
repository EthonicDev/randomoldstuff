import bpy

# Get the evaluated mesh object
evaluated_mesh = bpy.context.object.evaluated_get(bpy.context.evaluated_depsgraph_get()).to_mesh()

# Open the file for writing
with open("export.xml", "w") as file:
    # Write XML header and root tag
    file.write("<root>\n")
    file.write("  <value IsClosed=\"true\">\n")
    file.write("    <Points type=\"array\">\n")

    # Write vertex positions to the file
    for v in range(len(evaluated_mesh.vertices)):
        vertex_position = evaluated_mesh.vertices[v].co
        x = int(vertex_position.x)
        y = int(vertex_position.y)
        z = int(vertex_position.z)
        file.write(f"      <value>\n")
        file.write(f"        <Translate type=\"array\">\n")
        file.write(f"          <value>{x}f</value>\n")
        file.write(f"          <value>{y}f</value>\n")
        file.write(f"          <value>{z}f</value>\n")
        file.write(f"        </Translate>\n")
        file.write(f"      </value>\n")

    # Close XML tags
    file.write("    </Points>\n")
    file.write("  </value>\n")
    file.write("</root>\n")

print("Vertex positions exported to export.xml")
