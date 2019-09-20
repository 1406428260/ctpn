
s = "12345上山打老虎-@#$%"

print("串长:%d" % len(s))

half_word = 10
one_word  = 20
len = 0
for i in s:

    if ord(i)>=32 and ord(i)<=126:
        len+= half_word
    else:
        len+= one_word
print("len=%d" % len)