# Daily report on the use of machines
# Manager wants a report on the specific users on a system at a particular point in time
# There exist a system that collectes all logs of when users login to the machines and when they log out
# what inputs do we need - Alist of events, event is an instance of the Event class
# An event class contains the date when the event happened, the name of the machine where it happened, the user involved, and the event type.
# the login and logout event type.
#what outputs do we need - list machine names and list users logged in at the machine at a certain time
# Use sort() to sort the logs in chronological orrder
#Dictionary of set  - machine name is the key and users are sets - values of the key 
# sets allows us to only have unigue users in the queue - that means when users log out the user valeu will be deleted from the stored values
# 2 functions one that generates the dictionary and the other that prints 
class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

def get_event_date(event):
  return event.date

def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout"and event.user in machines[event.machine]:
      machines[event.machine].remove(event.user)
        
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))


events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

#Test the code
users = current_users(events)
print(users)

print(get_event_date(events[5]))

generate_report(users)