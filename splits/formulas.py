def time_to_seconds(hours, minutes, seconds):
    if hours is None or minutes is None or seconds is None:
        return 0
    return (hours * 3600) + (minutes * 60) + seconds


def seconds_to_time(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds - (hours * 3600)) // 60
    seconds = total_seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"


def seconds_to_float(total_seconds):
    return float(total_seconds / 3600)


def mi_to_km(distance):
    return distance * 1.609


def km_to_mi(distance):
    if distance > 0:
        return distance / 1.609


def calculate_pace(time, distance):
    if time > 0:
        return int(time / distance)
    else:
        return 0


def calculate_time(pace, distance):
    return int(distance * pace)


def calculate_distance(pace, time):
    if pace is None or time is None or pace == 0:
        return 0
    return time / pace
