from flask import session
import ibm_db
import hashlib
import datetime
import os

class Db:
    def __init__(self) -> None:
        hostname="ea286ace-86c7-4d5b-8580-3fbfa46b1c66.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
        uid="ljr08913"
        pwd="0wfoXAtjinaXZZxO"
        driver="{IBM DB2 ODBC DRIVER}"
        db="bludb"
        port="31505"
        cert="DigiCertGlobalRootCA.crt"
        dsn=(
                "DATABASE={0};"
                "HOSTNAME={1};"
                "PORT={2};"
                "UID={3};"
                "SECURITY=SSL;"
                "SSLServerCertificate={4};"
                "PWD={5};"
            
        ).format(db,hostname,port,uid,cert,pwd)
        self.conn=ibm_db.connect("dsn",'','')
        
    def generateId(self) -> str:
        return hashlib.md5("{}{}".format(
                session["active"],
                datetime.datetime.now().strftime('%m%d%Y%H%M%S%f')
                ).encode()).hexdigest()

    def execute(self, query: str) -> bool:
        try:
            ibm_db.exec_immediate(self.conn, query)
            return True
        except:
            print("SQLSTATE = {}".format(ibm_db.stmt_error()))
            return False
    
    def get(self, table_name: str, condition: str, columns : str = "*") -> tuple:
        try:
            query = f"SELECT {columns} FROM {table_name} WHERE {condition}"
            print(query)
            stmt = ibm_db.exec_immediate(self.conn, query)
            return ibm_db.fetch_tuple(stmt)
        except:
            print("SQLSTATE = {}".format(ibm_db.stmt_error()))
            return ()

    def getall(self, table_name: str, condition: str, columns : str = "*") -> list:
        query = f"SELECT {columns} FROM {table_name} WHERE {condition}"
        print(query)
        stmt = ibm_db.exec_immediate(self.conn, query)
        data = []
        while True:     
            temp = ibm_db.fetch_tuple(stmt) 
            if temp != False:       
                data.append(temp)
            else:
                break
        return data

    def delete(self, table_name:str, condition: str) -> bool:
        query = f"DELETE FROM {table_name} WHERE {condition}"
        print(query)
        return self.execute(query)

    def insert(self, table_name: str, values: list) -> bool:
        try:
            valuestup = ','.join("'{0}'".format(x) for x in values)
            query = f'INSERT INTO {table_name} VALUES ({valuestup})'  
            print(query)
            return self.execute(query)            
        except Exception as e:
            print(e)
            return False       