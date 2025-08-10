# Heartbeat_Monitoring_System
This project contains logic building and code solution for monitoring heartbeats every 60 second. If it misses three heartbeats in a row this system will trigger an alert.

This python script monitors service heartbeat events and raises alerts when a service misses 3 number of consecutive heartbeats.
Test cases are also given for handling different user inputs such as :-
* A workig alert case
* A "nearly missed" case (only 2 missed heartbeats -> no alert should trigger)
* Unodered input (checks whether this solution can handle heartbeats events that are not in chronological order.)
* At least 1 malformed event (missing field or invalid timestamp)

## Key Features
- Reads heartbeat events from a JSON file
- Groups events by service
- Detects missed heartbeats based on expected interval and allowed misses upto 2 
- Outputs alerts as JSON

## Requirements
- Python 3.8+
- Required Python packages:
  pip install python-dateutil
  pip install python-unittest
  pip install python-json 
  pip install python-datetime
