import pandas as pd
import matplotlib
# make the output of matplotlib Agg (instead of screen)
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import logging

logger = logging.getLogger('progress')
logger.setLevel(logging.DEBUG)
sh = logging.StreamHandler()
fmt = logging.Formatter('[%(levelname)s] %(message)s')
sh.setFormatter(fmt)
logger.addHandler(sh)

def read_csv(file):
    logger.info(f'reading file \'{file}\'')

    options = {
        'encoding': 's-jis',
        'usecols': [0, 1, 4],
        'skiprows': list(range(4)),
        'names': list(range(7)),
    }
    raw_data = pd.read_csv(file, **options)
    raw_data.columns = ['date', 'temp', 'humid']
    return raw_data

months = [
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
]
datas = [read_csv(f'lib/{month}.csv') for month in months]

for month, data in zip(months, datas):
    logger.info(f'starting to draw scatter of {month}')

    temp, humid = data.temp, data.humid
    cc = data.corr()['temp']['humid']
    
    plt.title(month)
    plt.xlabel('Temperature [℃]')
    plt.ylabel('Humid [%]')
    plt.axis([0, 40, 0, 100])

    plt.text(30, 5, f'r = {cc:.6}')

    sct = plt.scatter(temp, humid, 3)

    plt.savefig(f'dist/{month}.png')
    plt.cla()
