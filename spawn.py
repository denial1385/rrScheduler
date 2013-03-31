#-------------------------------------------------------------------------------
# Name:        spawn
# Purpose:      This module deals with creation and instantiation of
#               processes from a simulated OS boot time to right before
#               the created processes are ready to put into the Ready List
#
# Author:      Ngibuini, David and Breton, Matthew
#
# Created:     24/03/2013
# Copyright:   (c) Ngibuini 2013
# Licence:     Freeware
#-------------------------------------------------------------------------------
#!/usr/bin/env python




from collections import deque
from time import clock, time
import random

#hold_up = 0;
new_proc = chr
next_proc = str
proc_counter = 0
is_new_proc = bool
proc_name = str
counter = 10
proc_to_be_simulated = 0
arrival_time = 0;
cpu_time_request = 0.0
big_bang = 0.0  #this is the epoch when the processes are initially
                #spawned for the very first time, independent of
                #anything else, and can be viewed as initial OS bootup

def main():


        #new_proc = raw_input("Do you have a process (y/n)?")

        #if(new_proc is not 'y' or 'n'):
        #   print("Please enter a 'y' for yes, or 'n' for no!")


        new_process_list = deque('ABCDEFGHIJ')
        big_bang = time()
        print(big_bang)
        print("Simulated OS was turned on at ",big_bang, 'seconds')

        print("This is a list of the processes in the list ", new_process_list)
        proc_to_be_simulated = len(new_process_list)

        while proc_to_be_simulated > 0:
        #if(counter > 0):
            proc_to_be_simulated = len(new_process_list)
            is_new_proc == True
            new_proc = (new_process_list.popleft())
            print("This is the current process: "+new_proc)

            #this assigns a clocktime value to each new process
            #that will be assigned the arrival time, and also
            #assigns a  random float that will be used as the
            #CPU time that this new process will request

            arrival_time = time()
            print("This task has arrived at time (in nanoseconds) ",arrival_time)

            cpu_time_request = random.normalvariate(0.5,0.3)
            print('This is the CPU time this process will request randomly:',(cpu_time_request))

            print(len(new_process_list))
            proc_to_be_simulated = proc_to_be_simulated - 1
            print("This is the number of processes left: ",len(new_process_list))
        else:
            is_new_proc == False

            #proc_name = new_process_list.popleft()


        if(is_new_proc == True):
            #is_new_proc == True
            #proc_name = raw_input("What is your process's name? Input: ")
            print("I will queue this process "+proc_name+" into the Ready List.")
            proc_counter = proc_counter + 1



        else:
            is_new_proc == False
            print("There are no more processes to queue - for now!\nExiting....Please wait....")

        return
pass

if __name__ == '__main__':
    main()
