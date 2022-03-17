# flask: mikrowebframework, lader os udvikle webapplikationer
# from flask import Flask: 
# render_template: bruges til at generere output fra vores html
# request: til vores post metode

from flask import Flask, render_template, request 
import pyodbc # installed by pip - forbindelse til database


# objekt fra Flask-klassen med standardnavn __name__
app = Flask(__name__)

# vores dekorator. Fortæller applikationen hvilken url nedenstående funktion skal køre på
@app.route('/')
@app.route('/index')


def showindexpage() :
    # forbindelse til database
    conn = pyodbc.connect(Trusted_Connection = 'yes', driver = '{SQL Server}', server='DESKTOP-GSM8CHG\MSSQLSERVER01', database='CarsDB')

    # cursor = objekt der hjælper med at udføre forespørgslen og hente poster fra database
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Cars")

    mydata = cursor.fetchall()

    cursor.execute("SELECT * FROM Cars ORDER BY MaxSpeed DESC")
    fastest_car = cursor.fetchone()

    conn.close()
    return render_template("index.html", 
        the_title = "All cars",
        values = mydata,
        fastest_car = fastest_car)


# dekorator for funktion for at oprette siden create.html
@app.route('/create')

def create_page():
    return render_template(
        "create.html",
        the_title = "Create car")

# dekorator, nu koder for vi create.html men for den del der har en post. Klikker submit
@app.route('/create', methods=['POST'])
def create_car():
    model = request.form['model']
    maxspeed = request.form['maxSpeed']

    conn = pyodbc. connect(Trusted_Connection = 'yes', driver = '{SQL Server}', server = 'DESKTOP-GSM8CHG\MSSQLSERVER01', database = 'CarsDB')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Cars (Model, MaxSpeed) VALUES (?, ?)", model, maxspeed)
    conn.commit()

    conn.close()

    return render_template(
        'create.html',
        the_title = "Create car") 


# if til localhost 4449
if __name__ == '__main__' :
    app.run('localhost', 4449)

