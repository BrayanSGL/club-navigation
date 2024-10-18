from flask import Flask
from datetime import datetime, timedelta

app = Flask(__name__)
@app.route('/clock')
def clock():
    now = datetime.now()
    start_of_day = datetime(now.year, now.month, now.day)
    milliseconds_since_start_of_day = (now - start_of_day).total_seconds() * 1000
    new_time = milliseconds_since_start_of_day * 48
    new_date = start_of_day + timedelta(milliseconds=new_time)
    return new_date.strftime('%Y-%m-%d %H:%M:%S')
    
  
if __name__ == '__main__':
    app.run(host="0.0.0.0" , port=5000) 