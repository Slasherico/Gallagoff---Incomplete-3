import pgzrun

TITLE= 'Welcome to Gallagoff'
WIDTH= 750
HEIGHT= 750

game_state = True
score = 0
enemy = []
bullets = []
ship = Actor('ship')


ship.x=375
ship.y=650

for x in range(5):
    for y in range(5):
        bug = Actor('bug')
        bug.x = 100+ x*100
        bug.y = 100+ y*50
        enemy.append(bug)


def draw():
    global bullets, ship, score, game_state
    screen.fill('Black')
    if game_state == True:
        ship.draw()
        for b in bullets:
            b.draw()
        for e in enemy:
            e.draw()
    if enemy == []:
        game_state = False
        screen.draw.text(f'Game over you win your score: {score}', (WIDTH/3,HEIGHT/2), fontsize = 30)
    if game_state == 'lost':
        screen.fill('black')
        screen.draw.text(f'Game over you got eaten try again! Your Score: {score} \n Press (r or R) to restart', (WIDTH/4,HEIGHT/2+30), fontsize = 25)
    screen.draw.text(f'Score = {score}', (50,600), fontsize = 30)

def update():
    global score, game_state, enemy, bullets
    if keyboard.left and ship.x > 0:
        ship.x= ship.x-7.5
    if keyboard.right and ship.x < 750:
        ship.x= ship.x+7.5
    for b in bullets:
        b.y= b.y-15
    for e in enemy:
        e.y= e.y+0.5
        for b in bullets:
            if b.colliderect(e):
                bullets.remove(b)
                enemy.remove(e)
                score = score+1
        if e.colliderect(ship):
            game_state = 'lost'

def on_key_down(key):
    global bullets, ship
    if key == keys.SPACE:
        bullet = Actor('bullet')
        bullet.x = ship.x
        bullet.y = ship.y
        bullets.append(bullet)
    if game_state == False or game_state == 'lost':
        if key == keys.R:
            reset()
    
def reset():
    global game_state, bullets, enemy, score, ship, bug
    game_state = True
    bullets = []
    enemy = []
    score = 0  
    ship.x=375
    ship.y=650
    for x in range(5):
        for y in range(5):
            bug = Actor('bug')
            bug.x = 100+ x*100
            bug.y = 100+ y*50
            enemy.append(bug)
    
    

pgzrun.go()