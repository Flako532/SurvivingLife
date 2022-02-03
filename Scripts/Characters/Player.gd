extends "res://Scripts/Characters/BaseActor.gd"


func _physics_process(delta):
#	if InputSystem.input_activation:
#		activate_object()
	if InputSystem.input_direction:
		move_to(InputSystem.input_direction, delta)



# Make a vector of the direction we're facing, then ask the grid to interact
# with whatever is there
#func activate_object():
#	var direction_of_interaction = Vector2((int(dir == DIR.RIGHT) - int(
#			dir == DIR.LEFT)), (int(dir == DIR.DOWN) - int(dir == DIR.UP)))
#	overworld.request_interaction(self, direction_of_interaction)
