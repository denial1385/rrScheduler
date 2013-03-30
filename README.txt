So far, there are five methods:

	1. Creating a new job, e.g. spawn(),
	2. Entering new job into ready list, e.g. enqueue(),
	3. Dispatching current job, e.g. execute(), and,
	4. Simulating interrupts, e.g. interrupt().
	5. Deleting completed job, e.g. destroy()

As of 3/30, 0952, I am woeking on completing the last parts of the spawn method. It verifies user input of a new process
and will place that newly spawned process into the Ready List.  