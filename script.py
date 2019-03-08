import pandas as pd
import numpy as np

# !!!!!!!!!!!!!!!!! MESSY ASSIGNMENT !!!!!!!!!!!!!!

# Setting up pandas so that it displays all columns instead of collapsing them
desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 10)


visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

visits_cart_left = pd.merge(visits,
                            cart,
                            how='left'
                            )
print(visits_cart_left.info())

print('\n', len(visits_cart_left[visits_cart_left.cart_time.isnull()]))

not_placed_order = len(visits_cart_left[visits_cart_left.cart_time.isnull()])
total_visits = len(visits_cart_left)
percent_no_order = not_placed_order/float(total_visits)
print(percent_no_order)

cart_checkout_left = pd.merge(cart, checkout, how='left')
# print(cart_checkout_left.info())
cart_but_no_checkout = len(cart_checkout_left[cart_checkout_left.checkout_time.isnull()])
total_cart = len(cart_checkout_left)
percent_no_checkout = cart_but_no_checkout/float(total_cart)
print(percent_no_checkout)

all_data = visits\
            .merge(cart, how='left')\
            .merge(checkout, how='left')\
            .merge(purchase, how='left')
print(all_data.head(10))

checkout_no_purchase = all_data[(~all_data.checkout_time.isnull())
                                &
                                (all_data.purchase_time.isnull())]
checked_out = all_data[~all_data.checkout_time.isnull()]
print(checked_out['user_id'].nunique())
print(checkout_no_purchase['user_id'].nunique())
num_checkout_no_purchase = len(checkout_no_purchase)
num_checkout = len(all_data[~all_data.checkout_time.isnull()])
print(num_checkout_no_purchase)
print(num_checkout)
percent_checkout_no_purchase = float(num_checkout_no_purchase)/num_checkout
print(percent_checkout_no_purchase)

all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time
print(all_data.time_to_purchase.mean())
