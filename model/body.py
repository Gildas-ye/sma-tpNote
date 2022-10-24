import random
from random import randint

from pygame import Vector2


class Body:
    def __init__(self, fustrum):
        self.vivante = True
        self.position = Vector2(randint(0, 800), randint(0, 800))
        self.vel = Vector2(random.uniform(-5, 5), random.uniform(-5, 5))
        self.acceleration = Vector2()
        self.maxAcc = 1
        self.maxSpeed = 4
        self.vitesse = Vector2(0, 0)
        self.taille = 5

    def bordure(self, fenetre):
        if self.position.y < 0:
            self.position.y = fenetre[1]

        if self.position.y > fenetre[1]:
            self.position.y = 0

        if self.position.x < 0:
            self.position.x = fenetre[0]

        if self.position.x > fenetre[0]:
            self.position.x = 0


