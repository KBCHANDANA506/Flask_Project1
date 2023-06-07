from flask import Flask

FAI=Flask(__name__)

@FAI.route('/Happy')
def Happy():
    return "Hello.. Chandana Kamalapuram"

if __name__=='__main__':
    FAI.run(debug=True)