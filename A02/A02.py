import threading, time


class CounterThread(threading.Thread):
    """
    Diese Klasse stellt einen Thread dar,
    welcher ein ihm übergebene Wort ver- beziehungseweise
    entschlüsselt.

    :ivar String text: Text der verschlüsselt werden soll
    :ivar int thread_number: Nummer des Threads
    :param String text: Text der verschlüsselt werden soll
    :param int thread_number: Nummer des Threads
    """

    # Klassenvariable für die Anzahl an Threads
    __anzahl = 0

    # Dictionary für Verschlüsselung
    __dict = {'a':'z',
              'b':'a',
              'c':'b',
              'd':'c',
              'e':'d',
              'f':'e',
              'g':'f',
              'h':'g',
              'i':'h',
              'j':'i',
              'k':'j',
              'l':'k',
              'm':'l',
              'n':'m',
              'o':'n',
              'p':'o',
              'q':'p',
              'r':'q',
              's':'r',
              't':'s',
              'u':'t',
              'v':'u',
              'w':'v',
              'x':'w',
              'y':'x',
              'z':'y',
              ' ':' '}
    #Klassenvariable für die möglichen inputs
    __inputmessages = ['Which message do you want to encrypt?',
                       'How many threads should encrypt the message?',
                       'Your encrypted message:']
    #Verschlüsseltes Word
    __encryptword = ''
    #Entschlüsseltes Wort
    __decryptword = ''
    def __init__(self, thread_number, text):
        """
        Initialisiert die Superklasse und speichert
        die Parameter in die Instanzvariablen.
        :param thread_number: Nummer des neuen Threads
        :param text: Text der verschlüsselt werden soll
        """
        threading.Thread.__init__(self)
        self.thread_number = thread_number
        self.text = text
        CounterThread.__anzahl += 1


    @classmethod
    def get_thread_information(cls,outword):
        """
        Liefert die Gesamtanzahl an Threads sowie
        das ver- bzw entschlüsselte Wortzurück.
        :return: Anzahl an erzeugten Threads
        """
        s = ('Threads: %d         ' % (cls.__anzahl)
             )

        if outword == 0:
            return s + 'encrypted word: ' + cls.__encryptword
        else:
            return s + 'decrypted word: ' + cls.__decryptword


    def run(self):
        """
        Speichert für jeden Character den verchlüsselten Wert in __encryptword ab
        und den entschlüsselten in __decryptword.
        :return: None
        """
        for c in self.text:
            CounterThread.__encryptword += CounterThread.__dict[c]
            # print ('Thread Number: '+str(CounterThread.__anzahl)+'  Letters: '+CounterThread.__dict[c]),

        for g in CounterThread.__encryptword:
            CounterThread.__decryptword += list(CounterThread.__dict.keys())[list(CounterThread.__dict.values()).index(g)]

    def inputs(i):
        """
        Gibt die Nachricht am index i der Message-Liste aus.
        :param: i index einer bestimmten Nachricht
        :return: userinput: Eingabeaufforderung mit der richtigen Nachricht als Output
        """
        userinput = input(CounterThread.__inputmessages[i])
        return userinput


threads = []

#Gewünschter Text input
word = CounterThread.inputs(0).lower()

#Anzahl der gewünschten Threads input
anzthreads = CounterThread.inputs(1)

#Anzahl an Charactern die pro Thread verarbeitet wird
step = int(len(word)/int(anzthreads))+1

#Aktuellerr index beim Einlesen des Wortes
currentindex = 0


#Falls mehr Threads gewünscht als Character im Wort vorhanden sind
#wird die Anzahl auf diese reduziert.
if len(word) >= int(anzthreads):
    #Schleife zum Erzeugen einzenler Threads
    for i in range(0,int(anzthreads)):
        thread = CounterThread(i, word[currentindex:(currentindex + step)])
        threads += [thread]
        # Thread gleich starten
        thread.start()
        # Aktueller Index wird erhöht
        currentindex += step
    print (CounterThread.get_thread_information(0))
    print (CounterThread.get_thread_information(1))

else:
    anzthreads = len(word)
    print ("Useless number of threads."
           "Reduced to one thread per character")
    for i in range(0,int(anzthreads)):
        thread = CounterThread(i, word[currentindex:(currentindex + step)])
        threads += [thread]
        # Thread gleich starten
        thread.start()
        currentindex += step
    print (CounterThread.get_thread_information(0))
    print(CounterThread.get_thread_information(1))

# Auf die Terminierung aller Threads warten
for x in threads:
    x.join()
