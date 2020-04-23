def codetoname(code) :
    code = code.lower()
    if code == "af" :
        return "Afghanistan"
    elif code == "al" :
        return "Albania"
    elif code == "dz" :
        return "Algeria"
    elif code == "as" :
        return "American Samoa"
    elif code == "ad" :
        return "Andorra"
    elif code == "ao" :
        return "Angola"
    elif code == "ai" :
        return "Anguilla"
    elif code == "aq" :
        return "Antarctica"
    elif code == "ag" :
        return "Antigua and Barbuda"
    elif code == "ar" :
        return "Argentina"
    elif code == "am" :
        return "Armenia"
    elif code == "aw" :
        return "Aruba"
    elif code == "au" :
        return "Australia"
    elif code == "at" :
        return "Austria"
    elif code == "az" :
        return "Azerbaijan"
    
    
def nametocode(code) :
    code = code.lower()
    if code == "afghanistan" :
        return "AF"
    elif code == "albania" :
        return "AL"
    elif code == "algeria" :
        return "DZ"
    elif code == "american samoa" :
        return "AS"
    elif code == "andorra" :
        return "AD"
    elif code == "angola" :
        return "AO"
    elif code == "anguilla" :
        return "AI"
    elif code == "antarctica" :
        return "AQ"
    elif code == "antigua and barbuda" :
        return "AG"
    elif code == "argentina" :
        return "AR"
    elif code == "armenia" :
        return "AM"
    elif code == "aruba" :
        return "AW"
    elif code == "australia" :
        return "AU"
    elif code == "Austria" :
        return "AT"
    elif code == "azerbaijan" :
        return "AZ"
    
    
    
print(nametocode(input()))