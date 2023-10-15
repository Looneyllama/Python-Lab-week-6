def listCreation():
  thisList = []
  amount = int(input("Enter number of integers in list: "))
  for i in range(1,amount+1):
    thisList.append(input("Enter item #" + str(i) + ": "))
  return thisList

def maxNumber(thisList):
  new_copy = thisList.copy()
  new_copy.sort()
  print(thisList)
  return new_copy[-2]

def postiveList(thisList):
  for i in range(len(thisList)):
    if(int(thisList[i]) < 0):
      thisList[i] = -1 * int(thisList[i])

thisList = listCreation()
print("My original list: " + str(thisList))
print("Second largest integer in list is " + str(maxNumber(thisList)))
postiveList(thisList)
print("My now positive list is " + str(thisList))
