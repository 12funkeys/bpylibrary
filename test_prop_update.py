import bpy
from bpy.props import *

bl_info = {
    "name" : "Test Addon",
    "author" : "12funkeys",
    "version" : (0,1),
    "blender" : (2, 6, 5),
    "location" : "TEST",
    "description" : "simple addon template",
    "warning" : "",
    "wiki_url" : "",
    "tracker_url" : "",
    "category" : "TEST"
}

# operatator
class CHoge(bpy.types.Operator):
    bl_idname = "test.hoge"
    bl_label = "Hoge Menu"
    bl_description = "Hoge Piyo"
    bl_options = {'REGISTER', 'UNDO'}

    def update_func(self, context):
        print("heyheyhey", self)

    testprops = FloatProperty(
        name = "prop",
        description = "testprop",
        default = 1.0,
        subtype = 'NONE',
        min = 0.001,
        update= update_func )

    @classmethod
    def poll(cls, context):
        return context.mode == 'OBJECT'

    def draw(self, context):
        layout = self.layout
        #layout.label("OK!")
        layout.prop(self, 'testprops')

    def execute(self, context):
        self.report({'INFO'}, "execute") 
        return {'FINISHED'}


### add Tool Panel
class MenuRigidBodyTools(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "TEST"
    bl_context = "objectmode"
    bl_label = "TEST"


    @classmethod
    def poll(cls, context):
        return (context.object is not None)

    def draw(self, context):
        layout = self.layout
        layout.operator(CHoge.bl_idname)


def menu_func(self, context):
    self.layout.operator("test.hoge") 

def register():
    bpy.utils.register_module(__name__)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

if __name__ == "__main__":
    register()
