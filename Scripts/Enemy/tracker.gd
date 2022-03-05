extends KinematicBody2D

onready var debug = $Debug
onready var tween = $Tween
onready var timer_out = $TimerOut
onready var timer_in = $TimerIn
onready var health_mod = $health_mod
onready var hurtbox = $HurtBox
onready var tackle_area = $Area2D_tackle
export var MAX_HEALTH = 100
export var DAMAGE = 8
export var MAX_SPEED = 150
export var ACCELERATION = 100
export var STAND_BY_TIME = 1.8
export var CD_TIMER  = 3.0

enum STATES {MOVE, ATTACK}

var state = STATES.MOVE
var current_health = MAX_HEALTH
var velocity = Vector2()
var player_pos = Vector2.ZERO
var obj_vector = Vector2.ZERO
var stand_by = false

func _ready():
	hurtbox.connect("area_entered", self, "_on_hurtbox_entered", [])
	tackle_area.connect("body_entered", self, "_on_Area2D_tackle_body_entered", [])
	tackle_area.connect("body_exited", self, "_on_Area2D_tackle_body_exited", [])
	timer_out.connect("timeout", self, "_on_TimerOut_timeout", [])
	timer_in.connect("timeout", self, "_on_TimerIn_timeout", [])

func _process(delta):
	debug.text = """
				State : {state}
				Velocity : {vel} 
				Health : {health}
				""".format({"state": state,"vel": velocity,"health": current_health})
	
	player_pos = $"/root/Global".player.get_position()
	obj_vector = player_pos - self.get_position()
	
func _physics_process(delta):
	match state:
		STATES.MOVE:
			move_state(delta)
		STATES.ATTACK:
			if not stand_by:
				stand_by = true
				timer_in.start(STAND_BY_TIME)
			

func move_state(delta):
	velocity = velocity.move_toward(obj_vector.normalized() * MAX_SPEED, ACCELERATION * delta)
	move()

func attack_state():
	tween.interpolate_property(
		self, 
		"position", 
		self.get_position(),
		player_pos, 
		1, 
		tween.TRANS_BACK, 
		tween.EASE_OUT
	)
	tween.start()
	timer_out.start(CD_TIMER)


func move():
	velocity = move_and_slide(velocity)
	
func receive_damage(amount):
	health_mod.remove_health(amount) 
	
func _on_hurtbox_entered(hitbox):
	print("Tracker receive {dmg} damage".format({"dmg":hitbox.dmg_amount}))
	receive_damage(hitbox.dmg_amount)

func _on_Area2D_tackle_body_entered(body):
	if body == $"/root/Global".player:
		state = STATES.ATTACK

func _on_Area2D_tackle_body_exited(body):
	if body == $"/root/Global".player:
		velocity = Vector2.ZERO
		stand_by = false
		tween.stop(self, "position")
		if not timer_in.is_stopped():
			timer_in.stop()
		state = STATES.MOVE
	
func _on_TimerOut_timeout():
	stand_by = false

func _on_TimerIn_timeout():
	attack_state()
