from os import stat

#Function for loading a sequence from input txt file
def SequenceFromFile(file_name):
    try:
        with open(file_name, encoding="utf-8") as f:
            if stat(file_name).st_size == 0:
                print("File is empty.")
                quit()
            data = f.read().split()
            return data
    except FileNotFoundError:
        print(f"Cannot open file {file_name}. The file does not exist or the path to the file is incorrect")
        quit()
    except PermissionError:
        print(f"Program doesn't have permisson to acces file {file_name}.")
        quit()
    except Exception as e:
        print(f"Unexpected error opening {file_name}: {e}")
        quit()

#Function for writing into output txt file
def WriteToFile(file_name, text):
    try:
        with open(file_name, mode="a", encoding="utf-8") as f:
            return f.write(str(text))
    except FileNotFoundError:
        print(f"Cannot open file {file_name}. The file does not exist or the path to the file is incorrect")
        quit()
    except PermissionError:
        print(f"Program doesn't have permisson to acces file {file_name}.")
        quit()
    except Exception as e:
        print(f"Unexpected error opening {file_name}: {e}")
        quit()
    
#Function for converting string elements into integers
def StrToInt(list):
    sequence = []
    index = -1
    for x in list:
        index += 1
        try:
            y = int(x)
            sequence.append(y)
        except ValueError:
            print(f"Element in position {index} in {list} is not a number and the program will skip this element")
            continue
    return sequence

#Function for ascending sorting of list values
def SortList(input_list):
    for i in range(len(input_list)):
        min = i
        for j in range(i+1, len(input_list)):
            if input_list[min] > input_list[j]:
                min = j
        input_list[i], input_list[min] = input_list[min], input_list[i]
    return input_list

#Function for recognition of duplicate elements, storing their quantity and saving unique elements into new sequence and output file
def DeleteDuplicates(input_list, final_list, dictionary):
    i = 0
    while i < (len(input_list)-1):
        j = i+1
        if input_list[i] != input_list[j] and input_list[i] not in final_list:
            final_list.append(input_list[i])
            WriteToFile("output.txt", f"{input_list[i]} ")
        else:
            dictionary[input_list[i]] = dictionary.setdefault(input_list[j], 0) + 1
        i+=1

    #Check if the last element is in final list, if not append it
    max = len(input_list)-1
    if input_list[max] not in final_list:
        final_list.append(input_list[max])
        WriteToFile("output.txt", f"{input_list[max]} ")

#Loading sequence from file, converting elements into integers, sorting it and deleting duplicate elements
final = []
duplicates = {}
sequence = SortList(StrToInt(SequenceFromFile("input.txt")))
DeleteDuplicates(sequence, final, duplicates)

#Loop for writing duplicate elements and their quantity into output file
WriteToFile("output.txt", f"\n\nThese duplicate elements ({sum(duplicates.values())} in total) were deleted from original sequence:\n")
for (key, val) in duplicates.items():
    WriteToFile("output.txt", f"{key} - {val}x\n")