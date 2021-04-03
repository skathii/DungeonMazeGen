import random
import sys
from colorama import Fore, Back, Style, init

placeholder = '%'
path = 'O'
wall = 'X'

def maze_shell(height, width, maxlength, tunnelcount, colour):
		maze = []

		## Limitations on Height, Width.
		if width <= 3 or height <=3:
				sys.exit("Error: Please provide Width and Height values that are greater or equal to 4.")
				
		## Limitations on Maxlength and TunnelCount.    
		if tunnelcount < 1 or maxlength < 1:
				sys.exit("Error: You have specified a null or negative value for maxlength or tunnelcount.")
		
		## Creating a nested list with the dimensions specified by the function. Insert Placeholder value in to fill up.
		for i in range(height):
				row = []
				for j in range(width):
						row.append(wall)
				maze.append(row)

		## Generate a Random Co-ordinate in the nested list where the maze will begin. We give the generated co-ordinate the Path value.
		start_width = int(random.random() * width)
		start_height = int(random.random() * height)
		maze[start_height][start_width] = path
		home_cell = [start_height, start_width]
		
		## Create Next_Cell List: This will store potential routes from the home_cell:
		next_cells = []
		
		while tunnelcount > 0:
				
				## Path travelling North, West, East and South respectively. This is to ensure that potential routes do not start over the borders of the nested list.
				if not home_cell[0] == 0:
						next_cells.append([home_cell[0] - 1, home_cell[1]])

				if not home_cell[1] == 0:
						next_cells.append([home_cell[0], home_cell[1] - 1])

				if not home_cell[1] + 1 == width:
						next_cells.append([home_cell[0], home_cell[1] + 1])

				if not home_cell[0] + 1 == height:
						next_cells.append([home_cell[0] + 1, home_cell[1]])
						
				rand_length = int((random.random()*maxlength))+1
				rand_cell = int(random.random()*len(next_cells))
				next_cell = next_cells[rand_cell]

				direction = [home_cell[0] - next_cell[0], home_cell[1] - next_cell[1]]
				
				#North
				if direction[0] == 1 and direction[1] == 0:
						if home_cell[0] < rand_length:
								magnitude = home_cell[0]
						else:
								magnitude = rand_length
								
						for i in range(1, magnitude + 1):
								maze[home_cell[0] - i][home_cell[1]] = path
						
						home_cell = [home_cell[0] - magnitude, home_cell[1]]
				
				#East
				if direction[0] == 0 and direction[1] == -1:
						if width - 1 - home_cell[1] < rand_length:
								magnitude = width - 1 - home_cell[1]
						else:
								magnitude = rand_length
								
						for i in range(1, magnitude + 1):
								maze[home_cell[0]][home_cell[1] + i] = path
						
						home_cell = [home_cell[0], home_cell[1] + magnitude]
				
				#South
				if direction[0] == -1 and direction[1] == 0:
						if height - 1 - home_cell[0] < rand_length:
								magnitude = height - 1 - home_cell[0]
						else:
								magnitude = rand_length
								
						for i in range(1, magnitude + 1):
								maze[home_cell[0] + i][home_cell[1]] = path
						
						home_cell = [home_cell[0] + magnitude, home_cell[1]]
						
				#West
				if direction[0] == 0 and direction[1] == 1:
						if home_cell[1] < rand_length:
								magnitude = home_cell[1]
						else:
								magnitude = rand_length
						
						for i in range(1, magnitude + 1):
								maze[home_cell[0]][home_cell[1] - i] = path
						
						home_cell = [home_cell[0], home_cell[1] - magnitude]
						
				next_cells.clear()
				tunnelcount -= 1
				
		return maze

def print_maze(maze, colour):
		for x in range(len(maze)):
				for y in range(len(maze[0])):
						if maze[x][y] == 'X':
							if colour == True:
								print(Back.RED, f'{maze[x][y]}', end="")
							else:
								print(f'{maze[x][y]}', end="")

						elif maze[x][y] == 'O':
							if colour == True:
								print(Back.GREEN, f'{maze[x][y]}', end="")
							else:
								print(f'{maze[x][y]}', end="")

						elif maze[x][y] == '%':
							if colour == True:
									print(Back.WHITE, f'{maze[x][y]}', end="")
							else:
								print(f'{maze[x][y]}', end="")
						
				print('\n')

def create_maze(height, width, maxlength, tunnelcount, colour):
		maze = maze_shell(height, width, maxlength, tunnelcount, colour)
		print_maze(maze, colour)
