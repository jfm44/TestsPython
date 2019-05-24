#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import threading
import random
import time
import sys
from math import *

###############################################################################
class Requete(object):
    """objet REquete destiné aux execution par les threads par l'intermediaire du tableau blanc"""
    def __init__(self):
        self.Type           = 'Test'     # Type de la requete Test, Secenario, Requete...
        self.statut         = 'A'        # 'A'=en Attente de traitement, 'E'=En-cours de traitement, 'F'=Fini
        self.emetteur       = None       # si necessaire: coordonnee de l'emetteur du message
        self.destinataire   = None       # dans le cas ou un destinataire particulier serait requis
        self.traiteur       = None       # nom du thread qui est en train de traiter le message 
        self.requete        = None       # la requete à traiter
        self.delais         = None       # delais de reexecution en minutes
        self.reponse        = None       # la reponse du traiteur
        self.duree          = None       # duree du traitement
 
###############################################################################
class TBlanc(object):
    """objet de type file d'attente, base sur une pile fifo: on depile le plus ancien empile"""
 
    def __init__(self,maxpile=0):
        self.pile=[]
        self.maxpile = maxpile
 
    def empile(self,element):
        if (self.maxpile!=0) and (len(self.pile)==self.maxpile):
            raise ValueError ("erreur: tentative d'empiler une pile pleine")
        self.pile.insert(0,element)
 
    def depile(self,idx=-1):
        if len(self.pile)==0:
            raise ValueError ("erreur: tentative de depiler une pile vide")
        if idx<-len(self.pile) or idx>=len(self.pile):
            raise ValueError ("erreur: element de pile n'existe pas")
        return self.pile.pop(idx)
 
    def element(self,idx=-1):
        if idx<-len(self.pile) or idx>=len(self.pile):
            raise ValueError ("erreur: element de pile n'existe pas")
        return self.pile[idx]
 
    def copiepile(self,imin=0,imax=None):
        if imax==None:
            imax=len(self.pile)
        if imin<0 or imax>len(self.pile) or imin>=imax:
            raise ValueError ("erreur: mauvais indice pour extraction par copiepile")
        return list(self.pile[imin:imax])
 
    def cherche(self,stat,Type,nomthread=None):
        for idx in range(-1,-len(self.pile)-1,-1):
            if self.pile[idx].statut==stat and self.pile[idx].Type==Type:
                if nomthread==None or (nomthread!=None and self.pile[idx].traiteur==nomthread):
                    return idx
        return None
 
    def estvide(self):
        return len(self.pile)==0
 
    def estpleine(self):
        return self.maxpile>0 and len(self.pile)==self.maxpile
 
    def taille(self):
        return len(self.pile)
 
    def nbattentes(self):
        k = 0
        for idx in range(0,len(self.pile)):
            if self.pile[idx].statut=='A':
                k += 1
        return k
 
    def nbencours(self):
        k = 0
        for idx in range(0,len(self.pile)):
            if self.pile[idx].statut=='E':
                k += 1
        return k
 
    def nbfinis(self):
        k = 0
        for idx in range(0,len(self.pile)):
            if self.pile[idx].statut=='F':
                k += 1
        return k

###############################################################################
class TraiteurTest(threading.Thread):
 
    def __init__(self):
        threading.Thread.__init__(self)
        self.nbtraitements = 0
 
    def run(self):
        global vtblanc, tblanc
        while True:
            # attente d'une expression à calculer disponible dans le tableau blanc
            while True:
                #on bloque le tableau
                vtblanc.acquire()
                self.idx = tblanc.cherche('A')
                if self.idx!=None:
                    tblanc.pile[self.idx].statut = 'E'
                    tblanc.pile[self.idx].traiteur = self.getName()
                    self.expr = tblanc.pile[self.idx].requete
                    vtblanc.release()
                    break
                
                #On libere le tableau
                vtblanc.release()
                time.sleep(0.1)
 
            # calcul de l'expression
            self.tps = time.clock()
            try:
                self.result = "%s" % eval(self.expr)
            except:
                # Recup d'un eventuel message d'erreur
                self.result = "%s" % sys.exc_info()[1]
                
            self.tps = time.clock()-self.tps
            if self.tps < 0.001:
                self.duree = "< 0.001 s"
            else:
                self.duree = "%.3f s" % self.tps
 
            # donner la reponse dans le message traite du tableau blanc
            vtblanc.acquire()
            self.idx = tblanc.cherche('E',self.getName())
            tblanc.pile[self.idx].reponse = self.result
            tblanc.pile[self.idx].duree = self.duree
            tblanc.pile[self.idx].statut='F'
            vtblanc.release()
            #On compte les executions
            self.nbtraitements += 1
 
            # et bouclage pour un nouveau calcul

###############################################################################
class Fournisseur(threading.Thread):
    """ Le fournisseur accede a la table ordo puis e fonction du type aux tables complementaires """
    
    def __init__(self):
        threading.Thread.__init__(self)
 
    def run(self):
        global vrequetes,requetes
        while True:

            #Lecture de la table Ordo

            #Pour chaque requete active acces auc tables complementaires
            
                # creation d'une nouvelle Requete (avec le statut 'A' = en Attente)
                self.msg = Requete()
                # creation d'une nouvelle expression a calculer
                self.msg.requete = str(random.random()) + "*sqrt(2)+" + str(random.random()) + "*sin(" + str(random.random()) + ")"
 
                # empilage du nouveau message dans le tableau blanc pour traitement
                vtblanc.acquire()
                tblanc.empile(self.msg)
                t = tblanc.taille()
                vtblanc.release()
 
            # attente  jusqu'a t<20 si le tableau blanc est trop plein (t>=100)
            if t>=100:
                while True:
                    vtblanc.acquire()
                    t=tblanc.taille()
                    vtblanc.release()
                    if t<20:
                        break
                    # on se pose la requete avec une tempo pour laisser travailler les traiteurs
                    time.sleep(0.1)


###############################################################################
#      Programme Principal
###############################################################################

# creation du tableau blanc et du verrou qui lui est affecte
tblanc = TBlanc()
vtblanc = threading.Lock()
