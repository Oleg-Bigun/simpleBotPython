from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    # bot.change_currency(currency='USD')
    bot.select_place_to_go('New York')
    bot.select_dates(check_in_date='2022-12-10', check_out_date='2022-12-12')
    bot.select_adults(1)
    bot.click_search()
    bot.apply_filtrations()
    bot.refresh() # a workaround to let bot get results properly
    bot.report_results()