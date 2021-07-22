import pymysql
import json

class Database():
    def selectdb():
        try:
            # conn = pymysql.connect(host='데이터베이스 엔드포인트(외부에 알려지면 안됨!)', user='root', password='1234', db='playdata', charset='utf8')
            conn = pymysql.connect(host='database-3.caefhfvxhncb.ap-northeast-2.rds.amazonaws.com', user='admin', password='playdata', db='playdata', charset='utf8')
            cursor = conn.cursor()
            
            data = []
            cursor.execute("select * from emp")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            # print(row)
            # data.append({"empno" : row[0], "ename" : row[1], "job" : row[2], "mgr" : row[3], "hiredate" : row[4], "sal" :row[5], "comm" : row[6], "deptno" : row[7]})
                data.append({"empno" : row[0], "ename" : row[1], "job" : row[2], "mgr" : row[3], "deptno" : row[7]})

            
        except Exception as e:
            print(e)
        
        conn.commit()
        conn.close()
        print(data)
        return json.dumps(data)