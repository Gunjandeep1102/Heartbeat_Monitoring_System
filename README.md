# Heartbeat_Monitoring_System
This project contains logic building and code solution for monitoring heartbeats every 60 second. If it misses three heartbeats in a row this system will trigger an alert.

This python script monitors service heartbeat events and raises alerts when a service misses 3 number of consecutive heartbeats.

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
