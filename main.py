import pygame
import time

pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.mouse.set_visible(False)

FPS = 300
G = (0,255,0)
ts = time.time()
mouse = (0,0)
cursor_trail = []

def render():
	global cursor_trail
	if ts + 1/FPS > time.time():
		return

	screen.fill((0,0,0))

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
			pygame.draw.aaline(screen, G, p, q)
			q = [0, 0]
			q[0] = p[0] - trail_size * norm[0] - trail_size * perp[0]
			q[1] = p[1] - trail_size * norm[1] - trail_size * perp[1]
			pygame.draw.aaline(screen, G, p, q)

	pygame.draw.rect(screen, G, (mouse[0],mouse[1],3,3))
	
	pygame.display.flip()


while True:
	e = pygame.event.wait(30) # 30 ms
	if e.type == pygame.QUIT:
		break
	elif e.type == pygame.MOUSEMOTION:
		mouse = e.pos
		cursor_trail.append((mouse,time.time()))
	render()
