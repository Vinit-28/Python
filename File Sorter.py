import os
import shutil
import tkinter as tk
import tkinter.messagebox as msg


base = tk.Tk()
base.geometry('400x200')
base.title('File Sorter')
path = tk.StringVar()
tk.Label(base,text = 'WELCOME TO THE FILE SORTER',font ='Bold' ).place(x=72,y=40)
tk.Label(base,text = 'Folder Path').place(x=80,y=80)
tk.Entry(base,text = path,width =15).place(x=200,y=80)
tk.Button(base,text = 'Exit',command = quit,bg='lightgrey').place(x=290,y=130)
def sort():
    if path.get() == '':
        msg.showinfo('Error','Please Enter The Path')
        quit
    else:
        path1 = path.get()

        ##-----------Trying to make folder to carry other folders or file without extensions-----------##
        try:
            os.mkdir(path + '\\Folder of other folders')
            signal = True
        
        ##-----------If the folder ocurrs with the same name-----------##
        except:
            signal = False
        

        list_of_directories = os.listdir(path1)  ##-----------Variable to carry the list directories present in the folder-----------##
        list_of_file_formats = []  ##-----------Variable to store the number of file formats present ith directory-----------##

        ##-----------Getting into action-----------##     
        for folder_file in list_of_directories:

            ##-----------Trying to Process the work-----------##
            try:
                extension = folder_file.split('.')[1]   ##-----------Variable to store the extension-----------##

                ##-----------storing deifferent extensions in the variable "list_of_file_formats" and making directory the same name-----------##
                if '.' + extension not in list_of_file_formats:
                    os.mkdir(path1+"\\folder of '." + extension + "'")
            
                    list_of_file_formats.append('.' + extension)
                
                ##-----------If the extension is already present in the list thenwe have to move the file in that respective folder-----------##
                if '.' + extension in list_of_file_formats:
                    source_path =  path1 + '\\' + folder_file
                    destination_path = path1 + "\\folder of '." + extension + "'\\" + folder_file
                    
                    shutil.move(source_path,destination_path)
 
            ##-----------If an indexerror ocurrs due to line no.40-----------##
            except IndexError:
                signal = False  ##-----------Making Signal "False" so that we cannot delete it because it contains other files-----------##
                source_path =  path1 + '\\' + folder_file
                destination_path = path1 + "\\Folder of other folders\\" + folder_file

                ##-----------If "Folder of other folders" is aready present then we can't we it into itself-----------##
                if path1 + "\\Folder of other folders" is not source_path :
                    shutil.move(source_path,destination_path)

            ##-----------If other exception ocuurs-----------##
            except:
                pass
            
        ##-----------If the folder that we make earlier is not used the we have to delete it-----------##
        if signal:
            shutil.rmtree(path1 + "//Folder of other folders")

        msg.showinfo('Complete','Sorting completed')
        quit

tk.Button(base,text = 'Start',command = sort,bg='lightgrey').place(x=50,y=130)
base.mainloop()
