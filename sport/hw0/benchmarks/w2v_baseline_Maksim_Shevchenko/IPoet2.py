# -*- coding: utf-8 -*-
__author__ = "Veaceslav Kunitki"
__copyright__ = "Copyright 2016. Please inform me in case of usage"
__credits__ = ["No credits"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Veaceslav Kuntiki"
__email__ = "tumikosha@gmail.com"
__status__ = "Production"
# USAGE:
    # slogTokenizer  return the list of slogs
    # slogTokenizer  return the list of slogs
    # wordScheme  return the scheme of word with looking in dictionary "udar.txt"
    # need initialize :
    #                     iPoet.wordDict=loadWordDict("udar.txt")


import codecs
glas = { 'у', 'е', 'ы', 'а', 'о', 'э', 'я', 'ю', 'и','ё', 'У', 'Е', 'Ы', 'А', 'О', 'Э', 'Я', 'Ю', 'И', 'Ё', '́' };
#glas = { 'у', 'е', 'ы', 'а', 'о', 'э', 'я', 'ю', 'и','ё', 'У', 'Е', 'Ы', 'А', 'О', 'Э', 'Я', 'Ю', 'И', 'Ё' };
ch_udar = '́'; # знак ударения
vowel = "уеыаоэяюиУЕЫАОЭЯЮИ";
wordDict={}



def delUdar(slovo):
    #str.replace(old, new[, max])
    global ch_udar
    res=slovo.replace(ch_udar, "")
    #print(res)
    #res=res+""
    return res

def isUdar(slog):
    if str.find(slog,'́') > -1 :
        return True
    return False

def readFromFile(filename):
    fd = codecs.open(filename,'r',encoding='utf-8')
    with fd as myfile:
        data=myfile.readlines()
    res=""
    for line in data:
        res=res+line
    return res

def readLinesFromFile(filename):
    fd = codecs.open(filename,'r',encoding='utf-8')
    with fd as myfile:
        data=myfile.readlines()
    return data


def numSlogs(slovo):
    slog=0
    for ch in slovo: #for (int i = 0; i < slovo.length(); i++):
        if ch in glas:
            slog=slog+1
    return slog

def isGlas(ch):
    global glas
    if ch in glas: return True
    else: return False

def isSogl(ch):
    if (not isGlas(ch)):
        return True;
    return False;

def isNextGlas(slovo, ps):# проверяет является ли следющая буква гласной
    ch_next = ' ';
    if (ps < len(slovo) - 1):
        ch_next = slovo[ps + 1]
    else :
        ch_next = ' '

    return isGlas(ch_next);

def isNextUdar(slovo, ps):# проверяет является ли следющая буква знаком ударения
    ch_next = ' ';
    if (ps < len(slovo) - 1):
        ch_next = slovo[ps + 1]
    else :
        ch_next = ' '

    return isUdar(ch_next);

def stringTokenizer(sentense,delimiters):
    list=[]
    word=""
    isInWord=False
    for ch in sentense:
        if ch in delimiters:
            if isInWord: # поймали конец слова
                #print(word)
                list.append(word)
                isInWord=False
        else:
            if not isInWord: # поймали начало  слова
                word=""
                isInWord=True
            word=word+ch
    if isInWord: # поймали конец слова
            #rint(word)
            list.append(word)
            isInWord=False
    return list
def is_Before_onlyOne_sogl(slovo, ps):
    # проверяет идет ли перед буквой тоолько одна согласная
    #if (not isGlas(slovo,slovo[ps])):        return False
    ch_prev = ' ';
    ch_prev2 = 'а';
    if (ps > 0):
        ch_prev = slovo[ps - 1];
    if (ps > 1):
        ch_prev2 = slovo.charAt(ps - 2);
    if (isSogl(ch_prev) and (isGlas(ch_prev2))):    return True;
    return False;

def is_Before_MoreOne_sogl( slovo,  ps): #проверяет идет ли перед буквой больше двух согласных
    ch_prev = ' '
    ch_prev2 = 'а'
    if (ps > 0):
        ch_prev = slovo[ps - 1]

    if (ps > 1):
        ch_prev2 = slovo[ps - 2]

    if (isSogl(ch_prev) and (isSogl(ch_prev2))):
        return True


    return False

def sogl_tail(slovo):
    index = len(slovo) - 1;
    tail = "";
    while (isSogl(slovo[index]) and  (index > 0)):
        tail = slovo[index] + tail
        index = index - 1;

    return tail



def slogize3(slovo):
    full = ""
    slog = ""
    solgCounter = 0
    glasCounter = 0
    ch_next = ' '
    if numSlogs(slovo)==0:
        return slovo # нет слогов
    slog=""
    #for ch in slovo:
    for ps in range(len(slovo)):
        ch = slovo[ps];
        #print(">",ch)
        slog = slog + ch;
        #if (ch == '́'):continue;
        if (isNextUdar(slovo,ps)):continue;

        # 		// конец слога если следующая согласная «ко-а-ла»
        if (isGlas(ch) and isNextGlas(slovo, ps)):
            full = full + "-" + slog
            slog = ""
            continue
        if (isGlas(ch) and (not isNextGlas(slovo, ps))):
            full = full + "-" + slog
            slog = ""
            continue
        # на гласную, если перед ней только одна согласная («мо-ло-ко»)
        if (isGlas(ch) and is_Before_onlyOne_sogl(slovo, ps)):
            full = full + "-" + slog
            slog = ""
            continue

        # на гласную, если перед ней только одна согласная («мо-ло-ко»)
        if (isGlas(ch) and is_Before_MoreOne_sogl(slovo, ps)):
            full = full + "-" + slog
            slog = ""
            continue
    tail = sogl_tail(slovo)
    if (len(tail) > 0):
        #full = full + tail.substring(0);
        full = full + tail[0:]

    #return full.substring(1);
    return full[1:]


# def detectUdar(slovo1): # возвращает номер ударного слога
#     global wordDict
#     #slovo = StringUtils.lowerCase(delUdar(slovo1));
#     slovo = str.lower(delUdar(slovo1))
#     if (numSlogs(slovo) == 1):# всего один слог, он и есть ударный
#         return 1
#
#     # check id word exists in dict
#     #if (dict.containsKey(slovo)):
#     if wordDict.get(slovo,False):
#     #if (slovo in wordDict):
#         word = wordDict.get(slovo)
#         #slogs = slogize3(word);
#         slogs = slogize(word);
#         #String[] arr = StringUtil.split(slogs, "-");
#         arr = stringTokenizer(slogs,"-")
#         #for i in range (len(arr) - 1):
#         for i in range (len(arr) ):
#             if ("S" in arr[i]):
#                 #return i + 1
#                 return i
#
#         #ударения не обнаружено
#         return 0





def wordScheme(word): # u-u-u-S-u-u-u
    global wordDict
    slovo=str.lower(delUdar(word))
    new_word=wordDict.get(slovo,False)
    if new_word:
        scheme=slogize(new_word)
    else: scheme=slogize(word)
    return scheme
 # def wordSchemeSimple( word) : # u-u-u-S-u-u-u


# def wordSchemeSimple( word) : # u-u-u-S-u-u-u
#     stressPart = detectUdar(word)
#     scheme = "";
#     ns = numSlogs(word)
#     if (ns == 0) :
#         return ""
#     for i in range (ns):
#         if (i == stressPart):   scheme = scheme + "u-";
#         else:                   scheme = scheme + "u-"
#     return scheme[0:len(scheme) - 1]

def loadWordDict(filename):
    lines=readLinesFromFile ("udar.txt")
    lines2=dict()
    for line in lines:
        list=stringTokenizer(line,"., -!;")
        if len(list)>0:
            word1=list[0]
            lines2.update({str.lower(delUdar(word1)):str.lower(word1)})
            # if (str.lower(delUdar(word1))=="аббатиса"):
            #     print("YEAHHH SUKA")
    return lines2



def slogTokenizer3(word):
    word1=slogize3(word)
    list=stringTokenizer(word1,"-")
    return list

def sentenceScheme(sentense):
    words=stringTokenizer(sentense,",./?\|/:;'\"&~`!@#$%&*()-=+! ")
    result=""
    list1=[]
    list2=[]
    for word in words:
        scheme=wordScheme(word)
        list1.append(word)
        list2.append(scheme)
        result=result+scheme+" "
    return result,list1,list2

def wordNumByPositionInScheme(list,ps):
    num=-1
    length=0
    for word in list:
        num=num+1
        length=length+len(word)+1 # +1 for space
        if length>ps: return num

    return num

def slogTokenizer(word):
    slogs=slogTokenizer3(word)
    flag=False
    for z in range(len(slogs)):
        slog=slogs[z]
        if slog==ch_udar:
            flag=True
            break
    if flag:
        del slogs[z]
        slogs[z-1]=slogs[z-1]+ch_udar
    return slogs




def slogize(word):
     slogs=slogTokenizer(word);
     result=""
     for slog in slogs:
         if ch_udar in slog: result=result+"S-"
         else: result=result+"u-"
     return result[0:len(result)-1]

def isListInListByPostion(bigList,smalList,pos):
    if len(smalList)>len(bigList): return False
    for i in range(len(smalList)):
        if bigList[pos+i]!=smalList[i]: return False
    return True


def filterPhrase(sentense,filter):
    schemeS,list1S,list2S=sentenceScheme(sentense)
    #schemeF,list1F,list2F=sentenceScheme(filter)
    list2F=stringTokenizer(filter," ")
    result=[]
    for i in range(len(list2S)):
        #print("***",i,"***",list2S,":::",list2F)
        if i+len(list2F)>len(list2S): break
        if isListInListByPostion(list2S,list2F,i):
            record=[]
            for j in range(len(list2F)):
                record.append(list1S[i+j])
                #result.append(list1S[i+j])
            result.append(record)
    return result



class Parser:
    text=""
    cursor=0
    stdDelimiters=["???","!!!","!?","?!","'",'"','~','`','!','@','#','&','*','(',')','[',']','+','-','=','/','.',',','?','/','<','>','|','\\',"\n",'\t','\r',' ',";"]
    wordDelimiters=stdDelimiters
    sentenceDelimiters = ['.','?', '!'] # \n ?
    sentenceEndPostion=0
    sentenceStartPostion = 0
    sentenceList = []
    wordEndPostion=0
    wordStartPostion = 0
    wordList = []
    delimiters=[]
    #def __init__(self, initialText, delimitersList):
    def __init__(self):
        #self.text=initialText
        print ("parser initialized")

    def sentenceStartFound(self,startPostion):      self.sentenceStartPostion = startPostion
    def sentenceEndFound(self,endPostion):
        self.sentenceEndPostion=endPostion
        self.sentenceList.append({"sentence": self.text[self.sentenceStartPostion:endPostion], "start": self.sentenceStartPostion, "end": endPostion})
    def wordStartFound(self,startPostion):        self.wordStartPostion = startPostion
    def wordEndFound(self,endPostion):
        self.wordEndPostion=endPostion
        self.wordList.append({"word": self.text[self.wordStartPostion:endPostion], "start": self.wordStartPostion, "end": endPostion})



    def wordFound(self,word,startPostion,endPosition):
        print (word)
    def syllableFound(self,syllable,startPostion,endPosition):
        print (syllable)

    def parse(self,newText):
        self.text=newText
        wordList = []
        sentenceList=[]
        sentence=""
        sentenceStartPos=0
        word = ""
        wordStartPos=0
        syllable=""
        isInWord = False
        isInSentence = False
        isInSyllable = False
        for i in range (len(newText)):
            self.cursor=i
            ch=self.text[i]

            if ch in self.wordDelimiters: #-------------word----------------
                if isInWord:  # поймали конец слова
                    # print(word)
                    #wordList.append({"word":word,"start":wordStartPos,"end":i})
                    isInWord = False
                    self.wordEndFound(i)
            else:
                if not isInWord:  # поймали начало  слова
                    word = ""
                    isInWord = True
                    wordStartPos=i
                    self.wordStartFound(i)
                word = word + ch
            # ---------------

            if ch in self.sentenceDelimiters:#-------------sentence----------------
                if isInSentence:  # поймали конец предложения
                    self.sentenceEndFound(i)
                    #sentenceList.append({"sentence":self.text[sentenceStartPos:i],"start":sentenceStartPos,"end":i})
                    isInSentence = False
            else:
                if (not isInSentence) and (not(ch in self.stdDelimiters)):  # поймали начало предложения
                    sentence = ""
                    isInSentence = True
                    sentenceStartPos = i
                    self.sentenceStartFound( sentenceStartPos)
                sentence = sentence + ch
        if isInSentence:  # поймали конец слова
                #sentenceList.append({"sentence": sentence, "start": sentenceStartPos, "end": i})
                isInSentence = False
        #---------------
        if isInWord:  # поймали конец слова
            #sentenceList.append({"word":word,"start":wordStartPos,"end":i})
            isInWord = False
        #return sentenceList,wordList
        return None


    def getWords(self):
        list=[]
        for wordRec in self.wordList:
            #print (wordRec)
            list.append(wordRec['word'])
        return list


    def getSentences(self):
        list = []
        for rec in self.sentenceList:
            # print (wordRec)
            list.append(rec['sentence'])
        return list


    #-------------------parser2 routines------------------
    inWord=False
    def textStartFound(self,startPostion):        self.textStartPostion = startPostion
    def textEndFound(self,endPostion):
        self.textEndPostion=endPostion
        self.textList.append({"text": self.text[self.textStartPostion:endPostion], "start": self.textStartPostion, "end": endPostion})

    def delimFound(self,position,delim,size):
        if self.inWord==True: # поймали переход со слова на разделитель
            self.textEndFound(position)
        print(position,delim,["x" for x in range(len(delim))])
        self.inWord = False
    def textFound(self,position,ch):
        if self.inWord==False: # поймали переход со разделителя на слово
            self.textStartFound(position)
        print(position,ch , 'O')
        self.inWord=True

    def parse2(self, text):
        self.text=text
        i = 0
        inDelims=True
        while i < len(text):
            ch = text[i]
            flag=False
            for delim in self.stdDelimiters:
                chD = text[i:i+len(delim)]
                if chD==delim:
                    inDelims = True
                    flag=True
                    i=i+len(delim)
                    self.delimFound(i,chD,len(delim))
            if flag==False:
                self.textFound(i,text[i])
                i=i+1
