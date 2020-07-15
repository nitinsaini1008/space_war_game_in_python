import pygame
import os
import random
import time
x=pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Nitin's secound game")
icon=pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)
#-----------PLAYER---------------
player_img=pygame.image.load('spaceship.png')
player_x=200
player_y=560
move_l=False
move_r=False
s=0
def player():
	screen.blit(player_img,(player_x,player_y))
#-------------------------------------------
background=pygame.image.load('back.jpg')

#-----------ENEMY---------------
enemy_img=pygame.image.load('monster.png')
enemy_x=random.randint(32,568)
enemy_y=10
move_d=False
enemy_move_l=True
enemy_move_r=False

def enemy():
	screen.blit(enemy_img,(enemy_x,enemy_y))

#--------------------------------- 
#-----------FIREBALL-------------
fire_x=player_x
fire_y=player_y
start_fire=False
fire_img=pygame.image.load('fire.png')

def fire(x,y):
	screen.blit(fire_img,(x,y))
	
#--------------------------------
game_exit=False
while not game_exit:
	screen.blit(background,(0,0))
	#screen.fill((100,10,200))
	for i in pygame.event.get():
		if i.type==pygame.QUIT:
			game_exit=True
		if i.type==pygame.KEYDOWN:
			if i.key==pygame.K_LEFT:
				move_l=True
				move_r=False
			if i.key==pygame.K_RIGHT:
				move_r=True
				move_l=False
			if i.key==pygame.K_SPACE:
				start_fire=True
				fire_y=player_y
				fire_x=player_x

	font = pygame.font.Font('freesansbold.ttf', 32)  
	text = font.render('SCORE='+str(s), True, (0,200,0), (200,100,100)) 
	textRect = text.get_rect()  
	textRect.center = (100,100) 
	screen.blit(text, textRect)
	if move_l==True:
		if player_x>0:
			player_x-=3
	if move_r==True:
		if player_x<568:
			player_x+=3
	player()
	if start_fire==True:
		d=((enemy_x-fire_x)**2+(enemy_y-fire_y)**2)**0.5
		if d<=27:
			s+=1
			enemy_x=random.randint(32,568)
			enemy_y=0
		fire_y-=5
		fire(fire_x,fire_y)
		if fire_y<=10:
			start_fire=False
	enemy()
	if enemy_move_l==True:
		enemy_x-=3
		if enemy_x<=0:
			enemy_y+=20
			enemy_move_l=False
			enemy_move_r=True
	if enemy_move_r==True:
		enemy_x+=3
		if enemy_x>=560:
			enemy_y+=20
			enemy_move_r=False
			enemy_move_l=True
	
	if enemy_y>560:
		game_exit=True
	pygame.display.update()
pygame.quit()
quit()