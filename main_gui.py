from Tkinter import *
from autocompletion import *
from calculateonline import *
import time
import tkMessageBox
from tkFileDialog   import askopenfilename 
import sys
import thread
from thread import start_new_thread

def ask_quit():
		if tkMessageBox.askokcancel("Quit", "You want to quit now?"):
			root.destroy()
			sys.exit()
def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))
def fetch_studname():
	#global studname
	submit_info['studname']=ent.get()                 #studname


'''
	BLOCK FOR GETTING SGPA

'''
def selectTarget(selectOpt,ent):
	#global targetSGPA
	submit_info['targetSGPA'] = ent.get()
	#print targetSGPA                   #targetSGPA
	selectOpt.quit()
	selectOpt.destroy()
	try:
		if float(submit_info['targetSGPA']) > 10 or float(submit_info['targetSGPA']) < 0:
			getSGPA(INVALID=True)
	except:
		getSGPA(INVALID=True)

		
def getSGPA(INVALID=False):
	
	selectOpt = Toplevel()
	if FLAG_ICO:
		selectOpt.iconbitmap('icon.ico')


	selectOpt.geometry("200x150")
	center(selectOpt)
	if INVALID:
		labelfontHead = ('ariel',10,'bold')
		lb=Label(selectOpt,text='INVALID CGPA')
		lb.config(font=labelfontHead)
		lb.pack(side=TOP,pady=10)
		
	else:
		#Label(selectOpt,text='Enter Target CGPA').pack(side=TOP)
		labelfontHead = ('ariel',10,'bold')
		lb=Label(selectOpt,text='TARGET CGPA')
		lb.config(font=labelfontHead)
		lb.pack(side=TOP,pady=10)
	ent = Entry(selectOpt,text='Enter Target CGPA')
	ent.pack(side=TOP,padx=5,pady=10)
	buttonOpt = Button(selectOpt,command=(lambda: selectTarget(selectOpt,ent)),text='Select',width=10)
	buttonOpt.pack(side=BOTTOM,pady=10)
	selectOpt.mainloop()
'''
     END

'''
'''
	BLOCK FOR GETTING FRIENDS ROLL
'''
def getFriendroll():
	selectOpt = Toplevel()
	selectOpt.geometry("200x200")
	if FLAG_ICO:
		selectOpt.iconbitmap('icon.ico')
	center(selectOpt)
	labelfontHead = ('ariel',10,'bold')
	lb=Label(selectOpt,text='ENTER NAME')
	lb.config(font=labelfontHead)
	lb.pack(side=TOP,pady=10)
	#Label(selectOpt,text='Enter Friends Name').pack(side=TOP)
	ent = AutocompleteEntry(win=selectOpt,lista=names,toplevel=True)
	ent.pack(side=TOP,pady=10)
	buttonOpt = Button(selectOpt,command=(lambda: friendsRoll(selectOpt,ent)),text='Select')
	buttonOpt.pack(side=BOTTOM,pady=10)
	selectOpt.mainloop()
def friendsRoll(selectOpt,ent):
	#global friendsName          #friendsName 
	submit_info['friendsName'] = ent.get()
	selectOpt.quit()
	selectOpt.destroy()

'''
     END

'''

'''
	BLOCK FOR GETTING THE CLASS RANGE	

'''
def getClassRange(selectOpt,ent1,ent2):
	#global classStart
	submit_info['classStart'] = ent1.get()     #classStart
	#global classEnd
	submit_info['classEnd'] = ent2.get()       #classEnd
	selectOpt.quit()
	selectOpt.destroy()
	if submit_info['classStart'].find('130')!=0 or len(submit_info['classStart'])!=7:
		getClassRoll(True)
	if submit_info['classEnd'].find('130')!=0 or len(submit_info['classEnd'])!=7:
		getClassRoll(True)

def getClassRoll(INVALID=False):
	selectOpt = Toplevel()
	selectOpt.geometry("200x200")
	if FLAG_ICO:
		selectOpt.iconbitmap('icon.ico')
	center(selectOpt)
	if INVALID:
		Label(selectOpt,text='INVALID Roll Number Range').pack(side=TOP,pady=10)
	else:
		labelfontHead = ('ariel',10,'bold')
		lb=Label(selectOpt,text='Enter Roll Number Range')
		lb.config(font=labelfontHead)
		lb.pack(side=TOP,pady=10)

	Label(selectOpt,text='Start').pack(side=TOP,pady=(5,0))
	ent1= Entry(selectOpt)
	ent1.pack(side=TOP,pady=(0,10))
	Label(selectOpt,text='End').pack(side=TOP,pady=(5,0))
	ent2 = Entry(selectOpt)
	ent2.pack(side=TOP,pady=(0,10))
	buttonOpt = Button(selectOpt,command=(lambda: getClassRange(selectOpt,ent1,ent2)),text='Select')
	buttonOpt.pack(side=BOTTOM,pady=(0,15))
	selectOpt.mainloop()

'''
     END
     
'''
'''
	BLOCK FOR SELECT Programme

'''
def selectProgram():
	#global selection
	optionSelect()
	btnOption.config(text='Selected option '+str(submit_info['selection']))

def selectOption(var,selectOpt):
		#global selection  
		submit_info['selection'] = var.get()          #OPTION
		selectOpt.quit()
		selectOpt.destroy()

def optionSelect():
	selectOpt = Toplevel()
	var = IntVar()
	if FLAG_ICO:
		selectOpt.iconbitmap('icon.ico')
	center(selectOpt)
	R1 = Radiobutton(selectOpt, text="Show Stats", variable=var, value=1,command=NONE)
	R1.pack( anchor = W ,padx=10,pady=5)

	R2 = Radiobutton(selectOpt, text="Calculate Goal", variable=var, value=2,command=getSGPA)
	R2.pack( anchor = W ,padx=10,pady=5)

	R3 = Radiobutton(selectOpt, text='Compare with Friends', variable=var, value=3,command=getFriendroll)
	R3.pack( anchor = W ,padx=10,pady=5)

	R4 = Radiobutton(selectOpt, text='Class Peformance', variable=var, value=4,command=getClassRoll)
	R4.pack( anchor = W ,padx=10,pady=5)

	buttonOpt = Button(selectOpt,command=(lambda: selectOption(var,selectOpt)),text='Select',width=10)
	buttonOpt.pack(side=BOTTOM,pady=(0,20))
	selectOpt.mainloop()

'''
     END
     
'''
def display_info():
	def exit_info():
		infoBox.destroy()
		infoBox.quit()
	infoBox=Toplevel(root)
	infoBox.geometry('400x300')
	center(infoBox)
	if FLAG_ICO:
		infoBox.iconbitmap('icon.ico')
	infoBox.title('Information')
	infoBox.config(bg='white')
	lb = Label(infoBox,text='Marks Analyser(BETA)',bg='white')
	labelfont = ('ariel','20')
 	lb.config(font=labelfont,bd=2)
	lb.pack(side=TOP,fill=X,pady=(5,1))
	canvas = Canvas(infoBox,width=200,height=200,bg='white')
	try:
		photo=PhotoImage(file='info.gif')
		canvas.create_image((100,75),image=photo)
	except:
		canvas.create_text((100,75),text='IMAGE COULD NOT BE LOADED')

	canvas.create_text((100,150),text='wolframalphaV1.0@gmail.com')
	canvas.create_text((100,175),text='DPK')
	canvas.create_text((100,190),text='Preview Build 06')
	canvas.pack(side=TOP,expand=NO)
	Label(infoBox,text='source code @ https://github.com/wolframalpha/marks-analyser',bg='white').pack(fill=X,side=TOP)
	bt=Button(infoBox,text='OK',command=exit_info,width=17).pack(side=BOTTOM,pady=(0,10))
	infoBox.mainloop()


def submit():
	fetch_studname()
	submit_info['semester']=var1.get()
	#semesterList=['All Semesters','1st Semester','2nd Semester','3rd Semester','4th Semester','5th Semester','6th Semester','7th Semester','8th Semester']
	def semesterSelection(data):
		if data['semester']==semesterList[0]:
			return prep.getCurrentSemester()+1
		elif data['semester']==semesterList[1]:
			return 1
		elif data['semester']==semesterList[2]:
			return 2
		elif data['semester']==semesterList[3]:
			return 3
		elif data['semester']==semesterList[4]:
			return 4
		elif data['semester']==semesterList[5]:
			return 5
		elif data['semester']==semesterList[6]:
			return 6
		elif data['semester']==semesterList[7]:
			return 7
		elif data['semester']==semesterList[8]:
			return 8



	global ONCE           #semester
	if ONCE:
		canvas.pack_forget()
		myscrollbar.pack_forget()
	def scrollF(event):
		canvas.configure(scrollregion=canvas.bbox("all"),width=500,height=1000)
	
	
	OBJ=createProfile(prep,submit_info['studname'])
	if 'classEnd' in submit_info.keys():
		OBJ.calculateClassData(submit_info['classStart'],submit_info['classEnd'])
	info=OBJ.printData()
	#lb = Label(root,text='Marks Analyser')
	labelfontHead = ('ariel','15','bold')
	labelfontData = ('ariel','10') 
	#b.config(font=labelfont,bd=2)
	#lb.pack(side=TOP,fill=X)
	global canvas
	canvas=Canvas(frame2)
	frameC=Frame(canvas)
	frameC.config(bg='white')
	frameC.pack(expand=YES,fill=BOTH)
	global myscrollbar
	myscrollbar=Scrollbar(frame2,orient='vertical',command=canvas.yview)
	canvas.configure(yscrollcommand=myscrollbar.set,bg='white')

	myscrollbar.pack(side='right',fill='y')
	canvas.pack(fill=BOTH)
	canvas.create_window((0,0),window=frameC,anchor='nw')
	frameC.bind('<Configure>',scrollF)

	if semesterSelection(submit_info)==prep.getCurrentSemester()+1:
		for i in range(1,prep.getCurrentSemester()+1):
			lbH=Label(frameC,text='SEMESTER '+str(i),bg='white',fg='black')
			lbH.config(font=labelfontHead)
			lbH.pack(padx=300)
			info=OBJ.printData(i)
			for data in info:
				for line in data:
					if line[0]=='^':
						line.strip('^')
						lbD=Label(frameC,text=line,fg='dark green',bg='white')
					elif line[0]=='~':
						line.strip('~')
						lbD=Label(frameC,text=line,fg='red',bg='white')
					else:
						lbD=Label(frameC,text=line,fg='black',bg='white')
					lbD.config(font=labelfontData)
					lbD.pack(side=TOP)
		#canvas1=Canvas(frameC,width=500,height=200,bg='blue')
		#canvas1.pack(side=TOP)
		#print frameC.winfo_reqwidth()
	else:
		i=semesterSelection(submit_info)
		lbH=Label(frameC,text='SEMESTER '+str(i),bg='white',fg='black')
		lbH.config(font=labelfontHead)
		lbH.pack(padx=300)
		info=OBJ.printData(i)
		for data in info:
			for line in data:
				if line[0]=='^':
					line.strip('^')
					lbD=Label(frameC,text=line,fg='dark green',bg='white')
				elif line[0]=='~':
					line.strip('~')
					lbD=Label(frameC,text=line,fg='red',bg='white')
				else:
					lbD=Label(frameC,text=line,fg='black',bg='white')
				lbD.config(font=labelfontData)
				lbD.pack(side=TOP)
	ONCE=True
	#OBJ.packUP()
	

'''d
#
#	*THE UI STARTS FROM HERE
#
'''


def startup():
	def read_file():
		try:
			path=askopenfilename()
			global prep
			prep = prepareData(textfile=path)
			global names
			names=prep.returnNameList()
			load.quit()
			load.destroy()
		except:
			frame1.pack_forget()
			frame1.destroy()
			print 'failed to load'
			lb.config(text='Files does not exists')
			lb.pack(side=TOP,pady=(10,0))	
			sys.exit(0)

		
	def fetch_data_online():
		try:
			global prep
			prep = prepareData(url='https://docs.google.com/uc?authuser=0&id=0BwUusXozWAMjZFZkTXFXcUNidzg&export=download')
			global names
			names=prep.returnNameList()
			print False
			#mutex.acquire()
			load.after(10,load.destroy)
			#load.quit()	
			#mutex.release()
		except:	
			frame1.pack_forget()
			frame1.destroy()
			print 'failed to load'
			lb.config(text='There was a problem fetching data online')
			lb.pack(side=TOP,pady=(10,0))
			sys.exit(0)
	
	def ask_quit():
		if tkMessageBox.askokcancel("Quit", "You want to quit now?"):
			load.destroy()
			sys.exit()
	def fetchOpt():
		if var.get()==1:
			read_file()
		if var.get()==2:
			start_new_thread(fetch_data_online,())
			btn_fetch.config(text='WAIT')
			btn_fetch.config(state='disabled')
			#etch_data_online()
		return
	mutex=thread.allocate_lock()
	load = Tk()
	load.title('Marks Analyser(beta)')
	load.geometry('300x200')
	load.protocol("WM_DELETE_WINDOW", ask_quit)
	try:
		global FLAG_ICO
		FLAG_ICO=True
		load.iconbitmap('icon.ico')
		
	except:
		global FLAG_ICO
		FLAG_ICO=False
		tkMessageBox.showinfo('warning','icon pack failed to load')
		
	center(load)
	labelfontHead = ('ariel',10,'bold')
		
		
	lb=Label(load,text='SELECT OPTION')
	lb.config(font=labelfontHead)
	lb.pack(side=TOP,pady=10)

	frame1=Frame(load)

	var=IntVar()
	R1 = Radiobutton(frame1, text="FETCH FROM A FILE", variable=var, value=1)#,command=read_file)
	R1.pack( anchor = W ,padx=10,pady=10)

	R2 = Radiobutton(frame1, text="FETCH FROM ONLINE DATABASE", variable=var, value=2)#,command=fetch_data_online)
	R2.pack( anchor = W ,padx=10,pady=10)
	
	btn_fetch=Button(frame1,text='FETCH',command=fetchOpt,width=15)
	btn_fetch.pack(side=BOTTOM,pady=(0,15))

	
	frame1.pack(side=TOP,fill=BOTH,expand=YES,pady=(0,15),padx=(15,15))
	#lb['text']='Fetching from Database...'
	load.mainloop()

'''
	#
	#
	#
'''
#names=[]
startup()	
#print names
global ONCE
ONCE=False
submit_info={}
root = Tk()
root.geometry("800x600")
root.minsize(width=800,height=600)
root.protocol("WM_DELETE_WINDOW", ask_quit)
if FLAG_ICO:
	root.iconbitmap('icon.ico')

frame1 = Frame(root)
frame2 = Frame(root)

#lb = Label(root,text='Marks Analyser')
#labelfont = ('times','20','underline')
#b.config(font=labelfont,bd=2)
#lb.pack(side=TOP,fill=X)

Label(frame1, text='Name ').pack(side=LEFT,padx=10)
ent = AutocompleteEntry(win=frame1,lista=names,width=20,toplevel=False)
ent.pack(padx=10,side=LEFT)
#ent.bind('<Button-1>',(lambda event:fetch()))
#ent.bind('<Return>',(lambda event:fetch()))
 

var1 = StringVar()
semesterList=['All Semesters','1st Semester','2nd Semester','3rd Semester','4th Semester','5th Semester','6th Semester','7th Semester','8th Semester']
var1.set(semesterList[0])
opt1 = OptionMenu(frame1,var1,*semesterList[:prep.getCurrentSemester()+1]) #here selectio semester
opt1.pack(side=LEFT)
var1.set('Select Semester')
var1.set(semesterList[0])
opt1.config(width=20)


btnOption = Button(frame1,text='Select Programme',command=selectProgram)
btnOption.config(width=20)
btnOption.pack(side=LEFT,padx=20)


btnSubmit = Button(frame1,text='RUN',command=submit)
btnSubmit.config(width=20,bg='white')
btnSubmit.pack(side=LEFT,padx=20)


btnInfo = Button(root,text='About Marks Analyser',width=20,command=display_info)
btnInfo.config(width=20,bg='white')
btnInfo.pack(side=BOTTOM,pady=(10,10))


frame1.pack(side=TOP,pady=10,fill=X)


frame2.config(bd=8,relief=GROOVE,bg='white')
frame2.pack(side=BOTTOM,fill=BOTH,padx=20,pady=20,expand=YES)


center(root)
root.title('Marks Analyser(beta)')
root.mainloop()


'''
menuS = Menubutton(frame1,text='Select Semester',underline=0)
menuS.pack(side=RIGHT)
options=Menu(menuS)
options.add_command(label='1st Semester',command=menu,underline=0)
options.add_command(label='2st Semester',command=menu,underline=0)
options.add_command(label='3st Semester',command=menu,underline=0)
menuS.config(menu=options)
menuS.config(relief=RAISED)
menuS.config(width=16)
menuS.pack(side=LEFT,pady=20)
'''
