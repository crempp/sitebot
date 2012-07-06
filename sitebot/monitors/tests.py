from django.test import TestCase
from django.utils import timezone
from monitors.models import Monitor

class MonitorModelTest(TestCase):
    def test_creating_a_new_monitor_and_saving_it_to_the_database(self):
        # start by creating a new Monitor object with its name and URI
        monitor = Monitor()
        monitor.name = "testsite.com"
        monitor.uri = "http://testsite.com"

        # check we can save it to the database
        monitor.save()

        # now check we can find it in the database again
        all_monitors_in_database = Monitor.objects.all()
        self.assertEquals(len(all_monitors_in_database), 1)
        only_monitor_in_database = all_monitors_in_database[0]
        self.assertEquals(only_monitor_in_database, monitor)

        # and check that it's saved its two attributes: name and uri
        self.assertEquals(only_monitor_in_database.name, "testsite.com")
        self.assertEquals(only_monitor_in_database.uri, "http://testsite.com")
