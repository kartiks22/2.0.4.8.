import pygame
import time
import random

try:
	import android
except ImportError:
	android = None
pygame.init()

try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except ImportError:
    pass

white = (255,255,255)
black = (0,0,0)
green = (0,225,0)
grey = (240,220,240)
orange = (255,69,0)
purple = (75,0,130)
red = (255,0,0)

screen_width = 240
screen_height =270

gameDisplay = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption(' * *  2.0.4.8.  * * ')

icon = pygame.image.load("icon.jpg")
pygame.display.set_icon(icon)

start_sound = pygame.mixer.Sound("start_sound.wav")
blocks_sound = pygame.mixer.Sound("blocks_sound.wav")

if android:
	android.init()
	android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

h = 50
w = 50
m = 8
x=8
y=8
blocks_list=[]
img_dict = {}

score = 0
high_score = 0
big_list = []
			
a=2
img_2 = pygame.image.load(str(a)+".jpg")
img_dict[2] = img_2
a = a * 2
img_4 = pygame.image.load(str(a)+".jpg")
img_dict[4] = img_4
a = a * 2
img_8 = pygame.image.load(str(a)+".jpg")
img_dict[8] = img_8
a = a * 2
img_16 = pygame.image.load(str(a)+".jpg")
img_dict[16] = img_16
a = a * 2
img_32 = pygame.image.load(str(a)+".jpg")
img_dict[32] = img_32
a = a * 2
img_64 = pygame.image.load(str(a)+".jpg")
img_dict[64] = img_64
a = a * 2
img_128 = pygame.image.load(str(a)+".jpg")
img_dict[128] = img_128
a = a * 2
img_256 = pygame.image.load(str(a)+".jpg")
img_dict[256] = img_256
a = a * 2
img_512 = pygame.image.load(str(a)+".jpg")
img_dict[512] = img_512
a = a * 2
img_1024 = pygame.image.load(str(a)+".jpg")
img_dict[1024] = img_1024
a = a * 2
img_2048 = pygame.image.load(str(a)+".jpg")
img_dict[2048] = img_2048

font = pygame.font.SysFont(None,40)
big_font = pygame.font.SysFont(None,100)
small_font = pygame.font.SysFont(None,30)

def message_to_screen(msg,colour):
	screen_text = font.render(msg,True,colour)
	gameDisplay.blit(screen_text,[40,235])

def draw_blank_box(x,y,w,h,m):
	for i in range(4):
		for j in range(4):
			pygame.draw.rect(gameDisplay,grey,[x,y,w,h])
			x=x+w
			pygame.draw.rect(gameDisplay,black,[x,y,m,h])
			x=x+m
		x=8
		y=y+h+m

def make_block_list(x,y,blocks_list):
	x=8
	y=8
	number = 0
	state=0
	value=0

	for i in range(4):
		for j in range(4):
			k=[number,i,j,x,y,state,value]
			blocks_list.append(k)
			number +=1
			x=x+w+m
		x=8
		y=y+h+m
	return blocks_list

# 0:number , 1:i , 2:j , 3:x , 4:y , 5:state , 6:value

def move_right(w,h,blocks_list,score,big_list):
	score = big_list[1]
	del big_list[:]
	right_most = [3,7,11,15] 
	for i in right_most:
		count = 0
		hogya = False
		if blocks_list[i][5] == 0:
			count += 1
		
		
		if blocks_list[i-1][5] == 0:
			count += 1
		else:
			if count == 0:
				
				if blocks_list[i][6] == blocks_list[i-1][6]:
					
					blocks_list[i][6] = blocks_list[i][6] * 2
					gameDisplay.blit(img_dict[blocks_list[i][6]] , (blocks_list[i][3],blocks_list[i][4]))
					blocks_list[i][5] = 1
					
					blocks_list[i-1][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i-1][3],blocks_list[i-1][4],w,h])
					blocks_list[i-1][5] = 0
					count +=1
					hogya = True
					score += blocks_list[i][6]
				
				
			else :
					blocks_list[i][6] = blocks_list[i-1][6] 
					gameDisplay.blit( img_dict[blocks_list[i][6]], (blocks_list[i][3],blocks_list[i][4]))
					blocks_list[i][5] = 1
					
					blocks_list[i-1][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i-1][3],blocks_list[i-1][4],w,h])
					blocks_list[i-1][5] = 0

		if blocks_list[i-2][5] == 0:
			count += 1
		else:
			if count == 0:
				
				if blocks_list[i-2][6] == blocks_list[i-1][6] and hogya != True:
					
					blocks_list[i-1][6] = blocks_list[i-1][6] * 2
					gameDisplay.blit(img_dict[blocks_list[i-1][6]] , (blocks_list[i-1][3],blocks_list[i-1][4]))
					blocks_list[i-1][5] = 1
					
					blocks_list[i-2][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i-2][3],blocks_list[i-2][4],w,h])
					blocks_list[i-2][5] = 0
					count +=1
					hogya = True
					score += blocks_list[i-1][6]
				
				
			elif count == 1 :
				if blocks_list[i-2][6] == blocks_list[i][6] and hogya != True:
					
					blocks_list[i][6] = blocks_list[i][6] * 2
					gameDisplay.blit(img_dict[blocks_list[i][6]] , (blocks_list[i][3],blocks_list[i][4]))
					blocks_list[i][5] = 1
					
					blocks_list[i-2][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i-2][3],blocks_list[i-2][4],w,h])
					blocks_list[i-2][5] = 0
					count +=1
					hogya = True
					score += blocks_list[i][6] 


				else:
					blocks_list[i-1][6] = blocks_list[i-2][6] 
					gameDisplay.blit(img_dict[blocks_list[i-1][6]] , (blocks_list[i-1][3],blocks_list[i-1][4]))
					blocks_list[i-1][5] = 1
					
					blocks_list[i-2][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i-2][3],blocks_list[i-2][4],w,h])
					blocks_list[i-2][5] = 0

			else :
					blocks_list[i][6] = blocks_list[i-2][6] 
					gameDisplay.blit(img_dict[blocks_list[i][6]] , (blocks_list[i][3],blocks_list[i][4]))
					blocks_list[i][5] = 1
					
					blocks_list[i-2][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i-2][3],blocks_list[i-2][4],w,h])
					blocks_list[i-2][5] = 0

		if blocks_list[i-3][5] == 0:
			count += 1
		else:
			if count == 0:
				
				if blocks_list[i-3][6] == blocks_list[i-2][6] and hogya != True:
					
					blocks_list[i-2][6] = blocks_list[i-2][6] * 2
					gameDisplay.blit(img_dict[blocks_list[i-2][6]] , (blocks_list[i-2][3],blocks_list[i-2][4]))
					blocks_list[i-2][5] = 1
					
					blocks_list[i-3][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i-3][3],blocks_list[i-3][4],w,h])
					blocks_list[i-3][5] = 0
					count +=1
					hogya = True
					score += blocks_list[i-2][6]

			elif count == 1 :

				if blocks_list[i-3][6] == blocks_list[i-1][6] and hogya != True:
					
					blocks_list[i-1][6] = blocks_list[i-1][6] * 2
					gameDisplay.blit(img_dict[blocks_list[i-1][6]] , (blocks_list[i-1][3],blocks_list[i-1][4]))
					blocks_list[i-1][5] = 1
					
					blocks_list[i-3][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i-3][3],blocks_list[i-3][4],w,h])
					blocks_list[i-3][5] = 0
					count +=1
					hogya = True

				else:
					blocks_list[i-2][6] = blocks_list[i-3][6] 
					gameDisplay.blit(img_dict[blocks_list[i-2][6]] , (blocks_list[i-2][3],blocks_list[i-2][4]))
					blocks_list[i-2][5] = 1
					
					blocks_list[i-3][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i-3][3],blocks_list[i-3][4],w,h])
					blocks_list[i-3][5] = 0

			elif count == 2 :

				if blocks_list[i-3][6] == blocks_list[i][6] and hogya != True:
					
					blocks_list[i][6] = blocks_list[i][6] * 2
					gameDisplay.blit(img_dict[blocks_list[i][6]] , (blocks_list[i][3],blocks_list[i][4]))
					blocks_list[i][5] = 1
					
					blocks_list[i-3][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i-3][3],blocks_list[i-3][4],w,h])
					blocks_list[i-3][5] = 0
					count +=1
					hogya = True
					score += blocks_list[i][6] 

				else:
					blocks_list[i-1][6] = blocks_list[i-3][6] 
					gameDisplay.blit(img_dict[blocks_list[i-1][6]] , (blocks_list[i-1][3],blocks_list[i-1][4]))
					blocks_list[i-1][5] = 1
					
					blocks_list[i-3][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i-3][3],blocks_list[i-3][4],w,h])
					blocks_list[i-3][5] = 0

			else :
					blocks_list[i][6] = blocks_list[i-3][6] 
					gameDisplay.blit(img_dict[blocks_list[i][6]] , (blocks_list[i][3],blocks_list[i][4]))
					blocks_list[i][5] = 1
					
					blocks_list[i-3][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i-3][3],blocks_list[i-3][4],w,h])
					blocks_list[i-3][5] = 0
	big_list.append(blocks_list)
	big_list.append(score)
	return big_list
	
def move_left(w,h,blocks_list,score,big_list):
	score = big_list[1]
	del big_list[:]
	left_most = [0,4,8,12] 
	for i in left_most:
		count = 0
		hogya = False
		if blocks_list[i][5] == 0:
			count += 1
		
		if blocks_list[i+1][5] == 0:
			count += 1
		else:
			if count == 0:
				
				if blocks_list[i][6] == blocks_list[i+1][6]:
					
					blocks_list[i][6] = blocks_list[i][6] * 2
					gameDisplay.blit(img_dict[blocks_list[i][6]] , (blocks_list[i][3],blocks_list[i][4]))
					blocks_list[i][5] = 1
					
					blocks_list[i+1][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i+1][3],blocks_list[i+1][4],w,h])
					blocks_list[i+1][5] = 0
					count +=1
					hogya = True
					score += blocks_list[i][6]
				
				
			else :
					blocks_list[i][6] = blocks_list[i+1][6] 
					gameDisplay.blit( img_dict[blocks_list[i][6]], (blocks_list[i][3],blocks_list[i][4]))
					blocks_list[i][5] = 1
					
					blocks_list[i+1][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i+1][3],blocks_list[i+1][4],w,h])
					blocks_list[i+1][5] = 0

		if blocks_list[i+2][5] == 0:
			count += 1
		else:
			if count == 0:
				
				if blocks_list[i+2][6] == blocks_list[i+1][6] and hogya != True:
					
					blocks_list[i+1][6] = blocks_list[i+1][6] * 2
					gameDisplay.blit(img_dict[blocks_list[i+1][6]] , (blocks_list[i+1][3],blocks_list[i+1][4]))
					blocks_list[i+1][5] = 1
					
					blocks_list[i+2][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i+2][3],blocks_list[i+2][4],w,h])
					blocks_list[i+2][5] = 0
					count +=1
					hogya = True
					score += blocks_list[i+1][6]
				
				
			elif count == 1 :
				if blocks_list[i+2][6] == blocks_list[i][6] and hogya != True:
					
					blocks_list[i][6] = blocks_list[i][6] * 2
					gameDisplay.blit(img_dict[blocks_list[i][6]] , (blocks_list[i][3],blocks_list[i][4]))
					blocks_list[i][5] = 1
					
					blocks_list[i+2][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i+2][3],blocks_list[i+2][4],w,h])
					blocks_list[i+2][5] = 0
					count +=1
					hogya = True
					score += blocks_list[i][6]


				else:
					blocks_list[i+1][6] = blocks_list[i+2][6] 
					gameDisplay.blit(img_dict[blocks_list[i+1][6]] , (blocks_list[i+1][3],blocks_list[i+1][4]))
					blocks_list[i+1][5] = 1
					
					blocks_list[i+2][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i+2][3],blocks_list[i+2][4],w,h])
					blocks_list[i+2][5] = 0

			else :
					blocks_list[i][6] = blocks_list[i+2][6] 
					gameDisplay.blit(img_dict[blocks_list[i][6]] , (blocks_list[i][3],blocks_list[i][4]))
					blocks_list[i][5] = 1
					
					blocks_list[i+2][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i+2][3],blocks_list[i+2][4],w,h])
					blocks_list[i+2][5] = 0

		if blocks_list[i+3][5] == 0:
			count += 1
		else:
			if count == 0:
				
				if blocks_list[i+3][6] == blocks_list[i+2][6] and hogya != True:
					
					blocks_list[i+2][6] = blocks_list[i+2][6] * 2
					gameDisplay.blit(img_dict[blocks_list[i+2][6]] , (blocks_list[i+2][3],blocks_list[i+2][4]))
					blocks_list[i+2][5] = 1
					
					blocks_list[i+3][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i+3][3],blocks_list[i+3][4],w,h])
					blocks_list[i+3][5] = 0
					count +=1
					hogya = True
					score += blocks_list[i+2][6]

			elif count == 1 :

				if blocks_list[i+3][6] == blocks_list[i+1][6] and hogya != True:
					
					blocks_list[i+1][6] = blocks_list[i+1][6] * 2
					gameDisplay.blit(img_dict[blocks_list[i+1][6]] , (blocks_list[i+1][3],blocks_list[i+1][4]))
					blocks_list[i+1][5] = 1
					
					blocks_list[i+3][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i+3][3],blocks_list[i+3][4],w,h])
					blocks_list[i+3][5] = 0
					count +=1
					hogya = True
					score += blocks_list[i+1][6]

				else:
					blocks_list[i+2][6] = blocks_list[i+3][6] 
					gameDisplay.blit(img_dict[blocks_list[i+2][6]] , (blocks_list[i+2][3],blocks_list[i+2][4]))
					blocks_list[i+2][5] = 1
					
					blocks_list[i+3][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i+3][3],blocks_list[i+3][4],w,h])
					blocks_list[i+3][5] = 0

			elif count == 2 :

				if blocks_list[i+3][6] == blocks_list[i][6] and hogya != True:
					
					blocks_list[i][6] = blocks_list[i][6] * 2
					gameDisplay.blit(img_dict[blocks_list[i][6]] , (blocks_list[i][3],blocks_list[i][4]))
					blocks_list[i][5] = 1
					
					blocks_list[i+3][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i+3][3],blocks_list[i+3][4],w,h])
					blocks_list[i+3][5] = 0
					count +=1
					hogya = True
					score += blocks_list[i][6]

				else:
					blocks_list[i+1][6] = blocks_list[i+3][6] 
					gameDisplay.blit(img_dict[blocks_list[i+1][6]] , (blocks_list[i+1][3],blocks_list[i+1][4]))
					blocks_list[i+1][5] = 1
					
					blocks_list[i+3][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i+3][3],blocks_list[i+3][4],w,h])
					blocks_list[i+3][5] = 0

			else :
					blocks_list[i][6] = blocks_list[i+3][6] 
					gameDisplay.blit(img_dict[blocks_list[i][6]] , (blocks_list[i][3],blocks_list[i][4]))
					blocks_list[i][5] = 1
					
					blocks_list[i+3][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i+3][3],blocks_list[i+3][4],w,h])
					blocks_list[i+3][5] = 0
	big_list.append(blocks_list)
	big_list.append(score)
	return big_list

def move_up(w,h,blocks_list,score,big_list):
	score = big_list[1]
	del big_list[:]
	left_most = [0,4,8,12]
	top_most = [0,1,2,3] 
	for i in top_most:
		count = 0
		hogya = False
		if blocks_list[i][5] == 0:
			count += 1
		
		if blocks_list[i+4][5] == 0:
			count += 1
		else:
			if count == 0:
				
				if blocks_list[i][6] == blocks_list[i+4][6]:
					
					blocks_list[i][6] = blocks_list[i][6] * 2
					gameDisplay.blit(img_dict[blocks_list[i][6]] , (blocks_list[i][3],blocks_list[i][4]))
					blocks_list[i][5] = 1
					
					blocks_list[i+4][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i+4][3],blocks_list[i+4][4],w,h])
					blocks_list[i+4][5] = 0
					count +=1
					hogya = True
					score += blocks_list[i][6]
				
			else :
					blocks_list[i][6] = blocks_list[i+4][6] 
					gameDisplay.blit( img_dict[blocks_list[i][6]], (blocks_list[i][3],blocks_list[i][4]))
					blocks_list[i][5] = 1
					
					blocks_list[i+4][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i+4][3],blocks_list[i+4][4],w,h])
					blocks_list[i+4][5] = 0

		if blocks_list[i+8][5] == 0:
			count += 1
		else:
			if count == 0:
				
				if blocks_list[i+8][6] == blocks_list[i+4][6] and hogya != True:
					
					blocks_list[i+4][6] = blocks_list[i+4][6] * 2
					gameDisplay.blit(img_dict[blocks_list[i+4][6]] , (blocks_list[i+4][3],blocks_list[i+4][4]))
					blocks_list[i+4][5] = 1
					
					blocks_list[i+8][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i+8][3],blocks_list[i+8][4],w,h])
					blocks_list[i+8][5] = 0
					count +=1
					hogya = True
					score += blocks_list[i+4][6]
				
			elif count == 1 :
				if blocks_list[i+8][6] == blocks_list[i][6] and hogya != True:
					
					blocks_list[i][6] = blocks_list[i][6] * 2
					gameDisplay.blit(img_dict[blocks_list[i][6]] , (blocks_list[i][3],blocks_list[i][4]))
					blocks_list[i][5] = 1
					
					blocks_list[i+8][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i+8][3],blocks_list[i+8][4],w,h])
					blocks_list[i+8][5] = 0
					count +=1
					hogya = True
					score += blocks_list[i][6]


				else:
					blocks_list[i+4][6] = blocks_list[i+8][6] 
					gameDisplay.blit(img_dict[blocks_list[i+4][6]] , (blocks_list[i+4][3],blocks_list[i+4][4]))
					blocks_list[i+4][5] = 1
					
					blocks_list[i+8][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i+8][3],blocks_list[i+8][4],w,h])
					blocks_list[i+8][5] = 0

			else :
					blocks_list[i][6] = blocks_list[i+8][6] 
					gameDisplay.blit(img_dict[blocks_list[i][6]] , (blocks_list[i][3],blocks_list[i][4]))
					blocks_list[i][5] = 1
					
					blocks_list[i+8][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i+8][3],blocks_list[i+8][4],w,h])
					blocks_list[i+8][5] = 0

		if blocks_list[i+12][5] == 0:
			count += 1
		else:
			if count == 0:
				
				if blocks_list[i+12][6] == blocks_list[i+8][6] and hogya != True:
					
					blocks_list[i+8][6] = blocks_list[i+8][6] * 2
					gameDisplay.blit(img_dict[blocks_list[i+8][6]] , (blocks_list[i+8][3],blocks_list[i+8][4]))
					blocks_list[i+8][5] = 1
					
					blocks_list[i+12][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i+12][3],blocks_list[i+12][4],w,h])
					blocks_list[i+12][5] = 0
					count +=1
					hogya = True
					score += blocks_list[i+8][6]

			elif count == 1 :

				if blocks_list[i+12][6] == blocks_list[i+4][6] and hogya != True:
					
					blocks_list[i+4][6] = blocks_list[i+4][6] * 2
					gameDisplay.blit(img_dict[blocks_list[i+4][6]] , (blocks_list[i+4][3],blocks_list[i+4][4]))
					blocks_list[i+4][5] = 1
					
					blocks_list[i+12][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i+12][3],blocks_list[i+12][4],w,h])
					blocks_list[i+12][5] = 0
					count +=1
					hogya = True
					score += blocks_list[i+4][6]

				else:
					blocks_list[i+8][6] = blocks_list[i+12][6] 
					gameDisplay.blit(img_dict[blocks_list[i+8][6]] , (blocks_list[i+8][3],blocks_list[i+8][4]))
					blocks_list[i+8][5] = 1
					
					blocks_list[i+12][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i+12][3],blocks_list[i+12][4],w,h])
					blocks_list[i+12][5] = 0

			elif count == 2 :

				if blocks_list[i+12][6] == blocks_list[i][6] and hogya != True:
					
					blocks_list[i][6] = blocks_list[i][6] * 2
					gameDisplay.blit(img_dict[blocks_list[i][6]] , (blocks_list[i][3],blocks_list[i][4]))
					blocks_list[i][5] = 1
					
					blocks_list[i+12][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i+12][3],blocks_list[i+12][4],w,h])
					blocks_list[i+12][5] = 0
					count +=1
					hogya = True
					score += blocks_list[i][6]

				else:
					blocks_list[i+4][6] = blocks_list[i+12][6] 
					gameDisplay.blit(img_dict[blocks_list[i+4][6]] , (blocks_list[i+4][3],blocks_list[i+4][4]))
					blocks_list[i+4][5] = 1
					
					blocks_list[i+12][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i+12][3],blocks_list[i+12][4],w,h])
					blocks_list[i+12][5] = 0

			else :
					blocks_list[i][6] = blocks_list[i+12][6] 
					gameDisplay.blit(img_dict[blocks_list[i][6]] , (blocks_list[i][3],blocks_list[i][4]))
					blocks_list[i][5] = 1
					
					blocks_list[i+12][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i+12][3],blocks_list[i+12][4],w,h])
					blocks_list[i+12][5] = 0
	big_list.append(blocks_list)
	big_list.append(score)
	return big_list

def move_down(w,h,blocks_list,score,big_list):
	score = big_list[1]
	del big_list[:]
	bottom_most = [12,13,14,15] 
	for i in bottom_most:
		count = 0
		hogya = False
		if blocks_list[i][5] == 0:
			count += 1
		
		if blocks_list[i-4][5] == 0:
			count += 1
		else:
			if count == 0:
				
				if blocks_list[i][6] == blocks_list[i-4][6]:
					
					blocks_list[i][6] = blocks_list[i][6] * 2
					gameDisplay.blit(img_dict[blocks_list[i][6]] , (blocks_list[i][3],blocks_list[i][4]))
					blocks_list[i][5] = 1
					
					blocks_list[i-4][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i-4][3],blocks_list[i-4][4],w,h])
					blocks_list[i-4][5] = 0
					count +=1
					hogya = True
					score += blocks_list[i][6]
				
				
			else :
					blocks_list[i][6] = blocks_list[i-4][6] 
					gameDisplay.blit( img_dict[blocks_list[i][6]], (blocks_list[i][3],blocks_list[i][4]))
					blocks_list[i][5] = 1
					
					blocks_list[i-4][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i-4][3],blocks_list[i-4][4],w,h])
					blocks_list[i-4][5] = 0

		if blocks_list[i-8][5] == 0:
			count += 1
		else:
			if count == 0:
				
				if blocks_list[i-8][6] == blocks_list[i-4][6] and hogya != True:
					
					blocks_list[i-4][6] = blocks_list[i-4][6] * 2
					gameDisplay.blit(img_dict[blocks_list[i-4][6]] , (blocks_list[i-4][3],blocks_list[i-4][4]))
					blocks_list[i-4][5] = 1
					
					blocks_list[i-8][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i-8][3],blocks_list[i-8][4],w,h])
					blocks_list[i-8][5] = 0
					count +=1
					hogya = True
					score += blocks_list[i-4][6]
				
				
			elif count == 1 :
				if blocks_list[i-8][6] == blocks_list[i][6] and hogya != True:
					
					blocks_list[i][6] = blocks_list[i][6] * 2
					gameDisplay.blit(img_dict[blocks_list[i][6]] , (blocks_list[i][3],blocks_list[i][4]))
					blocks_list[i][5] = 1
					
					blocks_list[i-8][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i-8][3],blocks_list[i-8][4],w,h])
					blocks_list[i-8][5] = 0
					count +=1
					hogya = True
					score += blocks_list[i][6]


				else:
					blocks_list[i-4][6] = blocks_list[i-8][6] 
					gameDisplay.blit(img_dict[blocks_list[i-4][6]] , (blocks_list[i-4][3],blocks_list[i-4][4]))
					blocks_list[i-4][5] = 1
					
					blocks_list[i-8][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i-8][3],blocks_list[i-8][4],w,h])
					blocks_list[i-8][5] = 0

			else :
					blocks_list[i][6] = blocks_list[i-8][6] 
					gameDisplay.blit(img_dict[blocks_list[i][6]] , (blocks_list[i][3],blocks_list[i][4]))
					blocks_list[i][5] = 1
					
					blocks_list[i-8][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i-8][3],blocks_list[i-8][4],w,h])
					blocks_list[i-8][5] = 0

		if blocks_list[i-12][5] == 0:
			count += 1
		else:
			if count == 0:
				
				if blocks_list[i-12][6] == blocks_list[i-8][6] and hogya != True:
					
					blocks_list[i-8][6] = blocks_list[i-8][6] * 2
					gameDisplay.blit(img_dict[blocks_list[i-8][6]] , (blocks_list[i-8][3],blocks_list[i-8][4]))
					blocks_list[i-8][5] = 1
					
					blocks_list[i-12][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i-12][3],blocks_list[i-12][4],w,h])
					blocks_list[i-12][5] = 0
					count +=1
					hogya = True
					score += blocks_list[i-8][6]

			elif count == 1 :

				if blocks_list[i-12][6] == blocks_list[i-4][6] and hogya != True:
					
					blocks_list[i-4][6] = blocks_list[i-4][6] * 2
					gameDisplay.blit(img_dict[blocks_list[i-4][6]] , (blocks_list[i-4][3],blocks_list[i-4][4]))
					blocks_list[i-4][5] = 1
					
					blocks_list[i-12][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i-12][3],blocks_list[i-12][4],w,h])
					blocks_list[i-12][5] = 0
					count +=1
					hogya = True
					score += blocks_list[i-4][6]

				else:
					blocks_list[i-8][6] = blocks_list[i-12][6] 
					gameDisplay.blit(img_dict[blocks_list[i-8][6]] , (blocks_list[i-8][3],blocks_list[i-8][4]))
					blocks_list[i-8][5] = 1
					
					blocks_list[i-12][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i-12][3],blocks_list[i-12][4],w,h])
					blocks_list[i-12][5] = 0

			elif count == 2 :

				if blocks_list[i-12][6] == blocks_list[i][6] and hogya != True:
					
					blocks_list[i][6] = blocks_list[i][6] * 2
					gameDisplay.blit(img_dict[blocks_list[i][6]] , (blocks_list[i][3],blocks_list[i][4]))
					blocks_list[i][5] = 1
					
					blocks_list[i-12][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i-12][3],blocks_list[i-12][4],w,h])
					blocks_list[i-12][5] = 0
					count +=1
					hogya = True
					score += blocks_list[i][6]

				else:
					blocks_list[i-4][6] = blocks_list[i-12][6] 
					gameDisplay.blit(img_dict[blocks_list[i-4][6]] , (blocks_list[i-4][3],blocks_list[i-4][4]))
					blocks_list[i-4][5] = 1
					
					blocks_list[i-12][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i-12][3],blocks_list[i-12][4],w,h])
					blocks_list[i-12][5] = 0

			else :
					blocks_list[i][6] = blocks_list[i-12][6] 
					gameDisplay.blit(img_dict[blocks_list[i][6]] , (blocks_list[i][3],blocks_list[i][4]))
					blocks_list[i][5] = 1
					
					blocks_list[i-12][6] = 0
					pygame.draw.rect(gameDisplay,grey,[blocks_list[i-12][3],blocks_list[i-12][4],w,h])
					blocks_list[i-12][5] = 0
	big_list.append(blocks_list)
	big_list.append(score)
	return big_list

def game_over(big_list):
	a = True
	for i in big_list[0]:
		if i[5] !=1:
			a = False
	if a == True:
		pygame.draw.rect(gameDisplay,black,[0,0,screen_width,screen_height])
		screen_text = font.render("Game Over",True,white)
		gameDisplay.blit(screen_text,[(screen_width/2)-70,screen_height/2])
		message_to_screen("score : "+str(big_list[1]),grey)
		pygame.display.update()
		time.sleep(2)
		exit()

def win(big_list):
	for i in big_list[0]:
		if i[6] == 2048:
			pygame.draw.rect(gameDisplay,black,[0,0,screen_width,screen_height])
			screen_text = font.render("U win !!!",True,white)
			gameDisplay.blit(screen_text,[(screen_width/2)-70,screen_height/2])
			message_to_screen("score : "+str(big_list[1]),grey)
			pygame.display.update()
			time.sleep(2)
			exit()

def starting_screen():
	pygame.draw.rect(gameDisplay,red,[0,0,screen_width/2,screen_height/2])
	pygame.draw.rect(gameDisplay,purple,[screen_width/2,0,screen_width/2,screen_height/2])
	pygame.draw.rect(gameDisplay,purple,[0,screen_height/2,screen_width,screen_height/2])
	pygame.draw.rect(gameDisplay,red,[screen_width/2,screen_height/2,screen_width/2,screen_height/2])

	screen_text = big_font.render("2 0 4 8",True,white)
	gameDisplay.blit(screen_text,[(screen_width/2)-110,screen_height/2-80])
	
	screen_text = small_font.render("(c) k_studios",True,white)
	gameDisplay.blit(screen_text,[(screen_width/2)-90,screen_height/2+80])

	pygame.display.update()
	pygame.mixer.Sound.play(start_sound)
	time.sleep(4)

def game_loop(x,y,w,h,m,blocks_list,score,big_list):

	starting_screen()
	pygame.draw.rect(gameDisplay,black,[0,0,screen_width,screen_height])
	
	draw_blank_box(x,y,w,h,m)
	make_block_list(x,y,blocks_list)
	big_list.append(blocks_list)
	big_list.append(score)
	game_exit = False

	random_block = random.randrange(0,16)
	gameDisplay.blit(img_dict[2],(blocks_list[random_block][3],blocks_list[random_block][4]))
	blocks_list[random_block][5] = 1
	blocks_list[random_block][6] = 2
	pygame.display.update()
	
	while not game_exit:

		sltcr = random.randrange(1,2)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_exit = True
			if event.type == pygame.KEYDOWN:
				pygame.mixer.Sound.play(blocks_sound)
				if event.key == pygame.K_RIGHT:
					move_right(w,h,big_list[0],score,big_list)
					while(1):
						random_block = random.randrange(0,16)
						if blocks_list[random_block][5] == 0:
							if sltcr == 1:
								gameDisplay.blit(img_dict[2],(blocks_list[random_block][3],blocks_list[random_block][4]))
								blocks_list[random_block][5] = 1
								blocks_list[random_block][6] = 2
							else:
								gameDisplay.blit(img_dict[4],(blocks_list[random_block][3],blocks_list[random_block][4]))
								blocks_list[random_block][5] = 1
								blocks_list[random_block][6] = 4
							break
					
				elif event.key == pygame.K_LEFT:
					move_left(w,h,big_list[0],score,big_list)
					while(1):
						random_block = random.randrange(0,16)
						if blocks_list[random_block][5] == 0:
							if sltcr == 1:
								gameDisplay.blit(img_dict[2],(blocks_list[random_block][3],blocks_list[random_block][4]))
								blocks_list[random_block][5] = 1
								blocks_list[random_block][6] = 2
							else:
								gameDisplay.blit(img_dict[4],(blocks_list[random_block][3],blocks_list[random_block][4]))
								blocks_list[random_block][5] = 1
								blocks_list[random_block][6] = 4
							break
				
				elif event.key == pygame.K_UP:
					move_up(w,h,big_list[0],score,big_list)
					while(1):
						random_block = random.randrange(0,16)
						if blocks_list[random_block][5] == 0:
							if sltcr == 1:
								gameDisplay.blit(img_dict[2],(blocks_list[random_block][3],blocks_list[random_block][4]))
								blocks_list[random_block][5] = 1
								blocks_list[random_block][6] = 2
							else:
								gameDisplay.blit(img_dict[4],(blocks_list[random_block][3],blocks_list[random_block][4]))
								blocks_list[random_block][5] = 1
								blocks_list[random_block][6] = 4
							break
				elif event.key == pygame.K_DOWN:
					move_down(w,h,big_list[0],score,big_list)
					while(1):
						random_block = random.randrange(0,16)
						if blocks_list[random_block][5] == 0:
							if sltcr == 1:
								gameDisplay.blit(img_dict[2],(blocks_list[random_block][3],blocks_list[random_block][4]))
								blocks_list[random_block][5] = 1
								blocks_list[random_block][6] = 2
							else:
								gameDisplay.blit(img_dict[4],(blocks_list[random_block][3],blocks_list[random_block][4]))
								blocks_list[random_block][5] = 1
								blocks_list[random_block][6] = 4
							break
				
				game_over(big_list)	
		 
		pygame.draw.rect(gameDisplay,black,[0,230,240,40])
		message_to_screen("score : "+str(big_list[1]),grey)
		win(big_list)
		pygame.display.update()
		#time.sleep(1)
		

game_loop(x,y,w,h,m,blocks_list,score,big_list)