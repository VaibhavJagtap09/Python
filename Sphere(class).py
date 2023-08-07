class Sphere():
    def __init__(self,r):
        self.radius = r

    def diameter(self):
        return self.radius*2

    def circumference(self):
        return 2*self.radius*3.14

    def volume(self):
        return self.radius**3*3.14*4/3

NewSphere = Sphere(20)
print(NewSphere.diameter())
print(NewSphere.circumference())
print(NewSphere.volume())
