from sys import argv
import struct
script, name = argv
class circle:
   pi = 3.14
   def __init__(self, r=1):
      self.r = r
   def area(self):
      return self.r * self.r * circle.pi
   def perimeter(self):
      return self.r * 2 *circle.pi
   def setR(self, r):
      self.r = r
class rectangle:
   def __init__(self, a=1, b=1):
      self.a = a
      self.b = b
   def area(self):
      return self.a * self.b 
   def perimeter(self):
      return (self.b + self.a) * 2
   def setab(self, a, b):
      self.a = a
      self.b = b
c = circle()
r= rectangle()
if( name == "circle"):
   print "Nhap ban kinh hinh tron: "
   r = raw_input()
   r = float(r)
   c.setR(r)
   print "Dien tich hinh tron: %.2f"%c.area()
   print "Chu vi hinh tron: %.2f"%c.perimeter()
elif( name == "rect"):
   print "Nhap hai canh hinh chu nhat: "
   print "Nhap canh thu nhat: "
   a = raw_input()
   a = float(a)
   print "Nhap canh thu hai: "
   b = raw_input()
   b = float(b)
   r.setab(a,b)
   print "Dien tich hinh chu nhat: %.2f " %r.area()
   print "Chu vi hinh chu nhat: %.2f " %r.perimeter()
else:
   print "Ban nhap sai tham so dong lenh"

   

