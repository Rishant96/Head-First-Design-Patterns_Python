class Playing_Style:
	def __init__( damage ):
		self.damage_given = damage
		self.damage_taken = damage * self.multiplier

class Default_Style( Playing_Style ):
	def __init__( self, )

class Aggresive_Style( Playing_Style ):
	pass

class Passive_Style( Playing_Style ):
	pass

class Player:
	def __init__( self, weapon, play_style ):
		self.weapon = weapon
		self.health = 100
	def swap_weapon( self, new_weapon ):
		pass
	def fire( self, target ):
		pass