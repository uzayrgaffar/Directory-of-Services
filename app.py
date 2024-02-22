from flask import Flask, render_template, request, redirect, url_for, send_from_directory, app, session
import csv
import os

app = Flask(__name__)


RESOURCE = 'resource'
app.config['resource'] =  RESOURCE
app.secret_key = '24201962318371781011'

fieldnames = ['site', 'condition', 'action']
fieldnamesuser = ['site', 'username', 'password', 'role']
suggest1 = ['site', 'addedit', 'old', 'new']
resources = ['site', 'condition' ,'name', 'link']
imagefields = ['site', 'condition', 'name', 'image']

def load_users():
    users = {}
    with open('users.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            users[row['username']] = {
                'username': row['username'],
                'password': row['password'],
                'role': row['role'],
                'site': row['site']
            }
    return users

def replace_value(csv_file_path, old_value_to_replace, new_value_to_replace):
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    for row in rows:
        for i, value in enumerate(row):
            if value == old_value_to_replace:
                row[i] = new_value_to_replace

    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def readconditions(listname, letter):
    with open('conditions.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['condition'][0].lower() == letter:
                listname.append(row)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/verify.html", methods=["POST"])
def verify():
    users = load_users()
    username = request.form.get("username")
    password = request.form.get("password")
    session['username'] = request.form['username']
    session['password'] = request.form['password']

    if username in users and users[username]['password'] == password:
            site = users[username]['site']
            session['site'] = site
            return redirect("/AtoZ.html")
    else:
        return render_template("verify.html")

@app.route("/AtoZ.html")
def AtoZ():
    username = session.get('username')
    site = session.get('site') 
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']

    conditions = []

    with open('conditions.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
                conditions.append(row)

    filter_data = [line for line in conditions if line['site'] == site]
    
    return render_template("AtoZ.html", A=filter_data, role=role)

@app.route("/addusers.html")
def addusers():
    role = session.get('role')
    return render_template("addusers.html", role=role)

@app.route("/profile.html")
def profile():
    username = session.get('username')
    password = session.get('password')
    site = session.get('site')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']

    return render_template("profile.html", username=username, password=password, site=site, role=role)

@app.route("/suggest.html", methods=["POST"])
def usersuggestion():
    site = session.get('site')
    addedit = request.form.get('addedit')
    suggested_condition = request.form.get("suggested_condition")
    oldaction = request.form.get('oldaction')
    suggested_action = request.form.get("suggested_action")
    if suggested_condition:
        firstletter = suggested_condition[0].upper()
        suggested_condition = firstletter + suggested_condition[1:]
    if suggested_action:
        firstletter2 = suggested_action[0].upper()
        suggested_action = firstletter2 + suggested_action[1:]
    with open('suggest.csv', 'a') as file:
        writer = csv.DictWriter(file, fieldnames=suggest1)
        if addedit == 'Add':
            writer.writerow({'site': site, 'addedit': addedit, 'old': suggested_condition, 'new': ''})
        if addedit == 'Edit':
            writer.writerow({'site': site, 'addedit': addedit, 'old': oldaction, 'new': suggested_action})
    return redirect('AtoZ.html')

@app.route("/newuser.html", methods=["POST"])
def newuser():
    site = session.get('site')
    username = request.form.get("username")
    password = request.form.get("password")
    admin = request.form.get("admin")

    with open("users.csv", 'a') as file:
        writer = csv.DictWriter(file ,fieldnames=fieldnamesuser)
        if admin == 'Y':
            writer.writerow({'site': site, 'username': username, 'password': password, 'role': admin})
        else:
            writer.writerow({'site': site, 'username': username, 'password': password, 'role': 'N'})

    return redirect("addusers.html")

@app.route('/replace_value', methods=['POST'])
def replace_condition():
    csv_file_path = 'conditions.csv'
    old_value_to_replace = request.form['old_value_to_replace']
    new_value_to_replace = request.form['new_value_to_replace']

    replace_value(csv_file_path, old_value_to_replace, new_value_to_replace)

    return redirect('A.html')

@app.route("/addresources.html", methods=["POST"])
def addresources():
    site = session.get('site')
    condition = request.form.get('condition')
    name = request.form.get('name')
    link = request.form['link']
    attachment = request.files['file']
    
    if link:
        with open('resources.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=resources)
            firstletter = name[0].upper()
            name = firstletter + name[1:]
            writer.writerow({'site': site, 'condition': condition, 'name': name, 'link': link})

    if attachment:
        filename = os.path.join(app.config['resource'], attachment.filename)
        attachment.save(filename)
        with open('uploaded_files.csv', 'a', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=imagefields)
            firstlettername = name[0].upper()
            name = firstlettername + name[1:]
            csv_writer.writerow({'site': site, 'condition': condition, 'name': name, 'image': attachment.filename})

    return render_template('AtoZ.html', filename=attachment.filename, name=name)

@app.route("/register.html", methods=["POST"])
def register():
    site = session.get('site')
    condition = request.form.get("condition")
    action = request.form.get("action")

    with open('conditions.csv', 'a') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        firstletter = condition[0].upper()
        condition = firstletter + condition[1:] 
        writer.writerow({'site': site, 'condition': condition, 'action': action})
    
        return redirect("/AtoZ.html")

@app.route("/users.html")
def users_list():
    role = session.get('role')
    site = session.get("site")
    user_list = []
    with open('users.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            user_list.append(line)
        user_list = [line for line in user_list if line['site'] == site]
    return render_template("users.html", userslist=user_list, role=role)

@app.route("/suggestions.html")
def suggestions():
    role = session.get('role')
    site = session.get('site')
    suggestions = []
    with open('suggest.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            suggestions.append(line)
    suggestions = [line for line in suggestions if line['site'] == site]
    return render_template("suggestions.html", suggest=suggestions, role=role)

@app.route("/A.html")
def A():
    A_list = []
    username = session.get('username')
    site = session.get('site')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']
    readconditions(A_list, 'a')
    filter_data = [line for line in A_list if line['site'] == site]
    return render_template("A.html", A=filter_data, role=role)

@app.route("/B.html")
def B():
    A_list = []
    username = session.get('username')
    site = session.get('site')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']
    readconditions(A_list, 'b')
    filter_data = [line for line in A_list if line['site'] == site]
    return render_template("B.html", B=filter_data, role=role)

@app.route("/C.html")
def C():
    A_list = []
    username = session.get('username')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']
    readconditions(A_list, 'c')
    site = session.get('site')
    A_list = [line for line in A_list if line['site'] == site]
    return render_template("C.html", C=A_list, role=role)

@app.route("/D.html")
def D():
    A_list = []
    username = session.get('username')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']
    readconditions(A_list, 'd')
    site = session.get('site')
    A_list = [line for line in A_list if line['site'] == site]
    return render_template("D.html", D=A_list, role=role)

@app.route("/E.html")
def E():
    A_list = []
    username = session.get('username')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']
    readconditions(A_list, 'e')
    site = session.get('site')
    A_list = [line for line in A_list if line['site'] == site]
    return render_template("E.html", E=A_list, role=role)

@app.route("/F.html")
def F():
    A_list = []
    username = session.get('username')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']
    readconditions(A_list, 'f')
    site = session.get('site')
    A_list = [line for line in A_list if line['site'] == site]
    return render_template("F.html", F=A_list, role=role)

@app.route("/G.html")
def G():
    A_list = []
    username = session.get('username')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']
    readconditions(A_list, 'g')
    site = session.get('site')
    A_list = [line for line in A_list if line['site'] == site]
    return render_template("G.html", G=A_list, role=role)

@app.route("/H.html")
def H():
    A_list = []
    username = session.get('username')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']
    readconditions(A_list, 'h')
    site = session.get('site')
    A_list = [line for line in A_list if line['site'] == site]
    return render_template("H.html", H=A_list, role=role)

@app.route("/I.html")
def I():
    A_list = []
    username = session.get('username')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']
    readconditions(A_list, 'i')
    site = session.get('site')
    A_list = [line for line in A_list if line['site'] == site]
    return render_template("I.html", I=A_list, role=role)

@app.route("/J.html")
def J():
    A_list = []
    username = session.get('username')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']
    readconditions(A_list, 'j')
    site = session.get('site')
    A_list = [line for line in A_list if line['site'] == site]
    return render_template("J.html", J=A_list, role=role)

@app.route("/K.html")
def K():
    A_list = []
    username = session.get('username')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']
    readconditions(A_list, 'k')
    site = session.get('site')
    A_list = [line for line in A_list if line['site'] == site]
    return render_template("K.html", K=A_list, role=role)

@app.route("/L.html")
def L():
    A_list = []
    username = session.get('username')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']
    readconditions(A_list, 'l')
    site = session.get('site')
    A_list = [line for line in A_list if line['site'] == site]
    return render_template("L.html", L=A_list, role=role)

@app.route("/M.html")
def M():
    A_list = []
    username = session.get('username')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']
    readconditions(A_list, 'm')
    site = session.get('site')
    A_list = [line for line in A_list if line['site'] == site]
    return render_template("M.html", M=A_list, role=role)

@app.route("/N.html")
def N():
    A_list = []
    username = session.get('username')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']
    readconditions(A_list, 'n')
    site = session.get('site')
    A_list = [line for line in A_list if line['site'] == site]
    return render_template("N.html", N=A_list, role=role)

@app.route("/O.html")
def O():
    A_list = []
    username = session.get('username')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']
    readconditions(A_list, 'o')
    site = session.get('site')
    A_list = [line for line in A_list if line['site'] == site]
    return render_template("O.html", O=A_list, role=role)

@app.route("/P.html")
def P():
    A_list = []
    username = session.get('username')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']
    readconditions(A_list, 'p')
    site = session.get('site')
    A_list = [line for line in A_list if line['site'] == site]
    return render_template("P.html", P=A_list, role=role)

@app.route("/Q.html")
def Q():
    A_list = []
    username = session.get('username')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']
    readconditions(A_list, 'q')
    site = session.get('site')
    A_list = [line for line in A_list if line['site'] == site]
    return render_template("Q.html", Q=A_list, role=role)

@app.route("/R.html")
def R():
    A_list = []
    username = session.get('username')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']
    readconditions(A_list, 'r')
    site = session.get('site')
    A_list = [line for line in A_list if line['site'] == site]
    return render_template("R.html", R=A_list, role=role)

@app.route("/S.html")
def S():
    A_list = []
    username = session.get('username')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']
    readconditions(A_list, 's')
    site = session.get('site')
    A_list = [line for line in A_list if line['site'] == site]
    return render_template("S.html", S=A_list, role=role)

@app.route("/T.html")
def T():
    A_list = []
    username = session.get('username')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']
    readconditions(A_list, 't')
    site = session.get('site')
    A_list = [line for line in A_list if line['site'] == site]
    return render_template("T.html", T=A_list, role=role)

@app.route("/U.html")
def U():
    A_list = []
    username = session.get('username')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']
    readconditions(A_list, 'u')
    site = session.get('site')
    A_list = [line for line in A_list if line['site'] == site]
    return render_template("U.html", U=A_list, role=role)

@app.route("/V.html")
def V():
    A_list = []
    username = session.get('username')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']
    readconditions(A_list, 'v')
    site = session.get('site')
    A_list = [line for line in A_list if line['site'] == site]
    return render_template("V.html", V=A_list, role=role)

@app.route("/W.html")
def W():
    A_list = []
    username = session.get('username')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']
    readconditions(A_list, 'w')
    site = session.get('site')
    A_list = [line for line in A_list if line['site'] == site]
    return render_template("W.html", W=A_list, role=role)

@app.route("/X.html")
def X():
    A_list = []
    username = session.get('username')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']
    readconditions(A_list, 'x')
    site = session.get('site')
    A_list = [line for line in A_list if line['site'] == site]
    return render_template("X.html", X=A_list, role=role)

@app.route("/Y.html")
def Y():
    A_list = []
    username = session.get('username')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']
    readconditions(A_list, 'y')
    site = session.get('site')
    A_list = [line for line in A_list if line['site'] == site]
    return render_template("Y.html", Y=A_list, role=role)

@app.route("/Z.html")
def Z():
    A_list = []
    username = session.get('username')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']
    readconditions(A_list, 'z')
    site = session.get('site')
    A_list = [line for line in A_list if line['site'] == site]
    return render_template("Z.html", Z=A_list, role=role)

@app.route('/resources/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['resource'], filename)
    
@app.route("/action.html")
def action():
    condition = request.args.get('condition', '')
    site = session.get('site')
    A_list = []
    with open('conditions.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            A_list.append(line)
        filter_data = [line for line in A_list if line['condition'] == condition]
        filter_data = [line for line in filter_data if line['site'] == site]

    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
        filter_data2 = [line for line in resources_list if line['condition'] == condition]
        filter_data2 = [line for line in filter_data2 if line['site'] == site]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]
        filter_data3 = [line for line in filter_data3 if line['site'] == site]

    username = session.get('username')
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username in row.values():
                role = row['role']

    return render_template("action.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3, role=role)

@app.route("/remove_user/<userslist>", methods=["POST", "DELETE"])
def deregister_user(userslist):
    if request.method in ["POST", "DELETE"]:
        with open('users.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['username'] != userslist]

        with open('users.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnamesuser)
            writer.writeheader()
            writer.writerows(lines)
        return redirect("/users.html")
    
@app.route("/remove_suggest/<suggest>", methods=["POST", "DELETE"])
def deregister_suggest(suggest):
    if request.method in ["POST", "DELETE"]:
        with open('suggest.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['old'] != suggest]

        with open('suggest.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=suggest1)
            writer.writeheader()
            writer.writerows(lines)
        return redirect("/suggestions.html")
    
@app.route("/remove_resource/<name>", methods=["POST", "DELETE"])
def deregister_resource(name):
    if request.method in ["POST", "DELETE"]:
        with open('resources.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['name'] != name]

        with open('resources.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=resources)
            writer.writeheader()
            writer.writerows(lines)
        return redirect("/AtoZ.html")

@app.route("/remove/<A>", methods=["POST", "DELETE"])
def deregister_A(A):
    if request.method in ["POST", "DELETE"]:
        with open('conditions.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != A]

        with open('conditions.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)

        if request.path[8].lower() == 'a':
            return redirect("/A.html")
        elif request.path[8].lower() == 'b':
            return redirect("/B.html")
        elif request.path[8].lower() == 'c':
            return redirect("/C.html")
        elif request.path[8].lower() == 'd':
            return redirect("/D.html")
        elif request.path[8].lower() == 'e':
            return redirect("/E.html")
        elif request.path[8].lower() == 'f':
            return redirect("/F.html")
        elif request.path[8].lower() == 'g':
            return redirect("/G.html")
        elif request.path[8].lower() == 'h':
            return redirect("/H.html")
        elif request.path[8].lower() == 'i':
            return redirect("/I.html")
        elif request.path[8].lower() == 'j':
            return redirect("/J.html")
        elif request.path[8].lower() == 'k':
            return redirect("/K.html")
        elif request.path[8].lower() == 'l':
            return redirect("/L.html")
        elif request.path[8].lower() == 'm':
            return redirect("/M.html")
        elif request.path[8].lower() == 'n':
            return redirect("/N.html")
        elif request.path[8].lower() == 'o':
            return redirect("/O.html")
        elif request.path[8].lower() == 'p':
            return redirect("/P.html")
        elif request.path[8].lower() == 'q':
            return redirect("/Q.html")
        elif request.path[8].lower() == 'r':
            return redirect("/R.html")
        elif request.path[8].lower() == 's':
            return redirect("/S.html")
        elif request.path[8].lower() == 't':
            return redirect("/T.html")
        elif request.path[8].lower() == 'u':
            return redirect("/U.html")
        elif request.path[8].lower() == 'v':
            return redirect("/V.html")
        elif request.path[8].lower() == 'w':
            return redirect("/W.html")
        elif request.path[8].lower() == 'x':
            return redirect("/X.html")
        elif request.path[8].lower() == 'y':
            return redirect("/Y.html")
        elif request.path[8].lower() == 'z':
            return redirect("/Z.html")
        else:
            return redirect("/AtoZ.html")
        
if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
        
        