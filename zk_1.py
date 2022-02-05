#Function for loading a sequence from input txt file
def SequenceFromFile(file_name):
    try:
        with open(file_name, encoding="utf-8") as f:
            data = f.read().split()
    except FileNotFoundError:
        print(f"Cannot open file {file_name}. The file does not exist or the path to the file is incorect")
        quit()
    except PermissionError:
        print(f"Program doesn't have permisson to acces file {file_name}.")
        quit()
    except EOFError:
        print(f"File {file_name} is empty.")
        quit()
    except:
        print(f"Unexpected error opening {file_name}")
        quit()
    return data

#Function for writing into output txt file
def WriteToFile(file_name, text):
    try:
        with open(file_name, mode="a", encoding="utf-8") as f:
            return f.write(str(text))
    except FileNotFoundError:
        print(f"Cannot open file {file_name}. The file does not exist or the path to the file is incorect")
        quit()
    except PermissionError:
        print(f"Program doesn't have permisson to acces file {file_name}.")
        quit()
    except:
        print(f"Unexpected error opening {file_name}")
        quit()
    
#Loading sequence from input file and initialization of variables
sequence = SequenceFromFile("input.txt")
final_sequence = []
duplicates = {}
index = 0

#Loop for recognition of duplicate elements, storing their quantity and saving unique elements into new sequence and output file
for object in sequence:
    try:
        element = int(object)
    except ValueError:
        print(f"Element in position {index} is not a number and the program will skip this element")
        continue
    except:
        print(f"Unexpected error occurred with element in position {index} and the program will skip it")
    
    if element in final_sequence:
        duplicates[element] = duplicates.setdefault(element, 0) + 1
    else:
        final_sequence.append(element) 
        WriteToFile("output.txt", f"{element} ")
    index += 1

#Loop for writing duplicate elements and their quantity into output file
WriteToFile("output.txt", f"\n\nThese duplicate elements ({sum(duplicates.values())} in total) were deleted from original sequence:\n")
for (key, val) in duplicates.items():
    WriteToFile("output.txt", f"{key} - {val}x\n")

#print(sequence)
#print(final_sequence)
#print(duplicates)
