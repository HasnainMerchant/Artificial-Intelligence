# Best-First Search Approach
# 1. 8-Puzzle Problem
# 2. Robot Navigation
# 3. City-Distance Problem

from copy import deepcopy
from colorama import Fore, Back, Style, init
from queue import PriorityQueue
init(strip=False)
init(autoreset=True)

class Puzzle():
    # Goal Configuration Of Board
    goal = [[1, 2, 3],
            [8, 0, 4],
            [7, 6, 5]]

    # Board Config
    board_config = [[2, 3, 4],
                    [1, 8, 0],
                    [7, 6, 5]]

    # Heuristic Value Of Tiles In Place
    def calculate_fOfn(self, cal_config):
        # In BFS f(n) = h(n)
        # h(n) = Number Of Misplaced Tiles
        h = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if cal_config[i][j] != self.goal[i][j]:
                    h += 1
        return h

    def isSafe(self, x, y):
        return x >= 0 and x < 3 and y >= 0 and y < 3

    def print_board(self, print_config):
        for i in range(0, 3):
            for j in range(0, 3):
                print(" " + str(print_config[i][j]) + " ", end="")
            print()

    # Function To Find All Possible Board Configurations From Given Configurations
    def find_all_configs(self, all_config):
        config_boards = []
        config1 = deepcopy(all_config)
        config2 = deepcopy(all_config)
        config3 = deepcopy(all_config)
        config4 = deepcopy(all_config)

        for i in range(0, 3):
            for j in range(0, 3):
                if all_config[i][j] != 0:
                    # Check If We Can Move To The Top
                    if self.isSafe(i - 1, j):
                        if all_config[i - 1][j] == 0:
                            # Move Tile
                            config1[i - 1][j] = config1[i][j]
                            config1[i][j] = 0
                            config_boards.append(config1)

                    # Check If We Can Move To The Bottom
                    if self.isSafe(i + 1, j):
                        if all_config[i + 1][j] == 0:
                            # Move Tile
                            config2[i + 1][j] = config2[i][j]
                            config2[i][j] = 0
                            config_boards.append(config2)

                    # Check If We Can Move To The Right
                    if self.isSafe(i, j + 1):
                        if all_config[i][j + 1] == 0:
                            config3[i][j + 1] = config3[i][j]
                            config3[i][j] = 0
                            config_boards.append(config3)

                    # Check If We Can Move To The Left
                    if self.isSafe(i, j - 1):
                        if all_config[i][j - 1] == 0:
                            config4[i][j - 1] = config4[i][j]
                            config4[i][j] = 0
                            config_boards.append(config4)
        return config_boards

    def print_list(self, list):
        for j in range(3):
            for i in range(len(list)):
                print(str(list[i][j]) + '\t')

    # Hill Climbing Algorithm Function
    def puzzle_start(self, config, goal_heuristic):
        objective_values = []
        new_config = deepcopy(config)
        boards_configs = []
        open_list = []
        closed_list = []
        visited = []

        open_list.append(new_config)
        visited.append(new_config)
        print(Fore.RED + "\t\t\tLIST IS DISPLAYED IN ROW MAJOR ORDER\n\n")
        print("Initially - ")
        # Print Open List
        print("Open List - ")
        print(open_list)
        print()
        # Print Closed List
        print("Closed List - ")
        print(closed_list)
        print("\n\n")

        while True:
            boards_configs.clear()
            open_list.remove(new_config)
            closed_list.append(new_config)
            # Calculate Heuristic Value Of New Board Configurations
            heuristic_value = self.calculate_fOfn(new_config)
            if heuristic_value == goal_heuristic:
                print("Solution Reached !!")
                break
            boards_configs = self.find_all_configs(new_config)
            # Calculating Heuristic Values For All Child Configurations
            for i in boards_configs:
                visited.append(i)
                open_list.append(i)
                h = self.calculate_fOfn(i)
                objective_values.append(h)
            print("Open List - ")
            print(open_list)
            print("Closed List - ")
            print(closed_list)
            print("\n\n")

            # Selecting Maximum Heuristic Value From Child Nodes
            min_value = min(objective_values)
            min_value_index = objective_values.index(min_value)
            new_config = boards_configs[min_value_index]
            print("Board Configuration Selected With Heuristic Value - " + str(min_value))
            self.print_board(new_config)
            print("\n")
            objective_values.clear()

    def Start_Puzzle(self):
        print("8-Puzzle Problem Using Best First Search\n")
        goal_heuristic = self.calculate_fOfn(self.goal)
        self.puzzle_start(self.board_config, goal_heuristic)

class Robot():
    nav_map = [
          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
          ['-', Fore.BLACK+'#', '-', '-', '-', Fore.BLACK+'#', Fore.BLACK+'#', Fore.BLACK+'#', Fore.BLACK+'#', Fore.BLACK+'#', '-'],
          ['-', Fore.BLACK+'#', Fore.BLACK+'#', '-', '-', '-', Fore.GREEN+'G', '-', '-', Fore.BLACK+'#', '-'],
          [Fore.RED+'S', '-', Fore.BLACK+'#', Fore.BLACK+'#', Fore.BLACK+'#', Fore.BLACK+'#', Fore.BLACK+'#', Fore.BLACK+'#', Fore.BLACK+'#', Fore.BLACK+'#', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ]

    #Start Position
    startx = 0
    starty = 3

    #Goal Position
    goalx = 6
    goaly = 2

    visited = []
    queue = []
    new_nav_map = deepcopy(nav_map)

    # NAV_MAP [Y][X]
    def calManDist(self):
        for y in range(5):
            for x in range(11):
                if self.nav_map[y][x] != Fore.BLACK+'#':
                    self.new_nav_map[y][x] = abs(self.goalx - x) + abs(self.goaly - y)
        position = [self.startx, self.starty]
        self.queue.append((self.new_nav_map[self.starty][self.startx], position))

    def isSafe(self, x, y):
        return x > -1 and x < 11 and y > -1 and y < 5

    def calPossibleMoves(self):

        x = self.startx
        y = self.starty

        if self.isSafe(x+1, y) == True:
            position = [x+1, y]
            if self.new_nav_map[y][x+1] != Fore.BLACK+'#' and ((self.new_nav_map[y][x+1], position)) not in self.visited:
                self.queue.append((self.new_nav_map[y][x+1], position))

        if self.isSafe(x-1, y) == True:
            position = [x - 1, y]
            if self.new_nav_map[y][x-1] != Fore.BLACK+'#' and ((self.new_nav_map[y][x-1], position)) not in self.visited:
                self.queue.append((self.new_nav_map[y][x-1], position))

        if self.isSafe(x, y+1) == True:
            position = [x, y + 1]
            if self.new_nav_map[y+1][x] != Fore.BLACK+'#' and ((self.new_nav_map[y+1][x], position)) not in self.visited:
                self.queue.append((self.new_nav_map[y+1][x], position))

        if self.isSafe(x, y-1) == True:
            position = [x, y - 1]
            if self.new_nav_map[y-1][x] != Fore.BLACK+'#' and ((self.new_nav_map[y-1][x], position)) not in self.visited:
                self.queue.append((self.new_nav_map[y-1][x], position))

        self.queue.sort(reverse=True)

    def Start_Navigation(self):
        print("Initial Map - ")
        self.print_map(self.nav_map)
        print("\n\n\n")
        self.calManDist()
        print("After Calculating Manhanttan Distance - ")
        self.print_map(self.new_nav_map)
        print("\n\n\n")

        while (self.queue):
            input()
            next = self.queue.pop()
            print("Selecting Next Position : X = " + str(next[1][0]) + " , Y = " + str(next[1][1]))
            print("Heuristic Value = " + str(next[0]))
            print()
            if next[1][0] == self.goalx and next[1][1] == self.goaly:
                print(f"Goal State Reached")
                exit(1)
            if next[1] == [self.startx, self.starty]:
                self.nav_map[next[1][1]][next[1][0]] = Fore.BLUE+'S'
            else:
                self.nav_map[next[1][1]][next[1][0]] = Fore.BLUE+str(self.new_nav_map[next[1][1]][next[1][0]])
            self.visited.append(next)
            self.startx = next[1][0]
            self.starty = next[1][1]
            self.calPossibleMoves()
            self.print_map(self.nav_map)
            print('-----------------------------------------------------------------------------------------')

    def print_map(self, map):
        for i in range(5):
            for j in range(11):
                print(Fore.WHITE+str(map[i][j]), end='\t\t')
            print("\n")


class City_Distance():
    class Graph:
        def __init__(self, graph_dict=None, directed=True):
            self.graph_dict = graph_dict or {}
            self.directed = directed
            if not directed:
                self.make_undirected()

        # Create An Undirected Graph By Adding Symmetric Edges
        def make_undirected(self):
            for a in list(self.graph_dict.keys()):
                for (b, dist) in self.graph_dict[a].items():
                    self.graph_dict.setdefault(b, {})[a] = dist

        # Add a link from A and B of given distance, and also add the inverse link if the graph is undirected
        def connect(self, A, B, distance=1):
            self.graph_dict.setdefault(A, {})[B] = distance
            if not self.directed:
                self.graph_dict.setdefault(B, {})[A] = distance

        # Get Neighbors Or A Neighbor
        def get(self, a, b=None):
            links = self.graph_dict.setdefault(a, {})
            if b is None:
                return links
            else:
                return links.get(b)

        # Return A List Of Nodes In The Graph
        def nodes(self):
            s1 = set([k for k in self.graph_dict.keys()])
            s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
            nodes = s1.union(s2)
            return list(nodes)

        # Display Graph
        def display_graph(self):
            print(Fore.YELLOW+"\n\t\t\tTHE GRAPH IS - \n")
            for key in self.graph_dict:
                print(Fore.CYAN+key, Fore.WHITE+' -> ', self.graph_dict[key])

    # This class represent a node
    class Node:
        # Initialize the class
        def __init__(self, name: str, parent: str):
            self.name = name
            self.parent = parent
            self.g = 0  # Distance from start node
            self.h = 0  # Distance to goal node
            self.f = 0  # Total cost

        # Compare nodes
        def __eq__(self, other):
            return self.name == other.name

        # Sort nodes
        def __lt__(self, other):
            return self.f < other.f

        # Print node
        def __repr__(self):
            return ('({0},{1})'.format(self.position, self.f))

    # Best-first search
    def best_first_search(self, graph, heuristics, start, end):

        # Create lists for open nodes and closed nodes
        open = []
        closed = []

        # Create a start node and an goal node
        start_node = self.Node(start, None)
        goal_node = self.Node(end, None)

        # Add the start node
        open.append(start_node)

        # Loop until the open list is empty
        while len(open) > 0:
            print(Fore.BLUE+"\n\nOpen List - ")
            for i in open:
                print(i.name, end=" | ")
            print()

            print(Fore.BLUE+"Closed List - ")
            for i in closed:
                print(i.name, end=" | ")

            # Sort the open list to get the node with the lowest cost first
            open.sort()
            # Get the node with the lowest cost
            current_node = open.pop(0)
            # Add the current node to the closed list
            closed.append(current_node)

            # Check if we have reached the goal, return the path
            if current_node == goal_node:
                path = []
                while current_node != start_node:
                    path.append(current_node.name)
                    current_node = current_node.parent
                path.append(start_node.name)
                # Return reversed path
                return path[::-1]

            # Get neighbours
            neighbors = graph.get(current_node.name)
            # Loop neighbors
            for key, value in neighbors.items():
                # Create a neighbor node
                neighbor = self.Node(key, current_node)
                # Check if the neighbor is in the closed list
                if (neighbor in closed):
                    continue
                # Calculate cost to goal
                neighbor.h = heuristics.get(neighbor.name)
                neighbor.f = neighbor.h
                # Check if neighbor is in open list and if it has a lower f value
                if (self.add_to_open(open, neighbor) == True):
                    # Everything is green, add neighbor to open list
                    open.append(neighbor)
        # Return None, no path is found
        return None

    # Check If A Neighbor Should Be Added To Open List
    def add_to_open(self, open, neighbor):
        for node in open:
            if (neighbor == node and neighbor.f >= node.f):
                return False
        return True

    def start(self):
        # Create a graph
        graph = self.Graph()
        # Create graph connections (Actual distance)
        graph.connect('Oradea', 'Zerind', 71)
        graph.connect('Oradea', 'Sibiu', 151)
        graph.connect('Zerind', 'Arad', 75)
        graph.connect('Arad', 'Sibiu', 140)
        graph.connect('Arad', 'Timisoara', 118)
        graph.connect('Timisoara', 'Lugoj', 111)
        graph.connect('Lugoj', 'Mehadia', 70)
        graph.connect('Mehadia', 'Drobeta', 75)
        graph.connect('Drobeta', 'Craiova', 120)
        graph.connect('Craiova', 'Pitesti', 138)
        graph.connect('Craiova', 'Rimnicu Vilcea', 146)
        graph.connect('Sibiu', 'Fagaras', 99)
        graph.connect('Fagaras', 'Bucharest', 211)
        graph.connect('Sibiu', 'Rimnicu Vilcea', 80)
        graph.connect('Rimnicu Vilcea', 'Pitesti', 97)
        graph.connect('Pitesti', 'Bucharest', 101)
        graph.connect('Bucharest', 'Giurgui', 90)

        # Make graph undirected, create symmetric connections
        graph.make_undirected()

        # Display Graph
        graph.display_graph()

        # Create heuristics (straight-line distance, air-travel distance)
        heuristics = {}
        heuristics['Arad'] = 366
        heuristics['Bucharest'] = 0
        heuristics['Craiova'] = 160
        heuristics['Drobeta'] = 242
        heuristics['Fagaras'] = 176
        heuristics['Guirgiu'] = 77
        heuristics['Lugoj'] = 244
        heuristics['Mehadia'] = 241
        heuristics['Oradea'] = 380
        heuristics['Pitesti'] = 100
        heuristics['Rimnicu Vilcea'] = 193
        heuristics['Sibiu'] = 253
        heuristics['Timisoara'] = 329
        heuristics['Zerind'] = 800

        # Run search algorithm
        path = self.best_first_search(graph, heuristics, 'Arad', 'Bucharest')
        print(Fore.GREEN+"\n\nThe Path Is - ")
        for i in path:
            print(i)

print(Fore.BLUE+"\t\t\t\t\t\tBest First Search\n")
choice = int(input("Enter Your Choice - \n1. 8-Puzzle Problem\n2. Robot Navigation\n3. City-Distance Problem\nChoice - "))

if(choice == 1):
    temp = Puzzle()
    temp.Start_Puzzle()

elif(choice == 2):
    temp = Robot()
    temp.Start_Navigation()

elif(choice == 3):
    temp = City_Distance()
    temp.start()