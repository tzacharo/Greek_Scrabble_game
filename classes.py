# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 11:12:16 2021

@author: tzachar_r5
"""

import random
import  itertools
import json
import datetime 


FILENAME = "greek7.txt"

def loadWords():
    print('\n')
    print ("Φόρτωση λίστας λέξεων από αρχείο ...")
    gr = open(FILENAME, 'r', encoding="utf-8")
    
    wordList = []
    for line in  gr:
        wordList.append(line.strip())
    print ("  ", len(wordList), "φορτωμένες λέξεις .\n")
    return wordList

def isValidWord(word, hand, wordList):

    wordlist_copy=wordList[:]
    #hand_copy=hand[0].copy()
    l=0
    hand_copy ={}
    for i in hand[0]:
        hand_copy.setdefault(i,hand[1][l])
        l+=1
    flag=1
    if word in wordlist_copy:
        for ch in word:
            if ch in hand_copy:
                flag=0                
                hand_copy[ch]=hand_copy.get(ch,0)-1
                if(hand_copy.get(ch,0)==0):
                    del hand_copy[ch]
                
            else:
                flag=1
                break
    if (flag==0):
        return True
    else:
        return False

def getWordScore(word):

    score=0
    for ch in word:
        score+=SakClass.sak[ch][1]
   
    return score

def updateHand(hand, word):
    
    hand_g=hand[0]
    hand_v=hand[1]
    j = 0
    f = True 
    f2 = True 
    for ch in word:        
        while (f2):
            if (ch== hand_g[j] and f):
                del hand_g[j]
                del hand_v[j]
                f = False
                f2 = False
            elif (j == len(hand_g)):
                  f2 = False
            j += 1        
        f =True
        f2 = True 
        j =0
    hand_copy = [hand_g ,hand_v]
    return hand_copy

class SakClass () :
    sak = {'Α':[12,1],'Β':[1,8],'Γ':[2,4],'Δ':[2,4],'Ε':[8,1],
        'Ζ':[1,10],'Η':[7,1],'Θ':[1,10],'Ι':[8,1],'Κ':[4,2],
        'Λ':[3,3],'Μ':[3,3],'Ν':[6,1],'Ξ':[1,10],'Ο':[9,1],
        'Π':[4,2],'Ρ':[5,2],'Σ':[7,1],'Τ':[8,1],'Υ':[4,2],
        'Φ':[1,8],'Χ':[1,8],'Ψ':[1,10],'Ω':[3,3]        }
    
    sakrlet=102
    
    def getletters(n=7):
        #βγάζει από το σακουλάκι για τον παίκτη Ν = 7 γράμματα
        g=[]
        v=[]
        hand = []
        i = 0
        for  i in range(n):
            x = SakClass.randomize_sak()
            g.append(x)
            v.append(SakClass.sak [x][1])
            
        hand = [g,v] 
        return hand
    
    def putbackletters(p):
        #επιστρέφει γράμματα παίκτη στο σακουλάκι
        for i in p[0]:
            SakClass.sak [i][0] +=1
            SakClass.sakrlet +=1
    
    def randomize_sak():
        #«ετοιμάζει» το σακουλάκι με τα γράμματα
        
        l='ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'
        while True :
            x = l[random.randrange(0,len(l))]
            if SakClass.sak [x][0] != 0:
                SakClass.sak [x][0] -=1
                SakClass.sakrlet -=1
                break
              
        return x

class Player :
    '''
    βασική κλάση από την οποία παράγονται οι Human και
    Computer
    '''
    
    def __init__(self):
        self.phand = SakClass.getletters()
        self.pscor =0
    
    
    def __repr__(self):
        return f'Player(phand = SakClass.getletters() , self.pscor =0)'



class Human (Player):
    '''
    κλάση παράγωγος της Player που περιγράφει το πώς παίζει
    ο άνθρωπος-παίκτης
    '''
    def __init__(self,hname= 'User'):
        super().__init__()
        self.hname= hname
        
    def __repr__():
        return f'Human(super().__init__() , self.hname= hname)'
    def play(self,hname,phand,pscor,wordL):
        while (True and SakClass.sakrlet>0) :
            
            print("Σειρά του : " ,hname  )
            print("Γράμματα που απομένουν στο σακουλάκι : " , SakClass.sakrlet)
            print("Τρέχον χέρι : ")
            for i in range(len(phand[0])):
               print (phand[0][i] ,":", phand[1][i], end=" // " )
               
            print("\n")
            
            word=input('Εισαγάγετε λέξη,ή "1" για νέο χέρι,για πάσο το "0", ή "." για να δείξετε ότι έχετε τελειώσει: \n').upper()
            if(word=="."):
                print("Αντιο σας! Σύνολο σκορ: ",pscor, " πόντοι")
                Game.tern=2
                break
           
            
            elif(word=="1"):
                SakClass.putbackletters(phand)
                phand =SakClass.getletters()
                
            elif(word=="0"):
                print("Πήγατε πάσο!!! \n ")
                break
            
            else:
                if not isValidWord(word,phand,wordL):
                    print("\n")
                    print("-------------------------------")            
                    print("Μη έγκυρη λέξη, δοκιμάστε ξανά. ")
                    print("-------------------------------\n")  
                    continue
                else:
                    
                    ps = getWordScore(word)
                    pscor +=ps
                    print("Λέξη που δώσατε :" + '"' + str(word) + '"' + " κερδίσατε " + str(ps) + " πόντοι. Σύνολο: " + str(pscor) + " πόντοι. \n")
                    phand=updateHand(phand,word)
                    break
                
            if(SakClass.sakrlet==0):
                   print('!!!!!!!!Το σακουλάκι άδειασε , τέλος Παιχνιδιού !!!!!!!!')
                   Game.end()        
                    

class Computer (Player):
    '''
    κλάση παράγωγος της Player που περιγράφει το πώς
    παίζει ο υπολογιστής-παίκτης
    '''
    def __init__(self,cname='PC'):
        super().__init__()
        self.cname=cname
        
    def __repr__():
        return f'Computer(super().__init__() ,self.cname=cname)'
    
    def play(self,cname,phand,pcscor,wordL):
        print('-------------------------------')
        print("Σειρά του : " ,cname)
        print("Γράμματα που απομένουν στο σακουλάκι : " , SakClass.sakrlet)
        flc =True
        flc2=False
        tq= random.choice([2,3,4,5])
        if (len(phand[0])>= 2):
            SakClass.putbackletters(phand)
            phand =SakClass.getletters()
            
        for k in range(len(phand[0])-tq):
            q=list(itertools.permutations(phand[0],k+tq))             
            for i in range(len(q)):
                y=''
                for j in q[i]:
                    y+=j
                if isValidWord(y,phand,wordL):
                    flc=False 
                    cps = getWordScore(y)
                    pcscor +=cps
                    print("Λέξη που δώσατε :" + '"' + str(y) + '"' + " κερδίσατε " + str(cps) + " πόντοι. Σύνολο: " + str(pcscor) + " πόντοι. \n")
                    phand=updateHand(phand,y)
                    break

            if (flc== False): break 
                       
            if (k== len(phand[0])-(tq+1)):
                flc2=True
                break
            
            if(SakClass.sakrlet==0):
                   print('!!!!!!!!Το σακουλάκι σόδιασε τέλος Παιχνιδιού !!!!!!!!')
                   Game.end()
    
                
        if (flc and flc2):
            SakClass.putbackletters(phand)
            phand =SakClass.getletters()
            print('Πασο απο το PC \n')
            print("Σύνολο: " + str(pcscor) + " πόντοι. \n")
        print('-------------------------------')
        
class Game :
    '''
    κλάση που περιγράφει το πώς εξελίσσεται μια παρτίδα 
    '''
    tern = 0
    def __init__(self):
        self.h = Player()
        self.c= Player()        
        Game.setup(self.h,self.c)
        
    def __repr__():
        return f'Game(self.h = Player() , self.c= Player() , Game.setup(self.h,self.c) )'
    
    def setup(h,c):
        
        while True:
            
            choice=input('''
***** SCRABBLE *****
--------------------
1: Για να μοιραστεί ένα νέο χέρι
2: Για να δείτε τα προηγουμένα σας σκορ
q: Έξοδος
--------------------
Επιλογή : ''')

            if (choice == '1'):                
                Game.tern=0
                SakClass.sak = {'Α':[12,1],'Β':[1,8],'Γ':[2,4],'Δ':[2,4],'Ε':[8,1],
                                'Ζ':[1,10],'Η':[7,1],'Θ':[1,10],'Ι':[8,1],'Κ':[4,2],
                                'Λ':[3,3],'Μ':[3,3],'Ν':[6,1],'Ξ':[1,10],'Ο':[9,1],
                                'Π':[4,2],'Ρ':[5,2],'Σ':[7,1],'Τ':[8,1],'Υ':[4,2],
                                'Φ':[1,8],'Χ':[1,8],'Ψ':[1,10],'Ω':[3,3]}
        
                SakClass.sakrlet=102
                Game.run(h,c)
            elif (choice == '2'):
                print('Προηγουμένα σκορ: \n')
                with open('safescor.json') as df:
                    da_l =json.load(df)

                print (da_l)
            elif (choice == 'q'):
                Game.end()
                break
            
    def run(h,c):
        fgame = True
        wordList=loadWords()
        h=Human()
        c=Computer()
        while fgame:
            if (Game.tern== 0):
                h.play('User',h.phand,h.pscor,wordList)
                if (Game.tern != 0) : break
                c.play('PC',c.phand,c.pscor,wordList)
                
        else:
             Game.end(h.pscor)
                
            
    def end(r=0):

        choice=input("Αν θέλετε να σώσετε το σκορ σας επιλέξτε Y/y")
        if (choice == 'y' or choice == 'Y'):
            with open('safescor.json', 'w',encoding="utf-8") as f:
                p= 'Στις ' + str( datetime.date.today()) + ' το σκορ ήταν ' + str(r)
                json.dump(str(p), f)
        print ('good bay !!!!')
    
