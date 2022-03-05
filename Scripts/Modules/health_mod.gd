extends Node2D

signal health_changed(health)
signal death

export var MAX_HEALTH = 100

var current_health

func _ready():
	current_health = MAX_HEALTH
	
func _process(delta):
	if current_health <= 0:
		emit_signal("death")
		
func set_health(amount):
	current_health = clamp(amount, 0, MAX_HEALTH)
	emit_signal("health_changed", current_health)
	
func get_health():
	return current_health
	
func remove_health(amount):
	current_health = clamp(current_health - amount, 0, MAX_HEALTH)
	emit_signal("health_changed", current_health)
	
func add_health(amount):
	current_health = clamp(current_health + amount, 0, MAX_HEALTH)	
	emit_signal("health_changed", current_health)
	
