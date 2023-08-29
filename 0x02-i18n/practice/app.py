#!/usr/bin/env python3

from flask import Flask, render_template
from datetime import date, datetime
from flask_babel import numbers, dates
app = Flask(__name__)


@app.route('/')
def index():
    us_num = numbers.format_decimal(12345, locale='en_US')
    se_num = numbers.format_decimal(12345, locale='sv_SE')
    ge_num = numbers.format_decimal(12345, locale='de_DE')
    d = date(2023, 8, 29)
    us_date = dates.format_date(d, locale='en_US')
    se_date = dates.format_date(d, locale='sv_SE')
    ge_date = dates.format_date(d, locale='de_DE')
    results = {'us_num': us_num, 'se_num': se_num, 'de_num': ge_num,
               'us_date': us_date, 'se_date': se_date,
               'ge_date': ge_date}
    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
