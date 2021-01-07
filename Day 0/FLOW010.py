t =int(input())
while(t>0):
    n =input().split()[0]
    if n == 'B' | n=='b':
        print("BattleShip")
    if n == 'C' | n=='c':
        print("Cruiser")
    if n == 'D' | n=='d':
        print("Destroyer")
    if n == 'F' | n=='f':
        print("Frigate")
    t-=1
