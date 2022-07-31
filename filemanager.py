from configuration import Configuration

def setup(config: Configuration):
    global folder_Main
    global folder_BS
    global folder_BS_New

    folder_Main = config.folder_Main



def identify_new_files():
    print(folder_Main)
