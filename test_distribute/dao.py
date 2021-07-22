import pymysql
import json

class Database():
    def selectdb():
        conn = pymysql.connect(host='해당 데이터베이스의 엔드포인트!!', user='admin', password='playdata', db='playdata', charset='utf8')
        cursor = conn.cursor()
        
        data = []
        cursor.execute("select * from emp")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        # print(row)
        # data.append({"empno" : row[0], "ename" : row[1], "job" : row[2], "mgr" : row[3], "hiredate" : row[4], "sal" :row[5], "comm" : row[6], "deptno" : row[7]})
            data.append({"empno" : row[0], "ename" : row[1], "job" : row[2], "mgr" : row[3], "deptno" : row[7]})

        
        conn.commit()
        conn.close()
        print(data)
        return json.dumps(data)