# 可拾取物体

此交互必须与人类角色结合使用

vbp {character name} set_pickup 


类名： BP_GrabMoveDrop_C 

vbp {instance_name} {bp_function} {args1} {args2} ... 

## 💡提示

你可以通过调用 unrealcv api 手动生成可拾取物体并设置其位置：

self.unrealcv.set_new_obj(self, class_name, obj_name) 

self.unrealcv.set_obj_location(self, obj, loc)

示例：

self.unrealcv.set_new_obj(self, BP_GrabMoveDrop_C, pickable_object_1)  

self.unrealcv.set_obj_location(self, pickable_object_1, [0,0,100])