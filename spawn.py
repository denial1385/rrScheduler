#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ngibuini
#
# Created:     28/03/2013
# Copyright:   (c) Ngibuini 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from collections import deque
from time import clock, time


#hold_up = 0;

#arrival_time = 0;

def main():
        new_proc = None
        #newProc = None
        is_new_proc = False
        proc_name = str

        is_new_proc = raw_input("Do you have a process? (y/n)")

        if(is_new_proc == 'y'):
            proc_name = raw_input("What is your process's name? Input: ")
            print("I will queue this process "+proc_name+" into the Ready List.")
        #this simply creates a new blank queue that will be
        #implemented as the ready list

            readyList = []

            queue = deque(proc_name)
            readyList = len(queue)

            #if(readyList > 0):

            is_new_proc = raw_input("Do you have another process? (y/n)")
            return

        else:
            #isNewProc = False

            print("OK. There are no more processes to queue - for now!")

        return
pass

if __name__ == '__main__':
    main()
