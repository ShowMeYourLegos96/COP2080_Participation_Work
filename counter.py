class Counter:
    def getStroke(self):
        return self._stroke
    
    def click(self):
        #if self._value > self._limit:
         #print("Limit Exceeded")
        self._stroke = self._stroke + '|'
    def reset(self):
        self._stroke = ""
    
    def _init_(self):
        self._limit =0
    def setLimit(self, maximum):
        self._limit = maximum
   