import pymysql
import json

class Database():
    def selectdb():
        try:
            conn = pymysql.connect(host='localhost', user='root', password='1234', db='playdata', charset='utf8')
            cursor = conn.cursor()
            
            data = []
            cursor.execute("select * from emp")
            rows = cursor.fetchall()
            print(rows)
            data.append({"empno" : rows[0], "ename" : rows[1], "job" : rows[2], "mgr" : rows[3], "hiredate" : rows[4], "sal" :rows[5], "comm" : rows[6], "deptno" : rows[7]})

            
        except Exception as e:
            print(e)
        
        conn.commit()
        conn.close()
        print(data)
        return json.dumps(data)