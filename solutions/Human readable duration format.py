def format_duration(seconds):
    if seconds == 0:
        return "now"

    intervals = (
        ("year", 365 * 24 * 60 * 60),
        ("day", 24 * 60 * 60),
        ("hour", 60 * 60),
        ("minute", 60),
        ("second", 1)
    )

    result = []
    for name, duration in intervals:
        if seconds >= duration:
            count = seconds // duration
            seconds %= duration
            if count > 1:
                name += "s"
            result.append(f"{count} {name}")

    return ", ".join(result[:-1]) + " and " + result[-1] if len(result) > 1 else result[0]
