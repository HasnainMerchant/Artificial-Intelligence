# Assignment 2B - Water Jug Problem Using Depth First Search
# Name - Hasnain Merchant   Div - B     Roll No - 30

import random

def rules_Applicable(jug1_capacity, jug2_capacity):
    nodes = []
    # Rule 1 ~ If Jug 1 Is Empty, Fill Jug
    if jug1_capacity < jug1:
        nodes.append([jug1, jug2_capacity])

    # Rule 2 ~ If Jug 2 Is Empty, Fill Jug
    if jug2_capacity < jug2:
        nodes.append([jug1_capacity, jug2])

    # Rule 3 ~ If Jug 1 Is Full, Empty Jug
    if jug1_capacity >= jug1:
        nodes.append([0, jug2_capacity])

    # Rule 4 ~ If Jug 2 Is Full, Empty Jug
    if jug2_capacity >= jug2:
        nodes.append([jug1_capacity, 0])

    # Rule 5 ~ Transfer From Jug 1 to Jug 2
    if jug1_capacity > 0 and jug2_capacity < jug2:
        if jug2_capacity == 0 and jug1_capacity >= jug2:
            transfer = jug2
        else:
            if jug2_capacity == 0 and jug1_capacity < jug2:
                transfer = jug1_capacity
            else:
                transfer = jug2 - jug2_capacity
        transfer_quantity_jug1 = jug1_capacity - transfer
        tranfer_quantity_jug2 = jug2_capacity + transfer
        if transfer_quantity_jug1 <= jug1 and tranfer_quantity_jug2 <= jug2:
            nodes.append([transfer_quantity_jug1, tranfer_quantity_jug2])

    # Rule 6 ~ Transfer From Jug 2 to Jug 1
    if jug2_capacity > 0 and jug1_capacity < jug1:
        if jug1_capacity == 0 and jug2_capacity <= jug2:
            transfer = jug2_capacity
        else:
            transfer = jug1 - jug1_capacity
        transfer_quantity_jug1 = jug1_capacity + transfer
        tranfer_quantity_jug2 = jug2_capacity - transfer
        if transfer_quantity_jug1 <= jug1 and tranfer_quantity_jug2 <= jug2:
            nodes.append([transfer_quantity_jug1, tranfer_quantity_jug2])
    return nodes

def dfs(jug1, jug2, target, limit):
    # Root Node (0, 0)
    root = [0, 0]

    # To Find Path From Root To Target
    path = []

    # Queue Initialization
    stack = [root]

    # To Keep Track of Visited Nodes
    visited = []
    visited.append([0, 0])

    while limit != 0:
        # print(queue)
        current = stack.pop()
        jug1_capacity = int(current[0])
        jug2_capacity = int(current[1])

        path.append(current)

        if jug1_capacity == target:
            print("\nSolution Found")
            print("\nThe Path Is - ")
            print(path)
            break

        nodes = rules_Applicable(jug1_capacity, jug2_capacity)
        print("Nodes Than Can Be Generated from (" + str(jug1_capacity) + "," + str(jug2_capacity) + ") - ")
        print(nodes)
        random_num = random.randint(0, len(nodes) - 1)

        node_selected = nodes[random_num]
        print("Node Selected - ")
        print(node_selected)
        if node_selected not in visited:
            stack.append(node_selected)
            visited.append(node_selected)
            limit -= 1
        else:
            print("\nThis Node Is Already Selected\n")
            print("The Branch Is Going In A Loop....Exiting The Program\n")
            print("No Solution Is Found")
            return 1
    return 0

#jug1 = int(input("Enter Capacity Of Jug 1 - "))
#jug2 = int(input("Enter Capacity Of Jug 2 - "))
#3target = int(input("Enter Target Volume - "))
#imit = int(input("Enter DFS Search Limit - "))
jug1 = 4
jug2 = 3
target = 2
limit = 7
i = 0
while i < 50:
    k = dfs(jug1, jug2, target, limit)
    if k == 0:
        print("\nLimit Reached....Exiting\n")
    i += 1