from pushbullet import Pushbullet
from datetime import datetime
from datetime import timedelta
import socket
import alert_teams

class push: 

    def __init__(self):
        #pb = Pushbullet("o.YmPu7RjOX6sMo1m1Zs1zvWGOQPAxTy7n")
        output_csv = "alerts_log.csv"
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        now = datetime.now()
        dt_string = now.strftime(("%d-%m-%Y"))
        ti_string = now.strftime(("%H:%M:%S"))
        
        with open(output_csv, 'r') as f:
            lines = f.read().splitlines()
            last_line = lines[-1].split(",")

        if len(lines) > 1:
            if (datetime.strptime(ti_string, "%H:%M:%S") - datetime.strptime(last_line[2], "%H:%M:%S")) > timedelta(minutes=2):
                alert_teams.alert_teams(hostname, dt_string, ti_string)
                
                with open(output_csv,"a") as f:
                    f.write(hostname + "," + dt_string + "," + ti_string + "," + ip_address)
                    f.write("\n")
        else:
            alert_teams.alert_teams(hostname, dt_string, ti_string)
            with open(output_csv,"a") as f:
                f.write(hostname + "," + dt_string + "," + ti_string + "," + ip_address)
                f.write("\n")
            
