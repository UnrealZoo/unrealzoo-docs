# Pickable Object

This interactive must be incorporated with a human character

vbp {character name} set_pickup 


Class Name： BP_GrabMoveDrop_C 

vbp {instance_name} {bp_function} {args1} {args2} ... 

## 💡Hint

You could manually spawn pickable objects and set their location by calling the unrealcv api:

self.unrealcv.set_new_obj(self, class_name, obj_name) 

self.unrealcv.set_obj_location(self, obj, loc)

Example:

self.unrealcv.set_new_obj(self, BP_GrabMoveDrop_C, pickable_object_1)  

self.unrealcv.set_obj_location(self, pickable_object_1, [0,0,100])


