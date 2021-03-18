
def string_transformer(splitted_test_string):
    for i in range(len(splitted_test_string)):
        if splitted_test_string[i]== "INT":
            splitted_test_string[i] = 0
        if splitted_test_string[i]== "BOOL":
            splitted_test_string[i] = 1
        if splitted_test_string[i]== "STRING":
            splitted_test_string[i] = 2
    return list(splitted_test_string)
test_string = "STRING G90 STRING G40 STRING G17"
splitted_test_string = test_string.split()
command_list = string_transformer(splitted_test_string)
def converter(command_list):
    data_to_send = ""
    for i in range(len(command_list)):
        if (isinstance(command_list[i],int)):
            if(command_list[i] == 0):
               data_to_send = data_to_send + ((0).to_bytes(1, byteorder ='little') + 
               (4).to_bytes(1, byteorder ='little') + (int(command_list[i+1])).to_bytes(4, byteorder ='little')).hex() + " "
            if(command_list[i]== 1):
                data_to_send = data_to_send + ((1).to_bytes(1, byteorder ='little') + 
                (1).to_bytes(1, byteorder ='little') + (int(command_list[i+1])).to_bytes(1, byteorder ='little')).hex() + " "
            if (command_list[i] == 2):
                data_to_send = data_to_send + ((2).to_bytes(1, byteorder ='little') + 
               (len(command_list[i+1])).to_bytes(1, byteorder ='little')).hex() + command_list[i+1].encode().hex() + " "
    print(data_to_send.upper())
converter(command_list)