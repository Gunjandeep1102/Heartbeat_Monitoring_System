import unittest
from datetime import datetime, timedelta
from main import detecting_alerts

def dt(base, mins):
    return base + timedelta(minutes=mins)

class Heartbeat_Testing(unittest.TestCase):
    def setUp(self):
        self.base = datetime(2025, 8, 4, 10, 0)

    def test_alert_trigger(self):
        events = [("email", self.base), ("email", dt(self.base, 4))]
        alerts = detecting_alerts(events)
        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0]["service"], "email")

    def test_nearly_missed(self):             # missed only 2 intervals then no alert
        events = [("email", self.base), ("email", dt(self.base, 3))]
        alerts = detecting_alerts(events)
        self.assertEqual(len(alerts), 0)

    def test_unordered_data(self):
        events = [("email", dt(self.base,4)), ("email", self.base)]
        alerts = detecting_alerts(events)
        self.assertEqual(len(alerts), 1)

    def test_malformed_data(self):
        events = [("email", self.base)]
        alerts = detecting_alerts(events)
        self.assertEqual(len(alerts), 0)

if __name__ == "__main__":
    unittest.main()