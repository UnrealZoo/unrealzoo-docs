# Pickable Object

Pickable objects can be grabbed and carried by a human character. This interactive function must be used together with a human character.

```
vbp {character name} set_pickup
```

## Class

```
Class Name: BP_GrabMoveDrop_C
```

Command form:

```
vbp {instance_name} {bp_function} {args1} {args2} ...
```

## Blueprint Functions

| BP_function | input | output | help |
|---|---|---|---|
| `is_picked` | — | `{"is_picked":"0"}` | Return the object state, picked or not (0/1) |
| `set_app` | `{id}` | — | Set the appearance of the agent object, id: 0~20 |

## 💡 Hint

You can manually spawn pickable objects and set their location by calling the UnrealCV API:

```python
self.unrealcv.set_new_obj(self, class_name, obj_name)
self.unrealcv.set_obj_location(self, obj, loc)
```

Example:

```python
self.unrealcv.set_new_obj(self, 'BP_GrabMoveDrop_C', 'pickable_object_1')
self.unrealcv.set_obj_location(self, 'pickable_object_1', [0, 0, 100])
```
