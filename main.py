from flask import Flask, render_template

app = Flask(__name__)

professions = [
    "Инженер по жизнеобеспечению",
    "Космический пилот",
    "Специалист по связи",
    "Астрофизик",
    "Химик",
    "Медик",
    "Биолог"
]


@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    if list_type not in ['ol', 'ul']:
        return "Неверный параметр. Используйте 'ol' для нумерованного списка или 'ul' для маркированного."

    return render_template('list_prof.html', list_type=list_type, professions=professions)


if __name__ == '__main__':
    app.run(debug=True)
