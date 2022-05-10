from sys import *

def main():
   if (len(argv) < 2) or (len(argv) == 3 and (argv[2] != "-s" and argv[1] != "-s")):
      print('Usage: [-s] file_name')
      exit()

   
   if argv[1][-3:] == 'txt':
      try:
         inFile = open(argv[1], "r")
      except:
         print('Unable to open ' + argv[1])
         exit()
   elif argv[2][-3:] == 'txt':
      try:
         inFile = open(argv[2], "r")
      except:
         print('Unable to open ' + argv[2])
         exit()

   ints = other = floats = sums = 0
   if len(argv) == 2:
      for line in inFile:
         res = line.split()
         for ind in res:
            if ind.isdigit():
               ints += 1
            elif ind.isalpha():
               other += 1
            else: 
               try:
                  float(ind)
                  floats += 1
               except:
                  other += 1
      print("Ints: %i \nFloats: %i \nOther: %i" % (ints, floats, other))
   else:
      for line in inFile:
         res = line.split()
         for ind in res:
            if ind.isdigit():
               ints += 1
               sums += int(ind)
            elif ind.isalpha():
               other += 1
            else: 
               try:
                  float(ind)
                  floats += 1
                  sums += float(ind)
               except:
                  other += 1
      print("Ints: %i \nFloats: %i \nOther: %i \nSum: %.2f" % (ints, floats, other, sums))


if __name__ == "__main__":
   main()
         
   