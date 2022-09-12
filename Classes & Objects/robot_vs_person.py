# CREATE A ROBOT
# Define the class Robot
# Give the robot three attributes, height, weight, IQ
# Give the robot one method - the ability to compare IQ with a user.

# CREATE A PERSON
# Define the class Robot
# Give the person three attributes, height, weight, IQ
# Give the person one method - the ability flex on the robot.

# Compare the IQ of robot and person using the robot's function.
# At the end of this same function, make the robot taunt the person for having a lower IQ

# Respond using person's function to flex_on_haters and talk shit back


class Robot:
    def __init__(self, height, weight, IQ) -> None:
        self.height = height
        self.weight = weight
        self.iq = IQ

    def compare_iq(self, other_iq):
        if self.iq > other_iq:
            print(f"ROBOT SAYS: My IQ is {self.iq}. Yours is a measly {other_iq}. H A H A H A !")
        
class Person:
    def __init__(self, height, weight, IQ) -> None:
        self.height = height
        self.weight = weight
        self.iq = IQ

    def flex_on_haters(self, robot_iq):
        print(f"PERSON RESPONDS: I don't give a shit about your IQ of {robot1.iq}, robot scum. *flexes on the haters*")

robot1 = Robot(50,100,500)
person1 = Person(180,200,150)

robot1.compare_iq(person1.iq)
person1.flex_on_haters(robot1.iq)