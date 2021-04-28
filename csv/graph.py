import numpy as np
import os


def recursive_sum(csv):
    raw_data = np.genfromtxt(csv, delimiter=',')
    dbm_data = raw_data.T[0]
    freq_data = raw_data.T[1]
    value_data = raw_data.T[2]
    mean_list = []
    counter_list = []
    try:
        mean = 0
        counter = 0
        for index,value in enumerate(freq_data):
            #print("index : {} freq : {} value : {}".format(index,value,value_data[index]))
            counter=counter+1
            mean = mean + value_data[index]
            if freq_data[index] != freq_data[index+1]:
                mean = (mean / counter)
                mean_list.append(mean)
                counter_list.append(counter)
                mean = 0
                counter = 0
    except IndexError:
        mean = (mean / counter)
        mean_list.append(mean)
        counter_list.append(counter)
        #print(mean_list)
        #print(counter_list)
        pass
    return mean_list,counter_list



if __name__ == "__main__":


    csvs = os.listdir("E:\OKUL\cn0150\cn0150_detector\csv")
    print(csvs)
    f = open("datas.txt", 'w')
    f_csv = open("datas.csv", 'w')

    for file in csvs:
        if "csv" in file:
            x, y = recursive_sum(file)
            print("File: {} mean : {} count : {}".format(file, x, y))
            f.write("File: {} mean : {} count : {}\n".format(file, x, y))
            f_csv.write("{},{},{}\n".format(file, x, y))
        else:
            pass







