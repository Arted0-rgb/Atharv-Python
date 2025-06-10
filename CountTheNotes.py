number=int(input("What is the amount of ruppees?"))
note1=number//100
print("The amount of hundred rupee notes is,",  note1)
note2=(number%100)//50
print("The amount of fifty rupee notes is", note2)
note3=((number%100)%50)//10
print("The amount of ten rupee notes is", note3)