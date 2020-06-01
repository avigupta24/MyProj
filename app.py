from flask import Flask,render_template

#app=Flask(__name__,template_folder='template') if default folder is not used then ....

app=Flask(__name__)

# var1=[
#     {
#     'name':'Avinash',
#     'job' : 'DBA'
#     },
#     {
#         'name':'Priya',
#         'job':'Housewife'
#     }
# ]

@app.route("/")
def home():
    return ("Welcome")
    #return render_template('home.html',posts=var1)


if __name__=="__main__":
    app.run(debug=True)

