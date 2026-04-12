#solucion
import heapq

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.valid = True

    def __lt__(self, other):
        if self.salary == other.salary:
            return self.name < other.name
        return self.salary > other.salary

n, a = map(int, input().split())
employees = {}
queue = []

for _ in range(n):
    name, salary = input().split()
    salary = int(salary)
    employee = Employee(name, salary)
    employees[name] = employee
    heapq.heappush(queue, employee)

for _ in range(a):
    action = list(input().split())
    if action[0] == '1':
        name, raise_amount = action[1], int(action[2])
        employee = employees[name]
        employee.valid = False
        employee = Employee(name, employee.salary + raise_amount)
        employees[name] = employee
        heapq.heappush(queue, employee)
    elif action[0] == '2':
        while not queue[0].valid:
            heapq.heappop(queue)
        fired_employee = heapq.heappop(queue)
        print(fired_employee.name, fired_employee.salary)