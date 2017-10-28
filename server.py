import datetime
import bisect

from flask import render_template
from app import app, Order


def get_delay(time):
    key_moments = [datetime.timedelta(minutes=x) for x in [7, 30]]
    styles = ['success', 'danger', 'warning']
    return styles[bisect.bisect(key_moments, time)]


def get_unconfirmed_orders():
    return Order.query.filter(Order.confirmed.is_(None)).all()


def get_today_orders(today):
    return [order for order in Order.query.filter(Order.confirmed.isnot(None))
            if order.confirmed.day == today.day and order.confirmed.month == today.month]


def get_content():
    now = datetime.datetime.now()
    unconfirmed_orders = [(order, get_delay(now - order.created), order.created.strftime('%X')) for order in get_unconfirmed_orders()]
    today_orders = get_today_orders(now)
    content = {
        'unconfirmed': unconfirmed_orders,
        'unconfirmed_count': len(unconfirmed_orders),
        'today_count': len(today_orders),
        'time': now.strftime('%X')
    }
    return content


@app.route('/')
def score():
    content = get_content()
    return render_template('score.html', **content)


if __name__ == "__main__":
    app.run()
