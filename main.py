import tkinter as tk
import requests
import json

# To work with the OMDB API:
# Go to http://www.omdbapi.com/apikey.aspx and get an account.
# The free account lets you make 1,000 requests per day.
# Get an API Key.

# Format variables:
labels_font = 'arial 13'
entries_font = 'arial 16'
btns_font = 'arial 13'
btns_color = 'lightblue'

# Type your own api_key for omdbapi.com
api_key = 'YOUR KEY'


class MoviesData:

    def __init__(self):
        self.w = tk.Tk()
        self.w.title('Movies data collector')
        self.w.geometry('550x400+300+150')
        self.w.resizable(0, 0)

        # Widgets creation starts:
        self.frame_search = tk.Frame(self.w)
        self.lbl_title = tk.Label(self.frame_search, text='Title: ',
                                  font=labels_font)
        self.e_title = tk.Entry(self.frame_search, font=entries_font, width=30)
        self.lbl_year = tk.Label(self.frame_search, text='Year: ',
                                 font=labels_font)
        self.e_year = tk.Entry(self.frame_search, font=entries_font, width=30)
        self.btn_search = tk.Button(self.frame_search, text='Search',
                                    font=btns_font, bg=btns_color,
                                    command=self.search)
        self.lb_results = tk.Listbox(self.w)

        # Widgets creation ends.

        # Widgets placing starts:
        self.frame_search.pack(pady=10, padx=5)
        self.lbl_title.grid(row=0, column=0)
        self.e_title.grid(row=0, column=1)
        self.lbl_year.grid(row=1, column=0)
        self.e_year.grid(row=1, column=1)
        self.btn_search.grid(row=0, column=2, rowspan=2, padx=10)
        self.lb_results.pack(fill='both', expand='yes')

        # Widgets placing ends:

        self.w.mainloop()

    def search(self):
        '''
        Gets data from the OMDB API and inserts it to the results Listbox
        widget.
        '''
        title = self.e_title.get()
        year = self.e_year.get()
        request = requests.get('http://www.omdbapi.com/?'
                               't=' + title + '&'
                               'y=' + year + '&'
                               'apikey=' + api_key)
        data_dict = json.loads(request.text)
        self.lb_results.delete(0, tk.END)
        if data_dict['Response'] == 'True':
            self.lb_results.insert(tk.END, ('Title: ' + data_dict['Title']))
            self.lb_results.insert(tk.END, ('Release date: ' +
                                            data_dict['Released']))
            self.lb_results.insert(tk.END, ('Genre: ' + data_dict['Genre']))
            self.lb_results.insert(tk.END, ('Rated: ' + data_dict['Rated']))
            self.lb_results.insert(tk.END, ('Runtime: ' +
                                            data_dict['Runtime']))
            self.lb_results.insert(tk.END, ('Director: ' +
                                            data_dict['Director']))
            self.lb_results.insert(tk.END, ('Country: ' +
                                            data_dict['Country']))
            self.lb_results.insert(tk.END, ('Awards: ' + data_dict['Awards']))
            try:
                self.lb_results.insert(tk.END, ('Rotten tomatoes: ' +
                                                data_dict['Ratings'][2]
                                                ['Value']))
            except IndexError:
                self.lb_results.insert(tk.END, ('Rotten tomatoes: N/A'))
        else:
            self.lb_results.insert(tk.END, ('Movie not found'))


app = MoviesData()
