#GAME IS FINISHED BUT NO SOUNDS FOR BULLET TO SHIP COLLISIONS, SPACESHIP MOVEMENTs, EXPLOSION SOUND FOR SPACESHIP DYING, AND GAME AUTOMATICALLY QUITS ONCE SOMEONE WINS!!!
#CREATING A SPACESHIP VS SPACESHIP BATTLE GAME!!
#DON"T FORGET TO LOOK INTO YOUR NOTEBOOK NOTES FOR HELP AND CONTINUE WATCHING TUTORIALS THIS IS A STANDALONE PROJECT NOW!! OUR FIRST GAME PROJECT!!!
import pygame
pygame.font.init()
pygame.mixer.init()



#NEED TO MAKE SURE THE PYGAME PROGRAM CAN CLOSE WHEN WE CLICK THE EXIT BUTTON!!
#ALL OF OUR VARIABLES FOR OUR GAME
HEIGHT, WIDTH = 900, 900
OUR_SCREEN_SURFACE = pygame.display.set_mode((HEIGHT, WIDTH))
NAME_OF_GAME = pygame.display.set_caption("space game".title())
BACKGROUND_COLOR = (200, 50, 255) #Hot pink
BACKGROUND_IMAGE = pygame.image.load('space-galaxy-background.jpg')
BACKGROUND_IMAGE_SIZE = pygame.transform.scale(BACKGROUND_IMAGE,(900,900))

#START LOADING SPACESHIP IMAGES INTO OR ONTO PYGAME SCREEN/SURFACE, PLACED EMPTY TUPLE THERE FOR NOW
#can use images as long as in same file as python project folder if not in the same folder you have to use the os module to direct to images path!
GOOD_BLACK_SPACESHIP = pygame.image.load('aircraft.png')#WORKING!!
GOOD_BLCK_IMAGE_SIZE = pygame.transform.scale(GOOD_BLACK_SPACESHIP, (50, 70))
BAD_BLACK_SPACESHIP = pygame.image.load('star-wars.png')
BAD_BLACK_IMAGE_SIZE = pygame.transform.scale(BAD_BLACK_SPACESHIP,(50,70))
BAD_RECTANGLE = pygame.Rect(400, 250, 50, 70) #RECTANGLE WRAPPED AROUND IMAGE TO MOVE IMAGE
GOOD_RECTANGLE = pygame.Rect(400, 750, 50, 70) #RECTANGLE WRAPPED AROUND IMAGE TO MOVE IMAGE, (x,Y,WIDTH,HEIGHT)




#BULLETS:
BULLET_GOOD_IMAGE = pygame.image.load('bullet.png')
BULLET_BAD_IMAGE = pygame.image.load('bullet (1).png')
BULLET_BAD_IMAGE_SIZE = pygame.transform.scale(pygame.transform.rotate(BULLET_BAD_IMAGE, 223), (30,50))
BULLET_GOOD_IMAGE_SIZE = pygame.transform.scale(pygame.transform.rotate(BULLET_GOOD_IMAGE, 45), (30,50))
BAD_BULLETS = []
GOOD_BULLETS = []
MAX_BULLETS = 6
BAD_HIT = pygame.USEREVENT + 1 #pygame.USEREVENT creates our own custom made event and the + 1 just makes it a unique event and you need to add another number for every USeREVENT you make...
GOOD_HIT = pygame.USEREVENT + 2 #THESE pygame.USEREVENTS will handle , PERSONALLY I DON"T THINK THIS IS NECESSARY I THINK YOU COULD JUST PRINT OR DRAW ON THE SCREEN THESE IF THE BULLETS COLLIDE WITH THE SHIPS RECTANGLES.
#GOOD_BULLET_RECTANGLE = pygame.Rect(GOOD_RECTANGLE.x, GOOD_RECTANGLE.y, 30, 50)
#BAD_BULLET_RECTANGLE = pygame.Rect(BAD_RECTANGLE.x, BAD_RECTANGLE.y, 30, 50)


#VARIABLE FOR MOVEMENT SPEED:
VEL = 2
#VARIABLE FOR MIDDLE WALL BETWEEN SHIPS:
BORDER_COLOR = 255, 255, 0 #YELLOW

#health and winner_text
good_health = 12
bad_health = 12
winner_text = " "


#VARIABLE FOR FONT:
HEALTH_FONT = pygame.font.SysFont("comicsans", 60) #use render function to draw this on screen
WINNER_FONT = pygame.font.Font("ArissaTypeface.ttf", 200)



FPS = 60 #frames per second



#SOUNDS
GOOD_SHIP_FIRE_SOUND = pygame.mixer.Sound("Artillery Shoot.wav")
BAD_SHIP_FIRE_SOUND = pygame.mixer.Sound("Shooting.wav")
BACKGROUND_MUSIC = pygame.mixer.Sound("Dynamic Sci Fi.wav")
BACKGROUND_MUSIC_VOLUME = pygame.mixer.Sound.set_volume(BACKGROUND_MUSIC, -2.0) #VOLUME CHANGES MAY NOT BE WORKING FOR WAV FILES, OR IM JUST PLACING THESE IN THE WRONG PLACE
GOOD_SHIP_FIRE_SOUND_VOLUME = pygame.mixer.Sound.set_volume(GOOD_SHIP_FIRE_SOUND, 5.0) #VOLUME CHANGES MAY NOT BE WORKING FOR WAV FILES, OR IM JUST PLACING THESE IN THE WRONG PLACE
BAD_SHIP_FIRE_SOUND_VOLUME = pygame.mixer.Sound.set_volume(BAD_SHIP_FIRE_SOUND, 5.0) #VOLUME CHANGES MAY NOT BE WORKING FOR WAV FILES, OR IM JUST PLACING THESE IN THE WRONG PLACE
GAME_WINNER_SOUND = pygame.mixer.Sound("Game Win 03.wav")

def Good_ship_movement():
    # movement, under while loop only
    keys_pressed = pygame.key.get_pressed()  # THERE ARE TWO WAYS TO ADD MOVEMENTS FOR DIFFERENT KEYS THIS WAY AND THE event.type == pygame.keydown: way!!!
    # VEL = 2
    # MOVEMENT FOR GOOD SHIP:
    if keys_pressed[pygame.K_UP] and GOOD_RECTANGLE.y - VEL > 480:  # UP OR FORWARD #the other condition keeps our rectangle from going outside of the surface?display borders!
        GOOD_RECTANGLE.y -= VEL + 8
    if keys_pressed[pygame.K_DOWN] and GOOD_RECTANGLE.y - VEL < 830:  # DOWN OR BACKWARDS
        GOOD_RECTANGLE.y += VEL + 8
    if keys_pressed[pygame.K_LEFT] and GOOD_RECTANGLE.x - VEL > 0:  # LEFT
        GOOD_RECTANGLE.x -= VEL + 8
    if keys_pressed[pygame.K_RIGHT] and GOOD_RECTANGLE.x - VEL < 840:  # RIGHT
        GOOD_RECTANGLE.x += VEL + 8

def Bad_ship_movement():
    # movement, under while loop only
    keys_pressed = pygame.key.get_pressed()  # THERE ARE TWO WAYS TO ADD MOVEMENTS FOR DIFFERENT KEYS THIS WAY AND THE event.type == pygame.keydown: way!!!
    # VEL = 2
    # MOVEMENT FOR GOOD SHIP:
    if keys_pressed[pygame.K_w] and BAD_RECTANGLE.y - VEL > -8:  # UP OR FORWARD
        BAD_RECTANGLE.y -= VEL + 8
    if keys_pressed[pygame.K_s] and BAD_RECTANGLE.y - VEL < 380:  # DOWN OR BACKWARDS
        BAD_RECTANGLE.y += VEL + 8
    if keys_pressed[pygame.K_a] and BAD_RECTANGLE.x - VEL > 0:  # LEFT
        BAD_RECTANGLE.x -= VEL + 8
    if keys_pressed[pygame.K_d] and BAD_RECTANGLE.x - VEL < 840:  # RIGHT
        BAD_RECTANGLE.x += VEL + 8



def Handle_Collision(Bad_Bullets, Good_Bullets, Bad_rectangle, Good_rectangle): #BAD_BULLETS(list), GOOD_BULLETS(list), BAD_SHIP_RECTANGLE, GOOD_SHIP_RECTANGLE
    for Bullet in Bad_Bullets:
        Bullet.y += 13
        if Good_rectangle.colliderect(Bullet):
            pygame.event.post(pygame.event.Event(GOOD_HIT))
            Bad_Bullets.remove(Bullet) #erases bullet if it collides with enemy ship...
        elif Bullet.y > 900: #removes bullet if it hits edge of screen, we use elif to make sure we don't remove the bullet twice.
            Bad_Bullets.remove(Bullet)

    for Bullet in Good_Bullets:
        Bullet.y -= 13
        if Bad_rectangle.colliderect(Bullet):
            pygame.event.post(pygame.event.Event(BAD_HIT))
            Good_Bullets.remove(Bullet) #erases bullet if it collides with enemy ship...
        elif Bullet.y < 0:  #removes bullet if it hits edge of screen
            Good_Bullets.remove(Bullet)



def draw_on_screen(BAD,GOOD, BAD_bullets, GOOD_bullets, GD_HEALTH, BD_HEALTH): #ALL IMAGES AND COLORS ON THE DISPLAY WILL BE PLACED HERE!!

    BACKGROUND_IMAGE_PLACEMENT= OUR_SCREEN_SURFACE.blit(BACKGROUND_IMAGE_SIZE, (0,0))
    GOOD_BLCK_IMAGE_PLACEMENT = OUR_SCREEN_SURFACE.blit(GOOD_BLCK_IMAGE_SIZE, (GOOD.x, GOOD.y))# HAD TO REPLACE IMAGE WITH RESCALED IMAGE VARIABLE1
    BAD_BLACK_IMAGE_PLACEMENT = OUR_SCREEN_SURFACE.blit(BAD_BLACK_IMAGE_SIZE,(BAD.x, BAD.y))
    GOOD_SHIP_HEALTH_TEXT = HEALTH_FONT.render("HEALTH: " + str(GD_HEALTH), 1, (100, 100, 100) ) #(text, antialias - alwayes make this the number 1 for art purposes, color in tuple form)
    BAD_SHIP_HEALTH_TEXT = HEALTH_FONT.render("HEALTH: " + str(BD_HEALTH), 1, (50, 100, 50))  #(text, antialias - alwayes make this the number 1 for art purposes, color in tuple form)
    GOOD_SHIP_HEALTH_TEXT_PLACEMENT = OUR_SCREEN_SURFACE.blit(GOOD_SHIP_HEALTH_TEXT, (0, 863))
    BAD_SHIP_HEALTH_TEXT_PLACEMENT = OUR_SCREEN_SURFACE.blit(BAD_SHIP_HEALTH_TEXT, (0,0))
    BORDER = pygame.draw.rect(OUR_SCREEN_SURFACE, BORDER_COLOR,
                              (0, 450, 900, 40)) # dispSurf,color,(x,y,width,height)
    for bullet in BAD_bullets:
        BAD_BULLET_PLACEMENT = OUR_SCREEN_SURFACE.blit(BULLET_BAD_IMAGE_SIZE,(bullet.x, bullet.y))

    for bullet in GOOD_bullets:
        GOOD_BULLET_PLACEMENT = OUR_SCREEN_SURFACE.blit(BULLET_GOOD_IMAGE_SIZE, (bullet.x, bullet.y))


def draw_WINNER(text, texty2):
    draw_text = WINNER_FONT.render(text, 1, (255,204,229))  #(text, antialias - alwayes make this the number 1 for art purposes, color in tuple form)
    draw_text_2 = WINNER_FONT.render(texty2, 1, (255,204,229))
    OUR_SCREEN_SURFACE.blit(draw_text, (20, 250))
    OUR_SCREEN_SURFACE.blit(draw_text_2,(50,470))
    pygame.display.update()
    pygame.time.delay(5000) #will show the winner text for 5 seconds








def main_game_loop(loop_run= True):
    global bad_health, good_health, winner_text
    pygame.init()  # must be called before anything
    clock = pygame.time.Clock() #ACTIVATES THE TIME MODULE IN PYGAME to control the speed of the while loop
    BACKGROUND_MUSIC.play(-1)  # THE NEGATIVE ONE MAKES SURE OUR BACKGROUND MUSIC KEEPS ON LOOPING AFTER IT ENDS, IN ORDER TO WORK WITH SOUNDS IN THE LOOP THIS SOUND HAD TO BE CALLED COMPLETELY OUTSIDE ANY LOOPS BUT IN THE FUNCTION
    while loop_run:
        clock.tick(FPS)  # CONTROLS THE SPEED OF THE WHILE LOOP, and is using our clock variable first with the tick method
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop_run = False
                pygame.quit()
                exit()



            if event.type == pygame.KEYDOWN: #WORKS BUT BULLET IMAGES AREN"T STAYING ON SCREEN!!!
                if event.key == pygame.K_LCTRL and len(BAD_BULLETS) < MAX_BULLETS:  #the second conditional will limit the amount of BUllets that can be fired..
                    BAD_BULLET_RECTANGLE = pygame.Rect(BAD_RECTANGLE.x, BAD_RECTANGLE.y, 30, 50)
                    BAD_BULLETS.append(BAD_BULLET_RECTANGLE)
                    BAD_SHIP_FIRE_SOUND.play()



                if event.key == pygame.K_RCTRL and len(GOOD_BULLETS) < MAX_BULLETS:
                    GOOD_BULLET_RECTANGLE = pygame.Rect(GOOD_RECTANGLE.x, GOOD_RECTANGLE.y, 30, 50)
                    GOOD_BULLETS.append(GOOD_BULLET_RECTANGLE)
                    GOOD_SHIP_FIRE_SOUND.play()

            if event.type == GOOD_HIT:
                good_health -= 1

            if event.type == BAD_HIT:
                    bad_health -= 1

        #as long as the if statements aren't event.types it dosen;t have to go under the for loop it can just go under the while loop
        if good_health <= 0:
                winner_text = "BAD SHIP"
        if bad_health <= 0:
                winner_text = "GOOD SHIP"
        if winner_text != " ":
            BACKGROUND_MUSIC.stop()
            GAME_WINNER_SOUND.play()
            draw_WINNER(winner_text, "WINS!!!")


            break #stops while loop







        Good_ship_movement()
        Bad_ship_movement()
        Handle_Collision(BAD_BULLETS, GOOD_BULLETS, BAD_RECTANGLE, GOOD_RECTANGLE )
        draw_on_screen(BAD_RECTANGLE,GOOD_RECTANGLE, BAD_BULLETS, GOOD_BULLETS, good_health, bad_health)
        pygame.display.update()

    pygame.quit()



#ADDING MOVEMENT
#SOME FUNCTIONS SHOULD BE CALLED OUTSIDE OF ANY LOOPS





if __name__ == "__main__":
     main_game_loop()


#NOTES:
    #NEED TO CREATE A RECTANGLES FOR OUR IMAGES IN ORDER TO MOVE THEM USING THE pygame.Rect() function
    #For pygame.Rect function we should put this function in its own variable
    #pygame.Rect(x-position/placement, y-position/placement, Width of image, Height of image)
    #NEED TO ADD MOVEMENT FOR EACH SHIP!!!, HAVE TO USE RECT FUNCTION IN ORDER TO MOVE IMAGES THIS WAY USING HEIGHT AND WIDTH VARIABLES WON"T WORK!!
    #NEED TO ADD BREAK STATEMENT OR THE EXIT() FUNCTION AFTER pygame.quit() otherwiseyou will get a pygame.error: display surface quit, because pygame.quit() only quits the module but the loop will keep running and in turn the program keeps running
#MOVEMENT WORKS AS LONG AS IT's made in the while loop or in the draw_on_screen function and above the pygame.display.update() function

#NEXT TIME JUST DRAW BULLETS USING pygame.Draw.Rect instead of using images.

#every time we use if event.type == pygame.whatever it always goes under the for event in pygame.event.get() loop which is under our main game while loop
#whenever you want a number to decrase or increase by another number you have to use the operator + or - with an equal = sign attched to it for example += or -= otherwise the statemnet will have no effect

#for some reason because these are local variables we can't change them in a function unless we pass them threw as an argument
#BAD_BLACK_IMAGE_WIDTH = 400
#BAD_BLACK_IMAGE_HEIGHT = 250
#GOOD_BLCK_IMAGE_WIDTH = 400
#GOOD_BLCK_IMAGE_HEIGHT = 750


#CAN't restart game by calling main_game_loop() function again in our main_game_lop() function because there are certain constants/variables that needed to be inside of the function as well be we have them outside of the function.


#NEXT STEP:(FINISHED!!)
# - IF YOU WANT TOO YOU CAN ADD SOUNDS FOR BULLET TO SHIP COLLISIONS, SPACESHIP MOVEMENTs, EXPLOSION SOUND FOR SPACESHIP DYING
