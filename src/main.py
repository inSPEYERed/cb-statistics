from combine_pdf import combine_plot_pdfs
from evaluation import (evaluate_bookings_per_item, evaluate_bookings_per_week,
                        evaluate_bookings_per_weekday)
from plot_diagrams import (plot_bookings_per_item, plot_bookings_per_week,
                           plot_bookings_per_weekday)
from wordpress_parser import (combine, parse_postmeta_bookings,
                              parse_posts_booking_status_and_items)

############################# Read/Parse data ##################################

print()
print('🔘 Read/Parse data')

bookings = parse_postmeta_bookings()
bookings_status, items = parse_posts_booking_status_and_items()
item_names = list(items.values())
print(f'Found these items: {item_names}')
bookings = combine(bookings, bookings_status)
# get rid of post/booking ids, we don't need them
bookings = list(bookings.values())


################################ Evaluation ####################################

print()
print('🔘 Evaluation')
per_week_results = evaluate_bookings_per_week(bookings)
per_weekday_results = evaluate_bookings_per_weekday(bookings)
per_item_results = evaluate_bookings_per_item(bookings, items)


############################### Plot diagrams ##################################

print()
print('🔘 Plot & save diagrams')

plot_bookings_per_week(per_week_results)
plot_bookings_per_weekday(per_weekday_results)
plot_bookings_per_item(per_item_results, item_names)

combine_plot_pdfs()
