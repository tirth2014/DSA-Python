# When to use yield instead of return in Python?
# jyare values calculate karine series of values return karavvi hoy alag alag instead of calculating everything at once and sending them like a list.

def sqMe():
    i = 1
    while True:
        yield i*i
        i += 1
        
for num in sqMe():
    print(num, end=' ')
    if num >= 100:
        break
