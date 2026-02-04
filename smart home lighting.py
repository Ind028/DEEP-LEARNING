from datetime import datetime, time

now_dt = datetime.now()
current_date = now_dt.strftime("%Y-%m-%d")
current_time_str = now_dt.strftime("%H:%M")

def evaluate_lighting(time_str, people_count):
    now = datetime.strptime(time_str, "%H:%M").time()
    if people_count == 0:
        return "OFF (Energy Saving - House Empty)"
    if now >= time(23, 0) or now < time(6, 0):
        return "OFF (Sleep Mode)"
    if time(6, 0) <= now < time(18, 0):
        return "DIM (Daylight Balance)"
    return "BRIGHT (Evening Mode)"

people_at_home = int(input(f"Enter the number of ppl present at home: "))
action = evaluate_lighting(current_time_str, people_at_home)

print(f"\n--- Smart Home System Status ---")
print(f"Date: {current_date}")
print(f"Current Time: {current_time_str}")
print(f"Occupancy: {people_at_home} ppl")
print(f"Lighting Command: {action}")
