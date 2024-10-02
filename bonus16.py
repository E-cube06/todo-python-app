# import FreeSimpleGUI as sg
#
# labelA = sg.Text('Select files to compress')
# input_boxA = sg.Input()
# choose_ButtonA = sg.FilesBrowse('Choose')
#
# labelB = sg.Text('Select destination folder')
# input_boxB = sg.Input(tooltip='Enter a folder')
# choose_ButtonB = sg.FolderBrowse('Choose')
#
# compress_Button = sg.Button('Compress')
#
#
# window = sg.Window('File Zipper', layout=[[labelA, input_boxA, choose_ButtonA],[labelB, input_boxB, choose_ButtonB], [compress_Button]])
# window.read()
# window.close()
import FreeSimpleGUI as sg

label1 = sg.Text('Enter feet: ')
input_box1 = sg.InputText(tooltip='Enter feet')

label2 = sg.Text('Enter inches: ')
input_box2 = sg.InputText(tooltip='Enter inches')

convert_button = sg.Button('Convert')


window = sg.Window('Convertor', layout=[[label1, input_box1],
                                        [label2, input_box2],
                                        [convert_button]])
window.read()
window.close()

print('We are making progress')