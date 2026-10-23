# Automated system error routing engine 
error_severity = "CRITICAL"
is_admin_notified = False

if error_severity == "CRITICAL" and not is_admin_notified:
    print("System Action: SHUTDOWN ENGINE IMMEDIATELY AND ALERT ADMINISTRATOR.")
    is_admin_notified = True 
elif error_severity == "WARNING" or error_severity == "MINOR":
    print("System Action: Log sata saved to background traching file.")
else:
    print("System Action: No anomalies detected. Maintain standard operations.")