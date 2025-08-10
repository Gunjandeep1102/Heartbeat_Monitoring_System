import json
from datetime import timedelta
from dateutil import parser


EXPECTED_INTERVAL_SECOND = 60
ALLOWED_MISSES = 3


def processing_events(filename="events.json"):
    with open(filename) as f:
        data = json.load(f)

    events = []
    for e in data:
        try:
            ts = parser.isoparse(e["timestamp"])
            events.append((e["service"], ts))
        except Exception:
            continue
    return events


def detecting_alerts(events):
    alerts = []
    services = {}

    for svc, ts in events:                              #group by service
        services.setdefault(svc, []).append(ts)
    for svc, times in services.items():                   #processing each service
        times.sort()
        missed = 0
        expected = times[0] + timedelta(seconds=EXPECTED_INTERVAL_SECOND)
        for actual in times[1:]:
            while actual > expected:
                missed += 1
                if missed == ALLOWED_MISSES:
                    alerts.append({
                        "service": svc, "alert_at": expected.isoformat().replace("+00:00", "Z")
                    })
                    break                             # stop counting further for this service
                expected += timedelta(seconds=EXPECTED_INTERVAL_SECOND)
            else:
                missed = 0   #if didn't miss beats, reset counter
                expected = actual + timedelta(seconds=EXPECTED_INTERVAL_SECOND)
    return alerts

if __name__ == "__main__":
    events = processing_events("events.json")
    result = detecting_alerts(events)
    print(result)