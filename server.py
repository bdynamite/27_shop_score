import datetime
import bisect
import pytz
import argparse

from flask import render_template
from app import app
from models import Order


def get_delay(time):
    key_moments = [datetime.timedelta(minutes=x) for x in [7, 30]]
    styles = ['success', 'danger', 'warning']
    return styles[bisect.bisect(key_moments, time)]


def get_today_orders(today):
    orders = Order.query.filter(Order.created.between(today.combine(today, today.min.time(), today)))
    return orders


def get_content():
    time_zone = pytz.timezone('Europe/Moscow')
    current_date = datetime.datetime.now(tz=time_zone)
    today_orders = get_today_orders(current_date)
    unconfirmed_orders = today_orders.filter(Order.confirmed.is_(None)).all()
    content = {
        'unconfirmed': [(order, get_delay(current_date - order.created.replace(tzinfo=time_zone)),
                         order.created.strftime('%X')) for order in unconfirmed_orders],
        'unconfirmed_count': len(unconfirmed_orders),
        'today_count': len(today_orders.all()),
        'time': current_date.strftime('%X')
    }
    return content


@app.route('/')
def score():
    content = get_content()
    return render_template('score.html', **content)


@app.route('/robots.txt')
def robots():
    with open('robots.txt', mode='r') as robots_file:
        return robots_file.read()


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--connection', type=str)
    return parser.parse_args()


def set_db_uri(connection):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}'.format(connection)


if __name__ == "__main__":
    args = create_parser()
    set_db_uri(args.connection)
    app.run()
