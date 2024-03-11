print("Certificate Eligibitly checker")

status = int(input("enter 1 if you attended all day, enter 0 if you had a gap\n"))


if status == 1:
    assignment = (input("did you complete all the assignment(y/n) = "))
    if assignment == "y":
        liveClass = (input("did you complete all the live class(y/n) = ")) 
        if liveClass == "y":
            camera_on = (input("did you turned on your camera(y/n) = "))
            if camera_on == "y":
                print("Congratulaion you are eligible")
            elif camera_on =="n":
                print(" elligible")
            else:
                print("re-enter")
                
        elif liveClass == "n":
            print("not eligible")
        
        else:
            print("re-enter")
            
    elif assignment == "n":
        print("not eligible")

    else:
        print("re-enter")
        
elif status == 0:
    print("Not eligible")

else:
    print("Re-enter")
    
        