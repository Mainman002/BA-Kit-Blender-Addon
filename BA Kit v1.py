bl_info = {
    "name": "BA kit v1",
    "author": "Mainman002",
    "version": (1, 4),
    "blender": (2, 71, 0),
    "location": "View3D > Tool_Tab> BA Kit Links",
    "description": "BA Kit Download Links",
    "warning": "",
    "wiki_url": "",
    "category": "Object"}

import bpy
from bpy.app.handlers import persistent

class BAKitsTab(bpy.types.Panel):
    bl_label = "BA Kits v1 Download Links"
    bl_idname = "BA_Kits_Downloads"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "BAKits"
    bl_context = "objectmode"
    
    def draw(self,context):
        self.layout.operator("wm.url_open", text="BA Kits v1 Home", icon='HELP').url = "https://github.com/Mainman002?tab=repositories"
        self.layout.operator("wm.url_open", text="BA Kits v1 Download", icon='HELP').url = "https://github.com/Mainman002/BA-Kits-1"
        self.layout.operator("wm.url_open", text="Export Windows 32bit", icon='HELP').url = "https://github.com/Mainman002/BA-Kit-Exports-Windows-32bit-v1"
        self.layout.operator("wm.url_open", text="Export Windows 64bit", icon='HELP').url = "https://github.com/Mainman002/BA-Kit-Exports-Windows-64bit-v1"
        self.layout.operator("wm.url_open", text="Export Linux 32bit", icon='HELP').url = "https://github.com/Mainman002/BA-Kit-Exports-Linux-32bit-v1"
        self.layout.operator("wm.url_open", text="Export Linux 64bit", icon='HELP').url = "https://github.com/Mainman002/BA-Kit-Exports-Linux-64bit-v1"
        self.layout.operator("wm.url_open", text="Export Mac 64bit", icon='HELP').url = "https://github.com/Mainman002/BA-Kit-Exports-Mac-64bit-v1"
        
class BAKitsVideoTab(bpy.types.Panel):
    bl_label = "BA Kits v1 Video Links"
    bl_idname = "BA_Kits_Tutorial Videos"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "BAKits"
    bl_context = "objectmode"
    
    def draw(self,context):
        self.layout.operator("wm.url_open", text="BA Kit Playlist", icon='HELP').url = "https://www.youtube.com/playlist?list=PL359DaN9yjMqe0pWpL9P6CjYHkDMLgw1c"
        self.layout.operator("wm.url_open", text="BA Kit Q/A Video 1", icon='HELP').url = "https://youtu.be/uu8Jm0oBjNs?list=PL359DaN9yjMqe0pWpL9P6CjYHkDMLgw1c"
        
def register():
    bpy.utils.register_class(BAKitsTab)
    bpy.utils.register_class(BAKitsVideoTab)

def unregister():
    bpy.utils.unregister_class(BAKitsTab)
    bpy.utils.unregister_class(BAKitsVideoTab)

if __name__ == "__main__":  # only for live edit.
    bpy.utils.register_module(__name__)