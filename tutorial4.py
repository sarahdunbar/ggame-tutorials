from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.rotateLeft)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.rotateRight)
        SpaceGame.listenKeyEvent("keydown", "w", self.up)
        SpaceGame.listenKeyEvent("keydown", "s", self.down)
        SpaceGame.listenKeyEvent("keydown", "a", self.left)
        SpaceGame.listenKeyEvent("keydown", "d", self.right)
        SpaceGame.listenKeyEvent("keyup", "w", self.upoff)
        SpaceGame.listenKeyEvent("keyup", "s", self.downoff)
        SpaceGame.listenKeyEvent("keyup", "a", self.leftoff)
        SpaceGame.listenKeyEvent("keyup", "d", self.rightoff)
        self.fxcenter = self.fycenter = 0.5

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)

    def thrustOn(self, event):
        self.thrust = 1

    def thrustOff(self, event):
        self.thrust = 0
    
    def rotateLeft (self, event):
        self.rotation += .01
        
    def rotateRight (self, event):
        self.rotation += -.01
        
    def up (self, event):
        self.vy += -.1
    
    def down (self, event):
        self.vy += .1
        
    def left (self, event):
        self.vx += -.1
        
    def right (self, event):
        self.vx += .1
        
    def upoff (self, event):
        self.vy = 0
    
    def downoff (self, event):
        self.vy = 0
        
    def leftoff (self, event):
        self.vx = 0
        
    def rightoff (self, event):
        self.vx = 0
        



class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(width, height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        SpaceShip((100,100))
        SpaceShip((150,150))
        SpaceShip((200,50))

    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()


myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()