def averager():
    count = 0
    total = 0.0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count



