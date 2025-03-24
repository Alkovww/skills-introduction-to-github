def extended_gcd(a, b): 
    if b == 0: 
        return (a, 1, 0) 
    else: 
        g, x, y = extended_gcd(b, a % b) 
        return (g, y, x - (a // b) * y) 

def find_solution(a, b, c): 
    g, x, y = extended_gcd(a, b) 
    if c % g != 0: 
        return "Impossible" 
    x *= c // g 
    y *= c // g 
    t = b // g 
    x = x % t 
    if x < 0: 
        x += t 
    y = (c - a * x) // b 
    return f"{x} {y}" 

def main(): 
    print("Входные данные (введите a, b и c через пробел): ") 
    a, b, c = map(int, input().split())    
  
    result = find_solution(a, b, c) 
    print("Выходные данные: ", result) 
    print("Сдала Ковалевская Алёна Михайловна, 020303-АИСа-о24")

if __name__ == "__main__": 
    main()
