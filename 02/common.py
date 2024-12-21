def is_safe(levels):
    increasing = True
    if levels[1] < levels[0]:
        increasing = False
    safe = True
    for i in range(1, len(levels)):
        val = levels[i]
        prev_val = levels[i - 1]
        diff = abs(val - prev_val)
        if diff < 1 or diff > 3:
            safe = False
            break
        if (increasing and val < prev_val) or (not increasing and val > prev_val):
            safe = False
            break
    return safe
