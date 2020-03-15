import psycopg2
import postgres_copy
import matplotlib.pyplot as plot
import matplotlib.style as style
import pandas as pd
import numpy as np
def hitsfunc():
    con = psycopg2.connect(database="postgres", user="postgres", password="1234", host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute("COPY adminpanel_hit TO 'D:\\Vethics\\BLECONS\\Panel\\dashboard\\hits.csv' DELIMITER ',' CSV HEADER;")
    # style.use('ggplot')
    df=pd.read_csv("hits.csv")
    df.plot.bar(x = 'dept_name', y = 'hits')
    plot.title('chart')
    plot.savefig('D:\Vethics\\BLECONS\\Panel\\dashboard\\adminpanel\\static\\m1.png')
    # plot.show()
    con.close()
    
