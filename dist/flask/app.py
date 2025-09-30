from flask import Flask, render_template, request, redirect, url_for, flash
import ast
import operator as op

app = Flask(__name__)
app.secret_key = "dev"  # flash 메시지 사용 시 필요 (로컬 개발용)

# 허용된 연산자 매핑
_allowed_ops = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.FloorDiv: op.floordiv,
    ast.Mod: op.mod,
    ast.Pow: op.pow,
    ast.UAdd: lambda x: x,
    ast.USub: lambda x: -x,
}

def safe_eval(expr: str):
    """
    ast를 이용한 안전한 수식 평가기.
    숫자와 사칙연산, 제곱(pow), 나눗셈, 모듈로, 음수/양수만 허용.
    함수 호출이나 변수 참조, attribute 접근 등은 차단합니다.
    """
    expr = expr.strip()
    if not expr:
        raise ValueError("빈 수식")

    node = ast.parse(expr, mode='eval')

    def _eval(n):
        if isinstance(n, ast.Expression):
            return _eval(n.body)
        if isinstance(n, ast.Constant):  # Python 3.8+
            if isinstance(n.value, (int, float)):
                return n.value
            raise ValueError("허용되지 않는 상수입니다.")
        if isinstance(n, ast.Num):  # older
            return n.n
        if isinstance(n, ast.BinOp):
            left = _eval(n.left)
            right = _eval(n.right)
            op_type = type(n.op)
            if op_type in _allowed_ops:
                return _allowed_ops[op_type](left, right)
            raise ValueError("허용되지 않는 이항 연산자입니다.")
        if isinstance(n, ast.UnaryOp):
            operand = _eval(n.operand)
            op_type = type(n.op)
            if op_type in _allowed_ops:
                return _allowed_ops[op_type](operand)
            raise ValueError("허용되지 않는 단항 연산자입니다.")
        # 모든 호출, 변수, comprehension 등은 금지
        raise ValueError("허용되지 않는 표현식입니다.")

    return _eval(node)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gugudan", methods=["GET", "POST"])
def gugudan():
    table = None
    n = None
    if request.method == "POST":
        try:
            n_raw = request.form.get("n", "")
            n = int(n_raw)
            if not (1 <= n <= 999):
                flash("1 이상 999 이하의 정수를 입력하세요.")
                return redirect(url_for("gugudan"))
            table = [(i, n * i) for i in range(1, 10)]
        except ValueError:
            flash("올바른 정수를 입력하세요.")
            return redirect(url_for("gugudan"))
    return render_template("gugudan.html", n=n, table=table)

@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    result = None
    equation = ""
    error = None
    if request.method == "POST":
        equation = request.form.get("equation", "")
        try:
            value = safe_eval(equation)
            result = f"{equation} = {value}"
        except ZeroDivisionError:
            error = "오류: 0으로 나눌 수 없습니다."
        except Exception as e:
            error = f"오류: {e}"
    return render_template("calculator.html", equation=equation, result=result, error=error)

@app.route("/calculator_js")
def calculator_js():
    # 클라이언트 사이드 JS 계산기 예시 페이지
    return render_template("calculator_js.html")

if __name__ == "__main__":
    app.run(debug=True)
