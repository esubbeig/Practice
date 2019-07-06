'''
    AUTHOR  : ESUB BEIG
    DATE    : 07-07-2019
    THEME   : FLAMES FUN

'''
class flames():     #Created a class

    def __init__(self):         #Created Constructor
        #Removing spaces converting to lowercase & converting to list at the time of input taking only
        self.boy = list((((input('Enter boy name? ')).lower()).strip()).replace(" ",""))
        self.girl = list((((input('Enter girl name? ')).lower()).strip()).replace(" ",""))
        self.remove_match_char()    #Calling another funcion

    def remove_match_char(self):    #To remove duplicate characters from both the names
        for i in self.boy:
            if i in self.girl:
                self.boy.remove(i)
                self.girl.remove(i)
        self.length = len(self.boy)+len(self.girl)  #Finally caluculating the lenght of concatenated lists
        self.bussiness_logic()      #Calling another function

    def bussiness_logic(self):      #Created main Bussiness Logic
        self.result = ['Friends','Lovers','Affection','Marriage','Enemy','Siblings']
        while len(self.result) > 1:
            self.split_index = (self.length % len(self.result)-1)
            if self.split_index >= 0:
                self.right = self.result[self.split_index + 1 : ]
                self.left  = self.result[ : self.split_index]
                self.result = self.right + self.left
            else:
                self.result = self.result[ : len(self.result)-1]

    def dispaly(self):              #This function to display the output
        print('Relation ::: ',(self.result[0]).upper())

obj = flames()      #Created the object for the class
obj.dispaly()       #calling function on the class object