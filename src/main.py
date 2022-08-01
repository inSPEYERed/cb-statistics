from combine_pdf import combine_plot_pdfs
from evaluation import (evaluate_bookings_per_item, evaluate_bookings_per_week,
                        evaluate_bookings_per_weekday)
from plot_diagrams import (plot_bookings_per_item, plot_bookings_per_week,
                           plot_bookings_per_weekday)
from wordpress_parser import (combine, parse_postmeta_bookings,
                              parse_posts_booking_status)

############################# Read/Parse data ##################################

print()
print('🔘 Read/Parse data')

bookings = parse_postmeta_bookings()
bookings_status = parse_posts_booking_status()
bookings = combine(bookings, bookings_status)
# get rid of post/booking ids, we don't need them
bookings = list(bookings.values())

# This map could also be inferred from the posts JSON, you can do that
# if your are not as lazy as I am for this purpose ;-)
items_map = {
    438: 'Edgar',
    665: 'Emilio',
    617: 'Eva',
    774: 'Teeresa'
}


################################ Evaluation ####################################

print()
print('🔘 Evaluation')
per_week_results = evaluate_bookings_per_week(bookings)
per_weekday_results = evaluate_bookings_per_weekday(bookings)
per_item_results = evaluate_bookings_per_item(bookings, items_map)


############################### Plot diagrams ##################################

print()
print('🔘 Plot & save diagrams')

plot_bookings_per_week(per_week_results)
plot_bookings_per_weekday(per_weekday_results)
plot_bookings_per_item(per_item_results, list(items_map.values()))

combine_plot_pdfs()
