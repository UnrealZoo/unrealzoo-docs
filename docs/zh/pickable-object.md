# 可拾取物体

可拾取物体可被人类角色抓取和搬运。此交互功能必须与人类角色配合使用。

```
vbp {character name} set_pickup
```

## 类

```
Class Name: BP_GrabMoveDrop_C
```

命令格式：

```
vbp {instance_name} {bp_function} {args1} {args2} ...
```

## 蓝图函数

| BP_function | input | output | help |
|---|---|---|---|
| `is_picked` | — | `{"is_picked":"0"}` | 返回物体状态，是否被拾取（0/1） |
| `set_app` | `{id}` | — | 设置 agent 物体的外观，id：0~20 |

## 💡 提示

可通过调用 UnrealCV API 手动生成可拾取物体并设置其位置：

```python
self.unrealcv.set_new_obj(self, class_name, obj_name)
self.unrealcv.set_obj_location(self, obj, loc)
```

示例：

```python
self.unrealcv.set_new_obj(self, 'BP_GrabMoveDrop_C', 'pickable_object_1')
self.unrealcv.set_obj_location(self, 'pickable_object_1', [0, 0, 100])
```