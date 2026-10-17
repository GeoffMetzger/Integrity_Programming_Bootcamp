#Defining application state variables
assistant_name = "Intelligent Agent"
active_users = 104
is_processing_logs = True
print(f"Initial State: {assistant_name} has {active_users} active users.")

# Demonstrating mutability: Reassigning the Variable value on the fly
active_users = 105

print(f"Updated States: Acctive users shifted to {active_users}")