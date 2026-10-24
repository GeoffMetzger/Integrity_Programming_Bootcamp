# Managing complex multi-dimensional system log payloads
system_log_payload ={
    "timestamp": "2026-10-24T14:35:00Z",
    "service_origin": "fastspi_ingestion_engine", 
    "payload_metrics": {
        "status_code": 500,
        "traceback_active": True
    }   
}

print(f"Tracking Source: {system_log_payload['service_origin']}")
print(f"Error Signal Status: {system_log_payload['payload_metrics']['status_code']}")