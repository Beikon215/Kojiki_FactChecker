def lf_cleaner(s):
    if type(s) != str:
        return 0
    else:
        ans = ""
        for i in s:
            if i != "\n" and i != "　" and i != " ":
                ans += i
        return ans


with open("kojiki.txt", encoding="UTF-8") as k:
    input_str = lf_cleaner(input("検証する文字列を入力:"))
    kojiki = k.read()
    for i in range(len(kojiki)):
        if input_str[0] == kojiki[i]:
            for j in range(len(input_str)):
                if input_str[j] != kojiki[i+j]:
                    break
            else:
                print("古事記にもそう書いてある。")
                break
    else:
        print("古事記にはそう書いていない。")
