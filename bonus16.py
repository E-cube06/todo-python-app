import FreeSimpleGUI as sg
from zip_creator import make_archive

labelA = sg.Text('Select files to compress')
input_boxA = sg.Input()
choose_ButtonA = sg.FilesBrowse('Choose', key='files')

labelB = sg.Text('Select destination folder')
input_boxB = sg.Input(tooltip='Enter a folder')
choose_ButtonB = sg.FolderBrowse('Choose', key='folder')

compress_Button = sg.Button('Compress')
output_label = sg.Text(key='output', text_color='green')


window = sg.Window('File Zipper',
                   layout=[[labelA, input_boxA, choose_ButtonA],
                           [labelB, input_boxB, choose_ButtonB],
                           [compress_Button, output_label]])
while True:
    event, values = window.read()
    print(event)
    print(values)
    filepaths = values['files'].split(';')
    folder = values['folder']
    make_archive(filepaths, folder)
    window['output'].update(value='Compression completed')
    print(filepaths)
    print(folder)

window.close()
# import FreeSimpleGUI as sg
#
# label1 = sg.Text('Enter feet: ')
# input_box1 = sg.InputText(tooltip='Enter feet')
#
# label2 = sg.Text('Enter inches: ')
# input_box2 = sg.InputText(tooltip='Enter inches')
#
# convert_button = sg.Button('Convert')
#
#
# window = sg.Window('Convertor', layout=[[label1, input_box1],
#                                         [label2, input_box2],
#                                         [convert_button]])
# while True:
#     event, values = window.read()
#     print(event)
#     print(values)
#
# window.close()
#
# print('We are really making progress')