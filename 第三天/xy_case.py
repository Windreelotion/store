class case:
    login_success_data = [
        {"username": "jason", "passwork": "1234567", "expect": "Student Login"},
        {"username":"admin","passwork":"root","expect":"Student Login"},
        {"username": "jason", "passwork": "root", "expect": "Student Login12345"}
    ]

    login_error_data = [
        {"username": "jason0", "passwork": "1234567", "expect": "账户名错误或密码错误!别瞎弄!"},
        {"username": "jason", "passwork": "root0", "expect": "账户名错误或密码错误!别瞎弄!"}
    ]
