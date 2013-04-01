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

# Version: 1.2
# Modified and committed to GitHub on midnight,March 31st
#
#
#-------------------------------------------------------------------------------
#!/usr/bin/env python


#import statements

from collections import deque
from time import clock, time
import random

#flags ************************************************************************
is_new_proc = bool          #boolean variable that returns True if there
                            #is a new process

#variables ********************************************************************
new_proc = str              #this is the process popped from the spawn list
                            #to be inserted into the Ready List
curr_proc = str             #changes the new process into the current process

#assignment specified input variables *****************************************
hold_up = 0;                #this is the simulated dispatcher delay


#counters *********************************************************************
proc_counter = 0            #will keep track of how many processes are still
                            #in execution
completed_proc_counter = 0  #this counter will keep track of the completed
                            #processes and matches them against the proc_counter
                            #list for verification and tracking purposes
ready_list_counter = 0      #keeps track of how many processes in the Ready List

#other variables **************************************************************
proc_name = str             #this is the name of the created process
proc_to_be_simulated = 0    #gets assigned the returned value of the length
                            #of the new processes list
creation_time = 0;          #this is the simulated time when the process is
                            #ready for enqueing into the Ready List
real_creation_time = 0.0    #this is the creation time accounting for the
                            #dispatcher delay (hold_up)
cpu_time_request = 0.0      #this is how much CPU time a process will request
                            #to be allocated for this process' completion

big_bang = 0.0  #this is the epoch when the processes are initially
                #spawned for the very first time, independent of
                #anything else, and can be viewed as initial OS bootup
spec_mean = 0.5 #this is the specified mean that will be input into the
                #normalvariate randomizer, out of a range of 0 to 1. This
                #enables homogenity of processes to be averaged, but fall
                #on either side of 0.5 based on the deviation specified below
spec_deviation = 0.4 #this is the specified deviation that will be input
                #into the normalvariate randomizer. This enables numbers
                #generated to have a truly random likelihood of occurence,
                #from 0.1 to 0.9, in a range of 0 to 1

#******************************************************************************
#******************************************************************************

def main():

    #simulation of initial OS instantiation
        big_bang = (time()/1000000000)
        #print("This is when the OS is initialized: "+big_bang)
        print('Simulated OS turned on at (seconds)',big_bang)

    #this is where the processes are spawned into existence for the first time,
    #only after the simulated OS has been created.

        new_process_list = deque('ABCDEFGHIJ')

        print("This is a list of the processes in the list ", new_process_list)
        proc_to_be_simulated = len(new_process_list)

    #this function pops the left most element in the spawned processes list.
    #The left most element is the first one created, and the first one out (FIFO)
        while proc_to_be_simulated > 0:
        #if(counter > 0):
            proc_to_be_simulated = len(new_process_list)
            is_new_proc == True
            new_proc = (new_process_list.popleft())
            print("This is the current process: "+new_proc)

            curr_proc = new_proc
            #this assigns a clocktime value to each new process
            #that will be assigned the creation time, and also
            #assigns a  random float that will be used as the
            #CPU time that this new process will request

            creation_time = time()
            print('This task has been created at time (in seconds) ',creation_time/1000000000)

            cpu_time_request = random.normalvariate(spec_mean, spec_deviation)
            print("This is the CPU time this process will request randomly: ",cpu_time_request)

            print(len(new_process_list))
            proc_to_be_simulated = proc_to_be_simulated - 1
            print("This is the number of processes left: ",(len(new_process_list)))


        #enqueue into Ready List

            print('I will queue this process into the Ready List: Process '+curr_proc)

            ReadyList = deque([new_proc])
            #ReadyList = queue.append(proc_name)

            print("Process "+curr_proc+" is now ready for scheduling!")


        #specifies a set of different dispatchers. It will pop one value from a list
        #and populate this value as the dispatcher delay. It will then simulate the
        #dispatching of this process into the CPU awaiting execution in RR fashion


            dispatcher_time_setter = deque('0,5,10,15,20,25')
            ready_list_counter = 6 #len(dispatcher_time_setter)



            while(ready_list_counter is not 0):

                hold_up = (dispatcher_time_setter.popleft())

                #real_creation_time = creation_time + hold_up

                ready_list_counter = ready_list_counter - 1

#********************************************************************
#left off at 04/01/13 - 2330
#
#above code is not functional, i mean commented out code in
#
#while((ready_list_counter is not 0):
#
#
#but I am working on it, just have to be up early tomorrow
#so I'm calling it a night
#
#
#insert code to enqueue this process into another data structure
#maybe a stack so we can dip in and out at will, but no preference
#of type of data structure
#
#once a process is in execute list, this is the arrival time into
#the CPU, and start dividing requested CPU time (cpu_time_request)
#by the different time quanta. The time quanta will be set and changed
#to meet specifications by placing it into a queue and while-looping the
#simulation of the pop within the dispatcher loop directly
#above this comment block.
#
#we can add context switching delays to each process easily by tacking on
#a simple line to each iteration of execution.
#
#upon arrival of a new process, it can be tacked onto the end of the currently
#executing process, superseding all  other processes waiting in the list, but
#NOT interrupting the currently executing process. This just seems the most
#equitable way that also places high importance on getting newly arriving
#processes going right away so as to even out the wait times and completion
#times as well.
#
#QUESTION: DO YOU WANT TO START WORKING ON THE LOGIC OF THE ACTUAL RR PROCESS
#WHILE I WORK MY WAY TO THAT POINT? ALL THAT IS LEFT BETWEEN THE CURRENT
#COMPLETION OF THE PROGRAM THUS FAR, TO ACTUAL EXECUTION AND CONTEXT SWITCHING
#IS NESTING LOOPS AND DUPLICATING THE CODE WHILE CHANGING A FEW VARIABLES??
#
#
#destroy code is simply deleting the execute list upon completion
#and should be basic
#
#I am going to commit the current changes and point your attention to this
#comment block. For version control, please specify last modified comments
#or at least when you commit to GitHub or make significant changes.
#
#We should be in good shape for Thursday.
#
#***********************************************************************




                print("Hiya")
            #real_creation_time = creation_time + hold_up

            #print("\n\n")

        else:
            is_new_proc == False
            print("There are no more processes to queue - for now!\nExiting....Please wait....")

        return
pass

if __name__ == '__main__':
    main()
