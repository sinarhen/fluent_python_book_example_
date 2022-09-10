from collections import namedtuple


city = namedtuple('City', 'country population flag_color ')
delhi = city('India', '1200000', 'orange,white,green')
print(delhi._asdict())

