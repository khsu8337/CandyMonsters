from gamelib import *

game=Game(800,600,"Candy Monsters")
bk=Image("images2\\background.jpg",game)
bk.resizeTo(game.width,game.height)
game.setBackground(bk)

bk.draw()
game.drawText("Candy Monsters", game.width/4-50, game.height/4+20, Font(blue,90,blue))
game.drawText("Press [SPACE] to Begin",game.width/2+80, game.height -50, Font(blue,30,white))
game.update(1)
game.wait(K_SPACE)

crosshair=Image("images2\\crosshair.png",game)
crosshair.resizeBy(-99.99)

gun=Sound("Sound\\Gun2.wav",1)
                
chocolate=[]
sour=[]
monster1=[]
monster2=[]
jaw=[]

jumping = False #Used to check to see if you are jumping
landed = False #Used to check to see if you have landed on the ground
factor = 1 #Used for a slowing effect of the jumping

floor = Image("images2\\floor.png",game)
floor.moveTo(game.width / 2, game.height - 50)

bear = Image("images2\\gummy bear.png",game)
bear.resizeBy(-85)
bear.moveTo(100,465)
bear.draw()

crosshair=Image("images2\\crosshair.png",game)
crosshair.resizeBy(-80)

for num in range(50):
    chocolate.append( Image("images2\\chocolate.png",game) )

for num in range(70):
    sour.append( Image("images2\\sour patch.png",game) )

for num in range(110):
    monster1.append( Image("images2\\monster1.png",game) )

for num in range(110):
    monster2.append( Image("images2\\monster2.png",game) )

for num in range(70):
    jaw.append( Image("images2\\jawbreaker.png",game) )

for c in chocolate:
    c.resizeBy(-80)
    x = game.width + randint(100 ,10500)
    y = randint(5 ,475)
    s = randint(3,6)
    c.moveTo(x,y)
    c.setSpeed(s, 90)

for p in sour:
    p.resizeBy(-80)
    x = game.width + randint(100 ,10500)
    y = randint(5 ,475)
    s = randint(3,6)
    p.moveTo(x,y)
    p.setSpeed(s, 90)
    
for m in monster1:
    m.resizeBy(-80)
    x = game.width + randint(100 ,10500)
    y = randint(50 ,500)
    s = randint(3,6)
    m.moveTo(x,y)
    m.setSpeed(s, 90)
    m.draw()

for n in monster2:
    n.resizeBy(-80)
    x = game.width + randint(100 ,10500)
    y = randint(5 ,550)
    s = randint(3,6)
    n.moveTo(x,y)
    n.setSpeed(s, 90)

for j in jaw:
    j.resizeBy(-80)
    x = game.width + randint(100 ,10500)
    y = randint(5 ,550)
    s = randint(3,6)
    j.moveTo(x,y)
    j.setSpeed(s, 90)
game.score=0
bear.health=100
#Start Screen
while not game.over:
    game.processInput()
    game.scrollBackground("left",2)
    if keys.Pressed[K_RETURN]:
        game.over = True
        
    game.drawText("How to play:", game.width/4-100, game.height/5, Font(blue,150,blue))
    game.drawText("Press [W] to Jump",game.width/4-50, game.height/2+25, Font(blue,50,white))
    game.drawText("Press [A] or [D] to move left and right",game.width/4-50, game.height/2+75, Font(blue,50,white))
    game.drawText("Press [Enter] to start",200,500,Font(blue,50,blue))
    game.update(60)

game.over = False

while not game.over:
    game.processInput()
    game.scrollBackground("left",2)
    if keys.Pressed[K_a]:
        game.over = True
        
    game.drawText("Goal:", game.width/4-100, game.height/5, Font(blue,150,blue))
    game.drawText("Shoot the monsters and collect the candies",game.width/4-50, game.height/2+25, Font(blue,40,white))
    game.drawText("Collect 200 points to get to level 2",game.width/4-50, game.height/2+75, Font(blue,40,white))
    game.drawText("Press [A] to start",200,500,Font(blue,50,blue))
    game.update(60)

game.over = False
#Main Game

while not game.over:
    game.processInput()
    game.scrollBackground("left",2)
    floor.draw()
    bear.draw()
    crosshair.moveTo(mouse.x, mouse.y)

    if mouse.LeftButton:
        gun.play()

    #Jumping Logic    
    if bear.y >= 460:

        landed = True
        #300 is the floor.  Decision can be replaced with a more complex condition based on game
 
    if jumping:
        bear.y -= 45 * factor
        #Make the character go up.  Factor creates a slowing effect to the jump
        factor *= .95
        landed = False
        
        #Since you are jumping you are no longer staying on land
        if factor < .18:
            jumping = False
            #Stop jumping once the slowing effect finishes
            factor = 1
            
    if keys.Pressed[K_w] and landed and not jumping:
            #If you landed on the floor and are not jumping and press the SpaceBar then jump
            jumping = True
            
    if not landed:
        bear.y += 9
        #If you haven't landed then you are in the air, so you should fall.

    for c in chocolate:
        c.move()
        if bear.collidedWith(c):
            bear.health += 20
            c.makeVisible(False)
        if c.collidedWith(mouse)and mouse.LeftButton:
         c.makeVisible(False)
         game.score -= 20
            
    for p in sour:
        p.move()
        if bear.collidedWith(p):
            game.score += 20
            p.makeVisible(False)
        if p.collidedWith(mouse)and mouse.LeftButton:
            p.makeVisible(False)
            game.score -= 20

    for m in monster1:
        m.move()
        if bear.collidedWith(m):
            bear.health -= 20
            m.makeVisible(False)
        if m.collidedWith(mouse)and mouse.LeftButton:
            m.makeVisible(False)
            game.score += 10

    for n in monster2:
        n.move()
        if bear.collidedWith(n):
            bear.health -= 20
            n.makeVisible(False)
        if n.collidedWith(mouse)and mouse.LeftButton:
            n.makeVisible(False)
            game.score += 10

    for j in jaw:
        j.move()
        if bear.collidedWith(j):
            game.score -= 20
            j.makeVisible(False)
        if j.collidedWith(mouse)and mouse.LeftButton:
            j.makeVisible(False)
            game.score += 10

    if keys.Pressed[K_a]:
        bear.x -= 5
    if keys.Pressed[K_d]:
        bear.x += 5
        
    if game.score > 190:
        game.over=True
    game.drawText("Health:"+str(bear.health),200,5)
    game.displayScore()
    game.update(60)
    
    if bear.health < 20 or game.score < 0:   
        game.drawText("Game Over", game.width/4-50, game.height/4+20, Font(blue,90,blue))
        game.drawText("Press [SPACE] to Exit",game.width/2+80, game.height -50, Font(blue,30,white))
        game.update()
        game.wait(K_SPACE)
        game.quit()
game.drawText("Level 2", game.width/2-200, game.height/4+20, Font(blue,150,blue))
game.drawText("Press [SPACE] to Begin",game.width/2+80, game.height -50, Font(blue,30,white))
game.update(1)
game.wait(K_SPACE)
game.update()
game.wait(K_SPACE)
game.over=False

game.score=0
bear.health=100

bk2=Image("images2\\background2.jpg",game)
bk2.resizeTo(game.width,game.height)
game.setBackground(bk2)
bk2.draw()
game.update()

while not game.over:
    game.processInput()
    game.scrollBackground("left",2)
    if keys.Pressed[K_RETURN]:
        game.over = True
        
    game.drawText("Goal:", game.width/4-100, game.height/5, Font(blue,150,blue))
    game.drawText("Shoot the monsters and collect the candies",game.width/4-50, game.height/2+25, Font(blue,40,white))
    game.drawText("Collect 400 points to win",game.width/4-50, game.height/2+75, Font(blue,40,white))
    game.drawText("Press [Enter] to start",200,500,Font(blue,50,blue))
    game.update(60)

game.over=False
while not game.over:
    game.processInput()
    game.scrollBackground("left",2)
    floor.draw()
    bear.draw()
    crosshair.moveTo(mouse.x, mouse.y)

    if mouse.LeftButton:
        gun.play()

    #Jumping Logic    
    if bear.y >= 460:
        landed = True
        #300 is the floor.  Decision can be replaced with a more complex condition based on game

    if jumping:
        bear.y -= 45 * factor
        #Make the character go up.  Factor creates a slowing effect to the jump
        factor *= .95
        landed = False
        
        #Since you are jumping you are no longer staying on land
        if factor < .18:
            jumping = False
            #Stop jumping once the slowing effect finishes
            factor = 1
            
    if keys.Pressed[K_w] and landed and not jumping:
            #If you landed on the floor and are not jumping and press the SpaceBar then jump
            jumping = True
            
    if not landed:
        bear.y += 9
        #If you haven't landed then you are in the air, so you should fall.

    for c in chocolate:
        c.move()
        if bear.collidedWith(c):
            bear.health += 10
            c.makeVisible(False)
        if c.collidedWith(mouse)and mouse.LeftButton:
         c.makeVisible(False)
         game.score -= 20
            
    for p in sour:
        p.move()
        if bear.collidedWith(p):
            game.score += 10
            p.makeVisible(False)
        if p.collidedWith(mouse)and mouse.LeftButton:
            p.makeVisible(False)
            game.score -= 20

    for m in monster1:
        m.move()
        if bear.collidedWith(m):
            bear.health -= 20
            m.makeVisible(False)
        if m.collidedWith(mouse)and mouse.LeftButton:
            m.makeVisible(False)
            game.score += 10

    for n in monster2:
        n.move()
        if bear.collidedWith(n):
            bear.health -= 20
            n.makeVisible(False)
        if n.collidedWith(mouse)and mouse.LeftButton:
            n.makeVisible(False)
            game.score += 10

    for j in jaw:
        j.move()
        if bear.collidedWith(j):
            game.score -= 20
            j.makeVisible(False)
        if j.collidedWith(mouse)and mouse.LeftButton:
            j.makeVisible(False)
            game.score += 10

    if keys.Pressed[K_a]:
        bear.x -= 5
    if keys.Pressed[K_d]:
        bear.x += 5
            
    if bear.health < 20 or game.score < 0 or game.score > 390:
        game.over=True
        
    game.drawText("Health:"+str(bear.health),200,5)
    game.displayScore()
    game.update(100)

game.drawText("Game Over", game.width/4-50, game.height/4+20, Font(blue,90,blue))
game.drawText("Press [SPACE] to Exit",game.width/2+80, game.height -50, Font(blue,30,white))
game.update()
game.wait(K_SPACE)
game.quit()
