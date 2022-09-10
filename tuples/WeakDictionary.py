class Cheese:

    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return f'Cheese("{self.kind}")'

"""
                    Cheese('mozarellla')
                        Cheese("mozarellla")
                    import weakref
                    
                    stock = weakref.WeakValueDictionary()
                    catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), ]
                    catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Parmesan')]
                    catalog
                        [Cheese("Red Leicester"), Cheese("Tilsit"), Cheese("Parmesan")]
                    for cheese in catalog:
                        stock[cheese.kind] = cheese
                    
                    sorted(stock.keys())
                        ['Parmesan', 'Red Leicester', 'Tilsit']
                    del catalog
                    sorted(stock.keys())
                        ['Parmesan']
                    del cheese
                    sorted(stock.keys())
                        []
"""