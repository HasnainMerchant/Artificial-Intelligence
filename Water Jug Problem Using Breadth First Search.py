# Assignment 2A - Water Jug Problem Using Breadth First Search
# Name - Hasnain Merchant   Div - B     Roll No - 30

def print_Path(path):
    res = []
    for i in path:
        if i not in res:
            res.append(i)

    for i in res:
        print("(" + str(i[0]) + "," + str(i[1]) + ")" + " -> ", end="")


def bfs(jug1, jug2, target):

    # Root Node (0, 0)
    root = [0, 0]

    # To Find Path From Root To Target
    path = []

    # Queue Initialization
    queue = [root]

    # To Keep Track of Visited Nodes
    visited = []
    visited.append([0, 0])

    # Open List
    open_list = [root]

    # Closed List
    closed_list =[]
    print("\n")

    while queue:

        print("Open List - ")
        print(open_list)

        print("Closed List - ")
        print(closed_list)
        print("\n\n")

        current = queue.pop()
        closed_list.append(current)
        open_list.remove(current)
        jug1_capacity = int(current[0])
        jug2_capacity = int(current[1])

        path.append(current)

        if jug1_capacity == target:
            print("\n\nThe Path Is - ")
            print_Path(path)
            break


        # Rule 1 ~ If Jug 1 Is Empty, Fill Jug
        if jug1_capacity < jug1 and ([jug1, jug2_capacity]) not in visited:
            queue.append([jug1, jug2_capacity])
            open_list.append([jug1, jug2_capacity])
            visited.append([jug1, jug2_capacity])

        # Rule 2 ~ If Jug 2 Is Empty, Fill Jug
        if jug2_capacity < jug2 and ([jug1_capacity, jug2]) not in visited:
            queue.append([jug1_capacity, jug2])
            open_list.append([jug1_capacity, jug2])
            visited.append([jug1_capacity, jug2])

        # Rule 3 ~ If Jug 1 Is Full, Empty Jug
        if jug1_capacity >= jug1 and ([0, jug2_capacity]) not in visited:
            queue.append([0, jug2_capacity])
            open_list.append([0, jug2_capacity])
            visited.append([0, jug2_capacity])

        # Rule 4 ~ If Jug 2 Is Full, Empty Jug
        if jug2_capacity >= jug2 and ([jug1_capacity, 0]) not in visited:
            queue.append([jug1_capacity, 0])
            open_list.append([jug1_capacity, 0])
            visited.append([jug1_capacity, 0])

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
                if ([transfer_quantity_jug1, tranfer_quantity_jug2]) not in visited:
                    queue.append([transfer_quantity_jug1, tranfer_quantity_jug2])
                    open_list.append([transfer_quantity_jug1, tranfer_quantity_jug2])
                    visited.append([transfer_quantity_jug1, tranfer_quantity_jug2])

        # Rule 6 ~ Transfer From Jug 2 to Jug 1
        if jug2_capacity > 0 and jug1_capacity < jug1:
            if jug1_capacity == 0 and jug2_capacity <= jug2:
                transfer = jug2_capacity
            else:
                transfer = jug1 - jug1_capacity
            transfer_quantity_jug1 = jug1_capacity + transfer
            tranfer_quantity_jug2 = jug2_capacity - transfer
            if transfer_quantity_jug1 <= jug1 and tranfer_quantity_jug2 <= jug2:
                if ([transfer_quantity_jug1, tranfer_quantity_jug2]) not in visited:
                    queue.append([transfer_quantity_jug1, tranfer_quantity_jug2])
                    open_list.append([transfer_quantity_jug1, tranfer_quantity_jug2])
                    visited.append([transfer_quantity_jug1, tranfer_quantity_jug2])

# Driver Code
jug1 = int(input("Enter Capacity Of Jug 1 - "))
jug2 = int(input("Enter Capacity Of Jug 2 - "))
target = int(input("Enter Target Volume - "))

# Calling BFS Function
bfs(jug1, jug2, target)