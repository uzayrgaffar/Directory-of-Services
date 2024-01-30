from flask import Flask, render_template, request, redirect, url_for, send_from_directory, app
import csv
import os

app = Flask(__name__)


RESOURCE = 'resource'
app.config['resource'] =  RESOURCE
app.secret_key = '24201962318371781011'

fieldnames = ['condition', 'action']
fieldnamesuser = ['username', 'password', 'role']
suggest1 = ['addedit', 'oldaction', 'newaction']
suggestadd = ['addedit', 'condition']
resources = ['condition' ,'name', 'link']
imagefields = ['condition', 'name', 'image']

def load_users():
    users = {}
    with open('users.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            users[row['username']] = {
                'username': row['username'],
                'password': row['password'],
                'role': row['role']
            }
    return users

def upload_file_logic(file, name, upload_folder):
    if file:
        filename = os.path.join(upload_folder, name)
        file.save(filename)
        return True, filename
    return False, None


def remove_file(upload_folder, filename):
    filepath = os.path.join(upload_folder, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        return True
    return False

def get_unique_old_values(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Extract unique values from all columns
    all_values = [value for row in rows for value in row]
    unique_old_values = list(set(all_values))

    return unique_old_values

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

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/verify.html", methods=["POST"])
def verify():
    users = load_users()
    username = request.form.get("username")
    password = request.form.get("password")

    check_admin = []
    with open('users.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            check_admin.append(line)
        if username in users and users[username]['password'] == password:
            if users[username]['role'] == 'Y':
                return redirect("/AtoZ.html")
            else:
                return redirect("/AtoZ-standard.html")
        else:
            return render_template("verify.html")

@app.route("/AtoZ-standard.html")
def AtoZ_standard():
    A_list = []
    B_list = []
    C_list = []
    D_list = []
    E_list = []
    F_list = []
    G_list = []
    H_list = []
    I_list = []
    J_list = []
    K_list = []
    L_list = []
    M_list = []
    N_list = []
    O_list = []
    P_list = []
    Q_list = []
    R_list = []
    S_list = []
    T_list = []
    U_list = []
    V_list = []
    W_list = []
    X_list = []
    Y_list = []
    Z_list = []
    
    with open('A.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            A_list.append(line)
    with open('B.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            B_list.append(line)
    with open('C.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            C_list.append(line)
    with open('D.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            D_list.append(line)
    with open('E.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            E_list.append(line)
    with open('F.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            F_list.append(line)
    with open('G.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            G_list.append(line)
    with open('H.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            H_list.append(line)
    with open('I.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            I_list.append(line)
    with open('J.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            J_list.append(line)
    with open('K.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            K_list.append(line)
    with open('L.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            L_list.append(line)
    with open('M.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            M_list.append(line)
    with open('N.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            N_list.append(line)
    with open('O.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            O_list.append(line)
    with open('P.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            P_list.append(line)
    with open('Q.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            Q_list.append(line)
    with open('R.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            R_list.append(line)
    with open('S.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            S_list.append(line)
    with open('T.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            T_list.append(line)
    with open('U.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            U_list.append(line)
    with open('V.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            V_list.append(line)
    with open('W.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            W_list.append(line)
    with open('X.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            X_list.append(line)
    with open('Y.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            Y_list.append(line)
    with open('Z.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            Z_list.append(line) 
    
    return render_template("AtoZ-standard.html", A=A_list, B=B_list, C=C_list, D=D_list, E=E_list, F=F_list, G=G_list, H=H_list, I=I_list, J=J_list, K=K_list, L=L_list, M=M_list, N=N_list, O=O_list, P=P_list, Q=Q_list, R=R_list, S=S_list, T=T_list, U=U_list, V=V_list, W=W_list, X=X_list, Y=Y_list, Z=Z_list,)

@app.route("/AtoZ.html")
def AtoZ():
    A_list = []
    B_list = []
    C_list = []
    D_list = []
    E_list = []
    F_list = []
    G_list = []
    H_list = []
    I_list = []
    J_list = []
    K_list = []
    L_list = []
    M_list = []
    N_list = []
    O_list = []
    P_list = []
    Q_list = []
    R_list = []
    S_list = []
    T_list = []
    U_list = []
    V_list = []
    W_list = []
    X_list = []
    Y_list = []
    Z_list = []
    
    with open('A.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            A_list.append(line)
    with open('B.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            B_list.append(line)
    with open('C.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            C_list.append(line)
    with open('D.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            D_list.append(line)
    with open('E.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            E_list.append(line)
    with open('F.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            F_list.append(line)
    with open('G.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            G_list.append(line)
    with open('H.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            H_list.append(line)
    with open('I.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            I_list.append(line)
    with open('J.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            J_list.append(line)
    with open('K.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            K_list.append(line)
    with open('L.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            L_list.append(line)
    with open('M.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            M_list.append(line)
    with open('N.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            N_list.append(line)
    with open('O.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            O_list.append(line)
    with open('P.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            P_list.append(line)
    with open('Q.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            Q_list.append(line)
    with open('R.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            R_list.append(line)
    with open('S.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            S_list.append(line)
    with open('T.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            T_list.append(line)
    with open('U.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            U_list.append(line)
    with open('V.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            V_list.append(line)
    with open('W.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            W_list.append(line)
    with open('X.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            X_list.append(line)
    with open('Y.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            Y_list.append(line)
    with open('Z.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            Z_list.append(line) 
    
    return render_template("AtoZ.html", A=A_list, B=B_list, C=C_list, D=D_list, E=E_list, F=F_list, G=G_list, H=H_list, I=I_list, J=J_list, K=K_list, L=L_list, M=M_list, N=N_list, O=O_list, P=P_list, Q=Q_list, R=R_list, S=S_list, T=T_list, U=U_list, V=V_list, W=W_list, X=X_list, Y=Y_list, Z=Z_list,)

@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/addusers.html")
def addusers():
    return render_template("addusers.html")

@app.route("/forgotpassword.html")
def forgotpassword():
    return render_template('forgotpassword.html')

@app.route("/profile.html")
def profile():
    return render_template("profile.html")

@app.route("/suggestadd.html", methods=["POST"])
def suggestionAdd():
    suggested_condition = request.form.get("suggested_condition")
    with open('suggestadd.csv', 'a') as file:
        writer = csv.DictWriter(file, fieldnames=suggestadd)
        writer.writerow({'addedit': 'Add', 'condition': suggested_condition.capitalize()})
    return redirect('AtoZ-standard.html')

@app.route("/suggestedit.html", methods=["POST"])
def suggestionEdit():
    suggested_condition = request.form.get("suggested_condition")
    suggested_action = request.form.get("suggested_action")
    with open('suggest.csv', 'a') as file:
        writer = csv.DictWriter(file, fieldnames=suggest1)
        writer.writerow({'addedit': 'Edit', 'oldaction': suggested_condition.capitalize(), 'newaction': suggested_action.capitalize()})
    return redirect('AtoZ-standard.html')


@app.route("/newuser.html", methods=["POST"])
def newuser():
    username = request.form.get("username")
    password = request.form.get("password")
    admin = request.form.get("admin")

    with open("users.csv", 'a') as file:
        writer = csv.DictWriter(file ,fieldnames=fieldnamesuser)
        if admin == 'Y':
            writer.writerow({'username': username, 'password': password, 'role': admin})
        else:
            writer.writerow({'username': username, 'password': password, 'role': 'N'})

    return redirect("addusers.html")

@app.route('/replace_value_A', methods=['POST'])
def replace_value_A():
    csv_file_path = 'A.csv'
    old_value_to_replace = request.form['old_value_to_replace']
    new_value_to_replace = request.form['new_value_to_replace']

    replace_value(csv_file_path, old_value_to_replace, new_value_to_replace)

    return redirect('A.html')

@app.route('/replace_value_B', methods=['POST'])
def replace_value_B():
    csv_file_path = 'B.csv'
    old_value_to_replace = request.form['old_value_to_replace']
    new_value_to_replace = request.form['new_value_to_replace']

    replace_value(csv_file_path, old_value_to_replace, new_value_to_replace)

    return redirect('B.html')

@app.route('/replace_value_C', methods=['POST'])
def replace_value_C():
    csv_file_path = 'C.csv'
    old_value_to_replace = request.form['old_value_to_replace']
    new_value_to_replace = request.form['new_value_to_replace']

    replace_value(csv_file_path, old_value_to_replace, new_value_to_replace)

    return redirect('C.html')

@app.route('/replace_value_D', methods=['POST'])
def replace_value_D():
    csv_file_path = 'D.csv'
    old_value_to_replace = request.form['old_value_to_replace']
    new_value_to_replace = request.form['new_value_to_replace']

    replace_value(csv_file_path, old_value_to_replace, new_value_to_replace)

    return redirect('D.html')

@app.route('/replace_value_E', methods=['POST'])
def replace_value_E():
    csv_file_path = 'E.csv'
    old_value_to_replace = request.form['old_value_to_replace']
    new_value_to_replace = request.form['new_value_to_replace']

    replace_value(csv_file_path, old_value_to_replace, new_value_to_replace)

    return redirect('E.html')

@app.route('/replace_value_F', methods=['POST'])
def replace_value_F():
    csv_file_path = 'F.csv'
    old_value_to_replace = request.form['old_value_to_replace']
    new_value_to_replace = request.form['new_value_to_replace']

    replace_value(csv_file_path, old_value_to_replace, new_value_to_replace)

    return redirect('F.html')

@app.route('/replace_value_G', methods=['POST'])
def replace_value_G():
    csv_file_path = 'G.csv'
    old_value_to_replace = request.form['old_value_to_replace']
    new_value_to_replace = request.form['new_value_to_replace']

    replace_value(csv_file_path, old_value_to_replace, new_value_to_replace)

    return redirect('G.html')

@app.route('/replace_value_H', methods=['POST'])
def replace_value_H():
    csv_file_path = 'H.csv'
    old_value_to_replace = request.form['old_value_to_replace']
    new_value_to_replace = request.form['new_value_to_replace']

    replace_value(csv_file_path, old_value_to_replace, new_value_to_replace)

    return redirect('H.html')

@app.route('/replace_value_I', methods=['POST'])
def replace_value_I():
    csv_file_path = 'I.csv'
    old_value_to_replace = request.form['old_value_to_replace']
    new_value_to_replace = request.form['new_value_to_replace']

    replace_value(csv_file_path, old_value_to_replace, new_value_to_replace)

    return redirect('I.html')

@app.route('/replace_value_J', methods=['POST'])
def replace_value_J():
    csv_file_path = 'J.csv'
    old_value_to_replace = request.form['old_value_to_replace']
    new_value_to_replace = request.form['new_value_to_replace']

    replace_value(csv_file_path, old_value_to_replace, new_value_to_replace)

    return redirect('J.html')

@app.route('/replace_value_K', methods=['POST'])
def replace_value_K():
    csv_file_path = 'K.csv'
    old_value_to_replace = request.form['old_value_to_replace']
    new_value_to_replace = request.form['new_value_to_replace']

    replace_value(csv_file_path, old_value_to_replace, new_value_to_replace)

    return redirect('K.html')

@app.route('/replace_value_L', methods=['POST'])
def replace_value_L():
    csv_file_path = 'L.csv'
    old_value_to_replace = request.form['old_value_to_replace']
    new_value_to_replace = request.form['new_value_to_replace']

    replace_value(csv_file_path, old_value_to_replace, new_value_to_replace)

    return redirect('L.html')

@app.route('/replace_value_M', methods=['POST'])
def replace_value_M():
    csv_file_path = 'M.csv'
    old_value_to_replace = request.form['old_value_to_replace']
    new_value_to_replace = request.form['new_value_to_replace']

    replace_value(csv_file_path, old_value_to_replace, new_value_to_replace)

    return redirect('M.html')

@app.route('/replace_value_N', methods=['POST'])
def replace_value_N():
    csv_file_path = 'N.csv'
    old_value_to_replace = request.form['old_value_to_replace']
    new_value_to_replace = request.form['new_value_to_replace']

    replace_value(csv_file_path, old_value_to_replace, new_value_to_replace)

    return redirect('N.html')

@app.route('/replace_value_O', methods=['POST'])
def replace_value_O():
    csv_file_path = 'O.csv'
    old_value_to_replace = request.form['old_value_to_replace']
    new_value_to_replace = request.form['new_value_to_replace']

    replace_value(csv_file_path, old_value_to_replace, new_value_to_replace)

    return redirect('O.html')

@app.route('/replace_value_P', methods=['POST'])
def replace_value_P():
    csv_file_path = 'P.csv'
    old_value_to_replace = request.form['old_value_to_replace']
    new_value_to_replace = request.form['new_value_to_replace']

    replace_value(csv_file_path, old_value_to_replace, new_value_to_replace)

    return redirect('P.html')

@app.route('/replace_value_Q', methods=['POST'])
def replace_value_Q():
    csv_file_path = 'Q.csv'
    old_value_to_replace = request.form['old_value_to_replace']
    new_value_to_replace = request.form['new_value_to_replace']

    replace_value(csv_file_path, old_value_to_replace, new_value_to_replace)

    return redirect('Q.html')

@app.route('/replace_value_R', methods=['POST'])
def replace_value_R():
    csv_file_path = 'R.csv'
    old_value_to_replace = request.form['old_value_to_replace']
    new_value_to_replace = request.form['new_value_to_replace']

    replace_value(csv_file_path, old_value_to_replace, new_value_to_replace)

    return redirect('R.html')

@app.route('/replace_value_S', methods=['POST'])
def replace_value_S():
    csv_file_path = 'S.csv'
    old_value_to_replace = request.form['old_value_to_replace']
    new_value_to_replace = request.form['new_value_to_replace']

    replace_value(csv_file_path, old_value_to_replace, new_value_to_replace)

    return redirect('S.html')

@app.route('/replace_value_T', methods=['POST'])
def replace_value_T():
    csv_file_path = 'T.csv'
    old_value_to_replace = request.form['old_value_to_replace']
    new_value_to_replace = request.form['new_value_to_replace']

    replace_value(csv_file_path, old_value_to_replace, new_value_to_replace)

    return redirect('T.html')

@app.route('/replace_value_U', methods=['POST'])
def replace_value_U():
    csv_file_path = 'U.csv'
    old_value_to_replace = request.form['old_value_to_replace']
    new_value_to_replace = request.form['new_value_to_replace']

    replace_value(csv_file_path, old_value_to_replace, new_value_to_replace)

    return redirect('U.html')

@app.route('/replace_value_V', methods=['POST'])
def replace_value_V():
    csv_file_path = 'V.csv'
    old_value_to_replace = request.form['old_value_to_replace']
    new_value_to_replace = request.form['new_value_to_replace']

    replace_value(csv_file_path, old_value_to_replace, new_value_to_replace)

    return redirect('V.html')

@app.route('/replace_value_W', methods=['POST'])
def replace_value_W():
    csv_file_path = 'W.csv'
    old_value_to_replace = request.form['old_value_to_replace']
    new_value_to_replace = request.form['new_value_to_replace']

    replace_value(csv_file_path, old_value_to_replace, new_value_to_replace)

    return redirect('W.html')

@app.route('/replace_value_X', methods=['POST'])
def replace_value_X():
    csv_file_path = 'X.csv'
    old_value_to_replace = request.form['old_value_to_replace']
    new_value_to_replace = request.form['new_value_to_replace']

    replace_value(csv_file_path, old_value_to_replace, new_value_to_replace)

    return redirect('X.html')

@app.route('/replace_value_Y', methods=['POST'])
def replace_value_Y():
    csv_file_path = 'Y.csv'
    old_value_to_replace = request.form['old_value_to_replace']
    new_value_to_replace = request.form['new_value_to_replace']

    replace_value(csv_file_path, old_value_to_replace, new_value_to_replace)

    return redirect('Y.html')

@app.route('/replace_value_Z', methods=['POST'])
def replace_value_Z():
    csv_file_path = 'Z.csv'
    old_value_to_replace = request.form['old_value_to_replace']
    new_value_to_replace = request.form['new_value_to_replace']

    replace_value(csv_file_path, old_value_to_replace, new_value_to_replace)

    return redirect('Z.html')

@app.route("/addresources.html", methods=["POST"])
def addresources():
    condition = request.form.get('condition')
    name = request.form.get('name')
    link = request.form['link']
    attachment = request.files['file']
    
    if link:
        with open('resources.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=resources)
            writer.writerow({'condition': condition, 'name': name.capitalize(), 'link': link})

    if attachment:
        filename = os.path.join(app.config['resource'], attachment.filename)
        attachment.save(filename)
        with open('uploaded_files.csv', 'a', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=imagefields)
            csv_writer.writerow({'condition': condition, 'name': name.capitalize(), 'image': attachment.filename})

    return render_template('AtoZ.html', filename=attachment.filename, name=name)

@app.route("/register.html", methods=["POST"])
def register():
    condition = request.form.get("condition")
    action = request.form.get("action")
    attachment = request.files['file']

    if condition[0].lower() == "a":
        with open('A.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'condition': condition.capitalize(), 'action': action})

    if condition[0].lower() == "b":
        with open('B.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'condition': condition.capitalize(), 'action': action})

    if condition[0].lower() == "c":
        with open('C.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'condition': condition.capitalize(), 'action': action})

    if condition[0].lower() == "d":
        with open('D.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'condition': condition.capitalize(), 'action': action})

    if condition[0].lower() == "e":
        with open('E.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'condition': condition.capitalize(), 'action': action})

    if condition[0].lower() == "f":
        with open('F.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'condition': condition.capitalize(), 'action': action})
    
    if condition[0].lower() == "g":
        with open('G.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'condition': condition.capitalize(), 'action': action})

    if condition[0].lower() == "h":
        with open('H.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'condition': condition.capitalize(), 'action': action})

    if condition[0].lower() == "i":
        with open('I.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'condition': condition.capitalize(), 'action': action})

    if condition[0].lower() == "j":
        with open('J.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'condition': condition.capitalize(), 'action': action})

    if condition[0].lower() == "k":
        with open('K.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'condition': condition.capitalize(), 'action': action})

    if condition[0].lower() == "l":
        with open('L.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'condition': condition.capitalize(), 'action': action})

    if condition[0].lower() == "m":
        with open('M.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'condition': condition.capitalize(), 'action': action})

    if condition[0].lower() == "n":
        with open('N.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'condition': condition.capitalize(), 'action': action})

    if condition[0].lower() == "o":
        with open('O.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'condition': condition.capitalize(), 'action': action})

    if condition[0].lower() == "p":
        with open('P.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'condition': condition.capitalize(), 'action': action})

    if condition[0].lower() == "q":
        with open('Q.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'condition': condition.capitalize(), 'action': action})

    if condition[0].lower() == "r":
        with open('R.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'condition': condition.capitalize(), 'action': action})

    if condition[0].lower() == "s":
        with open('S.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'condition': condition.capitalize(), 'action': action})

    if condition[0].lower() == "t":
        with open('T.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'condition': condition.capitalize(), 'action': action})

    if condition[0].lower() == "u":
        with open('U.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'condition': condition.capitalize(), 'action': action})

    if condition[0].lower() == "v":
        with open('V.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'condition': condition.capitalize(), 'action': action})

    if condition[0].lower() == "w":
        with open('W.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'condition': condition.capitalize(), 'action': action})

    if condition[0].lower() == "x":
        with open('X.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'condition': condition.capitalize(), 'action': action})
    
    if condition[0].lower() == "y":
        with open('Y.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'condition': condition.capitalize(), 'action': action})

    if condition[0].lower() == "z":
        with open('Z.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'condition': condition.capitalize(), 'action': action})
        
    return redirect("index.html")

@app.route("/users.html")
def users_list():
    user_list = []
    with open('users.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            user_list.append(line)
    return render_template("users.html", userslist=user_list)

@app.route("/suggestions.html")
def suggestions():
    suggestions = []
    with open('suggest.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            suggestions.append(line)
    suggestionsadd =[]
    with open('suggestadd.csv', 'r') as csv_file1:
        csv_reader1 = csv.DictReader(csv_file1)
        for line1 in csv_reader1:
            suggestionsadd.append(line1)
    return render_template("suggestions.html", suggest=suggestions, suggestadd=suggestionsadd)

@app.route("/A.html")
def A():
    A_list = []
    with open('A.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            A_list.append(line)
    return render_template("A.html", A=A_list)

@app.route("/A2.html")
def A2():
    A2_list = []
    with open('A.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            A2_list.append(line)
    return render_template("A2.html", A2=A2_list)

@app.route("/B.html")
def B():
    B_list = []
    with open('B.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            B_list.append(line)
    return render_template("B.html", B=B_list)

@app.route("/B2.html")
def B2():
    B2_list = []
    with open('B.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            B2_list.append(line)
    return render_template("B2.html", B2=B2_list)

@app.route("/C.html")
def C():
    C_list = []
    with open('C.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            C_list.append(line)
    return render_template("C.html", C=C_list)

@app.route("/C2.html")
def C2():
    C2_list = []
    with open('C.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            C2_list.append(line)
    return render_template("C2.html", C2=C2_list)

@app.route("/D.html")
def D():
    D_list = []
    with open('D.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            D_list.append(line)
    return render_template("D.html", D=D_list)

@app.route("/D2.html")
def D2():
    D2_list = []
    with open('D.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            D2_list.append(line)
    return render_template("D2.html", D2=D2_list)

@app.route("/E.html")
def E():
    E_list = []
    with open('E.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            E_list.append(line)
    return render_template("E.html", E=E_list)

@app.route("/E2.html")
def E2():
    E2_list = []
    with open('E.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            E2_list.append(line)
    return render_template("E2.html", E2=E2_list)

@app.route("/F.html")
def F():
    F_list = []
    with open('F.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            F_list.append(line)
    return render_template("F.html", F=F_list)

@app.route("/F2.html")
def F2():
    F2_list = []
    with open('F.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            F2_list.append(line)
    return render_template("F2.html", F2=F2_list)

@app.route("/G.html")
def G():
    G_list = []
    with open('G.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            G_list.append(line)
    return render_template("G.html", G=G_list)

@app.route("/G2.html")
def G2():
    G2_list = []
    with open('G.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            G2_list.append(line)
    return render_template("G2.html", G2=G2_list)

@app.route("/H.html")
def H():
    H_list = []
    with open('H.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            H_list.append(line)
    return render_template("H.html", H=H_list)

@app.route("/H2.html")
def H2():
    H2_list = []
    with open('H.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            H2_list.append(line)
    return render_template("H2.html", H2=H2_list)

@app.route("/I.html")
def I():
    I_list = []
    with open('I.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            I_list.append(line)
    return render_template("I.html", I=I_list)

@app.route("/I2.html")
def I2():
    I2_list = []
    with open('I.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            I2_list.append(line)
    return render_template("I2.html", I2=I2_list)

@app.route("/J.html")
def J():
    J_list = []
    with open('J.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            J_list.append(line)
    return render_template("J.html", J=J_list)

@app.route("/J2.html")
def J2():
    J2_list = []
    with open('J.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            J2_list.append(line)
    return render_template("J2.html", J2=J2_list)

@app.route("/K.html")
def K():
    K_list = []
    with open('K.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            K_list.append(line)
    return render_template("K.html", K=K_list)

@app.route("/K2.html")
def K2():
    K2_list = []
    with open('K.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            K2_list.append(line)
    return render_template("K2.html", K2=K2_list)

@app.route("/L.html")
def L():
    L_list = []
    with open('L.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            L_list.append(line)
    return render_template("L.html", L=L_list)

@app.route("/L2.html")
def L2():
    L2_list = []
    with open('L.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            L2_list.append(line)
    return render_template("L2.html", L2=L2_list)

@app.route("/M.html")
def M():
    M_list = []
    with open('M.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            M_list.append(line)
    return render_template("M.html", M=M_list)

@app.route("/M2.html")
def M2():
    M2_list = []
    with open('M.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            M2_list.append(line)
    return render_template("M2.html", M2=M2_list)

@app.route("/N.html")
def N():
    N_list = []
    with open('N.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            N_list.append(line)
    return render_template("N.html", N=N_list)

@app.route("/N2.html")
def N2():
    N2_list = []
    with open('N.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            N2_list.append(line)
    return render_template("N2.html", N2=N2_list)

@app.route("/O.html")
def O():
    O_list = []
    with open('O.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            O_list.append(line)
    return render_template("O.html", O=O_list)

@app.route("/O2.html")
def O2():
    O2_list = []
    with open('O.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            O2_list.append(line)
    return render_template("O2.html", O2=O2_list)

@app.route("/P.html")
def P():
    P_list = []
    with open('P.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            P_list.append(line)
    return render_template("P.html", P=P_list)

@app.route("/P2.html")
def P2():
    P2_list = []
    with open('P.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            P2_list.append(line)
    return render_template("P2.html", P2=P2_list)

@app.route("/Q.html")
def Q():
    Q_list = []
    with open('Q.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            Q_list.append(line)
    return render_template("Q.html", Q=Q_list)

@app.route("/Q2.html")
def Q2():
    Q2_list = []
    with open('Q.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            Q2_list.append(line)
    return render_template("Q2.html", Q2=Q2_list)

@app.route("/R.html")
def R():
    R_list = []
    with open('R.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            R_list.append(line)
    return render_template("R.html", R=R_list)

@app.route("/R2.html")
def R2():
    R2_list = []
    with open('R.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            R2_list.append(line)
    return render_template("R2.html", R2=R2_list)

@app.route("/S.html")
def S():
    S_list = []
    with open('S.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            S_list.append(line)            
    return render_template("S.html", S=S_list)

@app.route("/S2.html")
def S2():
    S2_list = []
    with open('S.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            S2_list.append(line)            
    return render_template("S2.html", S2=S2_list)

@app.route("/T.html")
def T():
    T_list = []
    with open('T.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            T_list.append(line)
    return render_template("T.html", T=T_list)

@app.route("/T2.html")
def T2():
    T2_list = []
    with open('T.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            T2_list.append(line)
    return render_template("T2.html", T2=T2_list)

@app.route("/U.html")
def U():
    U_list = []
    with open('U.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            U_list.append(line)
    return render_template("U.html", U=U_list)

@app.route("/U2.html")
def U2():
    U2_list = []
    with open('U.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            U2_list.append(line)
    return render_template("U2.html", U2=U2_list)

@app.route("/V.html")
def V():
    V_list = []
    with open('V.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            V_list.append(line)
    return render_template("V.html", V=V_list)

@app.route("/V2.html")
def V2():
    V2_list = []
    with open('V.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            V2_list.append(line)
    return render_template("V2.html", V2=V2_list)

@app.route("/W.html")
def W():
    W_list = []
    with open('W.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            W_list.append(line)
    return render_template("W.html", W=W_list)

@app.route("/W2.html")
def W2():
    W2_list = []
    with open('W.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            W2_list.append(line)
    return render_template("W2.html", W2=W2_list)

@app.route("/X.html")
def X():
    X_list = []
    with open('X.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            X_list.append(line)
    return render_template("X.html", X=X_list)

@app.route("/X2.html")
def X2():
    X2_list = []
    with open('X.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            X2_list.append(line)
    return render_template("X2.html", X2=X2_list)

@app.route("/Y.html")
def Y():
    Y_list = []
    with open('Y.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            Y_list.append(line)
    return render_template("Y.html", Y=Y_list)

@app.route("/Y2.html")
def Y2():
    Y2_list = []
    with open('Y.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            Y2_list.append(line)
    return render_template("Y2.html", Y2=Y2_list)

@app.route("/Z.html")
def Z():
    Z_list = []
    with open('Z.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            Z_list.append(line)
    return render_template("Z.html", Z=Z_list)

@app.route("/Z2.html")
def Z2():
    Z2_list = []
    with open('Z.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            Z2_list.append(line)
    return render_template("Z2.html", Z2=Z2_list)

@app.route('/resources/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['resource'], filename)
    
@app.route("/actionA.html")
def actionA():
    condition = request.args.get('condition', '')
    A_list = []
    with open('A.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            A_list.append(line)
    filter_data = [line for line in A_list if line['condition'] == condition]

    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionA.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionA2.html")
def actionA2():
    condition = request.args.get('condition', '')
    A_list = []
    with open('A.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            A_list.append(line)
    filter_data = [line for line in A_list if line['condition'] == condition]

    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionA2.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)
   
@app.route("/actionB.html")
def actionB():
    condition = request.args.get('condition', '')
    B_list = []
    with open('B.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            B_list.append(line)
    filter_data = [line for line in B_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionB.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionB2.html")
def actionB2():
    condition = request.args.get('condition', '')
    B_list = []
    with open('B.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            B_list.append(line)
    filter_data = [line for line in B_list if line['condition'] == condition]

    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionB2.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionC.html")
def actionC():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('C.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]

    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionC.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)


@app.route("/actionC2.html")
def actionC2():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('C.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]

    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionC2.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionD.html")
def actionD():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('D.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]

    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionD.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionD2.html")
def actionD2():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('D.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]

    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("action2.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionE.html")
def actionE():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('E.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]

    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionE.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionE2.html")
def actionE2():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('E.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]

    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionE2.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionF.html")
def actionF():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('F.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionF.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionF2.html")
def actionF2():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('F.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionF2.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionG.html")
def actionG():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('G.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionG.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionG2.html")
def actionG2():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('G.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionG2.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionH.html")
def actionH():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('H.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionH.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionH2.html")
def actionH2():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('H.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionH2.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionI.html")
def actionI():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('I.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionI.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionI2.html")
def actionI2():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('I.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionI2.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionJ.html")
def actionJ():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('J.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionJ.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionJ2.html")
def actionJ2():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('J.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionJ2.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionK.html")
def actionK():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('K.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionK.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionK2.html")
def actionK2():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('K.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionK2.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionL.html")
def actionL():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('L.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionL.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionL2.html")
def actionL2():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('L.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionL2.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionM.html")
def actionM():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('M.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionM.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionM2.html")
def actionM2():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('M.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionM2.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionN.html")
def actionN():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('N.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionN.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionN2.html")
def actionN2():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('N.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionN2.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionO.html")
def actionO():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('O.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionO.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionO2.html")
def actionO2():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('O.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionO2.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionP.html")
def actionP():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('P.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionP.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionP2.html")
def actionP2():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('P.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionP2.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionQ.html")
def actionQ():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('Q.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionQ.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionQ2.html")
def actionQ2():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('Q.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionQ2.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionR.html")
def actionR():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('R.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionR.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionR2.html")
def actionR2():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('R.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionR2.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionS.html")
def actionS():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('S.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionS.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionS2.html")
def actionS2():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('S.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionS2.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionT.html")
def actionT():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('T.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionT.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionT2.html")
def actionT2():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('T.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionT2.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionU.html")
def actionU():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('U.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionU.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionU2.html")
def actionU2():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('U.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionU2.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionV.html")
def actionV():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('V.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionV.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionV2.html")
def actionV2():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('V.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionV2.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionW.html")
def actionW():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('W.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionW.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionW2.html")
def actionW2():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('W.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionW2.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionX.html")
def actionX():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('X.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionX.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionX2.html")
def actionX2():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('X.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionX2.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionY.html")
def actionY():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('Y.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionY.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionY2.html")
def actionY2():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('Y.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionY2.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionZ.html")
def actionZ():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('Z.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionZ.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

@app.route("/actionZ2.html")
def actionZ2():
    condition = request.args.get('condition', '')
    letter_list = []
    with open('Z.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            letter_list.append(line)
    filter_data = [line for line in letter_list if line['condition'] == condition]
    
    resources_list = []
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    with open('resources.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        for line2 in csv_reader2:
            resources_list.append(line2)
    filter_data2 = [line for line in resources_list if line['condition'] == condition]

    image_files = []
    with open('uploaded_files.csv', 'r') as csv_file3:
        csv_reader3 = csv.DictReader(csv_file3)
        for line3 in csv_reader3:
            image_files.append(line3)
        filter_data3 = [line for line in image_files if line['condition'] == condition]

    return render_template("actionZ2.html", A=filter_data, filename=condition, resources=filter_data2, image_files=files, files=filter_data3)

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
            lines = [line for line in csv_reader if line['condition'] != suggest]

        with open('suggest.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=suggest1)
            writer.writeheader()
            writer.writerows(lines)
        return redirect("/suggestions.html")
    
@app.route("/remove_suggestadd/<suggest>", methods=["POST", "DELETE"])
def deregister_suggestadd(suggest):
    if request.method in ["POST", "DELETE"]:
        with open('suggestadd.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != suggest]

        with open('suggestadd.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=suggestadd)
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

@app.route("/remove_A/<A>", methods=["POST", "DELETE"])
def deregister_A(A):
    if request.method in ["POST", "DELETE"]:
        success = remove_file(app.config['UPLOAD_FOLDER_A'], A)
        with open('A.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != A]

        with open('A.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)

        return redirect("/A.html")

@app.route("/remove_B/<B>", methods=["POST", "DELETE"])
def deregister_B(B):
    if request.method in ["POST", "DELETE"]:
        success = remove_file(app.config['UPLOAD_FOLDER_B'], B)
        with open('B.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != B]

        with open('B.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)

        return redirect("/B.html")

@app.route("/remove_C/<C>", methods=["POST", "DELETE"])
def deregister_C(C):
    if request.method in ["POST", "DELETE"]:
        success = remove_file(app.config['UPLOAD_FOLDER_C'], C)
        with open('C.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != C]

        with open('C.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)
        
        return redirect("/C.html")

@app.route("/remove_D/<D>", methods=["POST", "DELETE"])
def deregister_D(D):
    if request.method in ["POST", "DELETE"]:
        success = remove_file(app.config['UPLOAD_FOLDER_D'], D)
        with open('D.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != D]

        with open('D.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)

        return redirect("/D.html")

@app.route("/remove_E/<E>", methods=["POST", "DELETE"])
def deregister_E(E):
    if request.method in ["POST", "DELETE"]:
        success = remove_file(app.config['UPLOAD_FOLDER_E'], E)
        with open('E.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != E]

        with open('E.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)

        return redirect("/E.html")


@app.route("/remove_F/<F>", methods=["POST", "DELETE"])
def deregister_F(F):
    if request.method in ["POST", "DELETE"]:
        success = remove_file(app.config['UPLOAD_FOLDER_F'], F)
        with open('F.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != F]

        with open('F.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)

        return redirect("/F.html")

@app.route("/remove_G/<G>", methods=["POST", "DELETE"])
def deregister_G(G):
    if request.method in ["POST", "DELETE"]:
        success = remove_file(app.config['UPLOAD_FOLDER_G'], G)
        with open('G.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != G]

        with open('G.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)
        
        return redirect("/G.html")

@app.route("/remove_H/<H>", methods=["POST", "DELETE"])
def deregister_H(H):
    if request.method in ["POST", "DELETE"]:
        success = remove_file(app.config['UPLOAD_FOLDER_H'], H)
        with open('H.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != H]

        with open('H.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)

        return redirect("/H.html")

@app.route("/remove_I/<I>", methods=["POST", "DELETE"])
def deregister_I(I):
    if request.method in ["POST", "DELETE"]:
        success = remove_file(app.config['UPLOAD_FOLDER_I'], I)
        with open('I.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != I]

        with open('I.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)

        return redirect("/I.html")

@app.route("/remove_J/<J>", methods=["POST", "DELETE"])
def deregister_J(J):
    if request.method in ["POST", "DELETE"]:
        success = remove_file(app.config['UPLOAD_FOLDER_J'], J)
        with open('J.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != J]

        with open('J.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)

        return redirect("/J.html")

@app.route("/remove_K/<K>", methods=["POST", "DELETE"])
def deregister_K(K):
    if request.method in ["POST", "DELETE"]:
        success = remove_file(app.config['UPLOAD_FOLDER_K'], K)
        with open('K.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != K]

        with open('K.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)
        
        return redirect("/K.html")
    
@app.route("/remove_L/<L>", methods=["POST", "DELETE"])
def deregister_L(L):
    if request.method in ["POST", "DELETE"]:
        success = remove_file(app.config['UPLOAD_FOLDER_L'], L)
        with open('L.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != L]

        with open('L.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)

        return redirect("/L.html")
    
@app.route("/remove_M/<M>", methods=["POST", "DELETE"])
def deregister_M(M):
    if request.method in ["POST", "DELETE"]:
        success = remove_file(app.config['UPLOAD_FOLDER_M'], M)
        with open('M.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != M]

        with open('M.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)

        return redirect("/M.html")
        
@app.route("/remove_N/<N>", methods=["POST", "DELETE"])
def deregister_N(N):
    if request.method in ["POST", "DELETE"]:
        success = remove_file(app.config['UPLOAD_FOLDER_N'], N)
        with open('N.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != N]

        with open('N.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)

        return redirect("/N.html")
    
@app.route("/remove_O/<O>", methods=["POST", "DELETE"])
def deregister_O(O):
    if request.method in ["POST", "DELETE"]:
        success = remove_file(app.config['UPLOAD_FOLDER_O'], O)
        with open('O.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != O]

        with open('O.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)
        
        return redirect("/O.html")

@app.route("/remove_P/<P>", methods=["POST", "DELETE"])
def deregister_P(P):
    if request.method in ["POST", "DELETE"]:
        success = remove_file(app.config['UPLOAD_FOLDER_P'], P)
        with open('P.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != P]

        with open('P.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)

        return redirect("/P.html")

@app.route("/remove_Q/<Q>", methods=["POST", "DELETE"])
def deregister_Q(Q):
    if request.method in ["POST", "DELETE"]:
        success = remove_file(app.config['UPLOAD_FOLDER_Q'], Q)
        with open('Q.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != Q]

        with open('Q.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)

        return redirect("/Q.html")

@app.route("/remove_R/<R>", methods=["POST", "DELETE"])
def deregister_R(R):
    if request.method in ["POST", "DELETE"]:
        success = remove_file(app.config['UPLOAD_FOLDER_R'], R)
        with open('R.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != R]

        with open('R.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)

        return redirect("/R.html")
    
@app.route("/remove_S/<S>", methods=["POST", "DELETE"])
def deregister_S(S):
    if request.method in ["POST", "DELETE"]:
        success = remove_file(app.config['UPLOAD_FOLDER_S'], S)
        with open('S.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != S]

        with open('S.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)

        return redirect("/S.html")

@app.route("/remove_T/<T>", methods=["POST", "DELETE"])
def deregister_T(T):
    if request.method in ["POST", "DELETE"]:
        success = remove_file(app.config['UPLOAD_FOLDER_T'], T)
        with open('T.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != T]

        with open('T.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)

        return redirect("/T.html")

@app.route("/remove_U/<U>", methods=["POST", "DELETE"])
def deregister_U(U):
    if request.method in ["POST", "DELETE"]:
        success = remove_file(app.config['UPLOAD_FOLDER_U'], U)
        with open('U.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != U]

        with open('U.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)

        return redirect("/U.html")

@app.route("/remove_V/<V>", methods=["POST", "DELETE"])
def deregister_V(V):
    if request.method in ["POST", "DELETE"]:
        success = remove_file(app.config['UPLOAD_FOLDER_V'], V)
        with open('V.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != V]

        with open('V.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)

        return redirect("/V.html")

@app.route("/remove_W/<W>", methods=["POST", "DELETE"])
def deregister_W(W):
    if request.method in ["POST", "DELETE"]:
        success = remove_file(app.config['UPLOAD_FOLDER_W'], W)
        with open('W.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != W]

        with open('W.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)

        return redirect("/W.html")

@app.route("/remove_X/<X>", methods=["POST", "DELETE"])
def deregister_X(X):
    if request.method in ["POST", "DELETE"]:
        success = remove_file(app.config['UPLOAD_FOLDER_X'], X)
        with open('X.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != X]

        with open('X.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)

        return redirect("/X.html")

@app.route("/remove_Y/<Y>", methods=["POST", "DELETE"])
def deregister_Y(Y):
    if request.method in ["POST", "DELETE"]:
        success = remove_file(app.config['UPLOAD_FOLDER_Y'], Y)
        with open('Y.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != Y]

        with open('Y.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)

        return redirect("/Y.html")

@app.route("/remove_Z/<Z>", methods=["POST", "DELETE"])
def deregister_Z(Z):
    if request.method in ["POST", "DELETE"]:
        success = remove_file(app.config['UPLOAD_FOLDER_Z'], Z)
        with open('Z.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            lines = [line for line in csv_reader if line['condition'] != Z]

        with open('Z.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)

        return redirect("/Z.html")
        
if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
        
        