N = int(input())
#ver si N es un año bisiesto
if N%4==0 and (N%100!=0 or N%400==0):
    print("si")
else:
    print("no")