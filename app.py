from flask import Flask, request, jsonify
from PriorityQueue import PriorityQueue
from Queue import Queue
from Stack import Stack
import os.path

app = Flask(__name__)
pq = PriorityQueue()
queue = Queue()
stack = Stack()


@app.route('/pq/jobs', methods=['POST'])
def add_job_pq():
    data = request.json
    job_id = data.get('job_id')
    job_name = data.get('job_name')
    priority = data.get("priority")
    if not isinstance(priority, str):
        priority = str(priority)
    if job_id == None:
        return jsonify({"Field Missing": "job_id"})
    if job_name == None:
        return jsonify({"Field Missing": "job_name"})
    if priority == None:
        return jsonify({"Field Missing": "priority"})
    job = (job_id, job_name, priority)
    pq.pq_enqueue(job)
    return jsonify({"status": "success", "job_id": job_id}), 201

@app.route('/queue/jobs', methods=['POST'])
def add_job_queue():
    data = request.json
    job_id = data.get('job_id')
    job_name = data.get('job_name')
    priority = data.get("priority")
    job = (job_id, job_name, priority)
    queue.enqueue(job)
    return jsonify({"status": "success", "job_id": job_id}), 201

@app.route('/stack/jobs', methods=['POST'])
def add_job_stack():
    data = request.json
    job_id = data.get('job_id')
    job_name = data.get('job_name')
    priority = data.get("priority")
    job = (job_id, job_name, priority)
    stack.push(job)
    return jsonify({"status": "success", "job_id": job_id}), 201












@app.route('/pq/jobs', methods=['GET'])
def get_job_pq():
    job = pq.peek()
    if job:
        return jsonify({"job_id": job[0], "job_name": job[1], "priority": job[2]})
    return jsonify({"Error": "priority queue empty"}), 404

@app.route('/queue/jobs', methods=['GET'])
def get_job_queue():
    job = queue.peek()
    if job:
        return jsonify({"job_id": job[0], "job_name": job[1], "priority": job[2]})
    return jsonify({"Error": "queue empty"}), 404

@app.route('/stack/jobs', methods=['GET'])
def get_job_stack():
    job = stack.peek()
    if job:
        return jsonify({"job_id": job[0], "job_name": job[1], "priority": job[2]})
    return jsonify({"Error": "stack empty"}), 404





@app.route('/pq/file/<filename>', methods=['GET'])
def pq_from_file(filename):
    if os.path.isfile(filename):
        pq.pq_from_file(filename)
        return jsonify({"Status": "success"})
    return jsonify({"Error": "file not found"}), 404

@app.route('/queue/file/<filename>', methods=['GET'])
def queue_from_file(filename):
    if os.path.isfile(filename):
        queue.queue_from_file(filename)
        return jsonify({"Status": "success"})
    return jsonify({"Error": "file not found"}), 404

@app.route('/pq/file/<filename>', methods=['GET'])
def stack_from_file(filename):
    if os.path.isfile(filename):
        stack.stack_from_file(filename)
        return jsonify({"Status": "success"})
    return jsonify({"Error": "file not found"}), 404





@app.route('/pq/jobs/status', methods=['GET'])
def get_pq():
    queue = pq.get_queue()
    return jsonify(queue)

@app.route('/queue/jobs/status', methods=['GET'])
def get_queue():
    q = queue.get_queue()
    return jsonify(q)

@app.route('/stack/jobs/status', methods=['GET'])
def get_stack():
    s = stack.get_stack()
    return jsonify(s)







@app.route('/pq/jobs/<job_id>', methods=['GET'])
def pq_get_job_from_id(job_id):
    # if not isinstance(job_id, str):

    job = pq.get_job(job_id)
    if job == None:
        return jsonify({"Error": "job not found"}), 404
    return jsonify({"job_id": job[0], "job_name": job[1], "priority": job[2]})

@app.route('/queue/jobs/<job_id>', methods=['GET'])
def queue_get_job_from_id(job_id):
    job = queue.get_job(job_id)
    if job == None:
        return jsonify({"Error": "job not found"}), 404
    return jsonify({"job_id": job[0], "job_name": job[1], "priority": job[2]})


@app.route('/stack/jobs/<job_id>', methods=['GET'])
def stack_get_job_from_id(job_id):
    job = stack.get_job(job_id)
    if job == None:
        return jsonify({"Error": "job not found"}), 404
    return jsonify({"job_id": job[0], "job_name": job[1], "priority": job[2]})





@app.route('/pq/jobs/<uuid>', methods=['DELETE'])
def pq_delete(uuid):
    job = pq.remove_job_id(uuid)
    if job:
        return jsonify({"job_id": job[0], "job_name": job[1], "priority": job[2]})
    return jsonify({"Error": "job not found"}), 404

@app.route('/queue/jobs/<uuid>', methods=['DELETE'])
def queue_delete(uuid):
    job = queue.remove_job_id(uuid)
    if job:
        return jsonify({"job_id": job[0], "job_name": job[1], "priority": job[2]})
    return jsonify({"Error": "job not found"}), 404

@app.route('/stack/jobs/<uuid>', methods=['DELETE'])
def stack_delete(uuid):
    job = stack.remove_job_id(uuid)
    if job:
        return jsonify({"job_id": job[0], "job_name": job[1], "priority": job[2]})
    return jsonify({"Error": "job not found"}), 404

# @app.route('/pq/file/<filename>', methods=['POST'])
# def pq_from_file(filename):
#     job = stack.get_job(job_id)
#     if job == None:
#         return jsonify({"Error": "job not found"}), 404
#     return jsonify({"job_id": job[0], "job_name": job[1], "priority": job[2]})

@app.route('/pq/process', methods=['GET'])
def process_pq():
    ret = pq.process()
    return jsonify(ret)

@app.route('/queue/process', methods=['GET'])
def process_queue():
    queue.process()
    return jsonify({"status": "success"})

@app.route('/stack/process', methods=['GET'])
def process_stack():
    stack.process()
    return jsonify({"status": "success"})
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)