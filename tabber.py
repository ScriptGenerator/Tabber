from flask import Flask, url_for, jsonify, render_template
app = Flask(__name__)
import binascii
def b_to_s(bin):
    result = int(bin, 2)
    result = binascii.unhexlify('%x' % result)
    result = result.decode('utf-8')
    return result

#linko = "https://www.youtube.com/watch?v=9mbp0DugfCA"


@app.route('/')
def api_root():
    f = open('new_tab_link.txt','r')
    linko = f.read(4000)
    f.close()
    if linko != "dont":
        f = open('new_tab_link.txt','w')
        f.write('dont')
        f.close()
    return jsonify(link=linko)

@app.route('/boss')
def boss():
    return render_template('boss.html')

@app.route('/boss/<linko>')
def linko(linko):
    listo = linko.split('and')
    answer = ''
    for e in listo:
        answer += b_to_s(e)
    f = open('new_tab_link.txt','w')
    f.write(answer)
    f.close()
    return 'ok'


app.run(debug=True,port=140,host="0.0.0.0")
