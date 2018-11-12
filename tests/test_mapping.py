from unittest import TestCase

from chemondis.interviewcalendar.src.mapping import map_calendar


class TestMapping(TestCase):
    def setUp(self):
        self.data = [{'name': 'name1', 'fromhour': 8, 'tohour': 14, 'day': 4},
                     {'name': 'name2', 'fromhour': 9, 'tohour': 12, 'day': 4},
                     {'name': 'name3', 'fromhour': 8, 'tohour': 10, 'day': 4},
                     {'name': 'name3', 'fromhour': 9, 'tohour': 12, 'day': 3}]

    def test_map_calendar(self):
        out = map_calendar(self.data)
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0]['day'], 4)
        self.assertEqual(out[0]['slots'], [9, 10])

    def tearDown(self):
        return
