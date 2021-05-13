from flask import Flask, render_template, request, json, send_from_directory
from flask_wtf.csrf import CSRFProtect
from flask_mail import Message, Mail
from pdf_generator import editPDF
from pathlib import Path

app =Flask(__name__)

app.config['SECRET_KEY'] = 'f9bf78b9a18ce6d46a0cd2b0b86df9da'
app.config['MAIL_SERVER'] = 'smtpout.secureserver.net'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] ="no-reply@niompmo.com"
app.config['MAIL_PASSWORD'] = "niompmo@12345"
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False



csrf = CSRFProtect()
mail = Mail(app)


coordinate_ls = [
    (360,376,2,10,20,"Times-Bold",0,'black'),
    (326,315,3,10,13,"Times-Regular",0,'black'),
    (440,-120,3,10,13,"Times-Regular",60,'black'),
    (-220,633,3,10,13,"Times-Regular",300,'black'),
    (-507,-220,2,10,20,"Times-Bold",180,'black'),
    (-540,-303,3,10,13,"Times-Regular",180,'black'),
    (-130,-430,3,10,13,"Times-Regular",120,'black'),
    (-520,324,3,10,13,"Times-Regular",240,'black'),
    (80,-442,1.2,5,10,"Times-Bold",90,'white'),
    (-193,-423,1.1,5,10,"Times-Bold",150,'white'),
    (-636,10,1.1,5,10,"Times-Bold",210,'white'),
    (503,153,2,10,20,"Times-Bold",0,'black'),
    (455,78,3,10,13,"Times-Regular",0,'black'),
    (302,-360,3,10,13,"Times-Regular",60,'black'),
    (50,633,3,10,13,"Times-Regular",300,'black'),
    (220,153,2,10,20,"Times-Bold",0,'black'),
    (195,78,3,10,13,"Times-Regular",0,'black'),
    (178,-120,3,10,13,"Times-Regular",60,'black'),
    (-94,393,3,10,13,"Times-Regular",300,'black'),
]

@app.route('/')
def instruction():
    return render_template("instruction.html")

@app.route('/creator/studio/', methods=["POST","GET"])
def creator_studio():
    if request.method == "POST":
        data_ls = []
        for data in dict(json.loads(request.form["element_data"]))["mainElementData"].values():
            data_ls.append(data)
        
        file_name = editPDF(dict(zip(data_ls,coordinate_ls)))
        msg = Message("Digital A.M.P.S", sender = 'no-reply@niompmo.com', recipients = ["projects@nanotech-softapp.com",request.form["email"]])
        msg.html = f"""
            <div style="border: 1px solid black; width: 100%; display: block; float: left; padding: 10px;">
                <h1 style="width: 100%; text-align: center; font-weight: 600; font-size: 14px;">Digital A.M.P.S</h1>
                <br>
                <p style="width: 100%; font-size: 12px;"><span style="font-weight: 500;">Name:</span>&nbsp;{request.form["full_name"]}</p>
                <p style="width: 100%; font-size: 12px;"><span style="font-weight: 500;">Email:</span>&nbsp;{request.form["email"]}</p>
                <p style="width: 100%; font-size: 12px;"><span style="font-weight: 500;">Phone Number:</span>&nbsp;{request.form["contact_number"]}</p>
                <p style="width: 100%; font-size: 12px;"><span style="font-weight: 500;">Location:</span>&nbsp;{request.form["location"]}</p>
                <p style="width: 100%; font-size: 12px;"><span style="font-weight: 500;">Company Website:</span>&nbsp;{request.form["company_website"]}</p>
                <br>
                <h4 style="width: 100%; text-align: center;">Please find attachment:</h4>
            </div>
        """
        with app.open_resource(f"{file_name}") as fp:
            msg.attach(f"{Path(file_name).stem}.pdf",'document/pdf', fp.read())
        mail.send(msg)
        return json.dumps({"status":"Ok","link":f"{Path(file_name).stem}.pdf"})
    return render_template("creator_studio.html")

if __name__ == "__main__":
    app.run(debug=True,port=8000)