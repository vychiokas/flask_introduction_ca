def make_readable(seconds):
    seconds_per_hour = 3600
    seconds_per_minute = 60
    
    hours = seconds // seconds_per_hour
    seconds = seconds - hours * seconds_per_hour
    
    minutes = seconds // seconds_per_minute
    seconds = seconds - minutes * seconds_per_minute
    if hours < 10:
        hours = f"0{hours}"
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"
    return f"{hours}:{minutes}:{seconds}"
    
print(make_readable(0))