from tkinter import *
from tkinter import ttk
from re import *

#  Regex pattern
pattern = compile('^{[0-9A-Za-z]{8}-[0-9A-Za-z]{4}-[0-9A-Za-z]{4}-[0-9A-Za-z]{4}-[0-9A-Za-z]{12}}$')


root = Tk()
root.title('RAW ID converter')

#  Radiobuttons variable
a_text = StringVar()
a_c_btn = StringVar()
a_c_imgResponsive = StringVar()
a_target_blank = StringVar()
CleanID = StringVar()
linkMediaID = StringVar()
linkID = StringVar()


#  Select all with keyboard shotcut "Ctrl+A"
def slct(event=None):
    raw_ID_input.select_clear()
    raw_ID_input.select_range(0, 'end')
root.bind('<Control-a>',slct)

#  Paste the value from clipboard with "Ctrl+V"
def paste(event=None):
    paste_ID = root.clipboard_get()
    raw_ID_input.config(text=paste_ID)
root.bind('<Control-v>',paste)


def submit():
    raw_ID_input_re = raw_ID_input.get()
    isValid = pattern.match(raw_ID_input_re)
    if isValid:
        global CleanID
        global linkMediaID
        global linkID
        global a_text
        global a_c_btn
        global a_target_blank
        CleanID = raw_ID_input_re.replace('-', '').replace('{', '').replace('}', '')
        a_text_get = a_text.get()
        a_c_btn_get = a_c_btn.get()
        clean_ID_output.config(text=CleanID)
        linkMediaID = '<img src="-/media/'+f'{CleanID}'+'.ashx"'+f' {a_c_imgResponsive.get()}'+'/>'
        link_media_output.config(text=linkMediaID)
        linkID = '<a href="~/link.aspx?_id='+f'{CleanID}'+'&amp;_z=z"'+f' {a_c_btn_get}'+f' {a_target_blank.get()}'+'>'+f'{a_text_get}'+f'{e_ownCTA_input.get()}'+'</a>'
        link_ID_output.config(text=linkID)
    else:
        clean_ID_output.config(text='Invalid RAW Sitecore ID')


def copy_clean():
    global CleanID
    root.clipboard_clear()
    root.clipboard_append(CleanID)
    print(CleanID)


def copy_media():
    global linkMediaID
    root.clipboard_clear()
    root.clipboard_append(linkMediaID)
    print(linkMediaID)


def copy_link():
    global linkID
    root.clipboard_clear()
    root.clipboard_append(linkID)
    print(linkID)


#  Row 0
raw_ID = Label(root, width=30, text='Sitecore RAW ID: ').grid(row=0, column=0)
raw_ID_input = Entry(root, width=40, text='')
raw_ID_input.grid(row=0, column=1, sticky="w")
submit_btn = Button(root, text="Submit", command=submit).grid(row=0,column=2)

#  Row 2
CTA_text = Label(root, text='Link CTA: ').grid(row=2, column=0)
r_Learn_More = Checkbutton(root, text='"Learn More"', variable=a_text, onvalue='Learn More', offvalue='')
r_Learn_More.select()
r_Learn_More.grid(row=2, column=1, sticky="w")

#  Row 3
r_Read_More = Checkbutton(root, text='"Read More"', variable=a_text, onvalue='Read More', offvalue='')
r_Read_More.grid(row=3, column=1, sticky="w")

#  Row 4
r_Read_More = Checkbutton(root, text='"Watch Now"', variable=a_text, onvalue='Watch Now', offvalue='')
r_Read_More.grid(row=4, column=1, sticky="w")

#  Row 5
l_ownCTA = Label(root, text='Your own CTA: ').grid(row=5, column=0)
e_ownCTA_input = Entry(root, width=40, text='')
e_ownCTA_input.grid(row=5, column=1, sticky="w")

#  Row 6
c_Class = Label(root, text='CSS Class: ').grid(row=6, column=0)
c_btn = Checkbutton(root, text='".btn"', variable=a_c_btn, onvalue='class="btn"', offvalue='')
c_btn.grid(row=6, column=1, sticky="w")

#  Row 7
c_imgResponsive = Checkbutton(root, text='".img-responsive"', variable=a_c_imgResponsive, onvalue='class="img-responsive"', offvalue='')
c_imgResponsive.grid(row=7, column=1, sticky="w")

#  Row 8
c_a_target = Checkbutton(root, text='"target=_blank"', variable=a_target_blank, onvalue='target="_blank"', offvalue='')
c_a_target.grid(row=8, column=1, sticky="w")

#  Row 9
clean_ID = Label(root, text='Sitecore Clean ID: ').grid(row=8, column=0)
clean_ID_output = Label(root, text='')
clean_ID_output.grid(row=9, column=1, sticky="w")
clean_ID_btn = Button(root, text="Copy", command=copy_clean)
clean_ID_btn.grid(row=9, column=2)

#  Row 10
link_media = Label(root, text='Link Media (images, pdfs): ').grid(row=9, column=0)
link_media_output = Label(root, text='')
link_media_output.grid(row=10, column=1, sticky="w")
link_media_btn = Button(root, text="Copy", command=copy_media)
link_media_btn.grid(row=10, column=2)

#  Row 11
link_ID = Label(root, text='Hyperlink (.aspx): ').grid(row=10, column=0)
link_ID_output = Label(root, text='')
link_ID_output.grid(row=11, column=1, sticky="w")
link_ID_btn = Button(root, text="Copy", command=copy_link)
link_ID_btn.grid(row=11, column=2)


root.mainloop()
