import core
from model.agent import Agent
from model.body import Body
from model.fustrum import Fustrum


def computePerception():
    pass


def compteDecision():
    pass


def applyDecision():
    for a in core.memory("agents"):
        a.deplacementAleatoire()
        a.update(core.memory("agents"))
        a.body.bordure(core.WINDOW_SIZE)




def generate():
    core.memory("agents", [])
    core.memory("nbAgents", 80)
    for i in range(0, core.memory("nbAgents")-3):
        core.memory("agents").append(Agent(i, "S", Body(Fustrum())))
    for i in range(0, 3):
        core.memory("agents").append(Agent(i, "I", Body(Fustrum())))


def setup():
    core.fps = 30
    core.WINDOW_SIZE = [800, 800]
    generate()


def reset():
    core.memory("agents", [])
    generate()


def run():
    core.cleanScreen()
    if core.getKeyPressList("r"):
        reset()

    for a in core.memory("agents"):
        a.show()



    computePerception()
    compteDecision()
    applyDecision()


core.main(setup, run)
