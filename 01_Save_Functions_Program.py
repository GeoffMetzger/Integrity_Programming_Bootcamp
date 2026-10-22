# Encapsulation reusable system calculation logic

def calculate_system_efficiency(total_tasks, errors):
    success_rate = (total_tasks - errors) / total_tasks
    return success_rate

current_efficiency = calculate_system_efficiency(500, 12)
print(f"Current System State: {current_efficiency * 100}%")