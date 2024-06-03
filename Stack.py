from threading import Lock
import time

class Stack:#thread safe it 
    def __init__(self):
        self.stack = []
        self.set = set()
        self.lock = Lock()

    def push(self, job):
        with self.lock:
            if job in self.set:
                print("Error: job already in stack")
            self.stack.append(job)
            self.set.add(job)
    
    def pop(self):
        with self.lock:
            if len(self.stack) == 0:
                print("Error: stack empty")
                return None
            toRet = self.stack.pop()
            self.set.remove(toRet)
            return toRet
    
    def remove(self, job):
        with self.lock:
            if job not in self.set:
                print("Error: job not found")
                return None
            self.set.remove(job)
            return job.stack.remove(job)
    
    def remove_job_id(self, id):
        with self.lock:
            for job in self.stack:
                if job[0] == id:
                    self.set.remove(job)
                    self.stack.remove(job)
                    return job
            print("Error: job not found")
            return None
    
    def stack_from_file(self, filename):
        with self.lock:
            with open(filename, 'r') as file:
                for line in file:
                    job = tuple(line.strip().split(", "))
                    self.push(job)

    def process(self):
        while len(self.stack) != 0:
            temp = self.pop()
            print("Runnin $" + temp[0] + ", " + temp[1] + ", " + temp[2])
            if len(temp) == 4:
                time.sleep(temp[3])

    def get_stack(self):
        with self.lock:
            return self.stack


    def peek(self):
        with self.lock:
            if len(self.stack) == 0:
                return None
            return self.stack[len(self.stack)-1]
        
    def get_job(self, id):
        with self.lock:
            for x in self.stack:
                if x[0] == id:
                    return x
            return None