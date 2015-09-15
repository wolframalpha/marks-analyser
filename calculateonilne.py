import urllib
import urllib2
class prepareData():
	'''CLASS VARIABLES
		data[]
		names[]
		currentSemester
	'''
	def __init__(self,textfile='encryptedfile.txt',url=-1):
		def decryptFile(textfile):
			filer=open(textfile,'r')
			strings=filer.read()
			counter=-2
			string=''
			for word in strings:
				if counter==3:
					counter=-2
				string=string+chr(ord(word)-counter)
			filer.close()
			return string
		if url==-1:
			filer = decryptFile(textfile)
			lines = filer.split('\n')
			self.data=[]
			for line in lines:
	   			details=line.strip('\n').split(',')
	   			details.remove('')
	   			self.data.append(details)
	   		self.names=[x[1] for x in self.data]
	   		self.currentSemester = 0
			for x in self.data[1][2:]:
				self.currentSemester=self.currentSemester+1
			self.currentSemester=self.currentSemester/2

		else:
			response = urllib2.urlopen(url)
			the_page = response.read()
			lines = the_page.split('\n')
			self.data=[]
			for line in lines:
	   			details=line.strip('\n').split(',')
	   			if '' in details:
	   				details.remove('')
	   			if '\r' in details:
	   				details.remove('\r')	
	   			self.data.append(details)
	   		self.names=[x[1] for x in self.data]
	   		self.currentSemester = 0
			for x in self.data[1][2:]:
				self.currentSemester=self.currentSemester+1
			self.currentSemester=self.currentSemester/2
	
  	def returnNameList(self):
  		return self.names
  	def getCurrentSemester(self):
  		return self.currentSemester

'''data $ branchData
	[0]:roll
	[1]:name
	.
	.
	.
	[n-currentSemester-2]:CGPA-sem3
	[n-currentSemester-1]:CGPA-sem2
	[n-currentSemester]:CGPA-sem1
	.
	.
	.
	[n-2]:SGPA-sem3
	[n-1]:SGPA-sem2
	[n]:SGPA-sem1

	n=currentSemester*2+2-1

'''
class createProfile():
	'''CLASS VARIABLES
		data[]
		names[]
		branchData[]
		currentSemester
		profilename
		classRank_cgpa
		classRank_sgpa
		classAverage_cgpa
		classAverage_sgpa
		classData
		no_of_students_class
		no_of_students_branch
		averageCGPA
		averageSGPA
		allCGPARanks
		allSGPARanks
	'''
	def __init__(self,prepareData,name):
		self.data = prepareData.data
		self.names =prepareData.names 
		self.currentSemester = prepareData.currentSemester
		self.profilename = name.upper()
		ind=self.names.index(name)
		branch=self.data[ind][0][:4]
		self.branchData = []
		self.no_of_students_branch=0
		for dat in self.data:
			if dat[0].find(branch)>=0:
				self.branchData.append(dat)
				self.no_of_students_branch=self.no_of_students_branch+1
				if dat[1]==self.profilename:
					self.profileData=dat
		#self.branchData=sorted(self.branchData,key=lambda x:x[3],reverse=False)
		self.sizeD=self.currentSemester*2+2

	def calcAllRank(self,FLAG=-1):
		self.allSGPARanks = {}	
		self.allCGPARanks = {}
		for i in range(2,2+self.currentSemester):
			branchData=sorted(self.branchData,key=lambda x:x[i],reverse=True)
			counter=0
			previousGPA=0
			for dat in branchData:
				if previousGPA!=float(dat[i]):
					counter=counter+1
				if dat[1]==self.profilename:
					self.allCGPARanks['semester'+str(self.currentSemester-i+2)]=counter
					break

				previousGPA=float(dat[i])
		for i in range(2+self.currentSemester,self.sizeD):
			branchData=sorted(self.branchData,key=lambda x:x[i],reverse=True)
			counter=0
			previousGPA=0
			for dat in branchData:
				if previousGPA!=float(dat[i]):
					counter=counter+1
				if dat[1]==self.profilename:
					self.allSGPARanks['semester'+str(2*self.currentSemester+2-i)]=counter
					break
				previousGPA=float(dat[i])
		#print self.allCGPARanks
		#print self.allSGPARanks
		'''if FLAG != -1:
			if FLAG == 0:
				return self.allCGPARanks['semester'+str(self.currentSemester)]
			else:
				return self.allSGPARanks['semester'+str(FLAG)]
'''	
	def calctotalRank(self,FLAG=-1):
		self.total_SGPARanks = {}	
		self.total_CGPARanks = {}
		for i in range(2,2+self.currentSemester):
			branchData=sorted(self.branchData,key=lambda x:x[i],reverse=True)
			counter=0
			previousGPA=0
			for dat in branchData:
				if previousGPA!=float(dat[i]):
					counter=counter+1	
				previousGPA=float(dat[i])
			self.total_CGPARanks['semester'+str(self.currentSemester-i+2)]=counter

		for i in range(2+self.currentSemester,self.sizeD):
			branchData=sorted(self.branchData,key=lambda x:x[i],reverse=True)
			counter=0
			previousGPA=0
			for dat in branchData:
				if previousGPA!=float(dat[i]):
					counter=counter+1
				previousGPA=float(dat[i])
			self.total_SGPARanks['semester'+str(2*self.currentSemester-i+2)]=counter
		#print self.total_SGPARanks
		#print self.total_CGPARanks

	def calcAverage(self,FLAG=-1):
		self.averageSGPA = {}	
		self.averageCGPA = {}
		for i in range(2,2+self.currentSemester):
			branchData=sorted(self.branchData,key=lambda x:x[i],reverse=True)
			counter=0
			self.averageCGPA['semester'+str(self.currentSemester-i+2)]=0
			for dat in branchData:
				counter=counter+1
				self.averageCGPA['semester'+str(self.currentSemester-i+2)]=self.averageCGPA['semester'+str(self.currentSemester-i+2)]+float(dat[i])
			self.averageCGPA['semester'+str(self.currentSemester-i+2)]=self.averageCGPA['semester'+str(self.currentSemester-i+2)]/counter
		for i in range(2+self.currentSemester,self.sizeD):
			branchData=sorted(self.branchData,key=lambda x:x[i],reverse=True)
			counter=0
			self.averageSGPA['semester'+str(2*self.currentSemester+2-i)]=0
			for dat in branchData:
				counter=counter+1
				self.averageSGPA['semester'+str(2*self.currentSemester+2-i)]=self.averageSGPA['semester'+str(2*self.currentSemester+2-i)]+float(dat[i])
			self.averageSGPA['semester'+str(2*self.currentSemester+2-i)]=self.averageSGPA['semester'+str(2*self.currentSemester+2-i)]/counter
		#print self.averageCGPA
		#print self.averageSGPA

	def getRank(self,sem='All Semesters'):

		"""		
	 	semesterList={	'All Semesters':self.forall,'1st Semester':self.firstsem,
						'2nd Semester':self.secondsem,'3rd Semester':self.thirdsem,
						'4th Semester':self.fourthsem,'5th Semester'=self.fifthsem,
						'6th Semester'=self.sixthsem,'7th Semester':self.seventhsem,
						'8th Semester':self.eigthsem}

		"""			
		semesterList={	'All Semesters':(lambda:self.calcAllRank(0)),'1st Semester':(lambda:self.calcAllRank(1)),
						'2nd Semester':(lambda:self.calcAllRank(2)),'3rd Semester':(lambda:self.calcAllRank(3)),
						'4th Semester':(lambda:self.calcAllRank(4)),'5th Semester':(lambda:self.calcAllRank(5)),
						'6th Semester':(lambda:self.calcAllRank(6)),'7th Semester':(lambda:self.calcAllRank(7)),
						'8th Semester':(lambda:self.calcAllRank(8))
					}
		rank=semesterList[sem]()
		return rank
	
	'''def calculateClassRank(self):
		classData = sorted(self.classData,key=lambda x:x[2],reverse=True)
		counter=0
		previousGPA=0
		for dat in classData:
			if previousGPA!=float(dat[2]):
				counter=counter+1
			if dat[1]==self.profilename:
				break
			previousGPA=float(dat[2])
		self.classRank_cgpa=counter
		classData = sorted(self.classData,key=lambda x:x[2+self.currentSemester],reverse=True)
		counter=0
		previousGPA=0
		for dat in classData:
			if previousGPA!=float(dat[2]):
				counter=counter+1
			if dat[1]==self.profilename:
				break
			previousGPA=float(dat[2+self.currentSemester])
		self.classRank_sgpa=counter
		print self.classRank_sgpa
		print self.classRank_cgpa
	'''
	def calculateClassRank(self):
		self.allSGPARanks_class = {}	
		self.allCGPARanks_class = {}
		for i in range(2,2+self.currentSemester):
			classData=sorted(self.classData,key=lambda x:x[i],reverse=True)
			counter=0
			previousGPA=0
			for dat in classData:
				if previousGPA!=float(dat[i]):
					counter=counter+1
				if dat[1]==self.profilename:
					self.allCGPARanks_class['semester'+str(self.currentSemester-i+2)]=counter
					break

				previousGPA=float(dat[i])
		for i in range(2+self.currentSemester,self.sizeD):
			classData=sorted(self.classData,key=lambda x:x[i],reverse=True)
			counter=0
			previousGPA=0
			for dat in classData:
				if previousGPA!=float(dat[i]):
					counter=counter+1
				if dat[1]==self.profilename:
					self.allSGPARanks_class['semester'+str(2*self.currentSemester+2-i)]=counter
					break
				previousGPA=float(dat[i])
		#print self.allSGPARanks_class
		#print self.allCGPARanks_class
	def calctotalRank_class(self):
		self.total_SGPARanks_class = {}	
		self.total_CGPARanks_class = {}
		for i in range(2,2+self.currentSemester):
			classData=sorted(self.classData,key=lambda x:x[i],reverse=True)
			counter=0
			previousGPA=0
			for dat in classData:
				if previousGPA!=float(dat[i]):
					counter=counter+1	
				previousGPA=float(dat[i])
			self.total_CGPARanks_class['semester'+str(self.currentSemester-i+2)]=counter

		for i in range(2+self.currentSemester,self.sizeD):
			classData=sorted(self.classData,key=lambda x:x[i],reverse=True)
			counter=0
			previousGPA=0
			for dat in classData:
				if previousGPA!=float(dat[i]):
					counter=counter+1
				previousGPA=float(dat[i])
			self.total_SGPARanks_class['semester'+str(2*self.currentSemester-i+2)]=counter
		print self.total_SGPARanks_class
		print self.total_CGPARanks_class
	def calculateClassAverage(self):
		self.classAverage_cgpa=0
		self.classAverage_sgpa=0
		for dat in self.classData:
			self.classAverage_cgpa=self.classAverage_cgpa+float(dat[2])
			self.classAverage_sgpa=self.classAverage_sgpa+float(dat[2+self.currentSemester])
		self.classAverage_cgpa=self.classAverage_cgpa/self.no_of_students_class
		self.classAverage_sgpa=self.classAverage_sgpa/self.no_of_students_class

	def calculateClassData(self,classStart,classEnd): #callable
		self.classData=[]
		self.no_of_students_class=0
		for dat in self.branchData:
			if int(dat[0]) in range(int(classStart),int(classEnd)+1):
				self.classData.append(dat)
				self.no_of_students_class=self.no_of_students_class+1
		self.calculateClassRank()
		self.calculateClassAverage()
		self.calctotalRank_class()
	#def goalCGPA(self,goal):
		

	def packUP(self):
		self.encodedData={}
		self.calcAllRank()
		self.calcAverage()
		self.encodedData['currentSemester']=self.currentSemester
		self.encodedData['profilename']=self.profilename
		
		self.encodedData['no_of_students_branch']=self.no_of_students_branch
		self.encodedData['averageCGPA']=self.averageCGPA
		self.encodedData['averageSGPA']=self.averageSGPA
		self.encodedData['allCGPARanks']=self.allCGPARanks
		self.encodedData['allSGPARanks']=self.allSGPARanks
		if hasattr(self,'classData'):
			self.encodedData['classRank_cgpa']=self.allCGPARanks_class
			self.encodedData['classRank_sgpa']=self.allSGPARanks_class
			self.encodedData['classAverage_sgpa']=self.classAverage_sgpa
			self.encodedData['classAverage_cgpa']=self.classAverage_cgpa
			self.encodedData['no_of_students_class']=self.no_of_students_class
		#self.encodedData['classData']=self.classData
		return self.encodedData
	def printData(self,curr=-1):
		info=[]
		self.calcAllRank()
		self.calcAverage()
		self.calctotalRank()
		def profile(string):
			if string=='name':
				return self.profilename
			elif 'cgpa' in string:
				i=int(string[4])
				return pr(self.profileData[self.currentSemester-i+2])
			elif 'sgpa' in string:
				i=int(string[4])
				return pr(self.profileData[2*self.currentSemester-i+2])

		def semester(i):
			return 'semester'+str(i)
		def pr(num):
			return round(float(num),2)
		if curr==-1:
			curr=self.currentSemester
		info_current=[]
		line='CGPA : '+str(profile('cgpa'+str(curr)))
		info_current.append(line)
		line='SGPA : '+str(profile('sgpa'+str(curr)))
		info_current.append(line)
		
		line='Branch rank according to CGPA : '+str(self.allCGPARanks[semester(curr)])+' out of '+str(self.total_CGPARanks[semester(curr)])
		if self.allCGPARanks[semester(curr)]<self.total_CGPARanks[semester(curr)]/2:
			info_current.append('^'+line)
		else:
			info_current.append('~'+line)
		
		line='Branch rank according to SGPA : '+str(self.allSGPARanks[semester(curr)])+' out of '+str(self.total_SGPARanks[semester(curr)])
		if self.allSGPARanks[semester(curr)]<self.total_SGPARanks[semester(curr)]/2:
			info_current.append('^'+line)
		else:
			info_current.append('~'+line)
		
		line='Your current CGPA is '+str(profile('cgpa'+str(curr)))+' while branch average CGPA is '+str(pr(self.averageCGPA['semester'+str(curr)]))
		if profile('cgpa'+str(curr))>self.averageCGPA['semester'+str(curr)]:
			info_current.append('^'+line)
		else:
			info_current.append('~'+line)

		line='Your current SGPA is '+str(profile('sgpa'+str(curr)))+' while branch average SGPA is '+str(pr(self.averageSGPA['semester'+str(curr)]))
		if profile('sgpa'+str(curr))>self.averageSGPA['semester'+str(curr)]:
			info_current.append('^'+line)
		else:
			info_current.append('~'+line)
		
		print info_current

		info.append(info_current)
		if curr!=1:
			info_compare=[]
			if profile('sgpa'+str(curr))>profile('sgpa'+str(curr-1)):
				line = '^Your SGPA increased by '+str((profile('sgpa'+str(curr))-profile('sgpa'+str(curr-1)))*10)+' percent'
			else:
				line = '~Your SGPA decreased by '+str((profile('sgpa'+str(curr-1))-profile('sgpa'+str(curr)))*10)+' percent'
			if self.averageSGPA[semester(curr)]>self.averageSGPA[semester(curr-1)]:
				lineadd = '^branch average SGPA increased by '+str(pr(self.averageSGPA[semester(curr)]-self.averageSGPA[semester(curr-1)])*10)+' percent'
			else:
				lineadd = '~branch average SGPA decreased by '+str(pr(self.averageSGPA[semester(curr-1)]-self.averageSGPA[semester(curr)])*10)+' percent'
			info_compare.append(line+' '+lineadd)
			if self.allCGPARanks[semester(curr)]<self.allCGPARanks[semester(curr-1)]:
				line = '^Your rank decreased by '+str(self.allCGPARanks[semester(curr-1)]-self.allCGPARanks[semester(curr)])+' from the previous semester'
			else:
				line = '~Your rank increase by '+str(self.allCGPARanks[semester(curr)]-self.allCGPARanks[semester(curr-1)])+' from the previous semester'
			info_compare.append(line)
			print info_compare
			info.append(info_compare)
			#return info_current,info_compare
		if hasattr(self,'classData'):
			info_class=[]
			
			line = 'Class Rank according to CGPA : '+str(self.allCGPARanks_class[semester(curr)])+' out of '+str(self.total_CGPARanks_class[semester(curr)])
			if self.allCGPARanks_class[semester(curr)]<self.total_CGPARanks_class[semester(curr)]/2:
				info_class.append('^'+line)
			else:
				info_class.append('~'+line)
			
			line = 'Class Rank according to SGPA : '+str(self.allSGPARanks_class[semester(curr)])+' out of '+str(self.total_SGPARanks_class[semester(curr)])
			if self.allSGPARanks_class[semester(curr)]<self.total_SGPARanks_class[semester(curr)]/2:
				info_class.append('^'+line)
			else:
				info_class.append('~'+line)
			
			print info_class
			info.append(info_class)
		return info

if __name__ == '__main__':
	#print createProfile(prepareData(),'SUBODH KUMAR JHA').getRank('1st Semester')
	OBJ=createProfile(prepareData(),'AMRIT RAJ VARDHAN')
	OBJ.calculateClassData(1305118,1305183)
	#OBJ.packUP()
	OBJ.printData()


#print prepareData().returnNameList()
