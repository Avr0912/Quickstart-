from threading import Lock
import time

class Queue:
    def __init__(self):
        self.queue = []
        self.set = set()
        self.lock = Lock()

    def enqueue(self, job):
        with self.lock:
            if job in self.set:
                print("Error: job already in queue")
            self.set.add(job)
            self.queue.append(job)
    
    def dequeue(self):
        with self.lock:
            if len(self.queue) == 0:
                print("Error: queue empty")
                return None
            toRet = self.queue.pop(0)
            self.set.remove(toRet)
            return toRet
    
    def remove(self, job):
        with self.lock:
            if job not in self.set:
                print("Error: job not found")
                return None
            self.set.remove(job)
            return job.queue.remove(job)
    
    def remove_job_id(self, id):
        with self.lock:
            for job in self.queue:
                if job[0] == id:
                    self.set.remove(job)
                    self.queue.remove(job)
                    return job
            print("Error: job not found")
            return None
    
    def queue_from_file(self, filename):
        with self.lock:
            with open(filename, 'r') as file:
                for line in file:
                    job = tuple(line.strip().split(", "))
                    self.enqueue(job)

    def process(self):
        while len(self.queue) != 0:
            temp = self.dequeue()
            print("Runnin $" + temp[0] + ", " + temp[1] + ", " + temp[2])
            if len(temp) == 4:
                time.sleep(temp[3])

    def get_queue(self):
        with self.lock:
            return self.queue


    def peek(self):
        with self.lock:
            if len(self.queue) == 0:
                return None
            return self.queue[0]
        
    def get_job(self, id):
        with self.lock:
            for x in self.queue:
                if x[0] == id:
                    return x
            return None