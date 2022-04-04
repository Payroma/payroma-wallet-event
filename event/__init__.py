from .eventsignals import *


# The model that is inherited to objects
class EventForm:
    def events_listening(self):
        """Listen to all signals"""

        appStarted.listen(self.app_started_event)
        colorChanged.listen(self.color_changed_event)

    def app_started_event(self):
        pass

    def color_changed_event(self, name: str):
        pass
