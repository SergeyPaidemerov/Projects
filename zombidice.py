import zombiedice
class My_Zombie: 
    def __init__(self, name):
        self.name = name
    def turn(self, gameState):
        dice_Roll_Results = zombiedice.roll()
        brains = 0
        while dice_Roll_Results is not None:
            brains += dice_Roll_Results['brains']
            if brains < 2:
                dice_Roll_Results = zombiedice.roll()
            else:
                break
zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name= \
        'Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsOneMoreZombie(name= \
        'Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsOneMoreZombie(name= \
        'Stop at 1 Shotguns', minShotguns=1),
    My_Zombie(name='My Zombie Bot')
)
zombiedice.runWebGui(zombies=zombies, numGames=1000)

