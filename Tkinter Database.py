import tkinter as tk
import sqlite3

window=tk.Tk()
window.title("This is my Gui")
window.geometry("400x400")

conn=sqlite3.connect("address_book.db")
curs=conn.cursor()

"""
curs.execute(CREATE TABLE address(
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer            
            )
             )
"""
"""
curs.execute( CREATE TABLE address(
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer            
            ))
"""

def submit():
    conn=sqlite3.connect("address_book.db")
    curs=conn.cursor()
    
    curs.execute("INSERT INTO address VALUES(:f_name , :l_name , :address , :city , :state , :zipcode)",
             {
                'f_name':f_name.get(),
                'l_name':l_name.get(),
                'address':address.get(),
                'city':city.get(),
                'state':state.get(),
                'zipcode':zipcode.get(),
                })

    conn.commit()
    conn.close()

    f_name.delete(0 , tk.END)
    l_name.delete(0 , tk.END)
    address.delete(0 , tk.END)
    city.delete(0 , tk.END)
    state.delete(0 , tk.END)
    zipcode.delete(0 , tk.END)


def query():
    conn=sqlite3.connect("address_book.db")
    curs=conn.cursor()
    
    curs.execute("SELECT oid,* FROM address")
    records=curs.fetchall()
    
    print_records=" "
    
    for record in records:
        for i in record:
            print_records+=str(i)+', '
        print_records+='\n\n'
        
    q_label=tk.Label(window , text=print_records)
    q_label.grid(row=12 , column=0 , columnspan=2)

    conn.commit()
    conn.close()
    
def delete():
    conn=sqlite3.connect("address_book.db")
    curs=conn.cursor() 
    
    curs.execute("DELETE FROM address WHERE oid="+deletebox.get())
    deletebox.delete(0 , tk.END)
    
    conn.commit()
    conn.close()
    
def save():
    conn=sqlite3.connect("address_book.db")
    curs=conn.cursor() 
    
    update_id=updatebox.get()
    
    curs.execute(""" UPDATE address SET
                 first_name=:first,
                 last_name=:last,
                 address=:address,
                 city=:city,
                 state=:state,
                 zipcode=:zipcode
                 
                 WHERE oid=:oid""",
                 
                 {
                 'first':f_name_editor.get(),
                 'last':l_name_editor.get(),
                 'address':address_editor.get(),
                 'city':city_editor.get(),
                 'state':state_editor.get(),
                 'zipcode':zipcode_editor.get(),
                 'oid':update_id
                 }
                 )
    
    conn.commit()
    conn.close()
    
    editor.destroy()

    
    
    
def update():
    global editor
    
    editor=tk.Tk()
    editor.title("This is my updating window")
    editor.geometry("400x400") 
    
    conn=sqlite3.connect("address_book.db")
    curs=conn.cursor()
    
    update_id=updatebox.get()
    
    curs.execute("SELECT * FROM address WHERE oid=" +update_id)
    records=curs.fetchall()
    
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    
    f_name_editor=tk.Entry(editor , width=30)
    f_name_editor.grid(row=0 , column=1 , padx=20)
    l_name_editor=tk.Entry(editor , width=30)
    l_name_editor.grid(row=1 , column=1)
    address_editor=tk.Entry(editor , width=30)
    address_editor.grid(row=2 , column=1)
    city_editor=tk.Entry(editor , width=30)
    city_editor.grid(row=3 , column=1)
    state_editor=tk.Entry(editor , width=30)
    state_editor.grid(row=4 , column=1)
    zipcode_editor=tk.Entry(editor , width=30)
    zipcode_editor.grid(row=5 , column=1)
    
    for record in records:
        f_name_editor.insert(0 , record[0])
        l_name_editor.insert(0 , record[1])
        address_editor.insert(0 , record[2])
        city_editor.insert(0 , record[3])
        state_editor.insert(0 , record[4])
        zipcode_editor.insert(0 , record[5])

    f_name_label=tk.Label(editor , text="First Name")
    f_name_label.grid(row=0 , column=0)
    l_name_label=tk.Label(editor , text="Last Name")
    l_name_label.grid(row=1 , column=0)
    address_label=tk.Label(editor , text="Address")
    address_label.grid(row=2 , column=0)
    city_label=tk.Label(editor , text="City Name")
    city_label.grid(row=3 , column=0)
    state_label=tk.Label(editor , text="State Name")
    state_label.grid(row=4 , column=0)
    zipcode_label=tk.Label(editor , text="Zipcode")
    zipcode_label.grid(row=5 , column=0)
    
    save_btn=tk.Button(editor , text="Save Record" , command=save)
    save_btn.grid(row=6 , column=0 , columnspan=2 , padx=10 , pady=10 , ipadx=90)
    
    conn.commit()
    conn.close()
                       
f_name=tk.Entry(window , width=30)
f_name.grid(row=0 , column=1 , padx=20)
l_name=tk.Entry(window , width=30)
l_name.grid(row=1 , column=1)
address=tk.Entry(window , width=30)
address.grid(row=2 , column=1)
city=tk.Entry(window , width=30)
city.grid(row=3 , column=1)
state=tk.Entry(window , width=30)
state.grid(row=4 , column=1)
zipcode=tk.Entry(window , width=30)
zipcode.grid(row=5 , column=1)

deletebox=tk.Entry(window , width=30)
deletebox.grid(row=7 , column=1)

updatebox=tk.Entry(window , width=30)
updatebox.grid(row=9 , column=1)

f_name_label=tk.Label(window , text="First Name")
f_name_label.grid(row=0 , column=0)
l_name_label=tk.Label(window , text="Last Name")
l_name_label.grid(row=1 , column=0)
address_label=tk.Label(window , text="Address")
address_label.grid(row=2 , column=0)
city_label=tk.Label(window , text="City Name")
city_label.grid(row=3 , column=0)
state_label=tk.Label(window , text="State Name")
state_label.grid(row=4 , column=0)
zipcode_label=tk.Label(window , text="Zipcode")
zipcode_label.grid(row=5 , column=0)

delete_lbl=tk.Label(window , text="Delete ID")
delete_lbl.grid(row=7 , column=0)

update_lbl=tk.Label(window , text="Update ID")
update_lbl.grid(row=9 , column=0)

submit_btn=tk.Button(window , text="Submit record" , command=submit)
submit_btn.grid(row=6 , column=0 , columnspan=2 , padx=10 , pady=10 , ipadx=100)

query_btn=tk.Button(window , text="Show records" , command=query)
query_btn.grid(row=11 , column=0 , columnspan=2 , padx=10 , pady=10 , ipadx=100)

delete_btn=tk.Button(window , text="Delete" , command=delete)
delete_btn.grid(row=8 , column=0 , columnspan=2 , padx=10 , pady=10 , ipadx=120)

update_btn=tk.Button(window , text="Update" , command=update)
update_btn.grid(row=10 , column=0 , columnspan=2 , padx=10 , pady=10 , ipadx=120)


conn.commit()
conn.close()


window.mainloop()
