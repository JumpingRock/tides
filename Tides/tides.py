import datetime
import tideClasses as tc
import tideFunctions as tf

charl = tc.Notify(tc.Station('SCarolina', '8665530'), tc.Date(str(datetime.datetime.now().month), str(datetime.datetime.now().year)), str(datetime.datetime.now().day))
eliza = tc.Notify(tc.Station('Georgia', '8677344'), tc.Date(str(datetime.datetime.now().month), str(datetime.datetime.now().year)), str(datetime.datetime.now().day))
tf.plot(charl)