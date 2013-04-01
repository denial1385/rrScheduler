#-------------------------------------------------------------------------------
# Name:        enqueue
# Purpose:      This module deals with the queueing of processes into
#               the Ready List. The  processes are dispatched into the
#               ready list in various staggered increments of
#               variable named HOLD_UP 0, 5, 10, 15, 20 and, 25 time units.
#
#
# Author:      Ngibuini, David and Breton, Matthew
#
# Created:     27/03/2013
# Copyright:   (c) Ngibuini 2013
# Licence:     Freeware
#-------------------------------------------------------------------------------
#!/usr/bin/env python


from collections import deque
from time import clock, time
import random
import spawn

hold_up = 0,0;
new_proc = chr
next_proc = str
proc_counter = 0
is_new_proc = bool
proc_name = str
counter = 10
proc_to_be_simulated = 0
arrival_time = 0;
cpu_time_request = 0.0
big_bang = 0.0

def main():

        is_new_proc == True
        #my_new_process = spawn()
        counter = 0

        list.append(proc_name)
        print("Your process is ready for scheduling: Process ",proc_name)

        real_arrival_time = 0.0
        ReadyList = []

        if(is_new_proc == true):
             counter = counter+1

        real_arrival_time = arrival_time + hold_up
        list.append(new)




pass

if __name__ == '__main__':
    main()
