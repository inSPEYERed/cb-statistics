import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker

COLORS = ['tab:orange', 'tab:blue']

# https://stackoverflow.com/a/39566040/9655481
MEDIUM_SIZE = 8
MEDIUM_SIZE = 14
BIGGER_SIZE = 16

plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('axes', titlesize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
# plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title


def plot_bookings_per_week(per_week_results: dict[int, list[int]]) -> None:
    # Printout to the console
    for year in sorted(per_week_results):
        year_counts = per_week_results[year]
        print(f'Year {year}: {year_counts}')

    fig, ax = plt.subplots(figsize=(20, 9))
    x_values = np.arange(1, 53+1)  # [start, begin)
    bar_width = 0.35

    for i, year in enumerate(sorted(per_week_results)):

        year_counts = per_week_results[year]

        rects = plt.bar(x_values - (bar_width/2) + i*bar_width,
                        year_counts, bar_width, label=year, color=COLORS[i])
        # ax.bar_label(rects, padding=3)

    plt.xlabel('Kalenderwoche (KW)')
    plt.ylabel('Anzahl Ausleihen pro KW')
    plt.legend()

    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.set_xlim(1, 53)
    ax.grid(axis='y')

    plt.tight_layout()
    plt.show()
