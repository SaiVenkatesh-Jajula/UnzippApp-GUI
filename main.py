import PySimpleGUI as sg
import zipextractor as ze

label1=sg.Text("Select Archive:")
input1=sg.InputText()
choose1=sg.FileBrowse(key="filepath")

label2=sg.Text("Select Destination:")
input2=sg.InputText()
choose2=sg.FolderBrowse(key="folderpath")

Extract=sg.Button("Extract")


window = sg.Window("Archive Extractor", layout=[[label1,input1,choose1],
                                                [label2,input2,choose2],
                                                [Extract]])
while True:
    try:
        event, item = window.read()
        ze.extractor(item['filepath'],item['folderpath'])
        sg.popup("Extraction Completed! Please check.")
    except:
        print("Program Closed")
        break
window.close()