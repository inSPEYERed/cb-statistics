import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker

# COLORS = ['tab:orange', 'tab:blue']
COLORS = ['#057976', '#BF2118', '#014485']
PATTERNS = ['.', '/', '.O']

# https://stackoverflow.com/a/39566040/9655481
SMALL_SIZE = 12
MEDIUM_SIZE = 14
BIGGER_SIZE = 16

plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('axes', titlesize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
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
                        year_counts, bar_width, label=year, color=COLORS[i], hatch=PATTERNS[i])
        # ax.bar_label(rects, padding=3)

    plt.xlabel('Kalenderwoche (KW)')
    plt.ylabel('Anzahl Ausleihen pro KW')
    plt.legend()

    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.set_xlim(0, 53+1)
    ax.grid(axis='y')

    plt.tight_layout()
    plt.show()


def plot_bookings_per_weekday(per_weekday_results: dict[int, list[int]]) -> None:
    # Printout to the console
    for year in sorted(per_weekday_results):
        year_counts = per_weekday_results[year]
        print(f'Year {year}: {year_counts}')

    fig, ax = plt.subplots(figsize=(10, 9))
    x_values = np.arange(1, 7+1)  # [start, begin)
    bar_width = 0.35

    for i, year in enumerate(sorted(per_weekday_results)):

        year_counts = per_weekday_results[year]

        rects = plt.bar(x_values - (bar_width/2) + i*bar_width,
                        year_counts, bar_width, label=year, color=COLORS[i], hatch=PATTERNS[i])
        # ax.bar_label(rects, padding=3)

    plt.xlabel('Wochentag')
    plt.ylabel('Anzahl Ausleihen')
    plt.legend()

    x_labels = ['Montag', 'Dienstag', 'Mittwoch',
                'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']
    ax.set_xticklabels(['', ''] + x_labels)

    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.set_xlim(0, 7+1)
    ax.grid(axis='y')

    plt.tight_layout()
    plt.show()


def plot_bookings_per_item(per_item_results: dict[int, dict[str, int]]) -> None:
    # Printout to the console
    for year in sorted(per_item_results):
        year_counts = per_item_results[year]
        print(f'Year {year}: {year_counts}')

    fig, ax = plt.subplots(figsize=(10, 9))
    num_items = len(list(per_item_results.values())[0])
    x_values = np.arange(1, num_items+1)  # [start, begin)
    bar_width = 0.35

    x_ticklabels = []
    for i, year in enumerate(sorted(per_item_results)):
        year_results = per_item_results[year]
        values = list(year_results.values())
        print('VALUES')
        print(values)

        if i == 0:
            item_names = year_results.keys()
            x_ticklabels.extend(item_names)

        rects = plt.bar(x_values - (bar_width/2) + i*bar_width,
                        values, bar_width, label=year, color=COLORS[i], hatch=PATTERNS[i])
        # ax.bar_label(rects, padding=3)

    plt.xlabel('Lastenrad')
    plt.ylabel('Anzahl Ausleihen')
    plt.legend()

    ax.set_xticklabels(['', ''] + x_ticklabels)

    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.set_xlim(0, num_items+1)
    ax.grid(axis='y')

    plt.tight_layout()
    plt.show()
