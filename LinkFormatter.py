import tkinter as tk
from datetime import datetime

root = tk.Tk()

HEIGHT = 400
WIDTH = 600
radio_setting=tk.IntVar()
timeformat = '%H:%M'
ytlink=''

def get_ytlink(link):
    global ytlink
    ytlink = link[-11:]
    output_text.delete(0.0,tk.END)
    if ytlink != '':
        output_text.insert(tk.END, 'Link submitted!')
    else:
        output_text.insert(tk.END, 'No link was entered')
    
def get_seconds1(time):
    time = time.split()[0]        
    if time.count(':')==1:
        m,s = time.split(':')
        seconds = int(m)*60 + int(s)                
    if time.count(':')==2:
        h,m,s = time.split(':')
        seconds = int(h)*3600 + int(m)*60 + int(s)
    return str(seconds)  

def get_seconds2(start, end):
    end = end.split()[0]
    output = datetime.strptime(end, timeformat) - datetime.strptime(start,timeformat)
    return str(output.seconds)
        
def get_times(times_input):
    output_text.delete(0.0,tk.END)
    if ytlink == '': 
        output_text.insert(tk.END, 'Put in a youtube link first.')
        return
    try:
        if times_input.find('\n') > -1:
            times_list = times_input.split('\n')
            times_list = list(filter(None, times_list))
        else:
            times_list = times_input.split(',')
        if radio_setting.get() == 1:
            for entry in times_list:
                seconds = get_seconds1(entry)
                time_output = '['+entry.strip()+'](https://youtu.be/'+ytlink+'?t='+seconds+') \n'    
                output_text.insert(tk.END, time_output)
                
        if radio_setting.get() == 2:
            start_time = times_list[0]
            for entry in times_list:
                if entry != start_time:
                    seconds = get_seconds2(start_time, entry)
                    time_output = '['+entry.strip()+'](https://youtu.be/'+ytlink+'?t='+seconds+') \n'    
                    output_text.insert(tk.END, time_output)
    except:
        output_text.insert(tk.END, 'Something went wrong here!')
            
#make the whole window
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH, bg='#80c1ff')
canvas.pack()

#top frame to input youtube link
ytlink_frame = tk.Frame(root)
ytlink_frame.place(relx=0.025, rely=0.025, relheight=0.15, relwidth=0.95)

ytlink_entry = tk.Entry(ytlink_frame, bd=2)
ytlink_entry.place(relx=.01, rely=.5, relheight=0.4, relwidth=0.8)

ytlink_button = tk.Button(ytlink_frame, bd=2, text="Input link", command=lambda: get_ytlink(ytlink_entry.get()))
ytlink_button.place(relx=.83, rely=.1, relheight=0.8, relwidth=0.15)

ytlink_label = tk.Label(ytlink_frame, text="Plop your youtube link in here:")
ytlink_label.place(relx=.01, rely=.1)

#middle frame to input times
times_frame = tk.Frame(root)
times_frame.place(relx=0.025, rely=0.2, relheight=.15, relwidth=.95)

times_entry = tk.Entry(times_frame, bd=2)
times_entry.place(relx=.01, rely=.5, relheight=0.4, relwidth=0.8)

times_button = tk.Button(times_frame, bd=2, text="Input times", command=lambda: get_times(times_entry.get()))
times_button.place(relx=.83, rely=.1, relheight=0.8, relwidth=0.15)

times_label = tk.Label(times_frame, text="Put your times and comments separated by commas or new lines")
times_label.place(relx=.01, rely=.1)

#frame for the radio buttons
radio_frame = tk.Frame(root)
radio_frame.place(relx=.025, rely=.3625, relheight=.05, relwidth=.95)

radio_one = tk.Radiobutton(radio_frame, variable=radio_setting, value=1, text='Time in video')
radio_one.place(relx=0,rely=0)
radio_one.select()

radio_two = tk.Radiobutton(radio_frame, variable=radio_setting, value=2, text='AM/PM - make first input the start time of the video')
radio_two.place(relx=.35,rely=0)

#bottom frame to output links
output_frame = tk.Frame(root)
output_frame.place(relx=0.025, rely=0.425, relheight=.55, relwidth=.95)

output_text = tk.Text(output_frame)
output_text.place(relx=.01, rely=.01, relheight=.98, relwidth=.98)

root.mainloop()
