import tkinter
import time
import playsound


class __Alarm(object):
    """Base class for alarm"""

    def __init__(self, title: str):
        self.__title = title

    def set_time(self, time: time.struct_time):
        self.__ring_time = time

    def get_time(self):
        return self.__ring_time

    def get_title(self):
        return self.__title

    def get_state(self):
        return self.__activated

    def activate(self):
        self.__activated = True

    def deactivate(self):
        self.__activated = False

    def __compare_formatted(self, format):
        time1 = time.strftime(format, time.localtime())
        time2 = time.strftime(format, self.__ring_time)
        return time1 == time2

    def tick(self):
        if self.__activated:
            if self.__compare_formatted("%H:%M"):
                self.__ring()

    def __ring(self):
        pass


class AlarmOnce(__Alarm):
    """Alarm that rings once at given date"""

    def tick(self):
        if self.__activated:
            if self.__compare_formatted("%H:%M %x"):
                self.__ring()


class AlarmDOW(__Alarm):
    """Alarm that repeats on specified days of week"""

    def __init__(self, title: str, days: tuple):
        super().__init__(title)
        self.__days_of_week = days

    def get_DOW(self):
        return self.__days_of_week

    def tick(self):
        if self.__activated:
            if self.__compare_formatted("%H:%M"):
                if time.strftime("w",time.localtime()) in self.__days_of_week:
                    self.__ring()


alarms_window = tkinter.Tk()
alarms_window.mainloop()


