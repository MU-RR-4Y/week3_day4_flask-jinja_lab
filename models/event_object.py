from models.events import Events
import datetime

event_1 =Events(datetime.date(2023,2,20), 'Superbowl', 45000, 'America','NFL Final', True)
event_2 =Events(datetime.date(2023,3,10), 'Wimbeldom', 20000, 'London','Tennis Competition', True)
event_3 =Events(datetime.date(2023,3,23), 'Champions League Final', 50000, 'Paris', 'Football Final',False)
event_4 =Events(datetime.date(2023,4,15), 'Love Island Final', 50, 'Majorca', 'Reality TV Show',False)

events = [event_1, event_2, event_3, event_4]

def add_new_event(event):
    events.append(event)