s= (input('Введите текст: '))+' '
word=0
flag=True
for i in range(len(s)-1):
     if (s[i]==',' or s[i] == '.' or s[i]==';' or s[i+1]==" ") and flag:
          word+=1
          flag=False
     if not(s[i]==',' or s[i] == '.' or s[i]==';' or s[i+1]==" "):
          flag = True

print(word)