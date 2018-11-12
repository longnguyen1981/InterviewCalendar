from unittest import TestCase

from company.interviewcalendar.src.mapping import map_calendar, validate_time


class TestMapping(TestCase):
    def setUp(self):
        self.data = [{'name': 'name1', 'fromhour': 8, 'tohour': 14, 'day': 'Wed'},
                     {'name': 'name2', 'fromhour': 9, 'tohour': 12, 'day': 'Wed'},
                     {'name': 'name3', 'fromhour': 8, 'tohour': 10, 'day': 'Wed'},
                     {'name': 'name3', 'fromhour': 9, 'tohour': 12, 'day': 'Tue'}]
        self.data_failed_time = [{'name': 'name1', 'fromhour': 8.5, 'tohour': 14, 'day': 'Wed'},
                     {'name': 'name2', 'fromhour': 9, 'tohour': 12, 'day': 'Tue'}]

    def test_map_calendar(self):
        out = map_calendar(self.data)
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0]['day'], 'Wed')
        self.assertEqual(out[0]['slots'], [9, 10])

    def test_validate_time(self):
        out = validate_time(self.data)
        self.assertEqual(out['code'], 200)
        out_failed = validate_time(self.data_failed_time)
        self.assertEqual(out_failed['code'], 415)

    def tearDown(self):
        return
