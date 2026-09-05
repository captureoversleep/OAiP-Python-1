people_count = 3
price_loss_baggage = 890
price_flight_cancel = 875
price_sickness = 1345
price_loss_docs = 2199

total_price = (price_sickness + price_flight_cancel + price_loss_docs + price_loss_baggage) * people_count
print('Стоимость страхования семьи:', total_price)