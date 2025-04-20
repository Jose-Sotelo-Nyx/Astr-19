class axolotl():

	def __init__(self,arm_length,leg_length,eyes,tail,furry):
		self.arm_length = arm_length
		self.leg_length = leg_length
		self.eyes = eyes
		self.tail = tail
		self.furry = furry

	def description(self):
		print("Axolotl Characteristics:")
		print(f"- Arm Length: {self.arm_length} in")
		print(f"- Arm Length: {self.leg_length} in")
		print(f"- Number of Eyes: {self.eyes}")
		print(f"- Has a Tail {'Yes'if self.tail else 'No'}")
		print(f"- Is Furry {'Yes'if self.tail else 'No'}")

felipe = axolotl(1.5,2.0,2,True,False)
felipe.description()