from time import sleep
import sys

# ===============================
# Core: Vital ranges configuration
# ===============================
VITAL_LIMITS = {
    "temperature": (95, 102),
    "pulse": (60, 100),
    "spo2": (90, 100)
}

# ===============================
# Pure functions (testable logic)
# ===============================
def is_vital_normal(value, min_val, max_val):
    """Return True if value lies within the range [min_val, max_val]."""
    return min_val <= value <= max_val


def check_vitals(vitals: dict):
    """
    Check all vitals against their limits.
    Returns (bool, message) where:
      bool    = True if all are normal
      message = reason for failure if any
    """
    for vital, (low, high) in VITAL_LIMITS.items():
        if vital not in vitals:
            continue  # ignore missing vital, flexible design
        if not is_vital_normal(vitals[vital], low, high):
            return False, f"{vital.capitalize()} is out of range!"
    return True, "All vitals normal."


# ===============================
# I/O functions (alerts, printing)
# ===============================
def alert(message):
    """Show alert message with blinking stars."""
    print(message)
    for _ in range(6):
        print("\r* ", end="")
        sys.stdout.flush()
        sleep(1)
        print("\r *", end="")
        sys.stdout.flush()
        sleep(1)


def vitals_ok(temperature, pulseRate, spo2):
    """
    Entry point: check vitals and trigger alert if needed.
    Returns True/False.
    """
    ok, message = check_vitals({
        "temperature": temperature,
        "pulse": pulseRate,
        "spo2": spo2
    })
    if not ok:
        alert(message)
    return ok
