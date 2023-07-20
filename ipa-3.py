#!/usr/bin/env python
# coding: utf-8

# In[1]:


def relationship_status(from_member, to_member, social_graph):
    if from_member in social_graph[to_member]['following'] and to_member in social_graph[from_member]['following']:
        return "friends"
    
    elif to_member in social_graph[from_member]["following"]:
        return "follower"
    
    elif from_member in social_graph[to_member]['following']:
        return "followed by"
    
    else:
        return "no relationship"

    
    

def tic_tac_toe(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != '-':
            return row[0]

    for col in range(len(board)):
        if len(set([board[row][col] for row in range(len(board))])) == 1 and board[0][col] != '-':
            return board[0][col]

    if len(set([board[i][i] for i in range(len(board))])) == 1 and board[0][0] != '-':
        return board[0][0]

    if len(set([board[i][len(board)-1-i] for i in range(len(board))])) == 1 and board[0][len(board)-1] != '-':
        return board[0][len(board)-1]

    return "NO WINNER"




def eta(first_stop, second_stop, route_map):
    route = (first_stop, second_stop)
    if route in route_map:
        return route_map[route]['travel_time_mins']

    route_time = 0
    next_stop = None

    for stops in route_map.keys():
        if stops[0] == first_stop:
            next_stop = stops[1]
            route_time += route_map[stops]["travel_time_mins"]
            break

    if next_stop is None:
       
        return -1

    while next_stop != second_stop:
        found_next_stop = False
        for iter_stops, time in route_map.items():
            if iter_stops[0] == next_stop:
                next_stop = iter_stops[1]
                route_time += time["travel_time_mins"]
                found_next_stop = True
                break

        if not found_next_stop:
            
            return -1

    return route_time


# In[ ]:




