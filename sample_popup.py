import bpy

class UI(bpy.types.Panel):
  bl_label = "my panel"
  bl_space_type = "VIEW_3D"
  bl_region_type = "UI"
  
  def draw(self, context):
    self.layout.operator("my.button")
    

class MyButton(bpy.types.Operator):
  bl_idname = "my.button"
  bl_label = "text"

  my_float = bpy.props.FloatProperty(name="Some Floating Point")
  my_bool = bpy.props.BoolProperty(name="Toggle Option")
  my_string = bpy.props.StringProperty(name="String Value")
  
  def execute(self, context):
    message = "%f, %d, '%s'" % (self.my_float, self.my_bool, self.my_string)
    print(message)
    return{'FINISHED'}

  def invoke(self, context, event):
    return context.window_manager.invoke_props_dialog(self, width=800, height=400)

  #add
  def draw(self, context):
    layout = self.layout

    col = layout.column()

    col.label("Painting Mode")
    col.prop(self, 'my_float')
    col.separator()
    col.prop(self, 'my_bool')
   
bpy.utils.register_class(MyButton)
      
bpy.utils.register_module(__name__)
