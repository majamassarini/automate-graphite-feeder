import home

from graphite_feeder.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.alarm.armed.Event
    TITLE = "Alarm armed"
