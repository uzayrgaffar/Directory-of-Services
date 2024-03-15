from flask import Flask, render_template, request, redirect, send_from_directory, app, session
from sqlalchemy import create_engine, Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

app = Flask(__name__)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    site = Column(String, nullable=False)
    name = Column(Text, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_admin = Column(String)

class Condition(Base):
    __tablename__ = 'conditions'
    id = Column(Integer, primary_key=True)
    site = Column(String, nullable=False)
    condition = Column(String, nullable=False)
    action = Column(String, nullable=False)

class Resource(Base):
    __tablename__ = 'resources'
    id = Column(Integer, primary_key=True)
    site = Column(String, nullable=False)
    condition = Column(String, nullable=False)
    name = Column(String, nullable=False)
    link = Column(String)
    image = Column(String)

class Suggest(Base):
    __tablename__ = 'suggestions'
    id = Column(Integer, primary_key=True)
    site = Column(String, nullable=False)
    addoredit = Column(String, nullable=False)
    old = Column(String, nullable=False)
    new = Column(String)

engine = create_engine('sqlite:///dofs.db')

Base.metadata.create_all(engine)

RESOURCE = 'resource'
app.config['resource'] =  RESOURCE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dofs.db'
app.secret_key = '24201962318371781011'


def load_users():
    users = {}
    Session = sessionmaker(bind=engine)
    session = Session()
    
    query = session.query(User).all()
    
    for user in query:
        users[user.email] = {
            'username': user.email,
            'password': user.password,
            'role': user.is_admin,
            'site': user.site,
            'name': user.name
        }

    session.close()
    return users

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
            name = users[username]['name']
            session['name'] = name
            if users[username]['username'] == 'uzayrgaffar@gmail.com':
                return redirect('/dofsdeveloper.html')
            if users[username]['password'] == 'password':
                return redirect("/password")
            else:
                return redirect("/AtoZ.html")
    else:
        return render_template("verify.html")
    
@app.route("/password")
def newpassword():
    return render_template("password.html")

@app.route("/checkpassword")
def checkpassword():
    return render_template("checkpassword.html")

@app.route("/dofsdeveloper.html")
def dofsdeveloper():
    return render_template("dofsdeveloper.html")

@app.route("/devusers.html")
def devusers():
    Session = sessionmaker(bind=engine)
    db_session = Session()
    user_list = db_session.query(User).all()
    db_session.close()
    return render_template("devusers.html", userslist=user_list)

@app.route('/check.html', methods=['POST'])
def check():
    oldpassword = session.get('password')
    if request.method == 'POST':
        password = request.form.get('password')
        check = request.form.get('check')

        if password == oldpassword:
            return redirect("/checkpassword")

        Session = sessionmaker(bind=engine)
        db_session = Session()

        try:
            user = db_session.query(User).filter(User.password == oldpassword).first()

            if password == check:
                user.password = password
                db_session.commit()
            else:
                return redirect("/checkpassword")
        except Exception as e:
            print("Error:", str(e))
            db_session.rollback()
        finally:
            db_session.close()

    return redirect('AtoZ.html')



@app.route("/AtoZ.html")
def AtoZ():
    username = session.get('username')
    site = session.get('site') 
    users = load_users()
    role = users[username]['role']

    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter_by(site=site).all()
    db_session.close()
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
    users = load_users()
    role = users[username]['role']
    name = session.get('name')

    return render_template("profile.html", name=name, username=username, password=password, site=site, role=role)

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

    Session = sessionmaker(bind=engine)
    if addedit == 'Add':
        db_session = Session()
        new_suggestion = Suggest(site=site, addoredit=addedit, old=suggested_condition, new='')    
    if addedit == 'Edit':
        db_session = Session()
        new_suggestion = Suggest(site=site, addoredit=addedit, old=oldaction, new=suggested_action)

    db_session.add(new_suggestion)
    db_session.commit()
    db_session.close()
    return redirect('AtoZ.html')

@app.route("/newuser.html", methods=["POST"])
def newuser():
    site = session.get('site')
    email = request.form['username']
    password = request.form['password']
    admin = request.form.get('admin')
    name = request.form.get('name')

    Session = sessionmaker(bind=engine)
    db_session = Session()
    
    if admin == 'Y':
        new_user = User(site=site, email=email, password=password, is_admin=admin, name=name)
    else:
        new_user = User(site=site, email=email, password=password, is_admin='N', name=name)
    db_session.add(new_user)
    db_session.commit()
    db_session.close()

    return redirect("addusers.html")

@app.route("/newuserdeveloper.html", methods=["POST"])
def newuserdeveloper():
    site = request.form.get('site')
    email = request.form['username']
    password = request.form['password']
    admin = request.form.get('admin')
    name = request.form.get('name')

    Session = sessionmaker(bind=engine)
    db_session = Session()
    
    if admin == 'Y':
        new_user = User(site=site, email=email, password=password, is_admin=admin, name=name)
    else:
        new_user = User(site=site, email=email, password=password, is_admin='N', name=name)
    db_session.add(new_user)
    db_session.commit()
    db_session.close()

    return redirect("dofsdeveloper.html")

@app.route('/replace_condition', methods=['POST'])
def replace_condition():
    if request.method == 'POST':
        old_condition = request.form.get('old_condition')
        new_condition = request.form.get('new_condition')

        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            condition = session.query(Condition).filter(Condition.condition == old_condition).first()

            if condition:
                condition.condition = new_condition
                session.commit()
        except Exception as e:
            print("Error:", str(e))
            session.rollback()
        finally:
            session.close()

    return redirect('AtoZ.html')

@app.route('/replace_action', methods=['POST'])
def replace_action():
    if request.method == 'POST':
        old_action = request.form.get('old_action')
        new_action = request.form.get('new_action')

        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            condition = session.query(Condition).filter(Condition.action == old_action).first()

            if condition:
                condition.action = new_action
                session.commit()
        except Exception as e:
            print("Error:", str(e))
            session.rollback()
        finally:
            session.close()

    return redirect('AtoZ.html')

@app.route('/replace_action_from_suggestions/<int:suggest_id>', methods=['POST'])
def replace_action_from_suggestions(suggest_id):
    if request.method == 'POST':
        old_action = request.form.get('old_action')
        new_action = request.form.get('new_action')

        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            condition = session.query(Condition).filter(Condition.action == old_action).first()

            if condition:
                condition.action = new_action
                session.commit()
        except Exception as e:
            print("Error:", str(e))
            session.rollback()
        finally:
            session.close()
    
    Session = sessionmaker(bind=engine)
    session = Session()
    suggest = session.query(Suggest).filter_by(id=suggest_id).first()
    if suggest:
        session.delete(suggest)
        session.commit()
        session.close()
    return redirect("/suggestions.html")

@app.route("/addresources.html", methods=["POST"])
def addresources():
    site = session.get('site')
    condition = request.form.get('condition')
    name = request.form.get('name')
    link = request.form['link']
    attachment = request.files['file']
    
    if link:
        firstletter = name[0].upper()
        name = firstletter + name[1:]
        Session = sessionmaker(bind=engine)
        db_session = Session()
        new_resource = Resource(site=site, condition=condition, name=name, link=link)
        db_session.add(new_resource)
        db_session.commit()
        db_session.close()

    if attachment:
        filename = os.path.join(app.config['resource'], attachment.filename)
        attachment.save(filename)
        firstlettername = name[0].upper()
        name = firstlettername + name[1:]
        Session = sessionmaker(bind=engine)
        db_session = Session()
        new_resource = Resource(site=site, condition=condition, name=name, image=attachment.filename)
        db_session.add(new_resource)
        db_session.commit()
        db_session.close()

    return render_template('AtoZ.html', filename=attachment.filename, name=name)

@app.route("/register.html", methods=["POST"])
def register():
    site = session.get('site')
    condition = request.form.get("condition")
    action = request.form.get("action")

    firstletter = condition[0].upper()
    condition = firstletter + condition[1:] 

    Session = sessionmaker(bind=engine)
    db_session = Session()

    new_condition = Condition(site=site, condition=condition, action=action)
    db_session.add(new_condition)
    db_session.commit()
    db_session.close()
    
    return redirect("/AtoZ.html")

@app.route("/users.html")
def users_list():
    role = session.get('role')
    site = session.get('site')
    Session = sessionmaker(bind=engine)
    db_session = Session()

    user_list = db_session.query(User).all()
    user_list = [line for line in user_list if line.site == site]
    db_session.close()
    return render_template("users.html", userslist=user_list, role=role)

@app.route("/suggestions.html")
def suggestions():
    role = session.get('role')
    site = session.get('site')
    Session = sessionmaker(bind=engine)
    db_session = Session()

    suggest = db_session.query(Suggest).all()
    suggest = [line for line in suggest if line.site == site]
    db_session.close()
    return render_template("suggestions.html", suggest=suggest, role=role)


@app.route("/A.html")
def A():
    username = session.get('username')
    site = session.get('site')
    users = load_users()
    role = users[username]['role']

    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter(Condition.condition.startswith('A'), Condition.site == site).all()
    db_session.close()
    return render_template("A.html", A=filter_data, role=role)

@app.route("/B.html")
def B():
    username = session.get('username')
    site = session.get('site')
    users = load_users()
    role = users[username]['role']

    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter(Condition.condition.startswith('B'), Condition.site == site).all()
    db_session.close()
    return render_template("B.html", B=filter_data, role=role)

@app.route("/C.html")
def C():
    username = session.get('username')
    site = session.get('site')
    users = load_users()
    role = users[username]['role']

    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter(Condition.condition.startswith('C'), Condition.site == site).all()
    db_session.close()
    return render_template("C.html", C=filter_data, role=role)

@app.route("/D.html")
def D():
    username = session.get('username')
    site = session.get('site')
    users = load_users()
    role = users[username]['role']
    
    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter(Condition.condition.startswith('D'), Condition.site == site).all()
    db_session.close()
    return render_template("D.html", D=filter_data, role=role)

@app.route("/E.html")
def E():
    username = session.get('username')
    site = session.get('site')
    users = load_users()
    role = users[username]['role']

    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter(Condition.condition.startswith('E'), Condition.site == site).all()
    db_session.close()
    return render_template("E.html", E=filter_data, role=role)

@app.route("/F.html")
def F():
    username = session.get('username')
    site = session.get('site')
    users = load_users()
    role = users[username]['role']

    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter(Condition.condition.startswith('F'), Condition.site == site).all()
    db_session.close()
    return render_template("F.html", F=filter_data, role=role)

@app.route("/G.html")
def G():
    username = session.get('username')
    site = session.get('site')
    users = load_users()
    role = users[username]['role']

    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter(Condition.condition.startswith('G'), Condition.site == site).all()
    db_session.close()
    return render_template("G.html", G=filter_data, role=role)

@app.route("/H.html")
def H():
    username = session.get('username')
    site = session.get('site')
    users = load_users()
    role = users[username]['role']

    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter(Condition.condition.startswith('H'), Condition.site == site).all()
    db_session.close()
    return render_template("H.html", H=filter_data, role=role)

@app.route("/I.html")
def I():
    username = session.get('username')
    site = session.get('site')
    users = load_users()
    role = users[username]['role']

    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter(Condition.condition.startswith('I'), Condition.site == site).all()
    db_session.close()
    return render_template("I.html", I=filter_data, role=role)

@app.route("/J.html")
def J():
    username = session.get('username')
    site = session.get('site')
    users = load_users()
    role = users[username]['role']

    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter(Condition.condition.startswith('J'), Condition.site == site).all()
    db_session.close()
    return render_template("J.html", J=filter_data, role=role)

@app.route("/K.html")
def K():
    username = session.get('username')
    site = session.get('site')
    users = load_users()
    role = users[username]['role']

    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter(Condition.condition.startswith('K'), Condition.site == site).all()
    db_session.close()
    return render_template("K.html", K=filter_data, role=role)

@app.route("/L.html")
def L():
    username = session.get('username')
    site = session.get('site')
    users = load_users()
    role = users[username]['role']

    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter(Condition.condition.startswith('L'), Condition.site == site).all()
    db_session.close()
    return render_template("L.html", L=filter_data, role=role)

@app.route("/M.html")
def M():
    username = session.get('username')
    site = session.get('site')
    users = load_users()
    role = users[username]['role']

    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter(Condition.condition.startswith('M'), Condition.site == site).all()
    db_session.close()
    return render_template("M.html", M=filter_data, role=role)

@app.route("/N.html")
def N():
    username = session.get('username')
    site = session.get('site')
    users = load_users()
    role = users[username]['role']

    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter(Condition.condition.startswith('N'), Condition.site == site).all()
    db_session.close()
    return render_template("N.html", N=filter_data, role=role)

@app.route("/O.html")
def O():
    username = session.get('username')
    site = session.get('site')
    users = load_users()
    role = users[username]['role']

    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter(Condition.condition.startswith('O'), Condition.site == site).all()
    db_session.close()
    return render_template("O.html", O=filter_data, role=role)

@app.route("/P.html")
def P():
    username = session.get('username')
    site = session.get('site')
    users = load_users()
    role = users[username]['role']

    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter(Condition.condition.startswith('P'), Condition.site == site).all()
    db_session.close()
    return render_template("P.html", P=filter_data, role=role)

@app.route("/Q.html")
def Q():
    username = session.get('username')
    site = session.get('site')
    users = load_users()
    role = users[username]['role']

    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter(Condition.condition.startswith('Q'), Condition.site == site).all()
    db_session.close()
    return render_template("Q.html", Q=filter_data, role=role)

@app.route("/R.html")
def R():
    username = session.get('username')
    site = session.get('site')
    users = load_users()
    role = users[username]['role']

    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter(Condition.condition.startswith('R'), Condition.site == site).all()
    db_session.close()
    return render_template("R.html", R=filter_data, role=role)

@app.route("/S.html")
def S():
    username = session.get('username')
    site = session.get('site')
    users = load_users()
    role = users[username]['role']

    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter(Condition.condition.startswith('S'), Condition.site == site).all()
    db_session.close()
    return render_template("S.html", S=filter_data, role=role)

@app.route("/T.html")
def T():
    username = session.get('username')
    site = session.get('site')
    users = load_users()
    role = users[username]['role']

    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter(Condition.condition.startswith('T'), Condition.site == site).all()
    db_session.close()
    return render_template("T.html", T=filter_data, role=role)

@app.route("/U.html")
def U():
    username = session.get('username')
    site = session.get('site')
    users = load_users()
    role = users[username]['role']

    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter(Condition.condition.startswith('U'), Condition.site == site).all()
    db_session.close()
    return render_template("U.html", U=filter_data, role=role)

@app.route("/V.html")
def V():
    username = session.get('username')
    site = session.get('site')
    users = load_users()
    role = users[username]['role']

    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter(Condition.condition.startswith('V'), Condition.site == site).all()
    db_session.close()
    return render_template("V.html", V=filter_data, role=role)

@app.route("/W.html")
def W():
    username = session.get('username')
    site = session.get('site')
    users = load_users()
    role = users[username]['role']

    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter(Condition.condition.startswith('W'), Condition.site == site).all()
    db_session.close()
    return render_template("W.html", W=filter_data, role=role)

@app.route("/X.html")
def X():
    username = session.get('username')
    site = session.get('site')
    users = load_users()
    role = users[username]['role']

    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter(Condition.condition.startswith('X'), Condition.site == site).all()
    db_session.close()
    return render_template("X.html", X=filter_data, role=role)

@app.route("/Y.html")
def Y():
    username = session.get('username')
    site = session.get('site')
    users = load_users()
    role = users[username]['role']

    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter(Condition.condition.startswith('Y'), Condition.site == site).all()
    db_session.close()
    return render_template("Y.html", Y=filter_data, role=role)

@app.route("/Z.html")
def Z():
    username = session.get('username')
    site = session.get('site')
    users = load_users()
    role = users[username]['role']

    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter(Condition.condition.startswith('Z'), Condition.site == site).all()
    db_session.close()
    return render_template("Z.html", Z=filter_data, role=role)

@app.route('/resources/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['resource'], filename)
    
@app.route("/action.html")
def action():
    condition = request.args.get('condition', '')
    site = session.get('site')

    Session = sessionmaker(bind=engine)
    db_session = Session()
    filter_data = db_session.query(Condition).filter_by(condition=condition, site=site).all()
    db_session.close()
    
    files = [(files, files.split('.')[0]) for files in os.listdir(app.config['resource'])]
    ResourceSession = sessionmaker(bind=engine)
    resource_session = ResourceSession()

    resources = resource_session.query(Resource).filter_by(condition=condition, site=site).all()
    
    resources_with_link = [resource for resource in resources if resource.link is not None]
    resources_with_attachment = [resource for resource in resources if resource.image is not None]
 
    resource_session.close()

    username = session.get('username')
    users = load_users()
    role = users[username]['role']

    return render_template("action.html", A=filter_data, filename=condition, resources=resources_with_link, image_files=files, files=resources_with_attachment, role=role)

@app.route("/remove_user/<int:user_id>", methods=["POST", "DELETE"])
def deregister_user(user_id):
    if request.method in ["POST", "DELETE"]:
        Session = sessionmaker(bind=engine)
        session = Session()
        user = session.query(User).filter_by(id=user_id).first()

        if user:
            session.delete(user)
            session.commit()
            session.close()
        return redirect("/users.html")
    
@app.route("/devremove_user/<int:user_id>", methods=["POST", "DELETE"])
def devderegister_user(user_id):
    if request.method in ["POST", "DELETE"]:
        Session = sessionmaker(bind=engine)
        session = Session()
        user = session.query(User).filter_by(id=user_id).first()

        if user:
            session.delete(user)
            session.commit()
            session.close()
        return redirect("/devusers.html")
    
@app.route("/remove_suggest/<int:suggest_id>", methods=["POST", "DELETE"])
def deregister_suggest(suggest_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    suggest = session.query(Suggest).filter_by(id=suggest_id).first()
    if suggest:
        session.delete(suggest)
        session.commit()
        session.close()
        return redirect("/suggestions.html")
    
@app.route("/remove_resource/<int:resource_id>", methods=["POST", "DELETE"])
def deregister_resource(resource_id):
    if request.method in ["POST", "DELETE"]:
        Session = sessionmaker(bind=engine)
        session = Session()
        resource = session.query(Resource).filter_by(id=resource_id).first()

        if resource:
            session.delete(resource)
            session.commit()
            session.close()
        return redirect("/AtoZ.html")

@app.route("/remove/<int:condition_id>", methods=["POST", "DELETE"])
def deregister_A(condition_id):
    if request.method in ["POST", "DELETE"]:
        Session = sessionmaker(bind=engine)
        session = Session()
        condition = session.query(Condition).filter_by(id=condition_id).first()
        if condition:
            session.delete(condition)
            session.commit()
            session.close()
        return redirect("/AtoZ.html")
        
if __name__ == "__main__":
    app.run()
        
        