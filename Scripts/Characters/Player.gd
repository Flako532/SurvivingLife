extends KinematicBody2D

onready var debug = $Debug
onready var animPlayer = $AnimationPlayer
onready var animTree = $AnimationTree
onready var animState = animTree.get("parameters/playback")
onready var health = $health_mod
onready var hurtbox = $HurtBox
export var MAX_SPEED = 120
export var ROLL_SPEED = 150
export var ACCELERATION = 150
export var FRICTION = 350


enum STATES {MOVE, ROLL}

var state = STATES.MOVE
var velocity = Vector2()
var roll_vector = Vector2.DOWN


func _ready():
	$"/root/Global".register_player(self)
	health.connect("health_changed", self, "on_health_changed", [])
	hurtbox.connect("area_entered", self, "on_hurtbox_collision", [])

func _process(delta):
	debug.text = """
				State : {state}
				Velocity : {vel} 
				Health : {health}
				""".format({"state": state, "vel": velocity, "health": health.get_health()})
	

func _physics_process(delta):
	match state:
		STATES.MOVE:
			move_state(delta)
		STATES.ROLL:
			roll_state(delta)
		
func _on_roll_animation_finished():
	state = STATES.MOVE

func move_state(delta):
	var input_vector = InputSystem.input_direction
	
	# Movimiento
	if input_vector != Vector2.ZERO:
		roll_vector = input_vector
		animTree.set("parameters/Idle/blend_position", input_vector)
		animTree.set("parameters/Run/blend_position", input_vector)
		animTree.set("parameters/Roll/blend_position", input_vector)
		animState.travel("Run")
		velocity = velocity.move_toward(input_vector * MAX_SPEED, ACCELERATION * delta)
	else:
		animState.travel("Idle")
		velocity = velocity.move_toward(Vector2.ZERO, FRICTION * delta)
		
	move()
	
	if InputSystem.input_roll:
		state = STATES.ROLL
	
	if InputSystem.input_action:
		receive_damage(10)
	

func roll_state(delta):
	velocity = roll_vector * ROLL_SPEED
	animState.travel("Roll")
	move()
	
func move():
	velocity = move_and_slide(velocity)
	
func receive_damage(amount:float) -> void:
	health.remove_health(amount)
	
func get_position():
	return self.global_position

func on_health_changed(new_health):
	print("Player's new health is {amount}".format({"amount":new_health}))
	
func on_hurtbox_collision(area):
	print("Player receive {dmg} damage".format({"dmg":area.dmg_amount}))
	receive_damage(area.dmg_amount)
