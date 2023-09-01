import sleeper as sc
import map
import cal
import ai
import app


def fmin(t):
    t = t[11:16]
    h = int(t[:2])
    m = int(t[3:])
    return int((h * 60 + m)*60)


def ftmin(t):
    h = int(t//3600)
    m = int((t%3600)//60)
    return str(f"{h:02d}")+":"+str(f"{m:02d}")


def ringTime():
    c = cal.get_events(1)
    print("Calendar Data: ", c)
    s = sc.sleepcal(202)
    print("Sleep Data: ", s)
    start = fmin(c[1])
    loc = c[-1]
    here = 'Vellore Institute of Technology - Chennai, Vandalur - Mambakkam - Kelambakkam Road, Kolapakkam, Chennai, ' \
           'Chengalpattu, Chengalpattu District, Tamil Nadu, 600127, India '
    reach = (map.locate(here, loc))
    print("Travel Time: ", reach)
    leave = start - reach
    wakeTime = leave-3600
    snooze = ai.giveSnooze(s, wakeTime+4*3600)
    print("Snoozes: ", snooze)
    return wakeTime - snooze*600


print("Alarm will start ringing at: ", ftmin(ringTime()))
web = app.start()
web.run()




