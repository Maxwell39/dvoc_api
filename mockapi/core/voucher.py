import string
import random
import csv

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
  return ['DVPD-'+''.join(random.choice(chars) for _ in range(size))]

csvfile=open('voucher.csv','w', newline='')
obj=csv.writer(csvfile)
for x in range (0,99):
  obj.writerow(id_generator(12))
csvfile.close()