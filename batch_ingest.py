import os
import happybase
from datetime import datetime
#create connection
connection = happybase.Connection('localhost')
#open connection to perform operations
def open_connection():
    connection.open()
#close the opened connection
def close_connection():
    connection.close()
#get the pointer to a table
def get_table(name):
    open_connection()
    table = connection.table(name)
    close_connection()
    return table
#batch insert data
def batch_insert_data(filename):
    print("Starting batch insert")
    file = open(filename, "r")
    table_name = 'yellow_taxi_1'
    table = get_table(table_name)
    open_connection()
    start_time = datetime.now()
    i = 0
    line_num = 0
    with table.batch(batch_size=50000) as b:
        print('inside with:')
        for line in file:
            
            if line_num % 1000 == 0:
                print(line_num, 'Lines loaded')
            if i!=0:
                temp = line.strip().split(",")
                b.put(temp[0]+":"+temp[1]+":"+temp[2] , 
                { import os
import happybase
from datetime import datetime
#create connection
connection = happybase.Connection('localhost')
#open connection to perform operations
def open_connection():
    connection.open()
#close the opened connection
def close_connection():
    connection.close()
#get the pointer to a table
def get_table(name):
    open_connection()
    table = connection.table(name)
    close_connection()
    return table
#batch insert data
def batch_insert_data(filename):
    print("Starting batch insert")
    file = open(filename, "r")
    table_name = 'yellow_taxi'
    table = get_table(table_name)
    open_connection()
    start_time = datetime.now()
    i = 0
    line_num = 0
    with table.batch(batch_size=50000) as b:
        print('inside with:')
        for line in file:
            
            if line_num % 1000 == 0:
                print(line_num, 'Lines loaded')
            if i!=0:
                temp = line.strip().split(",")
                b.put(temp[0]+":"+temp[1]+":"+temp[2] , 
                { 'Trip_Details:VendorID':temp[0] ,'Trip_Details:tpep_pickup_datetime':temp[1] ,
                 'Trip_Details:tpep_dropoff_datetime':temp[2] ,
                  'Trip_Details:passenger_count':temp[3] ,'Trip_Details:trip_distance':temp[4] ,
                 'Trip_Details:RatecodeID':temp[5] ,'Trip_Details:store_and_fwd_flag':temp[6] ,
                 'Trip_Details:PULocationID':temp[7] ,'Trip_Details:DOLocationID':temp[8] ,
                 'Trip_Details:payment_type':temp[9] ,'Trip_Details:fare_amount':temp[10] ,
                 'Trip_Details:extra':temp[11] ,'Trip_Details:mta_tax':temp[12] ,
                 'Trip_Details:tip_amount':temp[13] ,'Trip_Details:tolls_amount':temp[14] ,
                 'Trip_Details:improvement_surcharge':temp[15] ,'Trip_Details:total_amount':temp[16] ,
                 'Trip_Details:congestion_surcharge':temp[17] ,'Trip_Details:airport_fee':temp[18]
                })
            i+=1
            line_num+= 1
        file.close()
        print("batch insert done line_num :",line_num)
        
        print(" ======================================================================================== ")
        print(" =============================== Completion of insertion ================================ ")
        print(" =================================== File: ",filename,"================================== ")
        print(" ====================== Run time: ",datetime.now()-start_time," ========================= ")
        print(" ======================================================================================== ")
        close_connection()
                

for filename in os.listdir() :
     if filename.startswith("yellow_tripdata_"):
        print('Loading data in '+filename)
        batch_insert_data(filename)
                })
            i+=1
            line_num+= 1
        file.close()
        print("batch insert done line_num :",line_num)
        
        print(" ======================================================================================== ")
        print(" =============================== Completion of insertion ================================ ")
        print(" =================================== File: ",filename,"================================== ")
        print(" ====================== Run time: ",datetime.now()-start_time," ========================= ")
        print(" ======================================================================================== ")
        close_connection()
                

for filename in os.listdir() :
     if filename.startswith("yellow_tripdata_"):
        print('Loading data in '+filename)
        batch_insert_data(filename)