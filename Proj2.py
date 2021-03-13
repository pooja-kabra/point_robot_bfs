# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 23:00:04 2021

@author: pooja
"""

from helpers import offsets, is_legal_pos, get_path
from queue_ll import Queue


def main():
    
    begin = (0, 0)
    
    end = (90, 70)
    
    # call to bfs
    print(bfs(begin,end))
    
    return None




def bfs(start,goal):
    
    queue = Queue()
    queue.enqueue(start)
    predecessors = {start: None}
    
    
    while not queue.is_empty():
        
        # pop off first state in the queue
        current_cell = queue.dequeue()
        
        # check if it is the goal itself
        if current_cell == goal:
            return get_path(predecessors, start, goal)

        for direction in ["up", "right", "down", "left", "down_right", "up_right", "down_left", "up_left"]:
            row_offset, col_offset = offsets[direction]
            neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            
            if is_legal_pos(neighbour) and neighbour not in predecessors: 
                queue.enqueue(neighbour) # add neighbour to exploration queue
                predecessors[neighbour] = current_cell # add neighbour to the parent-child dictionary for backtracking

    return None
    
    
if __name__ == "__main__":
    main()