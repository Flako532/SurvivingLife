extends KinematicBody2D

onready var sprite = $Sprite
export var speed = 200

var velocity = Vector2()

func _ready():
	sprite.set_animation("Idle")

func character_idle():
	sprite.set_animation("Idle")

func move_to(target_dir, delta):
	update_facing(target_dir)
	sprite.set_animation("Run")
	velocity = move_and_slide(target_dir * speed)	

#func _ready():	
#	# Set up z index here and simply match it to the y value
#	# This allows moving characters like the player to be drawn over
#	# a sprite when "in front," but if they move behind that character
#	# it will correctly update (sort y order for non-cells)
#	z_as_relative = false
#	set_z_index(position.y)
#
#
## Actor targets a position to move to
#func target_position(move_vector):
#	var target = overworld.request_move(self, move_vector)
#	# Whether we can move or not, update our facing first
#	update_facing(move_vector)
#	if target:
#		move_to(target)
#	else:
#		bump()


# Change how the character is facing.
func update_facing(direction):
	if direction.x == 1:  # Derecha
		sprite.flip_h = false
	elif direction.x == -1:  # Izquierda
		sprite.flip_h = true
#	elif direction.y == 1:  # Abajo
#		sprite.flip_h = true
#	elif direction.y == -1:  # Arriba
#		sprite.flip_h = false


# Define what an actor should do if it is interacted with in the child class.
#func interact():
#	print("I am an Actor with no interact defined.")
#
#
## Failure to move function.
#func bump():
#	set_process(false)
#	$AnimationPlayer.play("bump")
#	yield($AnimationPlayer, "animation_finished")
#	set_process(true)
#
#
## Movement animation processing
#func process_movement_animation():
#	match dir:
#		DIR.UP:
#			$AnimationPlayer.play("walk_up")
#		DIR.DOWN:
#			$AnimationPlayer.play("walk_down")
#		DIR.LEFT:
#			$AnimationPlayer.play("walk_horiz")
#		DIR.RIGHT:
#			$AnimationPlayer.play("walk_horiz")
