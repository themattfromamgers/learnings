
# MAKİNE DİLİ

class ascii:
    def __init__(self, binary):
        pass
    
    binary = {
        "100 0001": "A",
        "A": "100 0001",
        "110 0001": "a",
        "a": "110 0001",
        
        "100 0010": "B",
        "B": "100 0010",
        "110 0010": "b",
        "b": "110 0010",
        
        "100 0011": "C",
        "C": "100 0011",
        "110 0011": "c",
        "c": "110 0011"  
    }
    
    decimal = {
        "A": 65,
        65: "A",
        97: "a",
        "a": 97,
        
        66: "B",
        "B": 66,
        98: "b",
        "b": 98
        
        
    }
print(ascii.decimal.get("b"))