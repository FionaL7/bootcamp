import json
import csv
import pickle
import threading
from datetime import datetime
from collections import namedtuple
# JSON Dump/Load
data = {'name': 'Fi', 'age': 25}
json_str = json.dumps(data)
print("Serialized:", json_str)

loaded_data = json.loads(json_str)
print("Deserialized:", loaded_data)

# Pretty Print JSON
pretty = json.dumps(data, indent=4, sort_keys=True)
print("Pretty JSON:\n", pretty)

# CSV Read with DictReader
with open('data.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

# CSV Write
people = [{'name': 'Fi', 'age': 25}, {'name': 'Luna', 'age': 30}]
with open('output.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'age'])
    writer.writeheader()
    writer.writerows(people)


# Python Object
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

with open('data.pkl', 'rb') as f:
    loaded_pickle = pickle.load(f)
    print("Unpickled:", loaded_pickle)

# Secure Unpickling
counter = 0
lock = threading.Lock()


def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1


threads = [threading.Thread(target=increment) for _ in range(2)]
[t.start() for t in threads]
[t.join() for t in threads]
print("Final counter:", counter)

# Custom JSON Encoder for datetime


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return super().default(o)


now = {'time': datetime.now()}
print(json.dumps(now, cls=DateTimeEncoder))

# CSV to NamedTuples
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    headers = next(reader)
    Row = namedtuple('Row', headers)
    for r in reader:
        print(Row(*r))
