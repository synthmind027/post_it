import pygame
import time

pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.mouse.set_visible(False)

FPS = 300
C = (0,255,255)
G = (0,255,0)
ts = time.time()
mouse = (0,0)
cursor_trail = []



while True:


	e = pygame.event.wait(30) # timeout 30 ms
	
	if e.type == pygame.QUIT:
		break
	
	elif e.type == pygame.MOUSEMOTION:
		mouse = e.pos
		cursor_trail.append((mouse,time.time()))
	
	elif e.type == pygame.MOUSEBUTTONDOWN:
		print('dn')
		e.pos

	elif e.type == pygame.MOUSEBUTTONUP:
		print('up')
		e.pos

	elif e.type == pygame.KEYDOWN:
		if e.unicode != '':
			if e.scancode == 1:
				print('ESC')
			if e.scancode == 40:
				print('enter')
			elif e.scancode == 42:
				print('backspace')
			# 43 as tab
			# 44 as space
			print(e.unicode, ord(e.unicode), e.scancode)






	# render
	if ts + 1/FPS > time.time():
		continue

	# Draw background
	screen.fill((0,0,0))





	# Draw cursor trail

	trail_thre = 10
	trail_spacing = 10
	trail_size = 3.5
	trail_remain = 1/30
	cursor_trail_trim_idx = 0
	for i in range(len(cursor_trail)):
		if cursor_trail[i][1] + trail_remain < time.time():
			cursor_trail_trim_idx = i + 1
	cursor_trail = cursor_trail[cursor_trail_trim_idx:]
	for i in range(len(cursor_trail)-1):
		a = cursor_trail[i][0]
		b = cursor_trail[i+1][0]
		d = ( (b[0]-a[0])**2 + (b[1]-a[1])**2 ) ** 0.5
		if d < trail_thre:
			continue
		n = int( d / trail_spacing ) + 2
		norm = [0,0]
		norm[0] = (b[0] - a[0]) / d
		norm[1] = (b[1] - a[1]) / d
		perp = [-norm[1],norm[0]]
		for i in range(1, n):
			p = [0, 0]
			p[0] = a[0] * (i/n) + b[0] * (1-i/n)
			p[1] = a[1] * (i/n) + b[1] * (1-i/n)
			q = [0, 0]
			q[0] = p[0] - trail_size * norm[0] + trail_size * perp[0]
			q[1] = p[1] - trail_size * norm[1] + trail_size * perp[1]
			pygame.draw.aaline(screen, C, p, q)
			q = [0, 0]
			q[0] = p[0] - trail_size * norm[0] - trail_size * perp[0]
			q[1] = p[1] - trail_size * norm[1] - trail_size * perp[1]
			pygame.draw.aaline(screen, C, p, q)





	# Draw cursor

	pygame.draw.rect(screen, C, (mouse[0],mouse[1],3,3))
	


	pygame.display.flip()
