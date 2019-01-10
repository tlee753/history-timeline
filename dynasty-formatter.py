import sys

start = int(sys.argv[1])
end = int(sys.argv[2])
top = 0
bot = 0

if (start < -500):
    top = -4000 - start
    top /= 5
elif (start >= -500 and start < 500):
    top = -500 - start
    top -= 700
elif (start >= 500 and start < 1000):
    top = 500 - start
    top -= 1700
elif (start >= 1000 and start < 1500):
    top = 1000 - start
    top -= 2200
elif (start >= 1500 and start < 1800):
    top = 1500 - start
    top /= 0.5
    top -= 2700
elif (start >= 1800 and start < 1915):
    top = 1800 - start
    top /= 0.25
    top -= 3300
elif (start >= 1915):
    top = 1915 - start
    top /= 0.15
    top -= 3760

# print("top is    ", int(-top))

if (end < -500):
    bot = -4000 - end
    bot /= 5
elif (end >= -500 and end < 500):
    bot = -500 - end
    bot -= 700
elif (end >= 500 and end < 1000):
    bot = 500 - end
    bot -= 1700
elif (end >= 1000 and end < 1500):
    bot = 1000 - end
    bot -= 2200
elif (end >= 1500 and end < 1800):
    bot = 1500 - end
    bot /= 0.5
    bot -= 2700
elif (end >= 1800 and end < 1915):
    bot = 1800 - end
    bot /= 0.25
    bot -= 3300
elif (end >= 1915):
    bot = 1915 - end
    bot /= 0.15
    bot -= 3760

# print("height is ", int(-bot - -top))

print("""
<div class="dynasty" style="top: {}px; height: {}px; background: {}};">
    <p class="dynasty-begin">1947 CE</p>
    <p class="dynasty-content">Modern Japan</p>
    <p class="dynasty-end">1990 CE</p>
    <span class="dynasty-info">
        Modern Japan
        <p>This is informative...</p>
    </span>
</div>
""".format(int(-top), int(-bot - -top)), )