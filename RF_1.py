#program to record and store your sports results

import shelve
from tkinter import *
import collections

class Application(Frame):
    '''GUI application ере displays menu for the programm'''
    def __init__(self, master):
        '''Initialize Frame'''
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        ''' Create widgets to get story information and to display story. '''

        self.fileDat = 'data'  
        


        # label №
        Label(self,
              text = '№ of the training (total -  ' + str(self.tngAmount())+')'+ ':'
              ).grid(row = 0, column = 0, sticky = W)
        
        # field №
        self.number_ent = Entry(self)
        self.number_ent.grid(row = 0, column = 1, sticky = W)


        # label date
        Label(self,
              text = "date:"
              ).grid(row = 1, column = 0,  sticky = W)
        
        # field date
        self.date_ent = Entry(self)
        self.date_ent.grid(row = 1, column = 1, sticky = W)
      
      
        # label km
        Label(self,
              text = "km:"
              ).grid(row = 2, column = 0,  sticky = W)
        
        # field km
        self.km_ent = Entry(self)
        self.km_ent.grid(row = 2, column = 1, sticky = W)

        
        # label time
        Label(self,
              text = "time:"
              ).grid(row = 3, column = 0,  sticky = W)
        
        # field time
        self.time_ent = Entry(self)
        self.time_ent.grid(row = 3, column = 1, sticky = W)
       

        
        # create barefoot check button
        self.barefoot = BooleanVar()
        Checkbutton(self,
                    text = "barefoot",
                    variable = self.barefoot
                    ).grid(row = 4, column = 0, sticky = W)


        # create shirtless check button
        self.shirtless = BooleanVar()
        Checkbutton(self,
                    text = "shirtless",
                    variable = self.shirtless
                    ).grid(row = 4, column = 1, sticky = W)


        # create fire escape check button
        self.fireEscape = BooleanVar()
        Checkbutton(self,
                    text = "climb the fire escape",
                    variable = self.fireEscape
                    ).grid(row = 4, column = 2, sticky = W)



        # create neva check button
        self.dipNeva = BooleanVar()
        Checkbutton(self,
                    text = "take a dip in the Neva",
                    variable = self.dipNeva
                    ).grid(row = 5, column = 0, sticky = W)
        
        

        # create rain check button
        self.rain = BooleanVar()
        Checkbutton(self,
                    text = "rain",
                    variable = self.rain
                    ).grid(row = 5, column = 1, sticky = W)


        # create tower check button
        self.tower = BooleanVar()
        Checkbutton(self,
                    text = "climb the tower",
                    variable = self.tower
                    ).grid(row = 5, column = 2, sticky = W)

        


        # label temperature
        Label(self,
              text = 'temperature'
              ).grid(row = 6, column = 0, sticky = W)

        # field tempreture
        self.temperature = Entry(self)
        self.temperature.grid(row = 6, column = 1, sticky = W)


        
         # label extra
        Label(self,
              text = 'extra'
              ).grid(row = 7, column = 0,  sticky = W)

        # field extra
        self.extra = Entry(self)
        self.extra.grid(row = 7, column = 1, sticky = W)


        # record button
        Button(self,
               text = "record training",
               command = self.record
               ).grid(row = 8, column = 0, sticky = W)

        # show training button
        Button(self,
               text = "show all trainings",
               command = self.tngDisplay
               ).grid(row = 8, column = 1, sticky = W)

        

        


        # label number of training to remove
        Label(self,
              text = '№ of the trainig to remove'
              ).grid(row = 9, column = 0,  sticky = W)

        # field number of training to remove
        self.remove_ent = Entry(self)
        self.remove_ent.grid(row = 9, column = 1, sticky = W)

        # remove button
        Button(self,
               text = "remove",
               command = self.tngRemove
               ).grid(row =9, column = 2, sticky = W)


        # remove all trainings button
        Button(self,
               text = "remove all trainings",
               command = self.tngAllRemove
               ).grid(row =10, column = 0, sticky = W)
        

        # create tower check button
        self.allRemove = BooleanVar()
        Checkbutton(self,
                    text = "Are you sure?",
                    variable = self.allRemove
                    ).grid(row = 10, column = 1, sticky = W)


        # label clear the window
        Label(self,
              text = 'Clear the text field (don\'t worry your saved trainings will not be deleted)'
              ).grid(row = 11, column = 0, columnspan =2, sticky = W)

        # clear the window button
        Button(self,
               text = "clear the window",
               command = self.clear
               ).grid(row =11, column = 2, sticky = W)

        
        self.tngField = Text(self, width = 100, height = 10, wrap = WORD)
        self.tngField.grid(row = 12, column = 0, columnspan = 4)
        


    def listRecord( self):
        # make the list of records
        tng= []

        date = self.date_ent.get()
        if date:
            tng.append('date: ' + date)

        km = self.km_ent.get()
        if km:
            tng.append('km: ' + km)

        time = self.time_ent.get()
        if time:
            tng.append('time: ' + time)
         
        barefoot = self.barefoot.get()
        if barefoot:
            barefoot = 'barefoot'
            tng.append(barefoot)

        shirtless = self.shirtless.get()
        if shirtless:
            shirtless = 'shirtless'
            tng.append(shirtless)


        fireEscape = self.shirtless.get()
        if shirtless:
            shirtless = 'fireEscape'
            tng.append(fireEscape)

        dipNeva = self.dipNeva.get()
        if dipNeva:
            dipNeva = 'dipNeva'
            tng.append(dipNeva)

        rain = self.rain.get()
        if rain:
            rain = 'rain'
            tng.append(rain)

        tower = self.barefoot.get()
        if tower:
            tower = 'tower'
            tng.append(tower)


        temperature = self.temperature.get()
        if temperature:
            tng.append(shirtless)

        extra = self.extra.get()
        if extra:
            tng.append(extra)
        
        return tng

    
    def record (self):

        tngList = self.listRecord()
        tngNumber = self.number_ent.get()

        datFile = shelve.open(self.fileDat)
        datFile[tngNumber] = tngList
        datFile.sync()
        datFile.close()

    def tngAmount (self):
        datFile = shelve.open(self.fileDat)
        i = 0
        for key, item in datFile.items():
            i+=1
        datFile.sync()
        datFile.close()
        return i

    def tngRemove (self):
        datFile = shelve.open(self.fileDat)
        del datFile[self.remove_ent.get()]
        datFile.close()
        
    def tngAllRemove (self):
        datFile = shelve.open(self.fileDat)
        if self.allRemove.get():
            datFile.clear()
        datFile.close()

    def clear (self):
        self.tngField.delete(0.0, END)

    def tngDisplay (self):
        tng = ''
        
        self.tngField.delete(0.0, END)
        datFile = shelve.open(self.fileDat)
        
        datFileSorted = collections.OrderedDict(sorted(datFile.items()))
        for key, item in datFileSorted.items():
            tng = str(key) + ': ' + str(item)
            # display trainings                                
            self.tngField.insert('end', tng +'\n')
        datFile.sync()
        datFile.close()   
        

root = Tk()
root.title('RunForest')
app = Application(root)
root.mainloop()
