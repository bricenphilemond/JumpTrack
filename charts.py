# I asked AI how to import and use matplotlib to create line charts and wrote this based on the response
import matplotlib.pyplot as plt
def show_chart(jumps):
    long_jump_dates = []
    long_jump_distances = []
    triple_jump_dates = []
    triple_jump_distances = []
    for jump in jumps:
        if jump.event == "long jump":
            long_jump_dates.append(jump.date)
            long_jump_distances.append(jump.best_attempt())
        elif jump.event == "triple jump":
            triple_jump_dates.append(jump.date)
            triple_jump_distances.append(jump.best_attempt())
    # I asked AI how to plot data with matplotlib and wrote this based on the response
    plt.plot(long_jump_dates, long_jump_distances, label="long jump")
    plt.plot(triple_jump_dates, triple_jump_distances, label="triple jump")
    plt.xlabel("date")
    plt.ylabel("distance (m)")
    plt.title("JumpTrack Overtime")
    plt.legend()
    plt.show()