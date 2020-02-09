print("############## NEW DATA ##############")
print("##################################")
print()
raw_data = open("SMSSpamCollection").read()
print(raw_data[0:500])

print("############## NEW DATA ##############")
print("##################################")
print()

parse_data = raw_data.replace("\t" , "\n").split("\n")
print(parse_data[0:10])



print("############## NEW DATA ##############")
print("##################################")
print()
label_list = parse_data[0::2]
msg_list = parse_data[1::2]
print(label_list[0:5])
print(msg_list[0:5])

print("############## NEW DATA ##############")
print("##################################")
print() 

import pandas as pd


table_frame = pd.DataFrame({

    "label" : label_list[:-1] ,
    "SMS" : msg_list

    })

print(table_frame.head())

print()
print("############## NEW DATA ##############")
print("##################################")
print()


# METHOD TWO OF IMPORTING DATA

dataset  = pd.read_csv("SMSSpamCollection" , sep="\t" , header=None)
print(dataset)

