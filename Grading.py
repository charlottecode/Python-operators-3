mark1=int(input("enter your marks"))
mark2=int(input("enter your marks"))
mark3=int(input("enter your marks"))

avg=(mark1+mark2+mark3)/3
if avg>91 and avg<100:
    print("grade A1")

elif avg>=81 and avg<90:
    print("grade A2")
elif avg>=71 and avg<80:
    print("grade B1")
elif avg>=61 and avg<70:
    print("grade B2")
elif avg>=51 and avg<60:
    print("grade C1")
elif avg>=41 and avg<50:
    print("grade C2")
elif avg>=32 and avg<40:
    print("grade D")
elif avg>=10 and avg<33:
    print("grade E")

else:
    print("invalid")

