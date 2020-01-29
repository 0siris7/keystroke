from flask import Flask #Imports constructors of major mods
from public import public
from admin import admin
from user import user
app=Flask(__name__) #Flask constructor
app.register_blueprint(public) #Synonymous to creating a mould and ack its existence
app.register_blueprint(admin,url_prefix="/admin")
app.register_blueprint(user,url_prefix="/user")
app.run(debug="true",port="5000") #Start of program, debug enables us to see if its being executed(or so they say) at a port 5000
