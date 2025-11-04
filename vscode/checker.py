def checkRect(number01,number02):
    if(number01<=0 or number02<=0):
        return False
    else:
        return True
def checkCircle(number01):
    if(number01<=0):
        return False
    else:
        return True
def checkTriangle(number01,number02,number03):
    success=True
    if(number01<=0 or number02<=0 or number03<=0):
        success=False
    if(number01>number02+number03 or number02>number01+number03 or number03>number01+number02):
        success=False
    if success:
        return True
    else:
        return False
