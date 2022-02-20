import time


lc_time = time.localtime()

def current_time_in_header():
    
    current_year = lc_time[0] #years
    current_month = lc_time[1] #months
    current_day = lc_time[2] #days
    current_hour = lc_time[3] #hours
    current_minute = lc_time[4] #minutes
    current_second = lc_time[5] #seconds
    
    for i in range(1,5):
        if lc_time[1] < 10:
              current_month = str(0) + str(lc_time[1])
        if lc_time[2] < 10:
            current_day = str(0) + str(lc_time[2])
        if lc_time[3] < 10:
            current_hour = str(0) + str(lc_time[3])
        if lc_time[4] < 10:
            current_minute = str(0) + str(lc_time[4])
        if lc_time[5] < 10:
            current_second = str(0) + str(lc_time[5])
            
        
        
        return str(current_year) +"_"+ str(current_month) + "_" + str(current_day) + "_" + str(current_hour) + "_" + str(current_minute) + "_" + str(current_second)    
      
        
        

print(current_time_in_header())