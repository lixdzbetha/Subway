from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/informacion")
def informacion():
    return render_template("informacion.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

