def timeConversion(s: str):
    time, p = s[:-2], s[-2:]
    h, t, sec = time.split(":")
    h = str(int(h))
    if p == "PM" and int(h) != 12:
        h = str(int(h) + 12)
    elif p == "AM" and int(h) == 12:
        h = "00"
    answer = ":".join([h.zfill(2), t, sec])
    return answer


print(timeConversion("12:59:59AM"))
