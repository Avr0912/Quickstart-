from threading import Lock
import time

def getPriority(job):
        return job[2]


class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.size = 0
        self.firstIndex = dict()
        self.set = set()#to keep track of whether or not the queue contains an element
        self.lock = Lock()#to ensure thread safety in a possibly multi-threaded environment

    def dict_add(self, priority):#changes the dictionary of first indexes if a job of a certain priority is added
        for val in self.firstIndex.keys():
            if val>priority:
                self.firstIndex[val] += 1 

    def dict_remove(self, priority):#changes the dictionary of first index if a job of a certain priority is removed
        for val in self.firstIndex.keys():
            if val>priority:
                self.firstIndex[val] -= 1 

    def get_job(self, id):
        with self.lock:
            for x in self.queue:
                if x[0] == id:
                    return x
            return None


    def pq_enqueue(self, job):
        with self.lock:
            if job in self.set:
                print("Error: job already in queue")
                return None
            self.size += 1#changes size
            self.set.add(job)#adds job to the set for quick lookup
            priority = job[2]
            vals = list(self.firstIndex.keys())
            vals.sort()
            if vals != None:
                for val in vals:
                    if val>priority:
                        self.queue.insert(self.firstIndex[val], job)
                        if priority not in self.firstIndex.keys():
                            self.firstIndex[priority] = self.firstIndex[val]
                        self.dict_add(priority)
                        return

            self.queue.append(job)
            if priority not in self.firstIndex.keys():
                        self.firstIndex[priority] = len(self.queue)-1

    def pq_from_file(self, filename):
        with self.lock:
            with open(filename, 'r') as file:
                for line in file:
                    job = tuple(line.strip().split(", "))
                    self.queue.append(job)
                    self.set.add(job)
                    self.size += 1
            self.queue.sort(key=getPriority)
            for x in range(len(self.queue)):
                job = self.queue[x]
                if job[2] not in self.firstIndex.keys():
                    self.firstIndex[job[2]] = x
    
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        toRet = self.queue.pop(0)
        if len(self.queue) == 0 or self.queue[0][2] != toRet[2]:#checks to see if there are any more elements of the same priority
            self.firstIndex.pop(toRet[2])#if there aren't, remove the priority of the removed element from the list of first indices
        self.set.remove(toRet)#remove element from set
        self.dict_remove(toRet[2])#adjust dictionary accordingly
        return toRet
    
    def remove_job(self, job):
        with self.lock:
            if job not in self.set:
                print("Error: job not in queue")
                return None
            index = self.queue.index(job)
            if self.only_priority(job[2]):#checks to see if there are any more elements of the same priority
                self.firstIndex.pop(job[2])#if there aren't, remove the priority of the removed element from the list of first indices
            self.set.remove(job)
            self.dict_remove(job[2])
            return self.queue.pop(index)
             
    def remove_job_id(self, uuid):
        with self.lock:
            index = self.get_index(uuid)
            if index == None:
                return None
            job = self.queue[index]
            if self.only_priority(job[2]):#checks to see if there are any more elements of the same priority
                self.firstIndex.pop(job[2])#if there aren't, remove the priority of the removed element from the list of first indices
            self.set.remove(job)
            self.dict_remove(job[2])
            return self.queue.pop(index)


    def only_priority(self,priority):
        index = self.firstIndex[priority]
        if index == len(self.queue)-1:
            return True
        return priority != self.queue[index+1][2]
         
    def process(self):
        with self.lock:
            process = []
            while len(self.queue) != 0:
                temp = self.dequeue()
                print("Runnin $" + temp[0] + ", " + temp[1] + ", " + temp[2])
                process.append("Runnin $" + temp[0] + ", " + temp[1] + ", " + temp[2])
                if len(temp) == 4:
                    time.sleep(temp[3])
            return process
    
    def get_index(self, id):
        for x in range(len(self.queue)):
            if self.queue[x][0] == id:
                return x
        return None
    
    

    def get_queue(self):
        with self.lock:
            return self.queue


    def peek(self):
        with self.lock:
            if len(self.queue) == 0:
                return None
            return self.queue[0]
    
    


pq = PriorityQueue()
# pq.pq_from_file("jobs.txt")
# temp = 1
# job = ("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj", "first_job", "1")
# job2 = ("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", "second_job", "4")
# pq.pq_enqueue(job)
# pq.pq_enqueue(job2)
# temp = 1
# pq.process()
# pq.remove_job(job)
# pq.remove_job(job2)
# temp = 1
# temp = pq.dequeue()
# temp = pq.dequeue()
# temp = 1
# #add functionality for processing jobs and see if I should add more efficient lookup of elements given firstIndex
        
pq.pq_enqueue(("job1", "job1", "3"))
pq.pq_enqueue(("job1", "job1", "2"))
pq.pq_enqueue(("job1", "job1", "1"))
pq.remove_job_id("job1")
pq.remove_job_id("job1")
pq.remove_job_id("job1")
# pq.remove_job_id("0101")









