import subprocess

def get_logged_in_users_info():
    # whoコマンドを実行
    result = subprocess.run(['who'], stdout=subprocess.PIPE, text=True)
    output = result.stdout.strip()

    users_info = [] #リストを用意
    for line in output.split("\n"): #行毎に繰り返し
        parts = line.split() #空白で一行を分割
        if len(parts) >= 5: #要素が五個以上なら(正常動作なら)
            user = parts[0]  # ユーザー名
            terminal = parts[1]  # ログイン媒体.
            ip_address = parts[2] if '(' in parts[2] else None  # IPアドレス
            login_time = ' '.join(parts[3:5])  # ログイン時刻
            users_info.append({
                "user": user,
                "terminal": terminal,
                "ip_address": ip_address,
                "login_time": login_time
            })

    return users_info

# 結果を取得して表示
info = get_logged_in_users_info()
for entry in info:
    print(f"User: {entry['user']}, Terminal: {entry['terminal']}, IP: {entry['ip_address']}, Login Time: {entry['login_time']}")