class Stock:
    def __init__(self,name:str,price,volume):
        self.name = name
        self.price = price
        self.volume = volume
    
    def is_rising(self,prev_price):
        if self.price>prev_price:
            return True
        else:
            return False
class ETF(Stock):
    def __init__(self, name, price, volume,tracking_error):
        super().__init__(name, price, volume)
        self.tracking_error = tracking_error