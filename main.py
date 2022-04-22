# 文字列
print("python実習")
print("Lorem ipsum dolor sit amet, consectetur adipiscing elit")
print("left" + " " + "right")

# 数値
print(1 + 3) # 足し算
print(1 - 3) # 引き算
print(1 * 3) # かけ算
print(1 / 3) # 割り算
print(1 % 3) # 余り
print(2 ** 3) # べき乗

# 変数
x = 8
y = "python実習"
print(x)
print(y)

# リスト
stations = ["東京", "品川", "新横浜", "小田原", "熱海"]
print(stations)

print(stations[0])
print(stations[1])
print(stations[0], stations[1], stations[2], stations[3], stations[4])

# 比較演算子
print(100 > 10)

print(10 > 100)

# if 文
a = 5
b = a % 3

if b == 0:
    print("余りは0")
elif b == 1:
    print("余りは1")
else:
    print("余りは2")

# while 文
i = 0
while i < 10:
    print(i)
    i = i + 1  # iの数値を1増加

i = 0
while i < 10:
    if i == 3:
        break
    print(i)
    i = i + 1

# 無限ループになるためコメントアウトしている
# i = 0
# while True:
#   print(i)
#   i = i + 1

cases = [100, 125, 110, 135, 93, 95, 93]

index = 0  # インデックス値の初期値 0 を設定
total = 0  # casesリストの合計の初期値 0 を設定

while index < 7:  # インデックス値 < casesリストの要素数の間, ループを繰り返す
    total = total + cases[index]  # totalに, cases[index]を加算
    index = index + 1  # index に 1 を加算

print("合計は:", total)

# for 文
cases = [100, 125, 110, 135, 93, 95, 93]
total = 0
for case in cases:
    total = total + case

print("合計は:", total)

# 関数
print(abs(-200))

a = 5
b = 10


def multiply1(x, y):
    result = x * y
    return result


print(multiply1(a, b))  # multiply関数の実行結果がprint関数に渡されて出力される

a = 5
b = 10


def multiply2(x, y):
    result = x * y  # 計算結果を返さない


print(multiply2(a, b))
