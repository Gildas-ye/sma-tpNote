import random
import time

from pygame.math import Vector2

import core
from model.epidemie import Epidemie


class Agent:
    def __init__(self, id, status, body):
        self.uid = id
        self.body = body
        self.status = status
        self.vivante = True
        self.timeStart = 0

    def show(self):
        for a in core.memory("agents"):
            if a.status == "S":
                core.Draw.circle((255, 255, 255), a.body.position, a.body.taille)
            if a.status == "I":
                core.Draw.circle((255, 0, 0), a.body.position, a.body.taille)
            if a.status == "R":
                core.Draw.circle((255, 0, 0), a.body.position, a.body.taille)

    def deplacementAleatoire(self):
        if self.vivante:
            self.body.acceleration = Vector2(random.uniform(-1,1),random.uniform(-1,1))

            if self.body.acceleration.length() > self.body.maxAcc:
                self.body.acceleration.scale_to_length(self.body.maxAcc)

            self.body.vitesse = self.body.vitesse + self.body.acceleration

            if self.body.vitesse.length()>self.body.maxSpeed:
                self.body.vitesse.scale_to_length(self.body.maxSpeed)

            self.body.position = self.body.position + self.body.vitesse

            self.body.acceleration = Vector2(0,0)

    def update(self, agents):
        if self.status == "S":
            epidemie = Epidemie()
            etatPossible = ["s","I"]
            for a in agents:
                if a.body.position.distance_to(self.body.position) < epidemie.distanceMiniContagion and a.status == "I" and a.vivante and a.body.position.distance_to(self.body.position)>0:
                    #random.choice(arange(0, 1), p=[0.1, 0.05])
                    self.status = "I"
                    #self.timeStart = time.clock()
                    print(self.timeStart, "contagion")

        elif self.status == "I":
           pass
        elif self.status == "R":
            pass
        else:
            pass
