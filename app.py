"""
Задание

Создать страницу, на которой будет форма для ввода имени и электронной почты,
при отправке которой будет создан cookie-файл с данными пользователя,
а также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка «Выйти»,
при нажатии на которую будет удалён cookie-файл с данными пользователя и произведено
перенаправление на страницу ввода имени и электронной почты.
"""

from flask import Flask, request, render_template, make_response

app = Flask(__name__)
app.secret_key = 'e929b77fd371a3937f27409f6711ebed3701066b33d702d374be1964c83f8520'


@app.route('/')
def index():
    return f"<h1>Hello World!</h1>"


@app.route('/info/', methods=['GET', 'POST'])
def get_info():
    if request.method == 'POST':
        name = request.form.get('name')
        mail = request.form.get('mail')
        response = make_response(render_template(
            'index.html', name=request.cookies.get('username')))
        response.set_cookie('username', name)
        response.set_cookie('email', mail)
        return response
    return render_template('get_info.html', title='Авторизация')


@app.route('/exit/')
def exit():
    res = make_response(render_template('get_info.html', title='Авторизация'))
    res.set_cookie('username', 'None', max_age=0)
    res.set_cookie('email', 'None', max_age=0)
    return res


if __name__ == '__main__':
    app.run(debug=True)
