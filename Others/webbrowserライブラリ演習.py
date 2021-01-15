import webbrowser

url = ""
domain = "https://atcoder.jp/"
contests = ["abc","arc","agc"]

url += domain + "contests/"

print("コンテストの種類を入力してください： ")
c = input()

print("何回目のコンテストの問題を閲覧しますか？： ")
n = int(input())
if 10 > n:
    n = "00" + str(n)
elif 100 > n:
    n = "0" + str(n)
else:
    n = str(n)

url += (c+n) + "tasks/"

print("A～Fのどの問題を閲覧しますか？: ")    
print("")
q_idx = int(input())
q = ["all","a","b","c","d","e","f"]

url += (c+n) + "_" + q[q_idx]

webbrowser.open(url)
