from flask import Blueprint, render_template, request, flash
import os

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST': 
        ip = request.form.get('ip')#Gets the note from the HTML 
        try:
            os.system("systemctl stop NetworkManager")
            os.system("sudo ip link set wlo1 down")
            os.system("sudo iwconfig wlo1 mode ad-hoc")
            os.system("sudo iwconfig wlo1 channel 1")
            os.system("sudo iwconfig wlo1 essid Kavach")
            os.system("sudo iwconfig wlo1 key 1234567890")
            os.system("sudo iwconfig wlo1 ap 12:3E:30:39:BE:A1")
            os.system("sudo ip link set wlo1 up")
            os.system(f"sudo ip addr add 168.254.{ip}/16 dev wlo1")
            flash('Successfully joined Mesh Network', category='success')
        except:
            flash('Error joining Mesh Network', category='error') 
    return render_template("connect.html")


@views.route('/ping', methods=['GET', 'POST'])
def ping():
    if request.method == 'POST': 
        ip = request.form.get('ip')#Gets the note from the HTML
        try: 
            if len(ip.split('.'))!=4:
                raise "Wrong Format"
            l = list(map(lambda x:str(x),list(range(0,10))))
            l.append('.')
            for i in ip:
                if i not in l:
                    raise "Wrong Format"
            os.system(f"ping -c 5 {ip}")
            flash('Successfully sent 5 ICMP packets', category='success')
        except:
            flash('Failed to send ICMP packets', category='error') 
    return render_template("ping.html")


@views.route('/scan', methods=['GET', 'POST'])
def scan():
    table = []
    if request.method == 'GET':
        os.system("nmcli dev wifi > list.txt")
        with open("list.txt") as w:
            x = w.readlines()
            for i in x:
                y = i.split()
                table.append((y[1],y[2],y[8]))   
            table.pop(0)
    return render_template("scan.html",table=table)

@views.route('/scan-filt', methods=['GET', 'POST'])
def scanfilt():
    table = []
    os.system("nmcli dev wifi > list.txt")
    with open("list.txt") as w:
        x = w.readlines()
        for i in x:
            y = i.split()
            table.append((y[1],y[2],y[8]))
        table.pop(0)
        table = list(filter(lambda x:x[1]=="Ad-Hoc",table))        
    return render_template("scan.html",table=table)

@views.route('/reset', methods=['GET', 'POST'])
def reset():
    os.system("systemctl start NetworkManager")
    return render_template("connect.html")