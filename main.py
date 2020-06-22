from flask import Flask, request, render_template

app = Flask(__name__)


def square(board, x, y):
    if y == 0 or y == 3 or y == 6:
        offsety = 1
    if y == 1 or y == 4 or y == 7:
        offsety = 0
    if y == 2 or y == 5 or y == 8:
        offsety = -1
    if x == 0 or x == 3 or x == 6:
        offsetx = 1
    if x == 1 or x == 4 or x == 7:
        offsetx = 0
    if x == 2 or x == 5 or x == 8:
        offsetx = -1
    x = x + offsetx
    y = y + offsety
    rlist = board[y - 1][x - 1:x + 1 + 1]
    rlist += board[y][x - 1:x + 1 + 1]
    rlist += board[y + 1][x - 1:x + 1 + 1]
    # print("square is", rlist, x,y)
    return (rlist)

def solver(board):
    tries=0
    running = 1
    limit=1000
    while (running and tries < limit):
        running = 0
        tries+=1
        for y in range(0, 9):
            for x in range(0, 9):
                # print("INIT LOCATION",x,y)
                if board[y][x] == 0:
                    running = 1
                    # print("CHECKING LOCATION", x, y)
                    count = 0
                    for i in range(1, 10):
                        # print("checking i =",i,end=" ")
                        # check row
                        if i in board[y][0:9]:
                            # print(i,"was found in row xy location[0-8][",y,"]")
                            continue
                        # check column
                        rowlist = []
                        for row in range(0, 9):
                            rowlist += [board[row][x]]
                        if i in rowlist:
                            # print(i,"was found in column location",rowlist)
                            continue
                        # check square
                        if i in square(board, x, y):
                            # print(i,"was found in self.square(",x,y,")")
                            continue
                        xsol = x
                        ysol = y
                        isol = i
                        count += 1
                    if count == 1:
                        # print("**************Found only one solution for",xsol,ysol,":",isol)
                        # print("Replacing data...")
                        board[ysol][xsol] = isol
                        # print("new solution:")
                        # print(board)
    if tries >= limit:
        message="Note: Was not able to completely solve this Sodoku."
    else:
        message=""
    return message

@app.route('/')
def my_form():
    message="This is a test"
    return render_template("myform.html")

@app.route('/', methods=['POST'])
def my_form_post():
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0], \
             [0, 0, 0, 0, 0, 0, 0, 0, 0], \
             [0, 0, 0, 0, 0, 0, 0, 0, 0], \
             [0, 0, 0, 0, 0, 0, 0, 0, 0], \
             [0, 0, 0, 0, 0, 0, 0, 0, 0], \
             [0, 0, 0, 0, 0, 0, 0, 0, 0], \
             [0, 0, 0, 0, 0, 0, 0, 0, 0], \
             [0, 0, 0, 0, 0, 0, 0, 0, 0], \
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    invalidchar=0
    for y in range(0,9):
        for x in range(0,9):
            formvar="r"+str(y)+str(x)
            if request.form[formvar] != "":
                if request.form[formvar] in "123456789":
                    board[y][x] = int(request.form[formvar])
                else:
                    invalidchar=1
    #put the solver here
    message=solver(board)
    resultstring="<html>\n"
    resultstring+="<body style=background-color:darkblue;color:white;>"
    resultstring+="<br>"
    resultstring+="<h2>Solution</h2>"
    resultstring+="<table border=5>\n"
    resultstring+="<tbody\n"
    for y in range(0,9):
        if y%3 == 0 and y != 0:
            resultstring+="<tr>\n"
            for i in range(0,11):
                resultstring+="<td bgcolor=grey></td>\n"
            resultstring+="</tr>\n"
        resultstring+="<tr>\n"
        for x in range(0,9):
            if x%3 == 0 and x != 0:
                resultstring+="<td style=width:1% bgcolor=grey>"
            if board[y][x] == 0:
                board[y][x] = "."
            resultstring+="<td width=42 style=text-align:center>"+str(board[y][x])+"</td>"
        resultstring+="</tr>\n"
    resultstring+="</tbody>\n"
    resultstring+="</table>\n"
    resultstring+="<br>"
    resultstring+=message+"\n"
    resultstring+="<br>"
    if invalidchar == 1:
        resultstring+="Warning: Some invalid input characters were detected."
        resultstring+= "<br>"
    resultstring+="<br>"
    resultstring+="<form action=https://sodoku-280518.uc.r.appspot.com/>"
    resultstring+="<button type=submit>Solve Another</button>"
    resultstring+="</form>"
    resultstring+="</body>"
    resultstring+="</html>\n"
    return resultstring
#    return render_template("resultform.html")
#def sodoku():
#    """Return a friendly HTTP greeting."""
#    name = request.args['name']
#    return "hello"

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)

print("Content-Type: text/plain")
print("")
print("This is a Sodoku solver app.")
