'''João Victor Dell Agli Floriano - 10799783
   Jobs processing simulation program.'''

from queue import Queue
from abc import ABC, abstractmethod
import random

from desimul import Calendar, Event, Server

# Auxiliary simulation classes
class Job:
    '''Implements methods to verify waiting times for each job.'''

    def __init__(self, worktime, priority):
        '''Create a new job with the specified amount of work and priority. 
           Normal priority = 0
           High priority = 1'''
        self._arrival_time = None
        self._attended_time = None
        self._departure_time = None
        self._total_worktime = worktime
        self._priority = priority

    def arrival(self, time):
        '''Called when job arrives.'''
        self._arrival_time = time

    def attended(self, time):
        '''Callend when job is being processed'''
        self._attended_time = time

    def departure(self, time):
        '''Called when job departs.''' 
        self._departure_time = time

    def report(self):
        '''Report on arrival, processing and departure times (for statistics).'''
        return self._arrival_time, self._attended_time, self._departure_time

    def worktime(self):
        '''Inform total worktime needed to process the job.'''
        return self._total_worktime
    
    def priority(self):
        '''Inform priority of the job'''
        return self._priority




# Server classes
class QueueingSystem(ABC, Server):
    '''Abstract base class for all job queueing systems.'''

    def __init__(self, calendar):
        '''Creates a queue associated with the given calendar.'''
        Server.__init__(self, calendar)
        self._free_processors = Queue()  # This stores the free processors.

    def new_job(self, job):
        '''A new job to attend. Either send it to a free processor (if
        available) or to the waiting queue.'''
        if self._free_processors.empty():
            # No free processors. Put job on the queue.
            self.enqueue(job)
        else:
            # There is a free processor. Send job to them.
            processor = self._free_processors.get()
            cal = self.calendar()
            now = cal.current_time()
            event = JobToProcessorEvent(now, processor, job)
            cal.put(event)

    def free_processor(self, processor):
        '''A new free processor. Send it a job (if one is waiting) or put it in
        the waiting queue.'''
        if self.has_waiting_job(processor):
            # There is a job waiting.
            job = self.get_next_job(processor)
            cal = self.calendar()
            now = cal.current_time()
            event = JobToProcessorEvent(now, processor, job)
            cal.put(event)
        else:
            # No job waiting. Put processor in the free processors queue.
            self._free_processors.put(processor)

    @abstractmethod
    def enqueue(self, job):
        '''Inserts the job in the queue, according to queueing policy.'''
        pass

    @abstractmethod
    def has_waiting_job(self, processor):
        '''Verify if the processor has a waiting job according to queueing
        policy.'''
        pass

    @abstractmethod
    def get_next_job(self, processor):
        '''Get the next job for the given processor, according do queueing
        policy.'''
        pass




class PriorityQueues(QueueingSystem):
    '''A job queueing system with priority queues. 
       One queue is for high priority jobs, and the other is for normal priority'''

    def __init__(self, calendar):
        QueueingSystem.__init__(self, calendar)
        self._normalQueue = Queue()
        self._priorQueue = Queue()

    def enqueue(self, job):
        '''When jobs arrive, they go to the smallest queue.'''
        if(job.priority() == 0):
            self._normalQueue.put(job)
        else:
            self._priorQueue.put(job)

    def has_waiting_job(self, processor):
        if(self._normalQueue.qsize() == 0 and self._priorQueue.qsize() == 0):
            return 0 
        else: return 1

    def get_next_job(self, processor):
        '''Get job at the front of the queue of this processor.'''
        if(self._priorQueue.qsize() == 0):
            return self._normalQueue.get()
        else:
            return self._priorQueue.get()


class Processor(Server):
    '''Processors know how to attend a job.'''

    def __init__(self, calendar, queue):
        '''Create a processor server associated with the given calendar and queue'''
        Server.__init__(self, calendar)
        self._queue = queue
        self._free_time = []
        self._totalHighPriority = 0
        self._totalJobs = 0
        self._last_attending = 0.0

    def attend_job(self, job):
        '''Do the work required by the job (takes time). Afterwards, notify
        queue about free status.'''
        curr_time = self.calendar().current_time()
        job.attended(curr_time)

        time_to_finish = job.worktime() 
        finish_time = curr_time + time_to_finish
        job.departure(finish_time)

        event = ProcessorFreeEvent(finish_time, self._queue, self)
        self.calendar().put(event)

        #data update
        freetime = curr_time - self._last_attending
        if(freetime != 0.0):
            self._free_time.append(freetime)

        #If the job is of high priority, update counter
        if(job.priority() == 1):
            self._totalHighPriority += 1

        self._totalJobs += 1

        self._last_attending = finish_time

    def total_jobs(self):
        '''Return the total number of jobs attended'''
        return self._totalJobs
    
    def total_high_priority(self):
        '''Return the total number of high priority jobs attended'''
        return self._totalHighPriority

    def free_times(self):
        '''Return a list of all idle interval lengths.'''
        return self._free_time







# Event types
class JobArrivalEvent(Event):
    '''A job has arrived.'''

    def __init__(self, time, queue, job):
        '''Creates an event of the given job arriving at the given queue at
        the given time'''
        Event.__init__(self, time, queue)
        self._job = job

    def process(self):
        '''Record arrival time in the job and insert it in the queue.'''
        self._job.arrival(self.time())
        self.server().new_job(self._job)


class JobToProcessorEvent(Event):
    '''Job goes to a free processor.'''

    def __init__(self, time, processor, job):
        '''Create an event of a given processor starting to attend for a given
        job at a given time.'''
        Event.__init__(self, time, processor)
        self._job = job

    def process(self):
        '''Processor should attend to job.'''
        self.server().attend_job(self._job)


class ProcessorFreeEvent(Event):
    '''A processor has become free.'''

    def __init__(self, time, queue, processor):
        '''Creates an event of a given processor becoming free.'''
        Event.__init__(self, time, queue)
        self._free_processor = processor

    def process(self):
        '''Notify queueing system of the free processor.'''
        self.server().free_processor(self._free_processor)







# Auxiliary writing functions
def write_job_data(filename, jobs):
    '''Writes job timing information to file with filename prefix.'''

    with open(filename, 'w') as outfile:
        for job in jobs:

            arrival, attended, departure = job.report()
            print(arrival, job.priority(), job.worktime(), attended, file = outfile)


def write_processors(filename, processors):
    '''"Write free processor time information to file with filename prefix.'''

    with open(filename, 'w') as outfile:
        for processor in processors:
            print(processor.total_jobs(), processor.total_high_priority(), processor.free_times(), file = outfile)
            print(file=outfile)




# Code to run
print("")
print("Write down the simulation parameters:")
p = int(input("Number of processors: "))
Tau = float(input("Mean of work time values distribution: "))
rho = float(input("Standard Deviation of the Mean: "))
T = float(input("Total job spawn time: "))
m = int(input("Total normal priority jobs: "))
a = int(input("Alpha parameter for high priority jobs: "))
print("")



'''Program variables'''
jobs = []
processors = []

MainCalendar = Calendar()
MainQueue = PriorityQueues(MainCalendar)




for k in range(p):
    '''Spawning processors'''
    processors.append(Processor(MainCalendar, MainQueue))


for processor in processors:
    '''Registering starting free processors event'''
    MainCalendar.put(ProcessorFreeEvent(0.0, MainQueue, processor))






'''Jobs generation part''' 
i = 0
while i < m:

    arrival_time = random.uniform(0.0, T)

    worktime = random.gauss(Tau, rho)

    if(worktime > 0.0): #This is to avoid zero and negative worktimes

        j = Job(worktime, 0)

        jobs.append(j)

        MainCalendar.put(JobArrivalEvent(arrival_time, MainQueue, j))

        i += 1

i = 0
while i < m//a:
    arrival_time = random.uniform(0.0, T)

    worktime = random.gauss(Tau, rho)

    if(worktime > 0.0):
        j = Job(worktime, 1)

        jobs.append(j)

        MainCalendar.put(JobArrivalEvent(arrival_time, MainQueue, j))

        i += 1
    '''End of jobs generation part'''




'''Jobs processing part'''
MainCalendar.process_all_events()
'''End of jobs processing part'''




'''Writing program data'''
write_job_data("jobs.dat", jobs)
write_processors("processors.dat", processors)

print("Total time of simulation is " + str(MainCalendar.current_time()))