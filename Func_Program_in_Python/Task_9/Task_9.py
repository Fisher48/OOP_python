def segment_distance(speed, start_time, end_time):
    return speed * (end_time - start_time)

def odometer(oksana):
    speeds = oksana[0::2]
    times = [0] + oksana[1::2]

    return sum(
        segment_distance(speeds[i], times[i], times[i+1])
        for i in range(len(speeds))
    )

print(odometer([10,1,20,2])) # 30
print(odometer([15,2,20,4])) # 70


