sec = int(input())
hr = sec // 3600
sec%=3600
mins = sec // 60
sec%=60
print(hr,mins,sec)