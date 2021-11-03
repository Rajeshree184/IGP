import pandas as pd
import csv
import re
import math
import matplotlib.pyplot as plt
import xlrd
#input1 = input("Enter the name of the file: ")
workbook = xlrd.open_workbook('compositionexpbygrossincomedeciletofye20final.xlsx')
worksheet = workbook.sheet_by_name('One adult retired')
data = pd.read_excel ("compositionexpbygrossincomedeciletofye20final.xlsx", sheet_name=None)
worksheet  = workbook.sheet_by_index(1)
keys = [worksheet.cell(0, col_index).value for col_index in range(worksheet.ncols)]

boundry_group = []

xbx = []
num_rows = worksheet.nrows - 1
num_cells = worksheet.ncols - 1
curr_row = -1

list_out = []
list_in = []
while curr_row < num_rows:
  curr_row += 1
  row = worksheet.row(curr_row)
  print ('Row:', curr_row)
  
  curr_cell = -1
  x = 0
  list_in = []
  while curr_cell < num_cells:
  
    curr_cell += 1
    # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
    cell_type = worksheet.cell_type(curr_row, curr_cell)
    cell_value = worksheet.cell_value(curr_row, curr_cell)
    if cell_type !=0 and cell_type!=1:
    
        if cell_value=="..":
            cell_value =0
        
        print (' ', cell_type, ':', cell_value)
        list_in.append(cell_value)
        
  list_out.append(list_in)
        

f = open("tfile.csv", "a")
        
for x in list_out:
    for y in x:
        f.write(str(y)+",")
    f.write("\n")
def mean_function(list):
    sum = 0
    mean = 0
    count = 0
    for x in list:
        sum = sum + float(x)
        count += 1
    mean  = float(sum / count)
    print("Mean: "+str(mean))
    return str(mean)
        

def stdev_function(list):
    sum = 0
    mean = 0
    count = 0
    for x in list:
        sum = sum + float(x)
        count += 1
    mean  = float(sum / count)
    stdev = 0
    sum = 0
    
    for x in list:
        sum = sum  + float(pow((mean - float(x)),2))
        
    
    stdev  = float(sum /count)
    stdev = math.sqrt(stdev)
    print("Stdev: "+ str(stdev))
    return str(stdev)


def min_value(list):
    min = list[0]
    
    for x in list:
        if (min > float(x)):
            min = float(x)
    print("Minimum: " + str(min))
    return str(min)
    


def max_value(list):
    max = 0
    
    for x in list:
        if (max < float(x)):
            max = float(x)
    print("Maximum: "+ str(max))
    return str(max)
    

def percentile_value(list,n):
    size = len(list)
    x = float(float(n/100.0) * float(size))
    
    list.sort()
    
    list[int(x)]
   
    y = x
    i = []
    for k in list:
        i.append(float(k))
    
    i.sort()
    print(str(n)+ "%: "+ str(i[int(y)]))
    return str(i[int(y)])


def stats(list):
    count = 0
    for x in list:
        count += 1
    print("Count: "+ str(count))
    
    mean_function(list)
    stdev_function(list)
    min_value(list)
    percentile_value(list,25)
    percentile_value(list,50)
    percentile_value(list,75)
    
    max_value(list)

def CSV_READ_full_data_stats(name):
    
    
    with open(name, 'r') as file:
        my_reader = csv.reader(file, delimiter=',')
        list_of_csv = []
        count = 0
        for row in my_reader:
            list_of_csv.append(row)
        list_full = []
        list_name  = []
        for column in range (0,len(list_of_csv[0])):
            list_print = []
            
            list_name.append(str(list_of_csv[0][column]) + ":")
            #print(str(list_of_csv[0][column]) + ":")
            for i in range(1,len(list_of_csv)):
                if column < len(list_of_csv[i]):
                    
                    list_print.append(list_of_csv[i][column])
                
            
            #print(list_print)
            list_full.append(list_print)
            #point = dict.fromkeys(list_print, str(list_of_csv[0][column]) + ":")
            
        for x in range(0,len(list_full)):
            for y in range(0,len(list_full[x])):
                if list_full[x][y] == '':
                    list_full[x][y] = 0
        
        i=0
        #print(list_full)
        
        list_stats = []
        list_full_stats = []
        for i in range(0, len(list_full)):
            for y in range (0,len(list_full[i])):
                list_full[i][y] = float(list_full[i][y])
      
        for x in list_full:
            list_stats = []
            y = str()
            
            #str(y).replace("Mean: "," ")
             
            
            print(list_stats)
            # Printing modified list
            #print ("Modified list is : " + str(test_list))
          
           
            list_stats.append(len(x))
            
            list_stats.append(mean_function(x))
            list_stats.append(stdev_function(x))
            list_stats.append(min_value(x))
            list_stats.append(percentile_value(x,25))
            list_stats.append(percentile_value(x,50))
            list_stats.append(percentile_value(x,75))
            
            list_stats.append(max(x))
            
            
            
            #print(mean[0].replace("a"," "))
            #print(mean)
            
            list_full_stats.append(list_stats)
          
        print(list_stats)
        
    import matplotlib.pyplot as plt
    
    print(list_stats[0])
    x = [4,5,6]
    y = [[1,2,3],[4,5,6],[7,8,9]]
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("A test graph")
    for i in range(len(y[0])):
        plt.plot(x,[pt[i] for pt in y],label = 'id %s'%i)
    plt.legend()
    plt.show()
    
    print(dict(zip(list_name,list_full_stats)))
    return dict(zip(list_name,list_full_stats ))
        
        
   
def to_table(name):
    dic = CSV_READ_full_data_stats(name)
    print("\n\n\n")
    print("\n\n\n")
    k = []
    for row in zip(*([key] + (value) for key, value in sorted(dic.items()))):
        k.append(re.sub(r"\((.*?)\)", r"\1", str(row)))
    count = 0
    
    print("\n")
    
    
    
    print("\n")
    for x in k:
        
        if (count == 0) :
            print("\n")
        
           
        count += 1
        
print("\n\n\n")
print("\n\n\n")
to_table("tfile.csv")

