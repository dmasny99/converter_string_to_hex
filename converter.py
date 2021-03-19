
def string_transformer(string_data):
    splitted_test_string = string_data.split()
    for i in range(len(splitted_test_string)):
        if splitted_test_string[i]== "INT":
            splitted_test_string[i] = 0
        if splitted_test_string[i]== "BOOL":
            splitted_test_string[i] = 1
        if splitted_test_string[i]== "STRING":
            splitted_test_string[i] = 2
    return list(splitted_test_string)

def validation(list_in,list_out):
    try:
        for i in range(len(input_list)):
            if(input_list[i] == output_list[i]):
                return True
            else:
                print(i)
                return False
    except Exception:
        print("Exception has occured")

def converter(string_data):
    command_list = string_transformer(string_data)
    data_to_send = ""
    for i in range(len(command_list)):
        if (isinstance(command_list[i],int)):
            if(command_list[i] == 0):
               data_to_send = data_to_send + ((0).to_bytes(1, byteorder ='little') + 
               (4).to_bytes(1, byteorder ='little')).hex()
               if (int(command_list[i+1]) >= 0):
                   data_to_send = data_to_send + int(command_list[i+1]).to_bytes(4, byteorder ='little', signed = False).hex() + " "
               if (int(command_list[i+1]) < 0):
                   data_to_send = data_to_send + int(command_list[i+1]).to_bytes(4,byteorder ='little', signed = True).hex() + " "
            if(command_list[i]== 1):
                data_to_send = data_to_send + ((1).to_bytes(1, byteorder ='little') + 
                (1).to_bytes(1, byteorder ='little') + (int(command_list[i+1])).to_bytes(1, byteorder ='little')).hex() + " "
            if (command_list[i] == 2):
                data_to_send = data_to_send + ((2).to_bytes(1, byteorder ='little') + 
               (len(command_list[i+1])).to_bytes(1, byteorder ='little')).hex() + command_list[i+1].encode().hex() + " "
    return(data_to_send.upper())

input_list =[]
output_list =[]

with open('test_data.txt', 'r') as f:
    nums = f.read().splitlines()
    for s in nums:
        input_list.append(converter(s))
with open('test_data_output.txt', 'r') as f:
    nums = f.read().splitlines()
    for s in nums:
        output_list.append(s)
test_string = "INT -10"

print(input_list,validation(input_list,output_list))
#converter(test_string)