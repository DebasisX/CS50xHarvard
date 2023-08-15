import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")



@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    if request.method == "GET":
        id = session["user_id"]
        totalx = 0.0

        traverse = db.execute("SELECT symbol, shares FROM data where id = ?", id)
        for i in traverse:
            temp = i['symbol']
            t = i['shares']
            value = lookup(temp)
            price = value['price']

            symbol = value['symbol']
            total = price * t
            price = round(price, 2)
            total = round(total, 2)
            totalx += total
            db.execute("UPDATE data SET price = ?, total = ? WHERE id = ? AND symbol = ?", price, total, id, symbol)

        userdata = db.execute("SELECT * FROM data WHERE id = ?", id)
        amount = db.execute("SELECT cash FROM users WHERE id = ?", id)
        cash = round((amount[0]['cash']), 2)
        gtot = round((round(cash, 2) + totalx), 2)
        if userdata == []:
            return render_template("index.html", cash=cash)
        else:
            return render_template("index.html", userdata=userdata, cash=cash, gtot=gtot)
    else:
        return render_template("index.html")




@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":
        symbol = request.form.get("symbol")
        share = request.form.get("shares")

        if symbol == "":
            return apology("Invalid Symbol", 400)
        if share == "" or share == 0 or share == None:
            return apology("Invalid Shares", 400)
        else:
            shares = int(share)
            id = session["user_id"]
            value = lookup(symbol)

            price = value['price']
            total = round((shares * price), 4)
            temp = db.execute("SELECT cash FROM users WHERE id = ?", id)
            cash = temp[0]['cash']
            remain = cash - total
            db.execute("INSERT INTO history (id, symbol, share, price, total) VALUES (?, ?, ?, ?, ?)", id, symbol, shares, price, total)
            temp2 = db.execute("SELECT symbol FROM data WHERE id = ? AND symbol = ?", id, symbol)

            if temp2 != []:
                same = temp2[0]['symbol']
                share = db.execute("SELECT shares FROM data WHERE id = ? AND symbol = ?", id, symbol)
                share = share[0]['shares']
                share = share + shares
                if symbol == same and share > 0 and cash >= price:
                    db.execute("UPDATE data SET shares = ? WHERE id = ? AND symbol = ?", share, id, symbol)
                    total = 0.0
                    total = round((share * price), 4)

                    remain = cash - total
                    db.execute("UPDATE data SET price = ? WHERE id = ? AND symbol = ?", price, id, symbol)
                    db.execute("UPDATE data SET total = ? WHERE id = ? AND symbol = ?", total, id, symbol)
                    db.execute("UPDATE users SET cash = ? WHERE id = ?", remain, id)
                    return redirect("/")

            db.execute("UPDATE users SET cash = ? WHERE id = ?", remain, id)
            if shares <= 0 or value == None or cash < price:
                return apology("Invalid Shares", 400)
            else:
                db.execute("INSERT INTO data (id, shares, price, symbol, total) VALUES (?, ?, ?, ?, ?)", id, shares, price, symbol, total)
                return redirect("/")
    else:
        return render_template("buy.html")



@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    if request.method == "GET":
        id = session["user_id"]
        history = db.execute("SELECT * FROM history WHERE id = ?", id)
        return render_template("history.html", history=history)
    else:
        return render_template("history.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        sym = request.form.get("symbol")
        value = lookup(sym)
        if sym != "":
            if value != None:
                return render_template("quoted.html", value=value)
            else:
                return apology("invalid symbol", 400)
        else:
            return apology("blank symbol", 400)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        name = request.form.get("username")
        usernames = db.execute("SELECT username FROM users WHERE username = ?", name)

        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if name != "" and confirmation != "" and password != "" and password == confirmation:
            hash_val = generate_password_hash(password)
            check = db.execute("SELECT hash FROM users WHERE username = (?)", name)
            if usernames != []:
                return apology("invalid username", 400)
            else:
                db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", name, hash_val)
                return render_template("login.html")
        else:
             return apology("must provide username and password", 400)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        id = session["user_id"]
        symbols = db.execute("SELECT symbol FROM data WHERE id = ?", id)
        return render_template("sell.html", symbols=symbols)


    else:
        id = session["user_id"]
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))

        temp = db.execute("SELECT shares FROM data WHERE id = ? AND symbol = ?", id, symbol)
        share = temp[0]['shares']

        if shares <= share:
            value = lookup(symbol)
            price = value['price']
            amount = price * shares

            cash = db.execute("SELECT cash FROM users WHERE id = ?", id)
            paisa = round(cash[0]['cash'], 2)
            sabmilake = amount + paisa
            sharenow = share - shares
            db.execute("INSERT INTO history (id, symbol, share, price, total) VALUES (?, ?, ?, ?, -?)", id, symbol, shares, price, amount)
            db.execute("UPDATE users SET cash = ? WHERE id = ?", sabmilake, id)
            db.execute("UPDATE data SET shares = ? WHERE id = ? AND symbol = ?", sharenow, id, symbol)
            if shares == share:
                db.execute("DELETE FROM data WHERE id = ? AND symbol = ?", id, symbol)
            return redirect("/")
        else:
            return redirect("/")

@app.route("/delete", methods=["GET", "POST"])
@login_required
def delete():
    """DELETE user Permanentely"""
    if request.method == "GET":
        return render_template("delete.html")
    else:
        id = session["user_id"]

        db.execute("DELETE FROM data WHERE id = ?", id)
        db.execute("DELETE FROM history WHERE id = ?", id)
        db.execute("DELETE FROM users WHERE id = ?", id)
        return render_template("login.html")
