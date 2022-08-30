import speedtest, datetime
class TSpeedMeasure:
    dSpeed = 0;
    dtNow = "";
    st = None
#------------------------------------------------------------------------------
    def __init__(self):
        self.dSpeed = 0;
        self.dtNow = "";
        self.st = speedtest.Speedtest()
#------------------------------------------------------------------------------
    def measure_time(self):
        self.dSpeed = self.st.download()
        self.dtNow = datetime.datetime.now()
#------------------------------------------------------------------------------
    def get_speed (self):
        return(self.dSpeed)
