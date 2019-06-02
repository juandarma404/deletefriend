import os
try:
    from requests import get,post
except:
    print "[*] installing libary ..."
    os.system('pip2 install requests;pip install requests')
import json,sys
from time import sleep
W  = '\033[1;37m' 
N  = '\033[0m'
R="\033[1;37m\033[31m" 
B  = '\033[1;37m\033[34m' 
G  = '\033[1;32m' 
r = "\033[91m"
b = "\033[94m"
h = "\033[96m"
y = "\033[93m"
alfan = "###### Automatically delete Facebook friends ######"
pm = "===================================================="
Banner =(
r+"""                   MultiBruteForce   
            #####    ACHMAD 404    #####
                 WA : 085608035292 
                    versi : 2.0 """)
print(y+pm)
print(Banner)
print(y+pm)
print(h+alfan)
print(y+pm)
print "[1] Automatic Delete".format(B,G,B,W)
print "[2] From list\n".format(B,G,B,W)
print(y+pm)
print

class mass():
	def __init__(self):
		self.main()
		
	def main(self):
		while True:
			self.choice=raw_input('{}[++ {}Choice : '.format(R,W))
			if self.choice == "":
				self.main()
				pass
			elif "1" in self.choice:
				self.kontol()
			elif "2" in self.choice:
				self.ngewe()
				self.ngentot()
			else:
				print "{}[-{} Wrong input!".format(R,W)
				
	def kontol(self):
		try:
			self.token=open(raw_input('{}[+{} Masukan list token mu : '.format(B,W))).readline().split('\n')[0]
			print "{}[*]{} Sukses mengambil token ..".format(B,W)
			self.friends= get('https://graph.facebook.com/me/friends?access_token='+self.token).text
			self.data=json.loads(self.friends)
			for self.teman in self.data['data']:
				try:
					self.hitung=self.teman['id']
					try:
						print "\r"+B+"[*]"+W+" mengambil id teman "+str(self.hitung)+" ...",;sys.stdout.flush()
						sleep(000.0001)
					except:
						pass
				except:
					pass
			print "\n{}[*]{} Selesai mengambil id teman ...".format(B,W)
			print "\r"+B+"[*]"+W+" Menghapus semua teman ...\n"
			for self.menghapus in self.data['data']:
				self.hapus=self.menghapus['id']
				self.mulai= post('https://graph.facebook.com/me/friends/'+self.hapus+'?method=delete&access_token='+self.token+'').text
				if "true" in self.mulai:
					print B+"[*] "+W+self.menghapus['name']+R+" =>"+W+" unfriend."
				else:
					print R+"[- Error message :",self.data['error']['message']
		except:
			print R+"[- Failed to open list!"
			self.kontol()
			
	def ngentot(self):
		self.list=raw_input(B+'[+ '+W+'masukan list id '+G+'TEMAN'+W+' mu : ')
		try:
			self.bukaList=open(self.list).readlines()
			self.menghitungList=len(self.bukaList)
			print "{}[*]{} Sukses mengambil id ..".format(B,W)
			print B+"[*] "+R+str(self.menghitungList)+W+" id teman terambil ..."
			print "\r"+B+"[*]"+W+" Menghapus semua teman ...\n"
			for self.gentod in self.bukaList:
				self.a=str(self.gentod).replace('\n','')
				
				self.target=post('https://graph.facebook.com/me/friends/'+str(self.a)+'?method=delete&access_token='+self.token+'').text
				self.js=json.loads(self.target)
				if "true" in self.target:
					try:
						self.e=get('https://graph.facebook.com/'+self.a+'?access_token='+self.token).text
						self.m=json.loads(self.e)
						print B+"[*] "+W+self.m['name']+R+" => "+W+"unfriend."
					except:
						pass
				else:
					print R+"[- Error message :",self.js['error']['message']
		except:
			print R+"[- Failed to open list!"
			self.ngentot()
			
	def ngewe(self):
		try:
			self.token=open(raw_input(B+'[+ '+W+'Masukan list '+G+'TOKEN'+W+' mu : ')).readline().split('\n')[0]
			print B+"[*] "+W+"Sukses mengambil token .."
		except:
			print R+"[- Failed to open list!"
			self.ngewe()
		self.ngentot()
		
if __name__ == "__main__":
	mass()
	
r = "\033[91m"
b = "\033[94m"
h = "\033[96m"
y = "\033[93m"
alfan = "###### Automatically delete Facebook friends ######"
pm = "===================================================="
Banner =(
r+"""                   MultiBruteForce   
            #####    ACHMAD 404    #####
                 WA : 085608035292 
                    versi : 2.0 """)
print(y+pm)
print(Banner)
print(y+pm)
print(h+alfan)
print(y+pm)
print "[1] Automatic Delete"
print "[2] From list\n"
print(y+pm)

class mass():
	def __init__(self):
		self.main()
	def main(self):
		while True:
			peak = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
			if peak == '':
				self.main()
				pass
			elif "1" in peak:
				self.kontol()
			elif "2" in peak:
				self.ngewe()
				self.ngentot()
			else:
				print "{}[-{} Wrong input!".format(R,W)
	
	def kontol(self):
		try:
			print(y+pm)
			self.token=open(raw_input('{}[+{} Masukan list token mu : '.format(B,W))).readline().split('\n')[0]
			print "{}[*]{} Sukses mengambil token ..".format(B,W)
			self.friends= get('https://graph.facebook.com/me/friends?access_token='+self.token).text
			self.data=json.loads(self.friends)
			for self.teman in self.data['data']:
				try:
					self.hitung=self.teman['id']
					try:
						print "\r"+B+"[*]"+W+" mengambil id teman "+str(self.hitung)+" ...",;sys.stdout.flush()
						sleep(000.0001)
					except:
						pass
				except:
					pass
			print "\n{}[*]{} Selesai mengambil id teman ...".format(B,W)
			print "\r"+B+"[*]"+W+" Menghapus semua teman ...\n"
			for self.menghapus in self.data['data']:
				self.hapus=self.menghapus['id']
				self.mulai= post('https://graph.facebook.com/me/friends/'+self.hapus+'?method=delete&access_token='+self.token+'').text
				if "true" in self.mulai:
					print B+"[*] "+W+self.menghapus['name']+R+" =>"+W+" unfriend."
				else:
					print R+"[- Error message :",self.data['error']['message']
		except:
			print R+"[- Failed to open list!"
			self.kontol()
			
	def ngentot(self):
		self.list=raw_input(B+'[+ '+W+'masukan list id '+G+'TEMAN'+W+' mu : ')
		try:
			self.bukaList=open(self.list).readlines()
			self.menghitungList=len(self.bukaList)
			print "{}[*]{} Sukses mengambil id ..".format(B,W)
			print B+"[*] "+R+str(self.menghitungList)+W+" id teman terambil ..."
			print "\r"+B+"[*]"+W+" Menghapus semua teman ...\n"
			for self.gentod in self.bukaList:
				self.a=str(self.gentod).replace('\n','')
				
				self.target=post('https://graph.facebook.com/me/friends/'+str(self.a)+'?method=delete&access_token='+self.token+'').text
				self.js=json.loads(self.target)
				if "true" in self.target:
					try:
						self.e=get('https://graph.facebook.com/'+self.a+'?access_token='+self.token).text
						self.m=json.loads(self.e)
						print B+"[*] "+W+self.m['name']+R+" => "+W+"unfriend."
					except:
						pass
				else:
					print R+"[- Error message :",self.js['error']['message']
		except:
			print R+"[- Failed to open list!"
			self.ngentot()
			
	def ngewe(self):
		try:
			self.token=open(raw_input(B+'[+ '+W+'Masukan list '+G+'TOKEN'+W+' mu : ')).readline().split('\n')[0]
			print B+"[*] "+W+"Sukses mengambil token .."
		except:
			print R+"[- Failed to open list!"
			self.ngewe()
		self.ngentot()
		
if __name__ == "__main__":
	mass()