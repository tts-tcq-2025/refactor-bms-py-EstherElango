import unittest
from monitor import vitals_ok, check_vitals, is_vital_normal


class MonitorTest(unittest.TestCase):

    def test_temperature_out_of_range(self):
        self.assertFalse(vitals_ok(104, 72, 95))  # too high
        self.assertFalse(vitals_ok(94, 72, 95))   # too low

    def test_pulse_out_of_range(self):
        self.assertFalse(vitals_ok(98, 55, 95))   # too low
        self.assertFalse(vitals_ok(98, 120, 95))  # too high

    def test_spo2_out_of_range(self):
        self.assertFalse(vitals_ok(98, 72, 85))   # too low

    def test_all_vitals_ok(self):
        self.assertTrue(vitals_ok(98, 72, 95))

    def test_check_vitals_returns_message(self):
        ok, msg = check_vitals({"temperature": 110, "pulse": 80, "spo2": 95})
        self.assertFalse(ok)
        self.assertIn("Temperature", msg)

    def test_is_vital_normal_helper(self):
        self.assertTrue(is_vital_normal(100, 95, 102))
        self.assertFalse(is_vital_normal(104, 95, 102))


if __name__ == "__main__":
    unittest.main()

