import os


def find_csv():
    # -------------------------------------------------------------------
    # Look for files in the "csv" folder under the main folder.
    print(os.getcwd())
    print()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.path.join(dir_path, "csv\\csv-new")
    print("Looking for files in " + dir_path + ".")
    print()
    files = os.listdir(dir_path)
    print(str(len(files)) + " files were found.")

    # Determine the longest file name size
    files_num_max_len = len(max(files, key=len))

    for files_num in files:
        print(files_num, end=' ')
        if len(files_num) == 47:
            print(" " * (files_num_max_len - len(files_num)), end='')
            print("This file is from an ING bank account")
        elif len(files_num) == 24:
            print(" " * (files_num_max_len - len(files_num)), end='')
            print("This file is from a BNP bank account")
        elif len(files_num) == 19:
            print(" " * (files_num_max_len - len(files_num)), end='')
            print("This file is a master CSV file")
        else:
            print(" " * (files_num_max_len - len(files_num)), end='')
            print("This file is from an unidentified bank account")
            raise Exception("Unidentified bank account")

    print()

    return files
