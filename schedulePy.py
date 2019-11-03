import time
import datetime
#import Schedule

class Event:
    def __init__(self, name, dayweek, start_time, end_time):
        #starttime and endtime are tuples in 24 hour time. (hour, minute)
        self.name = name
        self.dayweek = dayweek
        self.start_time = start_time
        self.end_time = end_time
        self.duration = (end_time[0] - start_time[0], end_time[1] - start_time[1])

class Assignment:
    def __init__(self, name, dayweek, estimate_time):
        self.dayweek = dayweek
        self.name = name
        self.estimate_time = estimate_time

class Schedule:
    def __init__(self, username):
        self.username = username
        self.events = {}
        self.assignments = {}

    def addevent(self, name, dayweek, start_time, end_time):
        name = Event(name, dayweek, start_time, end_time)
        self.events.update({name.name:name})

    def addassignment(self, name, dayweek, estimate_time):
        name = Assignment(name, dayweek, estimate_time)
        self.assignments.update({name.name:name})

    def delevent(self, eventname):
        self.events.pop(eventname)

#experiment
myschedule = Schedule('user')
myschedule.addevent('nail', [1, 2, 3, 4, 5], (16,0), (16,30))
myschedule.addevent('butt', [1, 2, 3, 4, 5], (16, 45), (17,21))
myschedule.addevent('School', [1, 2, 3, 4, 5], (8,20), (15,21))
myschedule.addevent('poo', [1, 2, 3, 4, 5], (15,48), (16, 0))

myschedule.addassignment('Math HW', 6, (0, 30))
#make sure there are no overlapping times
def timeschedule(classls):
    global orderedls
    orderedls = []
    while classls != []:
        bignum = ((24, 59), (0,0))
        bigclass = None
        for event in classls:
            if classls[event].start_time[0] < bignum[0][0]:
                bignum = classls[event].start_time
                bigclass = classls[event]
            elif classls[event].start_time[0] == bignum[0][0]:
                if classls[event].start_time[1] < bignum[0][1]:
                    bignum = classls[event].start_time
                    bigclass = classls[event]
                else:
                    pass
            else:
                pass
        orderedls.append(bigclass)
        classls.remove(bigclass)
    print(orderedls)
    classls = orderedls

def freetime(orderedls):
    global freetimes
    freetimes = []
    for times in orderedls:
        try:
            if times[1][1] > orderedls[orderedls.index(times) + 1][0][1]:
                mins = 60 - times[1][1]
                mins + orderedls[orderedls.index(times) + 1][0][1]
                hour = orderedls[orderedls.index(times) + 1][0][0] - times[1][0] + 1
            else:
                mins = orderedls[orderedls.index(times) + 1][0][1] - times[1][1]
                hour = orderedls[orderedls.index(times) + 1][0][0] - times[1][0]
            if hour == 0 and mins == 0:
                pass
            else:
                freetimes.append((hour, mins))
        except IndexError:
            break

timeschedule(myschedule.events)
freetime(orderedls)








#Instead of list inside of dict schedule, make a dictionary, Ex. key = p1, value = length of p1
def blockscheduler(p1, p2, p3, p4, p5, p6, p7, p8, gfree_D, gfree_P, Slab_D, Slab1, Slab2, Scourse):
    schedule = {"A Day": [p1, p2, "Morning Break", p3, p4, p5, "Break", p6, p7, p8],
                    "B Day": [p2, p3, "Morning Break", p4, p1, p6, "Break", p7, p8, p5],
                    "C Day": [p3, p4, "Morning Break", p1, p2, p7, "Break", p8, p1, p2],
                    "D Day": [p4, p1, "Morning Break", p2, p3, p8, "Break", p5, p6, p7],
                   "E Day": [p3, p1, "Break", p7, p5, "Tiger Time"],
                    "F Day": [p4, p2, "Break", p8, p6, "Activity"],
                    "HR Day": [p1, p2, "Homeroom", p3, p4, p5, "Break", p6, p7, p8]}
    schedule[gfree_D] = "Free Period"
    schedule[Slab_D][Slab1] = Scourse
    schedule[Slab_D][Slab2] = Scourse
    return schedule

def cur_class(day):
    curtime = time.localtime(time.time())

    if curtime.tm_hour == 8:
        return schedule[day][0]

        # Days

    elif day == "A Day" or day == "B Day" or day == "C Day" or day == "D Day":

        if curtime.tm_hour == 9:
            if curtime.tm_min < 4:
                return schedule[day][0]
            elif curtime.tm_min < 52:
                return schedule[day][1]
            else:
                return schedule[day][2]

        elif curtime.tm_hour == 10:
            if curtime.tm_min < 3:
                return schedule[day][2]
            elif curtime.tm_min < 51:
                return schedule[day][3]
            else:
                return schedule[day][4]

        elif curtime.tm_hour == 11:
            if curtime.tm_min < 35:
                return schedule[day][4]
            else:
                return schedule[day][5]

        elif curtime.tm_hour == 12:
            if curtime.tm_min < 23:
                return schedule[day][5]
            else:
                return schedule[day][6]

        elif curtime.tm_hour == 13:
            if curtime.tm_min < 45:
                return schedule[day][7]
            else:
                    return schedule[day][8]

        elif curtime.tm_hour == 14:
            if curtime.tm_min < 33:
                return schedule[day][8]
            else:
                return schedule[day][9]

freetimes = {}
#input
p1 = "Public Speaking"
p2 = "Studio Art"
p3 = "Geometry 1 Accelerated"
p4 = "US History"
p5 = "French 3a"
p6 = "English"
p7 = "PE"
p8 = "Bio Accel"
gfree_D = "C Day"
gfree_P = 5
Slab_D = "B Day"
Slab1 = "5"
Slab2 = "6"
Scourse = "Bio Accel"
print()
#All free times

freetimes[str(gfree_P)] = gfree_D
freetimes["Tiger Time"] = "E Day"
print(freetimes)