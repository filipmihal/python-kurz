import pymysql
#test
def ConnectToDB():
    return pymysql.connect(host="localhost",   
        user="root", # your username
        passwd="", # your password
        db="test",
        charset='utf8') 
    