from flask import Flask, request

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Flask App</title>
  </head>
  <body>
    {content}
    <hr>
    <nav>
      <a href="/">Home</a> 
      <a href="/add/1/2">Add</a> 
      <a href="/reverse?q=example">Reverse</a>
    </nav>
  </body>
</html>
""".strip()


@app.route("/")
def home():
    content = "<h1>Welcome to Flask App</h1><p>This is the home page.</p>"
    return TEMPLATE.format(content=content)


@app.route("/add/<x>/<y>")
def add(x, y):
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        return TEMPLATE.format(content="<p>Invalid numbers provided.</p>"), 400

    result = f"{x} + {y} = {x + y}"
    content = f"<p>{result}</p>"
    return TEMPLATE.format(content=content)


@app.route("/reverse")
def reverse():
    q = request.args.get("q", "")
    reversed_q = q[::-1]
    content = f"<p>{q}: {reversed_q}</p>"
    return TEMPLATE.format(content=content)


if __name__ == "__main__":
    app.run(debug=True)

