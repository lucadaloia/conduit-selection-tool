#from ConduitFill import last_oid
from tkinter import *
import sqlite3
from PIL import ImageTk, Image
import os

# --- GLOBAL VARIABLE INITIALIZATION ---
# Logic & Math Variables
total_amount = 0
cable_total_area = 0.0
percentage = 0.0
last_oid = 0

# Lists for Data Processing
num_list = []
num_list1 = []
areas_list = []

# GUI Component Handles (initialized as None)
pg1 = None
table_frame = None
answer_frame = None
select = None

# Tkinter Entry/Variable Objects
name = None
name_editor = None
amount = None
amount_editor = None
diam = None
diam_editor = None
delete_text_box = None
id_select_entry = None
name_cable = None
# ---------------------------------------

root = Tk()
root.geometry('920x560+10+210')
root.title('Conduit Program')
icon_name = 'icon.ico'
root.iconbitmap(icon_name)
connect = sqlite3.connect('cable_book.db')
c = connect.cursor()
def page_1():
    pg1 = Frame(root, width=920, height=560).place(x=0, y=0, anchor=NW)
    table_frame = Tk()
    table_frame.title('Cable Records')
    table_frame.geometry('0x0+10+10')
    icon_name = 'icon.ico'
    table_frame.iconbitmap(icon_name)
    def submit():
        connect = sqlite3.connect('cable_book.db')
        c = connect.cursor()
        test = name.get()
        test2 = diam.get()
        test3 = amount.get()
        if test!= '' and test2!= '' and (test3!= ''):
            c.execute('INSERT INTO cables VALUES (:name, :diam, :amount)', {'name': name.get(), 'diam': diam.get(), 'amount': amount.get()})
            connect.commit()
        else:
            return None
        name.delete(0, END)
        diam.delete(0, END)
        amount.delete(0, END)
        update()
    def open():
        table_frame = Tk()
        table_frame.title('Cable Records')
        table_frame.geometry('920x160+10+10')
        table_frame.grid_propagate(FALSE)
        icon_name = 'icon.ico'
        table_frame.iconbitmap(icon_name)
    def delete():
        connect = sqlite3.connect('cable_book.db')
        c = connect.cursor()
        c.execute('DELETE FROM cables WHERE oid=' + delete_text_box.get())
        connect.commit()
        update()
    def delete_all():
        connect = sqlite3.connect('cable_book.db')
        c = connect.cursor()
        c.execute('DELETE FROM cables')
        connect.commit()
        update()
        connect.close()
    def select():
        connect = sqlite3.connect('cable_book.db')
        c = connect.cursor()
        id_selected = id_select_entry.get()
        c.execute('SELECT * FROM cables WHERE oid = ' + id_selected)
        table = c.fetchall()
        show_name = ''
        show_diam = ''
        show_amount = ''
        name_show = ''
        diam_show = ''
        amount_show = ''
        for data in table:
            show_name += str(data[0]) + '\n'
            show_diam += str(data[1]) + '\n'
            show_amount += str(data[2]) + '\n'
            name_show = str(data[0])
            diam_show = str(data[1])
            amount_show = str(data[2])
        name_editor.insert(0, name_show)
        diam_editor.insert(0, diam_show)
        amount_editor.insert(0, amount_show)
    def create_list(n):
        list = []
        for i in range(1, n + 1):
            list.append(i)
        return list
    total_amount = ''
    def count():
        num_list1 = []
        num_list = []
        connect = sqlite3.connect('cable_book.db')
        c = connect.cursor()
        c.execute('SELECT cable_amount FROM cables')
        num1 = str(c.fetchall())
        num_list = (item for item in num1 if item not in ['[', ']', ',', ')', '(', ' '])
        print(num_list)
        for value in num_list:
            int_value = int(value)
            num_list1.append(int_value)
        num_sum = sum(num_list1)
        total_amount = int(num_sum)
        connect.close()
    def generate():
        answer_frame = Frame(pg1, width=900, height=190, bg='gray94', highlightbackground='gray', highlightthickness=1)
        answer_frame.place(x=10, y=360, anchor=NW)
        answer_frame.grid_propagate(FALSE)
        def update_answer():
            """\n            blank = Label(answer_frame, text = \"\")\n            blank.grid(row = 0, column = 3, sticky = W)\n            blank1 = Label(answer_frame, text = \"\")\n            blank1.grid(row = 1, column= 3, sticky = W, columnspan=2)\n            return\n            """

            close(answer_frame)
            answer_frame = Frame(pg1, width=900, height=190, bg='gray94', highlightbackground='gray', highlightthickness=1)
            answer_frame.place(x=10, y=360, anchor=NW)
            answer_frame.grid_propagate(FALSE)
        update_answer()
        pi = 3.141592653589793
        import math
        import os
        import time
        def CAT6(x):
            y = x / 2
            z = pow(y, 2) * pi
            return z
        class Cable:
            def __init__(self, name):
                self.name = name
                self.area = None
                self.num_cables = None
        connect = sqlite3.connect('cable_book.db')
        c = connect.cursor()
        total_num_cables = total_amount
        if total_num_cables == int(1):
            percentage = 0.53
            percent = str('53%')
        else:
            if total_num_cables == int(2):
                percentage = 0.31
                percent = str('31%')
            else:
                percentage = 0.4
                percent = str('40%')
        select = ''
        areas_list = []
        for num in create_list(last_oid):
            select = str(num)
            real_select = str(int(select) - 1)
            c.execute('SELECT * FROM cables WHERE oid = ' + select)
            table = c.fetchall()
            cable_area = ''
            calc_diam = ''
            calc_amount = ''
            calc_name = ''
            float_calc_diam = ''
            name = ''
            cable_area_label = ''
            overall_area = ''
            for data in table:
                name = 'The total area of ' + data[0] + ' cables is: '
                cable_area = CAT6(data[1])
                cable_total_area = cable_area * data[2]
                rounded_area = round(cable_total_area, 4)
                cable_area_label = str(rounded_area)
                name_cable = data[0]
            connect = sqlite3.connect('areas.db')
            c2 = connect.cursor()
            c2.execute('INSERT INTO areas (cable_area) VALUES (?)', (float(cable_total_area),))
            connect.commit()
            connect = sqlite3.connect('areas.db')
            c2 = connect.cursor()
            c2.execute('SELECT cable_area FROM areas WHERE oid = ' + select)
            table2 = c2.fetchone()
            c2.execute('SELECT cable_area FROM areas WHERE oid = ' + select)
            table1 = c2.fetchone()
            table1_area = table1[0]
            table1_str = str(table1)
            stripped_table1 = table1_str.strip('(,)')
            float_table1 = float(stripped_table1)
            areas_list.append(float_table1)
        overall_area = sum(areas_list)
        rounded_overall_area = round(overall_area, 4)
        overall_area_label = Label(answer_frame, text='The total area of all the cables in squared inches is: ', padx=2, pady=2)
        overall_area_label.grid(row=1, column=0, sticky=W)
        overall_area_value = Label(answer_frame, text=str(rounded_overall_area), font=('', 11), fg='red')
        overall_area_value.grid(row=1, column=3, sticky=W, columnspan=2)
        cond_05 = 0.632
        cond_area_05 = pow(cond_05 / 2, 2) * pi
        cond_area_percent_05 = cond_area_05 * float(percentage)
        cond_075 = 0.836
        cond_area_075 = pow(cond_075 / 2, 2) * pi
        cond_area_percent_075 = cond_area_075 * float(percentage)
        cond_1 = 1.063
        cond_area_1 = pow(cond_1 / 2, 2) * pi
        cond_area_percent_1 = cond_area_1 * float(percentage)
        cond_125 = 1.394
        cond_area_125 = pow(cond_125 / 2, 2) * pi
        cond_area_percent_125 = cond_area_125 * float(percentage)
        cond_15 = 1.624
        cond_area_15 = pow(cond_15 / 2, 2) * pi
        cond_area_percent_15 = cond_area_15 * float(percentage)
        cond_2 = 2.083
        cond_area_2 = pow(cond_2 / 2, 2) * pi
        cond_area_percent_2 = cond_area_2 * float(percentage)
        cond_25 = 2.489
        cond_area_25 = pow(cond_25 / 2, 2) * pi
        cond_area_percent_25 = cond_area_25 * float(percentage)
        cond_3 = 3.09
        cond_area_3 = pow(cond_3 / 2, 2) * pi
        cond_area_percent_3 = cond_area_3 * float(percentage)
        cond_35 = 3.57
        cond_area_35 = pow(cond_35 / 2, 2) * pi
        cond_area_percent_35 = cond_area_35 * float(percentage)
        cond_4 = 4.05
        cond_area_4 = pow(cond_4 / 2, 2) * pi
        cond_area_percent_4 = cond_area_4 * float(percentage)
        cond_5 = 5.073
        cond_area_5 = pow(cond_5 / 2, 2) * pi
        cond_area_percent_5 = cond_area_5 * float(percentage)
        cond_6 = 6.093
        cond_area_6 = pow(cond_6 / 2, 2) * pi
        cond_area_percent_6 = cond_area_6 * float(percentage)
        print(total_num_cables)
        print(percentage)
        print(cond_6, ':', cond_area_6 * percentage)
        print(cond_5, ':', cond_area_5 * percentage)
        print(cond_4, ':', cond_area_4 * percentage)
        print(cond_35, ':', cond_area_35 * percentage)
        print(cond_3, ':', cond_area_3 * percentage)
        print(cond_25, ':', cond_area_25 * percentage)
        print(cond_2, ':', cond_area_2 * percentage)
        print(cond_15, ':', cond_area_15 * percentage)
        print(cond_1, ':', cond_area_1 * percentage)
        print(cond_075, ':', cond_area_075 * percentage)
        print(cond_05, ':', cond_area_05 * percentage)
        print('overall area:', overall_area)
        if overall_area <= cond_area_percent_05:
            smallest = str('1/2 (0.5)')
            smallest_cond = Label(answer_frame, text='The smallest conduit that can hold these cables is: ', font=('', 9))
            smallest_cond.grid(row=0, column=0, columnspan=3, sticky=W)
        else:
            if overall_area <= cond_area_percent_075:
                smallest = str('3/4 (0.75)')
                smallest_cond = Label(answer_frame, text='The smallest conduit that can hold these cables is: ', font=('', 9))
                smallest_cond.grid(row=0, column=0, columnspan=3, sticky=W)
            else:
                if overall_area <= cond_area_percent_1:
                    smallest = str('1')
                    smallest_cond = Label(answer_frame, text='The smallest conduit that can hold these cables is: ', font=('', 9))
                    smallest_cond.grid(row=0, column=0, columnspan=3, sticky=W)
                else:
                    if overall_area <= cond_area_percent_125:
                        smallest = str('1 1/4 (1.25)')
                        smallest_cond = Label(answer_frame, text='The smallest conduit that can hold these cables is: ', font=('', 9))
                        smallest_cond.grid(row=0, column=0, columnspan=3, sticky=W)
                    else:
                        if overall_area <= cond_area_percent_15:
                            smallest = str('1 1/2 (1.5)')
                            smallest_cond = Label(answer_frame, text='The smallest conduit that can hold these cables is: ', font=('', 9))
                            smallest_cond.grid(row=0, column=0, columnspan=3, sticky=W)
                        else:
                            if overall_area <= cond_area_percent_2:
                                smallest = str('2')
                                smallest_cond = Label(answer_frame, text='The smallest conduit that can hold these cables is: ', font=('', 9))
                                smallest_cond.grid(row=0, column=0, columnspan=3, sticky=W)
                            else:
                                if overall_area <= cond_area_percent_25:
                                    smallest = str('2 1/2 (2.5)')
                                    smallest_cond = Label(answer_frame, text='The smallest conduit that can hold these cables is: ', font=('', 9))
                                    smallest_cond.grid(row=0, column=0, columnspan=3, sticky=W)
                                else:
                                    if overall_area <= cond_area_percent_3:
                                        smallest = str('3')
                                        smallest_cond = Label(answer_frame, text='The smallest conduit that can hold these cables is: ', font=('', 9))
                                        smallest_cond.grid(row=0, column=0, columnspan=3, sticky=W)
                                    else:
                                        if overall_area <= cond_area_percent_35:
                                            smallest = str('3 1/2 (3.5)')
                                            smallest_cond = Label(answer_frame, text='The smallest conduit that can hold these cables is: ', font=('', 9))
                                            smallest_cond.grid(row=0, column=0, columnspan=3, sticky=W)
                                        else:
                                            if overall_area <= cond_area_percent_4:
                                                smallest = str('4')
                                                smallest_cond = Label(answer_frame, text='The smallest conduit that can hold these cables is: ', font=('', 9))
                                                smallest_cond.grid(row=0, column=0, columnspan=3, sticky=W)
                                            else:
                                                if overall_area <= cond_area_percent_5:
                                                    smallest = str('5')
                                                    smallest_cond = Label(answer_frame, text='The smallest conduit that can hold these cables is: ', font=('', 9))
                                                    smallest_cond.grid(row=0, column=0, columnspan=3, sticky=W)
                                                else:
                                                    if overall_area <= cond_area_percent_6:
                                                        smallest = str('6')
                                                        smallest_cond = Label(answer_frame, text='The smallest conduit that can hold these cables is: ', font=('', 9))
                                                        smallest_cond.grid(row=0, column=0, columnspan=3, sticky=W)
                                                    else:
                                                        smallest = None
                                                        not_fit = Label(answer_frame, text='The cables will not fit in any conduit up to 6 inches diameter', font=('', 11), fg='red')
                                                        not_fit.grid(row=0, column=0, sticky=W)
        final_answer = Label(answer_frame, text=smallest, font=('', 12), fg='red')
        final_answer.grid(row=0, column=3, sticky=W)
        inch_answer = Label(answer_frame, text='inch conduit', font=('', 12), fg='red')
        inch_answer.grid(row=0, column=4, sticky=W)
    def save():
        connect = sqlite3.connect('cable_book.db')
        c = connect.cursor()
        record_id = id_select_entry.get()
        c.execute('UPDATE cables SET\n                    cable_name = :name,\n                    cable_diam = :diam,\n                    cable_amount = :amount\n                    WHERE oid = :oid', {'name': name_editor.get(), 'diam': diam_editor.get(), 'amount': amount_editor.get(), 'oid': record_id})
        connect.commit()
        connect.close()
        name_editor.delete(0, END)
        diam_editor.delete(0, END)
        amount_editor.delete(0, END)
        connect = sqlite3.connect('cable_book.db')
        c = connect.cursor()
        empty_4 = Label(pg1)
        empty_4.grid(row=0, column=1, columnspan=6)
        empty_3 = Label(pg1)
        empty_3.grid(row=4, column=1, columnspan=6)
        empty_2 = Label(pg1)
        empty_2.grid(row=2, column=1, columnspan=6)
        connect.commit()
        update()
    def close(page):
        page.destroy()
    def update():
        connect = sqlite3.connect('areas.db')
        c = connect.cursor()
        c.execute('DELETE FROM areas')
        connect.commit()
        connect = sqlite3.connect('cable_book.db')
        c = connect.cursor()
        c.execute('SELECT *, oid FROM cables')
        table = c.fetchall()
        show_name = ''
        show_diam = ''
        show_amount = ''
        show_id = ''
        for data in table:
            show_id += str(data[3]) + '\n'
            show_name += str(data[0]) + '\n'
            show_diam += str(data[1]) + '\n'
            show_amount += str(data[2]) + '\n'
            last_oid = data[3]
        close(table_frame)
        open()
        data_table_id = Label(table_frame, text=show_id)
        data_table_id.grid(row=6, column=0, padx=20, pady=20)
        data_table_name = Label(table_frame, text=show_name)
        data_table_name.grid(row=6, column=1, padx=20, pady=20)
        data_table_diam = Label(table_frame, text=show_diam)
        data_table_diam.grid(row=6, column=2, padx=20, pady=20)
        data_table_amount = Label(table_frame, text=show_amount)
        data_table_amount.grid(row=6, column=3, padx=20, pady=10)
        id_label = Label(table_frame, text='List Number (ID)').grid(row=5, column=0, padx=40)
        name_label = Label(table_frame, text='Cable Name').grid(row=5, column=1, padx=40)
        diam_label = Label(table_frame, text='Cable Diameter (in)').grid(row=5, column=2, padx=40)
        amount_label = Label(table_frame, text='Amount of Cables').grid(row=5, column=3, padx=40)
        count()
        connect.commit()
        connect.close()
    data_entry = Frame(pg1, width=900, height=60, bg='gray94', highlightbackground='gray', highlightthickness=1)
    data_entry.place(x=10, y=30, anchor=NW)
    frame_title = Label(data_entry, text='Data Entry', pady=3, font=('arial', 10))
    frame_title.grid(row=0, column=0)
    name = Entry(data_entry, width=21)
    name.grid(row=1, column=1, pady=5, padx=5)
    diam = Entry(data_entry, width=21)
    diam.grid(row=1, column=3, pady=5, padx=5)
    amount = Entry(data_entry, width=21)
    amount.grid(row=1, column=5, pady=5, padx=5)
    name_label = Label(data_entry, text='Cable Name:', padx=5)
    name_label.grid(row=1, column=0)
    diam_label = Label(data_entry, text='Cable\'s Diameter (in):', padx=3)
    diam_label.grid(row=1, column=2)
    amount_label = Label(data_entry, text='Amount of Cables:', padx=5)
    amount_label.grid(row=1, column=4)
    submit_btn = Button(data_entry, text='Submit Data', command=submit, width=20)
    submit_btn.grid(row=1, column=6, pady=1, padx=2)
    data_entry.grid_propagate(FALSE)
    commands = Frame(pg1, width=450, height=120, bg='gray94', highlightbackground='gray', highlightthickness=1)
    commands.place(x=10, y=100, anchor=NW)
    frame_title = Label(commands, text='Commands/Buttons', font=('arial', 10))
    frame_title.grid(row=0, column=0, sticky=W)
    generate_btn = Button(commands, text='Generate Answer', command=generate, width=50, bg='gray70')
    generate_btn.grid(row=1, column=0, pady=5, padx=40, columnspan=2, sticky=E)
    show_btn = Button(commands, text='Open Records', command=update, width=24)
    show_btn.grid(row=2, column=0, pady=5, padx=3, sticky=E)
    quit_btn = Button(commands, text='Close Program', command=root.quit, width=24, bg='gray85')
    quit_btn.grid(row=2, column=1, pady=5, padx=3, sticky=W)
    delete_frame = Frame(pg1, width=440, height=120, bg='gray94', highlightbackground='gray', highlightthickness=1)
    delete_frame.place(x=470, y=100, anchor=NW)
    delete_title = Label(delete_frame, text='Delete Data', font=('', 10))
    delete_title.grid(row=0, column=0, sticky=W)
    delete_all_btn = Button(delete_frame, text='Delete All Cables', command=delete_all, width=20)
    delete_all_btn.grid(row=2, column=0, pady=5, padx=10, sticky=W)
    id_label = Label(delete_frame, text='Type ID of cable to be deleted', font=('arial', 8))
    id_label.grid(row=1, column=0, columnspan=3, padx=3)
    delete_text_box = Entry(delete_frame, width=3, borderwidth=3, border=3)
    delete_text_box.grid(row=1, column=3, columnspan=1, padx=3, sticky=W)
    empty_del = Label(delete_frame).grid(row=1, column=4)
    delete_btn = Button(delete_frame, text='Delete', command=delete, width=10)
    delete_btn.grid(row=1, column=5, pady=1, padx=3, sticky=E)
    delete_frame.grid_propagate(FALSE)
    commands.grid_propagate(FALSE)
    data_edit = Frame(pg1, width=900, height=120, bg='gray94', highlightbackground='gray', highlightthickness=1)
    data_edit.place(x=10, y=230, anchor=NW)
    name_editor = Entry(data_edit, width=30)
    name_editor.grid(row=2, column=1, pady=5, padx=5, columnspan=2, sticky=W)
    diam_editor = Entry(data_edit, width=25)
    diam_editor.grid(row=2, column=4, pady=5, padx=5)
    amount_editor = Entry(data_edit, width=25)
    amount_editor.grid(row=2, column=6, pady=5, padx=5)
    id_select_entry = Entry(data_edit, width=3, borderwidth=3, border=3)
    id_select_entry.grid(row=1, column=2, padx=6, sticky=W)
    name_label_editor = Label(data_edit, text='Cable Name:', padx=10, pady=5)
    name_label_editor.grid(row=2, column=0)
    diam_label_editor = Label(data_edit, text='Cable\'s Diameter:', padx=5, pady=5)
    diam_label_editor.grid(row=2, column=3)
    amount_label_editor = Label(data_edit, text='Amount of Cables:', padx=5, pady=5)
    amount_label_editor.grid(row=2, column=5)
    id_select_label = Label(data_edit, text='Type ID of cable to be edited', font=('arial', 8))
    id_select_label.grid(row=1, column=0, padx=10, columnspan=2, sticky=W)
    frame_title = Label(data_edit, text='Edit Data on a Cable', pady=3, font=('', 10))
    frame_title.grid(row=0, column=0, sticky=W)
    save_btn = Button(data_edit, text='Save', command=save, width=12)
    save_btn.grid(row=3, column=0, pady=3, padx=10, columnspan=3, sticky=W)
    select_btn = Button(data_edit, text='Edit', command=select, width=7)
    select_btn.grid(row=1, column=2, padx=3)
    data_edit.grid_propagate(FALSE)
info = Label(root, text='This Program determines the smallest conduit that can support/hold a certain amount of cables according to NEC regulations.', bg='gray94', fg='black', font=('', 10), pady=10)
info.place(x=460, y=280, anchor=S)
continue_btn = Button(root, text='Continue', command=page_1, width=20)
continue_btn.place(x=460, y=280, anchor=N)
root.mainloop()