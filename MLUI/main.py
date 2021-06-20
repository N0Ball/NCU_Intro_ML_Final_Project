from flask import(
    Blueprint, render_template, request, flash
)

bp = Blueprint('root', __name__, url_prefix='')

test_data = {
    "title": "Test File",
    "size": 10,
    "datas": {
        "Column 1": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 0
        ],
        "Float Columns": [
            25.1, 2, 2.54, 26, 3, 7.56, 37 ,26.04 ,347, 48.545
        ],
        "String Columns": [
            "ouo", 'nice', 'This', 'is', 'so', 'good', 'i', 'good', 'hell', 'yah'
        ],
        "Boolean Columns":[
            True, False, True, True, True, True, False, True, True, False
        ],
        "Dummy Columns":[
            1, 2, 3, 4, 5, 6, 7, 8, 9, 0
        ],
        "Dummy Columns":[
            1, 2, 3, 4, 5, 6, 7, 8, 9, 0
        ],
        "Dummy Columns":[
            1, 2, 3, 4, 5, 6, 7, 8, 9, 0
        ],
        "Dummy Columns":[
            1, 2, 3, 4, 5, 6, 7, 8, 9, 0
        ],
        "Dummy Columns":[
            1, 2, 3, 4, 5, 6, 7, 8, 9, 0
        ]
    }
}

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')

@bp.route('/view')
def view():

    if request.method == "GET":
        return render_template('view.html', title="表格標題", data=test_data, main_color="warning")

    if request.method == "POST":
        flash("test")

@bp.route('/test')
def test():
    return render_template('test.html', title="輸出", test=test_data, main_color="info")

@bp.route('/user')
def user():
    return render_template('user.html', title="個人資料", main_color="success")