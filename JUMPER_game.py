import pygame, os
pygame.init()
clock = pygame.time.Clock()
pygame.font.init()




loopy = True
WIDTH, HEIGHT = 1400, 800
OUR_SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE = pygame.display.set_caption("KING JUMPER")
FPS = 60
BACKGROUND_COLOR = OUR_SCREEN.fill((50,80,90))


#GAME STATES:
game_active = False
start_time = 0





#MOVEMENT VARIABLES:
snail_movement = 7






#IMAGES
ground_image = pygame.image.load("ground.png").convert_alpha()
sky_image = pygame.image.load("Sky.png").convert_alpha()
ground_image_transformed = pygame.transform.scale(ground_image,(WIDTH,170))
sky_image_transformed = pygame.transform.scale(sky_image,(WIDTH,HEIGHT))
snail_image = pygame.image.load("snail1.png").convert_alpha()
snail_image_transformed = pygame.transform.scale(snail_image, (90,90))
player_image_walk_1 = pygame.image.load("/home/vision16/Documents/images/player_walk_1.png").convert_alpha()
player_image_walk_transformed = pygame.transform.scale(player_image_walk_1, (90,150))
player_image_jump = pygame.image.load("/home/vision16/Documents/images/jump.png").convert_alpha()
player_image_standing = pygame.image.load("/home/vision16/Documents/images/player_stand.png").convert_alpha()
player_image_standing_transformed = pygame.transform.scale(player_image_standing,(250,500))


#GAME ICON:
GAME_ICON = pygame.display.set_icon(player_image_standing)





#FONTS:
test_font = pygame.font.Font("ArissaTypeface.ttf", 100)
test_font2 = pygame.font.Font("ArissaTypeface.ttf", 50)
test_font3 = pygame.font.Font("ArissaTypeface.ttf", 80)
test_font_render = test_font.render("KING JUMPER", 1, (250,0,0))
game_start_instructions_font  = test_font3.render("PRESS SPACE BAR TO START GAME!", 1, (250,0,0))








#rectangles:
snail_image_rectangle = pygame.Rect(WIDTH,548, 90,90)
player_image_rectangle = pygame.Rect(200,489, 90, 150) #walking image 1
player_image_standing_rectangle = player_image_standing_transformed.get_rect(center = (700,390)) #center placement of middle of rectangle





#GRAVITY:
player_gravity = 0






#keys
keys = pygame.key.get_pressed()
#if keys[pygame.K_SPACE]:
    #OUR_SCREEN.blit(player_image_jump, (player_image_rectangle.x, player_image_rectangle.y))




def display_score():
    global current_time
    current_time = int((pygame.time.get_ticks() / 1000)) - start_time  # gets current time, by dividing by 1,000 the get.ticks() turns the seconds to minutes
    score_text = test_font2.render(f"TIME = {current_time}", 1, (0,0,0))
    score_rectangle = pygame.Rect(580, 40, 90, 90)
    OUR_SCREEN.blit(score_text, (score_rectangle.x, score_rectangle.y))
    print(current_time)
    return current_time #doing this instead of making this variable global
































#main_game_loop
while loopy:
    GAME_SPEED = clock.tick(FPS)
    global current_time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
           if event.type == pygame.MOUSEBUTTONDOWN:
                if player_image_rectangle.y >= 489:
                    if player_image_rectangle.collidepoint(event.pos):
                            player_gravity = -25
                            print("player jumped!!")

           if event.type == pygame.KEYDOWN:
                if player_image_rectangle.y >= 489:
                        if event.key == pygame.K_SPACE:
                                player_gravity = -25
                                print("player jumped!!")
        #RESTARTS GAME:
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_active = True
            snail_image_rectangle.x = WIDTH
            player_image_rectangle.y = 489
            start_time = int(pygame.time.get_ticks() / 1000)


    if game_active:


        # DRAWN IMAGES AND RECTANGLES ON SCREEN:
        OUR_SCREEN.blit(sky_image_transformed, (0, 0))
        OUR_SCREEN.blit(ground_image_transformed, (0, 632))
        OUR_SCREEN.blit(snail_image_transformed, (snail_image_rectangle.x, snail_image_rectangle.y))
        OUR_SCREEN.blit(player_image_walk_transformed, (player_image_rectangle.x, player_image_rectangle.y))

        # score:
        SCORE = display_score()


        # jump:
        player_gravity += 1
        player_image_rectangle.y += player_gravity
        if player_image_rectangle.y > 489:
            player_image_rectangle.y = 489

        # animation/movement:
        snail_image_rectangle.x -= snail_movement
        if snail_image_rectangle.x <= -200:
            snail_image_rectangle.x = 1600
        if current_time >= 60:
            if snail_image_rectangle.x == 1600:
                if snail_movement <= 11:
                    snail_movement += 1
        if current_time >= 120:
            if snail_image_rectangle.x == 1600:
                if snail_movement <= 15:
                    snail_movement += 1
        if current_time >= 180:
            if snail_image_rectangle.x == 1600:
                if snail_movement <= 19:
                    snail_movement += 1
        if current_time >= 240:
            if snail_image_rectangle.x == 1600:
                if snail_movement <= 23:
                    snail_movement += 1
        if current_time >= 300:
            if snail_image_rectangle.x == 1600:
                if snail_movement <= 27:
                    snail_movement += 1



        # collisions:
        if snail_image_rectangle.colliderect(player_image_rectangle):
            game_active = False

        pygame.display.update()


    else:
        OUR_SCREEN.fill((50, 40, 80))
        OUR_SCREEN.blit(player_image_standing_transformed, (player_image_standing_rectangle.x, player_image_standing_rectangle.y))
        OUR_SCREEN.blit(test_font_render, (430, 0))
        OUR_SCREEN.blit(game_start_instructions_font, (120, 700))

        #score_message = test_font3.render(f"YOUR TIME: {SCORE}", False, (250, 0, 0))
        #score_message_rectangle = score_message.get_rect(center=(120, 750))
        #if SCORE == 0:
            #OUR_SCREEN.blit(game_start_instructions_font, (120,700))
        #else:
            #OUR_SCREEN.blit(score_message,score_message_rectangle)


        pygame.display.update()

#NOTES:
# - DRAW ALL OUR ELEMENTS and images IN main game loop
# - UPDATE EVERYTHING IN main game loop
# - the .convert_alpha() and .convert() functions convert the image from a png file to something else that works better with python this is not neccessary but it makes your game run smoother and faster and is good pygame etiqutte
# - Rectangles are not needed to move images you can just make the x and y oordinates of a blited image into a variable and move that variable under the main game whole loop but its better to use rectangles because of their collision detection capabilities
# - if you want continous movement of a rectangle it has to be done only under the main game while loop not any for loops
# - display score after finish playing game