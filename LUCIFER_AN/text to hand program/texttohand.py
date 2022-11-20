import pywhatkit as pw 
print("Type To Convert as Handwritten : ")
txt = input()

pw.text_to_handwriting(txt, "demo.png",[0,0,138])

print("Your File Is Converted Thanks!")