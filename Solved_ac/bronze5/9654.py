#9654 나부 함대 데이터

A = ['SHIP NAME', 'N2 Bomber', 'J-Type 327', 'NX Cruiser', 'N1 Starfighter', 'Royal Cruiser']
B = ['CLASS', 'Heavy Fighter', 'Light Combat', 'Medium Fighter', 'Medium Fighter', 'Light Combat']
C = ['DEPLOYMENT', 'Limited', 'Unlimited', 'Limited', 'Unlimited', 'Limited']
D = ['IN SERVICE', '21', '1', '18', '25', '4']

for a, b, c, d in zip(A, B, C, D):
    print(f'{a:15}{b:15}{c:11}{d:10}')