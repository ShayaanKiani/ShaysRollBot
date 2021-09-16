from datetime import datetime, timedelta


def calculate_time_difference(next_session):
    duration = next_session - datetime.now()
    total_seconds = duration.total_seconds()
    sec = timedelta(seconds=int(total_seconds))
    d = datetime(1, 1, 1) + sec

    time_till_next_session = (
        "Time Till Next Game: ```\n{} Days, {} Hours, {} Minutes\n```".format(
            str(d.day - 1), str(d.hour), str(d.minute)
        )
    )

    return time_till_next_session


def calculate_percent_to_next_session(last_session, next_session):
    duration = next_session - last_session
    total_seconds = duration.total_seconds()
    duration = next_session - datetime.now()
    total_seconds_from_now = duration.total_seconds()

    percent = (total_seconds_from_now / total_seconds) * 100

    return 100 - percent


def sixty_seconds_left(next_session):
    duration = next_session - datetime.now()
    total_seconds = duration.total_seconds()
    
    if total_seconds <= 60:
        return True
    else:
        return False
