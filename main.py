# CREATOR : ZENTBOT 
from tmp.important import *
parserr = argparse.ArgumentParser(description='Selfbot By maxbots')
#parserr.add_argument('-u', '--user', type=str, metavar='', required=True, help='Name User  | Example : Kxxx')
#parserr.add_argument('-T', '--traceback', type=str2bool, nargs='?', default=False, metavar='', required=False, const=True, choices=[True, False], help='Using Traceback | Use : True/False')
args = parserr.parse_args()

defaultJson = livejson.File('user.json', True, False, 4)
helperJson = livejson.File('tmp/setting.json', True, False, 4) 
usernamee = "!"
try:
    userJson = defaultJson['role']['info']['yus']
except:
    print("{} not in list user".format('yus'))
    sys.exit()


try:
    position = livejson.File(userJson['json']['position'],True, True, 4)
    w=position['admin']
except:
    bw = open('{}'.format(userJson['json']['position']),'w').write('{}'.format(open('Linebot/position.json','r').read()))
    position = livejson.File(userJson['json']['position'], True, True, 4)
try:
    settings = livejson.File(userJson['json']['setting'],True, True, 4)
    s=settings['autoAdd']
except:
    bs = open('{}'.format(userJson['json']['setting']),'w').write('{}'.format(open('Linebot/setting.json','r').read()))
    settings = livejson.File(userJson['json']['setting'], True, True, 4)
try:
    listsett = livejson.File(userJson['json']['listset'],True, True, 4)
    le=listsett['textt']
except:
    blt = open('{}'.format(userJson['json']['listset']),'w').write('{}'.format(open('Linebot/listset.json','r').read()))
    listsett = livejson.File(userJson['json']['listset'], True, True, 4)


appNameJs = "app=desktopwin"

appS = livejson.File('appName.json', True, False, 4)
appF = appS["appName"]
#try:
#    with open('token.txt','r') as tokens:
#        token = tokens.read()
#    print(str(token))
#except Exception as e:
#    maxbots = LINE("อีเมล","รหัสผ่าน")
maxbots = LINE("อีเมล","รหัสผ่าน")
#maxbots = LINE(token,appName=appF)
maxbots.log("Auth Token : " + str(maxbots.authToken))
myMid = maxbots.profile.mid
programStart = time.time()
oepoll = OEPoll(maxbots)
flexklr = flexKLR.template(maxbots)

#for publicKey in maxbots.talk.getE2EEPublicKeys():
#    maxbots.talk.removeE2EEPublicKey(publicKey)

#apiJG = imjustgood(helperJson["apiKey"]["JG"])
#apiBE = BEAPI(helperJson["apiKey"]["BE"])
#apiVH = helperJson["apiKey"]["VH"]

apiJG = imjustgood("AdinDa8791bots")
apiBE = BEAPI("Apikey")
apiVH = "elfoxbsd15"


if settings['setKey']['rname'] == "!":
    rnmnya = usernamee
    settings['setKey']['rname'] = rnmnya

thebos = "u0b6d826e613c6cd463ea43db4bf8110b"
teambot = "u0b6d826e613c6cd463ea43db4bf8110b"

protectname = settings["protectname"]
protectqr = settings["protectqr"]
protectinvite = settings["protectinvite"]
protectjoin = settings["protectjoin"]
protectkick = settings["protectkick"]
protectcancel = settings["protectcancel"]

tmp_text = []

lastseen = {
    "find": {},
    "username": {}
}  
     
read2 = {
    "cctv": {},
    "imgurl": {}
}

lurk = {
    "mode": {},
    "readMember": {},
    "readPoint": {}
}      

bool_dict = {
    True: ['Yes', '✓', 'Success', 'https://i.ibb.co/4NvFJxH/kalera-on.png', 'On'],
    False: ['No', '✘', 'Failed', 'https://i.ibb.co/X255xdv/kalera-off.png', 'Off']
}

last_game = {
    "ROM":{},
    "msg_dict": {},
    "spamer": {},
    "spamertime": {},
    "addText": {},
} 

limited = {
    "fake": {},
    "respontag": {},
    "respontagstc": {},
    "respontagemo": {},
    "call": {},
    "greetjm": {},
    "greetjs": {},
    "greetje": {},
    "greetlm": {},
    "greetls": {},
    "greetle": {},
    "list1": {},
    "list2": {},
    "list3": {},
    "list4": {},
    "list5": {},
    "list6": {},
    "list7": {},
    "list8": {},
    "list9": {},
    "uns": {}, 
    "notifi": {}, 
    "ceks": {}
}

wait = {
    "inviteContact":False,
    "selfbot": False,
    "wfriendlist": False,
    "dfriendlist": False,
    "wblocklist": False,
    "dblocklist": False,
    "wblacklist": False,
    "dblacklist": False,
    "wwhitelist": False,
    "dwhitelist": False,
    "wadminlist": False,
    "dadminlist": False,
    "wsquadlist": False,
    "dsquadlist": False,
    "wtalkbanlist": False,
    "dtalkbanlist": False,
    "getpictcontact": False,
    "getcovercontact": False,
    "getexcovercontact": False,
    "getvideocontact": False,
    "getnamecontact": False,
    "getrenamecontact": False,
    "getbiocontact": False,
    "getmidcontact": False,
    "getcontactcontact": False,
    "gettimelinecontact": False,
    "getstorycontact": False,
}   

if not settings:
    print ('##----- LOAD DEFAULT JSON -----##')
    try:
        default_settings = maxbots.server.getJson('https://17hosting.id/default.json')
        settings.update(default_settings)
        print ('##----- LOAD DEFAULT JSON (Success) -----##')
    except Exception:
        print ('##----- LOAD DEFAULT JSON (Failed) -----##')

def restartProgram():
    print ('##----- PROGRAM RESTARTED -----##')
    python = sys.executable
    os.execl(python, python, *sys.argv)

def logError(error, write=True):
    errid = str(random.randint(100, 999))
    filee = open('tmp/errors/%s.txt'%errid, 'w') if write else None
    if args.traceback: traceback.print_tb(error.__traceback__)
    if write:
        traceback.print_tb(error.__traceback__, file=filee)
        filee.close()
        with open('errorLog.txt', 'a') as e:
            e.write('\n%s : %s'%(errid, str(error)))
    print ('++ Error : {error}'.format(error=error))
    
def command(text):
    pesan = text.lower()
    if settings['setKey']['status']:
        if pesan.startswith(settings['setKey']['key']):
            cmd = pesan.replace(settings['setKey']['key'],'')
        else:
            cmd = 'Undefined command'
    else:
        cmd = text.lower()
    return cmd
def publiccmd(text):
    pesan = text.lower()
    if pesan.startswith(settings['setKey']['rname'] +  " "):
        pub = pesan.replace(settings['setKey']['rname'] +  " ",'')
    else:
        pub = 'Undefined command'
    return pub

def geTreply(msg):
    aping = None
    if msg.relatedMessageId != None:
        rhmnirza = maxbots.getRecentMessagesV2(msg.to, 1001)
        for litaaping in rhmnirza:
            if msg.relatedMessageId == litaaping.id:
                aping = litaaping
                break
    return aping

def geTmention(msg):
    if 'MENTION' in msg.contentMetadata.keys() != None:
        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
        mntn = mention['MENTIONEES']
        target = []                
        for mention in mntn:
            if mention["M"] not in target:
                target.append(mention["M"])                
        return target
    else:return None        

def commandMen(msg, text,cmdnya):
    kalera = None
    if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():     
        mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
        mentionees = [mention['M'] for mention in mentions['MENTIONEES']]             
        pesan = text.lower()     
        if myMid in mentionees: 
            b = pesan.replace("@" ,'')
            asuuu = b.lower()
            if cmdnya in asuuu:
                ktl = asuuu.split(f"{cmdnya} ")
                tol = asuuu.replace(ktl[0] + f"{cmdnya} ","")
                kalera = tol
    return kalera

def removeCmd(cmdnya, text):
    aprilia = cmdnya
    nadiul = aprilia[-1:]
    ktl = text.split(f"{nadiul} ")
    tol = text.replace(ktl[0] + f"{nadiul} ","")
    return tol 

def mrt2(text):
    mrt2002 = requests.get("https://tinyurl.com/api-create.php?url={}".format(text))
    return mrt2002.text

def allowLiff():
    url = 'https://access.line.me/dialog/api/permissions'
    data = {
        'on': [
            'P',
            'CM'
        ],
        'off': []
    }
    headers = {'X-Line-Access': maxbots.authToken,'X-Line-Application': maxbots.server.APP_NAME,'X-Line-ChannelId': listsett["liff1"],'Content-Type': 'application/json'}
    requests.post(url, json=data, headers=headers)
def sendTemplate(to, data):
    allowLiff()
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest(listsett["liff2"], xyzz)
    token = maxbots.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {'Content-Type': 'application/json','Authorization': 'Bearer %s' % token.accessToken}
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def timeRESET():
    if settings['timereset']:
        if datetime.now(tz=pytz.timezone("Asia/Jakarta")) > parser.parse(settings['timereset']):
            try:
                position["today"] = {"add": 0,"cancel": 0,"chatrecv": 0,"chatsend": 0,"invite": 0,"kick": 0,"kicked": 0,"invited": 0,"canceled": 0,"added": 0}
                os.popen('echo 1 | sudo tee /proc/sys/vm/drop_caches\necho 2 | sudo tee /proc/sys/vm/drop_caches\necho 3 | sudo tee /proc/sys/vm/drop_caches\n').read()
                position['ROM'] = {}
                last_game['ROM'] = {}
                settings['timereset'] = str(datetime.now(tz=pytz.timezone("Asia/Jakarta"))+timedelta(hours=24))
            except Exception as e:
                logError(e)
                print(f"{e}")
                settings['timereset']  = None

def spamerunbloked():
    for k, v in last_game['spamertime'].items():            
        if v["time"]:
            if datetime.now(tz=pytz.timezone("Asia/Jakarta")) > parser.parse(v["time"]):
                maxbots.unblockContact(k)
                del last_game["spamertime"][k]      
def rahman(to, aping):
    if settings["stattemp"] == True:
        sendTemp(to, aping)     
    elif settings["statfooter"] == True:
        sendFooter(to, aping)     
    else:
        maxbots.sendMessage(to, aping)
def rahmanp(to, aping):  
    if settings["stattemp"] == True:
        sendFooterFoto(to, aping)    
    elif settings["statfooter"] == True:
        sendFooterFoto(to, aping)
    else:
        maxbots.sendImageWithURL(to, aping)    
def rahmanv(to, aping):  
    if settings["stattemp"] == True:
        sendFooterVideo(to,aping)    
    elif settings["statfooter"] == True:
        sendFooterVideo(to,aping)
    else:
        maxbots.sendVideoWithURL(to,aping)    
def rahmana(to, aping):  
    if settings["stattemp"] == True:
        sendFooterAudio(to,aping)    
    else:
        if settings["statfooter"] == True:
            sendFooterAudio(to,aping)
        else:
            maxbots.sendAudioWithURL(to,aping)    
def rahmanH(to):  
    if settings["stattemp"] == True:
        kaleraFlex(to)    
    else:
        rahman(to,help())
def rahmanSTAT(to):  
    if settings["stattemp"] == True:
        statusHTemp(to)    
    else:
        rahman(to,statusH())
def sendMedias(to, aping, aping2):
    if settings["stattemp"] == True:
        sendTemplate(to, aping)
    else:
        if settings["statfooter"] == True:
            sendTemplate(to, aping)
        else:
            rahman(to, aping2)    
def sendMedias2(to, aping, aping2, aping3):
    if settings["stattemp"] == True:
        sendTemplate(to, aping)
    else:
        rahmanp(to, aping3)
        rahman(to, aping2)    
def sendTemp(to, aping):
    if settings["tempyans"] == True:
        tempyans(to, aping)     
    else:
        if settings["temprobot"] == True:
            temprobotflex(to, aping)     
        else:
            if settings["yansnew"] == True:
                yansdefult(to, aping)     
            else:
                if settings["statlinetempblack"] == True:
                    templatelineblack(to, aping)     
                else:
                    if settings["statigtempblack"] == True:
                        templateigblack(to, aping)     
                    else:
                        if settings["statigtempnormal"] == True:
                            templateignormal(to, aping)     
                        else:
                            if settings["invitekontak"] == True:
                                tempallnormal(to, aping)     
                            else:
                            	if settings["tempRyansbot"] == True:
                                    newResponseTemp(to, aping)     
def rahmanlike(to, aping):
    if settings["stattemp"] == True:
        profile = maxbots.getContact(myMid)
        username = profile.displayName
        if profile.pictureStatus: picture = "https://obs.line-scdn.net/"+str(profile.pictureStatus)
        else: picture = "https://s20.directupload.net/images/220423/uxdxnp5a.jpg"
        data = {
      "type": "bubble",
  "size": "kilo",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://i.ibb.co/0Z4cY4r/biruputar.png",
        "size": "full",
        "animated":True,
        "aspectMode": "cover",
        "aspectRatio": "12:6",
        "gravity": "center"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/zGWWscM/Autolike.png",
            "animated":True,
            "size": "full",
            "aspectRatio": "12:6",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "254px",
        "height": "125px",
        "borderWidth": "1px",
        "borderColor": "#000000",
        "cornerRadius": "6px",
        "offsetTop": "2px",
        "offsetStart": "2px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": username,
            "size": "10px",
            "color": "#ffd700",
            "align": "center",
            "weight": "bold",
            "wrap": True,
          }
        ],
        "position": "absolute",
        "width": "100px",
        "height": "15px",
        "borderWidth": "1px",
        "borderColor": "#808080",
        "cornerRadius": "2px",
        "offsetBottom": "3px",
        "offsetStart": "80px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "UDAH DI LIKE MEK",
            "size": "8px",
            "color": "#f5f5f5",
            "align": "center",
            "weight": "bold",
            "wrap": True,
          }
        ],
        "position": "absolute",
        "width": "120px",
        "height": "13px",
        "borderWidth": "1px",
        "borderColor": "#808080",
        "cornerRadius": "2px",
        "offsetTop": "2.2px",
        "offsetStart": "70px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url":"https://i.ibb.co/DYPLqnV/botjoget.png",
            "animated":True,
            "size": "full",
            "aspectRatio": "1:1",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "50px",
        "height": "50px",
        "borderWidth": "0px",
        "borderColor": "#808080",
        "cornerRadius": "0px",
        "offsetBottom": "1px",
        "offsetStart": "1.5px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url":"https://i.ibb.co/DYPLqnV/botjoget.png",
            "animated":True,
            "size": "full",
            "aspectRatio": "1:1",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "50px",
        "height": "50px",
        "borderWidth": "0px",
        "borderColor": "#808080",
        "cornerRadius": "0px",
        "offsetBottom": "1px",
        "offsetEnd": "1.5px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url":"https://i.ibb.co/PGgGrbB/putarr.png",
            "animated":True,
            "size": "full",
            "aspectRatio": "1:1",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "20px",
        "height": "20px",
        "borderWidth": "1px",
        "borderColor": "#808080",
        "cornerRadius": "50px",
        "offsetTop": "5px",
        "offsetStart": "5px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url":"https://i.ibb.co/PGgGrbB/putarr.png",
            "animated":True,
            "size": "full",
            "aspectRatio": "1:1",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "20px",
        "height": "20px",
        "borderWidth": "1px",
        "borderColor": "#808080",
        "cornerRadius": "50px",
        "offsetTop": "5px",
        "offsetEnd": "5px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url":"https://i.ibb.co/0Z4cY4r/biruputar.png",
            "animated":True,
            "size": "full",
            "aspectRatio": "1:1",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "56px",
        "height": "56px",
        "borderWidth": "0px",
        "borderColor": "#808080",
        "cornerRadius": "50px",
        "offsetTop": "34px",
        "offsetStart": "98.5px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": picture,
            "animated":True,
            "size": "full",
            "aspectRatio": "1:1",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "50px",
        "height": "50px",
        "borderWidth": "1px",
        "borderColor": "#808080",
        "cornerRadius": "50px",
        "offsetTop": "37px",
        "offsetStart": "101px"
      },
    ],
    "paddingAll": "0px",
    "borderWidth": "1px",
    "borderColor": "#808080",
    "cornerRadius": "10px",
    "action": {
      "type": "uri",
      "label": "action",
      "uri": "https://line.me/ti/p/~max.panupong.sawaeng"
    }
  },
  "styles": {
    "body": {
      "backgroundColor": "#03303Acc"
    }
  }
}
        sendTemplate(to,{"type": "flex", "altText": settings["footerlabel"], "contents": data})(to, aping)     
    else:
        if settings["statfooter"] == True:
            sendFooter(to, aping)     
        else:
            maxbots.sendMessage(to,aping)
def siderTemplate(op):
    if "@!" in settings["sider"]: message = settings["sider"].replace("@!","")
    else: message = settings["sider"]
    contact = maxbots.getContact(op.param2)
    name = contact.displayName
    if contact.pictureStatus: picture = "https://obs.line-scdn.net/"+contact.pictureStatus
    else: picture = "https://s20.directupload.net/images/220423/uxdxnp5a.jpg"
    data = {"type": "bubble","size": "kilo","body": {"type": "box","layout": "vertical","contents": [{"type": "image","url": "https://i.ibb.co/zGWWscM/Autolike.png","size": "full","animated": True,"aspectMode": "cover","aspectRatio": "6:3.5","gravity": "center"},{"type": "box","layout": "vertical","contents": [{"type": "image","url": "https://i.ibb.co/zQBSCnL/sideryan.png","animated": True,"size": "full","aspectRatio": "6:3.5","aspectMode": "cover"}],"position": "absolute","width": "260px","height": "350px","borderWidth": "0px","borderColor": "#000000","cornerRadius": "0px","offsetTop": "0px","offsetEnd": "0px"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": message,"size": "10px","color": "#ffffff","weight": "bold","align": "center","wrap": True,}],"position": "absolute","width": "150px","height": "30px","borderColor": "#808080","cornerRadius": "0px","offsetTop": "80px","offsetStart": "48px"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": name,"size": "13px","color": "#ffffff","weight": "bold","align": "center","wrap": True,}],"position": "absolute","width": "150px","height": "30px","borderWidth": "0px","borderColor": "#808080","cornerRadius": "0px","offsetTop": "47.7px","offsetStart": "80px"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "Read Chat","size": "6px","color": "#ffffff","weight": "bold","align": "center","wrap": True,}],"position": "absolute","width": "50px","height": "12px","cornerRadius": "0px","offsetTop": "100px","offsetEnd": "30px"},{"type": "box","layout": "vertical","contents": [{"type": "image","url":"https://i.ibb.co/0Z4cY4r/biruputar.png","animated": True,"size": "full","aspectRatio": "1:1","aspectMode": "cover"}],"position": "absolute","width": "47px","height": "47px","borderWidth": "0px","borderColor": "#870000","cornerRadius": "0px","offsetTop": "52px","offsetStart": "30px"},{"type": "box","layout": "vertical","contents": [{"type": "image","url": picture,"animated": True,"size": "full","aspectRatio": "1:1","aspectMode": "cover"}],"position": "absolute","width": "43px","height": "43px","cornerRadius": "0px","offsetTop": "54px","offsetStart": "31.5px"},{"type": "box","layout": "vertical","contents": [{"type": "image","url":"https://i.ibb.co/kJfRgzk/kupu.png","animated": True,"size": "full","aspectRatio": "6:3.5","aspectMode": "cover"}],"position": "absolute"}],"paddingAll": "0px","borderWidth": "2px","borderColor": "#ccac00","cornerRadius": "10px","action": {"type": "uri","label": "action","uri": "https://line.me/ti/p/~max.panupong.sawaeng"}},"styles": {"body": {"backgroundColor": "#03303Acc"}}}
    sendTemplate(op.param1,{"type": "flex", "altText": "{} read the chat.".format(name), "contents": data})
def kaleraFlex(to):
    profile = maxbots.getContact(myMid)
    userpict = "https://obs.line-scdn.net/"+str(profile.pictureStatus)
    if profile.pictureStatus is None:userpict = "https://s20.directupload.net/images/220423/uxdxnp5a.jpg"        
    username = profile.displayName
    clicks   = "{}".format(settings["idline"])
    if settings['setKey']['status'] == True:kalera = settings['setKey']['key']
    else:kalera = ''
    commands = [kalera + "Mode", kalera +  "Self", kalera +  "Steal", kalera + "Profile", kalera + "Friend", kalera + "Group", kalera + "Command", kalera + "Mention", kalera +  "Protect", kalera + "Banning", kalera + "Broadcast", kalera + "Setkick", kalera + "Js", kalera + "Spam", kalera + "Media", kalera + "Fun", kalera + "Setting", kalera + "About", kalera + "Speed", kalera + "Runtime", kalera + "Cekbot", kalera + "Status", kalera + "Listset", kalera + "Vpsinfo", kalera + "Mute", kalera + "Unmute", kalera + "Logout" ]    
    data = flexklr.kaleraHelp(clicks, userpict, username, commands)
    sendTemplate(to,{"type": "flex", "altText": settings["footerlabel"], "contents": {"type": "carousel", "contents": data}})
def statusHTemp(to):
    profile = maxbots.getContact(myMid)
    username = profile.displayName
    userpict = "https://obs.line-scdn.net/"+str(profile.pictureStatus)
    if profile.pictureStatus is None:
        userpict = "https://s20.directupload.net/images/220423/uxdxnp5a.jpg"                       
    data = flexklr.kaleraStatus(settings, userpict, username, bool_dict)
    sendTemplate(to,{"type": "flex", "altText": settings["footerlabel"], "contents": data})
def newResponseTemp(to, aping):
    profile = maxbots.getContact(myMid)
    username = profile.displayName
    userpict = "https://obs.line-scdn.net/"+str(profile.pictureStatus)
    if profile.pictureStatus is None:
        userpict = "https://s20.directupload.net/images/220423/uxdxnp5a.jpg"           
    data = flexklr.yansblue(settings, userpict, username, aping)
    sendTemplate(to,{"type": "flex", "altText": settings["footerlabel"], "contents": data})    
def tempallnormal(to, aping):
    profile = maxbots.getContact(myMid)
    username = profile.displayName
    userpict = "https://obs.line-scdn.net/"+str(profile.pictureStatus)
    if profile.pictureStatus is None:
        userpict = "https://s20.directupload.net/images/220423/uxdxnp5a.jpg"           
    data = flexklr.kaleraMain(settings, userpict, username, aping)
    sendTemplate(to,{"type": "flex", "altText": settings["footerlabel"], "contents": data})
def tempyans(to,aping):
    profile = maxbots.getContact(myMid)
    username = profile.displayName
    userpict = "https://obs.line-scdn.net/"+str(profile.pictureStatus)
    if profile.pictureStatus is None:
        userpict = "https://s20.directupload.net/images/220423/uxdxnp5a.jpg"           
    data = flexklr.flexyans(settings, userpict, username, aping)
    sendTemplate(to,{"type": "flex", "altText": settings["footerlabel"], "contents": data})
def temprobotflex(to,aping):
    profile = maxbots.getContact(myMid)
    username = profile.displayName
    userpict = "https://obs.line-scdn.net/"+str(profile.pictureStatus)
    if profile.pictureStatus is None:
        userpict = "https://s20.directupload.net/images/220423/uxdxnp5a.jpg"           
    data = flexklr.flexrobot(settings, userpict, username, aping)
    sendTemplate(to,{"type": "flex", "altText": settings["footerlabel"], "contents": data})
def yansdefult(to,aping):
    profile = maxbots.getContact(myMid)
    username = profile.displayName
    userpict = "https://obs.line-scdn.net/"+str(profile.pictureStatus)
    if profile.pictureStatus is None:
        userpict = "https://s20.directupload.net/images/220423/uxdxnp5a.jpg"           
    data = flexklr.yansred(settings, userpict, username, aping)
    sendTemplate(to,{"type":"flex","altText":settings["footerlabel"],"contents": data})    
def templatelineblack(to,aping):
    tz = pytz.timezone("Asia/Jakarta")
    inihari = datetime.now(tz=tz)
    data = flexklr.kaleraLine2(settings, inihari, aping)
    sendTemplate(to,{"type":"flex","altText":settings["footerlabel"],"contents": data})    
def templateigblack(to, aping):
    tz = pytz.timezone("Asia/Jakarta")
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    for i in range(len(hari)):
       if hr == hari[i]: hasil = hari[i]
    data = flexklr.kaleraIG1(settings, inihari, hr,aping)
    sendTemplate(to,{"type":"flex","altText":settings["footerlabel"],"contents": data})       
def templateignormal(to, aping):
    tz = pytz.timezone("Asia/Jakarta")
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    for i in range(len(hari)):
       if hr == hari[i]: hasil = hari[i]
    data = flexklr.kaleraIG2(settings, inihari, hr,aping)
    sendTemplate(to,{"type":"flex","altText":settings["footerlabel"],"contents": data})           
def sendFooter(to, aping):
    sendTemplate(to, {"type": "text","text": aping,"sentBy": {"label": "{}".format(settings["footerlabel"]),"iconUrl": "{}".format(settings["footerpict"]),"linkUrl": "{}".format(settings["idline"])}})
def sendFooterFoto(to, aping):
    sendTemplate(to, {"type": "image","originalContentUrl": aping,"previewImageUrl": aping,"sentBy": {"label": "{}".format(settings["footerlabel"]),"iconUrl": "{}".format(settings["footerpict"]),"linkUrl": "{}".format(settings["idline"])}})
def sendFooterVideo(to, aping):
    sendTemplate(to, {"type": "video", "originalContentUrl": mrt2(aping), "previewImageUrl": "{}".format(settings["footerpict"])})
def sendFooterAudio(to, aping):
    sendTemplate(to, {"type": "audio","originalContentUrl": aping,"duration": 1000})
def sendON(to, aping):
    sendTemplate(to,{"type":"flex","altText":settings["footerlabel"],"contents": flexklr.kaleraON(settings, aping)})           
def sendOFF(to, aping):
    sendTemplate(to,{"type":"flex","altText":settings["footerlabel"],"contents": flexklr.kaleraOFF(settings, aping)})           

def notifi(loc, enmy, text):    
    namaGC = maxbots.getChats([loc]).chats[0].chatName
    jam = pytz.timezone("Asia/Jakarta")
    jamSek = datetime.now(tz=jam)
    tanggal = datetime.strftime(jamSek, '%d-%m-%Y')
    jamnya = datetime.strftime(jamSek,'%H:%M:%S')
    kiker = maxbots.getContact(enmy)
    res = f"「 Notif 」\n › Type: Notif {text}♪"
    res += f"\n    • In Group: {namaGC}"
    res += f"\n    • Date: {tanggal}"
    res += f"\n    • Time: {jamnya}"
    res += f"\n    • Name: {kiker.displayName}"
    res += "\n    • User: @!"
    try:
        if len(position["basenotif"]) > 0:
            for x in position["basenotif"]:
                maxbots.sendTag(x, res,[kiker.mid])
                maxbots.sendContact(x, kiker.mid)
        else:
            maxbots.sendTag(teambot, res,[kiker.mid])
            maxbots.sendContact(teambot, kiker.mid)
    except:
        maxbots.sendTag(teambot, res,[kiker.mid])
        maxbots.sendContact(teambot, kiker.mid)
def notifi2(enmy):    
    jam = pytz.timezone("Asia/Jakarta")
    jamSek = datetime.now(tz=jam)
    tanggal = datetime.strftime(jamSek, '%d-%m-%Y')
    jamnya = datetime.strftime(jamSek,'%H:%M:%S')
    kiker = maxbots.getContact(enmy)
    res = f"「 Notif 」\n › Type: Notif Add♪"
    res += f"\n    • Date: {tanggal}"
    res += f"\n    • Time: {jamnya}"
    res += f"\n    • Name: {kiker.displayName}"
    res += "\n    • User: @!"
    try:
        if len(position["basenotif"]) > 0:
            for x in position["basenotif"]:
                maxbots.sendTag(x, res,[kiker.mid])
                maxbots.sendContact(x, kiker.mid)
        else:
            maxbots.sendTag(teambot, res,[kiker.mid])
            maxbots.sendContact(teambot, kiker.mid)
    except:
        maxbots.sendTag(teambot, res,[kiker.mid])
        maxbots.sendContact(teambot, kiker.mid)
    position["today"]["added"] += 1
def notifi3(loc, enmy, text):    
    namaGC = maxbots.getChats([loc]).chats[0].chatName
    jam = pytz.timezone("Asia/Jakarta")
    jamSek = datetime.now(tz=jam)
    tanggal = datetime.strftime(jamSek, '%d-%m-%Y')
    jamnya = datetime.strftime(jamSek,'%H:%M:%S')
    kiker = maxbots.getContact(enmy)
    res = f"「 Notif 」\n › Type: Notif Tag♪"
    res += f"\n    • In Group: {namaGC}"
    res += f"\n    • Date: {tanggal}"
    res += f"\n    • Time: {jamnya}"
    res += f"\n    • Name: {kiker.displayName}"
    res += "\n    • User: @!"
    res += f"\n    • Message:\n\n {text}"
    try:
        if len(position["basenotif"]) > 0:
            for x in position["basenotif"]:
                maxbots.sendTag(x, res,[kiker.mid])
                maxbots.sendContact(x, kiker.mid)
        else:
            maxbots.sendTag(teambot, res,[kiker.mid])
            maxbots.sendContact(teambot, kiker.mid)
    except:
        maxbots.sendTag(teambot, res,[kiker.mid])
        maxbots.sendContact(teambot, kiker.mid)
def ngelastlist(loc, type, target):
    if loc not in last_game['ROM']:
        last_game['ROM'][loc] = {}
    if type not in last_game['ROM'][loc]:
        last_game['ROM'][loc][type] = {"last": "","list": []}
    last_game['ROM'][loc][type]["last"] = target
    if target not in last_game['ROM'][loc][type]["list"]:
        last_game['ROM'][loc][type]["list"].append(target)
def ngeclearlast(loc,type, text):
    if loc in last_game['ROM']:
        if type in last_game['ROM'][loc]:
            rahman(loc, f"「 Last 」\n › Type: {text} Clear♪\n    • Amount: {len(last_game['ROM'][loc][type]['list'])}\n    • Status: Success")
            last_game['ROM'][loc][type]["list"].clear()
        else:
            rahman(loc, f"「 Last 」\n › Type: {text}♪\n    • Status: Nothing")
    else:
        rahman(loc, f"「 Last 」\n › Type: {text}♪\n    • Status: Nothing")
def deldellast(to,mmk,type,data,text):
    x = splitdel(str(mmk), last_game['ROM'][to][type]["list"])
    z = len(last_game['ROM'][to][type]["list"])//100
    for c in range(z+1):
        if c == 0:
            maxbots.datamentionslast(to,'Last',x[:100],data,last_game,ps=f'\n › Type: {text}♪')
        else:
            maxbots.datamentionslast(to,'Last',x[c*100 : (c+1)*100],data,position,ps=f'\n › Type: {text}♪')     
def iilast(to, mmk, type):
    if mmk == "all":
        ktl = maxbots.getChats([to]).chats[0]
        target = []
        for x in last_game['ROM'][to][type]["list"]:
            if x not in ktl.extra.groupExtra.memberMids and x not in ktl.extra.groupExtra.inviteeMids and x not in target:
                target.append(x)
        if target:
            total = 500 - len(ktl.extra.groupExtra.memberMids) - len(ktl.extra.groupExtra.inviteeMids)
            if total != 0: 
                maxbots.inviteIntoChat(to, target[0:total]) 
                for xxx in target[0:total]:
                    ngelastlist(to, "lastinvite", xxx)
                position["today"]["invite"] += len(target[0:total])
    else:
        xx = splitdel(str(mmk), last_game['ROM'][to][type]["list"])
        z = len(last_game['ROM'][to][type]["list"])//100
        for c in range(z+1):
            if c == 0:
                ktl = maxbots.getChats([to]).chats[0]
                target = []
                for x in xx[:100]:
                    if x not in ktl.extra.groupExtra.memberMids and x not in ktl.extra.groupExtra.inviteeMids and x not in target:
                        target.append(x)
                if target:
                    total = 500 - len(ktl.extra.groupExtra.memberMids) - len(ktl.extra.groupExtra.inviteeMids)
                    if total != 0: 
                        maxbots.inviteIntoChat(to, target[0:total]) 
                        for xxx in target[0:total]:
                            ngelastlist(to, "lastinvite", xxx)
                        position["today"]["invite"] += len(target[0:total])
            else:
                ktl = maxbots.getChats([to]).chats[0]
                target = []
                for x in xx[c*100 : (c+1)*100]:
                    if x not in ktl.extra.groupExtra.memberMids and x not in ktl.extra.groupExtra.inviteeMids and x not in target:
                        target.append(x)
                if target:
                    total = 500 - len(ktl.extra.groupExtra.memberMids) - len(ktl.extra.groupExtra.inviteeMids)
                    if total != 0: 
                        maxbots.inviteIntoChat(to, target[0:total]) 
                        for xxx in target[0:total]:
                            ngelastlist(to, "lastinvite", xxx)
                        position["today"]["invite"] += len(target[0:total])
def kklast(to, mmk, type):
    if mmk == "all":  
        list = last_game['ROM'][to][type]["list"]
        cm = 'kickall.js gid={} type=dual token={} {}'.format(to, maxbots.authToken, appNameJs)
        for x in list:
            cm += ' uik={}'.format(x)
            position["today"]["cancel"] += 1
        for x in list:
            cm += ' uid={}'.format(x)
            position["today"]["kick"] += 1
        success = execute_js(cm)        
    else:
        xx = splitdel(str(mmk), last_game['ROM'][to][type]["list"])
        z = len(last_game['ROM'][to][type]["list"])//100
        for c in range(z+1):
            if c == 0:
                list = xx[:100]
                cm = 'kickall.js gid={} type=dual token={} {}'.format(to, maxbots.authToken, appNameJs)
                for x in list:
                    cm += ' uik={}'.format(x)
                    position["today"]["cancel"] += 1
                for x in list:
                    cm += ' uid={}'.format(x)
                    position["today"]["kick"] += 1
                success = execute_js(cm)        
            else:
                list = xx[c*100 : (c+1)*100]
                cm = 'kickall.js gid={} type=dual token={} {}'.format(to, maxbots.authToken, appNameJs)
                for x in list:
                    cm += ' uik={}'.format(x)
                    position["today"]["kick"] += 1
                for x in list:
                    cm += ' uid={}'.format(x)
                    position["today"]["kick"] += 1
                success = execute_js(cm)        
def cclast(to, mmk, type):
    if mmk == "all":
        ktl = last_game['ROM'][to][type]["list"]
        for x in ktl:
            time.sleep(0.5)
            canceled(to, x)
            position["today"]["cancel"] += 1
    else:
        xx = splitdel(str(mmk), last_game['ROM'][to][type]["list"])
        z = len(last_game['ROM'][to][type]["list"])//100
        for c in range(z+1):
            if c == 0:
                for x in xx[:100]:
                    time.sleep(0.5)
                    canceled(to, x)
                    position["today"]["cancel"] += 1
            else:
                for x in xx[c*100 : (c+1)*100]:
                    time.sleep(0.5)
                    canceled(to, x)
                    position["today"]["cancel"] += 1
def accepted(loc):
    maxbots.acceptChatInvitation(loc)
def rejected(loc):
    maxbots.rejectChatInvitation(loc)
def leaveed(loc):
    maxbots.deleteSelfFromChat(loc)
def finded(enmy):
    if enmy not in maxbots.getAllContactIds():
        maxbots.findAndAddContactsByMid(enmy)
        position["today"]["add"] += 1
    else:pass
def mentext(loc, isi):
    if '@!' not in isi:
        maxbots.sendMessage(loc, isi)                    
    else:
        maxbots.sendTag(loc, isi, [loc])         
def mentext2(loc, enmy, isi):
    if '@!' not in isi:
        maxbots.sendMessage(loc, isi)                    
    else:
        maxbots.sendTag(loc, isi, [enmy])                   
def sendEmo(loc, type1, type2 ,type3):
    ktl = type1
    mmk = type2
    if '(' not in ktl:
        maxbots.sendMessage(loc, '',mmk)        
    else:
        if '@!' not in ktl:
            maxbots.sendMessage(loc, ktl,mmk)                                                                      
        else:
            maxbots.sendMentionEmot(loc, ktl, mmk, type3, settings, [loc])                                       
def sendEmo2(loc, enmy, type1, type2 ,type3):
    ktl = type1
    mmk = type2
    if '(' not in ktl:
        maxbots.sendMessage(loc, '',mmk)        
    else:
        if '@!' not in ktl:
            maxbots.sendMessage(loc, ktl,mmk)                                                                      
        else:
            maxbots.sendMentionEmot(loc, ktl, mmk, type3, settings, [enmy])                                       
def ngebl(enmy):
    if enmy not in position["blacklist"]:
        position['blacklist'].append(enmy)                 
    else:pass
def kicked(loc, enmy):
    maxbots.deleteOtherFromChat(loc, [enmy])
    ngelastlist(loc, "lastkick", enmy)
    position["today"]["kick"] += 1
def canceled(loc, enmy):
    maxbots.cancelChatInvitation(loc, [enmy])    
    ngelastlist(loc, "lastcancel", enmy)
    position["today"]["cancel"] += 1
def invited(loc, enmy):
    finded(enmy)
    ktl = maxbots.getChats([loc]).chats[0]
    if enmy not in ktl.extra.groupExtra.memberMids and enmy not in ktl.extra.groupExtra.inviteeMids:
        maxbots.inviteIntoChat(loc, [enmy])   
        ngelastlist(loc, "lastinvite", enmy)
        position["today"]["invite"] += 1
    else:pass
def kickedJS(loc, enmy):
    jutsu = 'kickall.js gid={} type=dual token={} {}'.format(loc, maxbots.authToken, appNameJs)
    for die in enmy:
       jutsu += ' uid={}'.format(die)    
       position["today"]["kick"] += 1    
    execute_js(jutsu)
def canceledJS(loc, enmy):
    jutsu = 'kickall.js gid={} type=dual token={} {}'.format(loc, maxbots.authToken, appNameJs)
    for die in enmy:
       jutsu += ' uik={}'.format(die)      
       position["today"]["cancel"] += 1   
    execute_js(jutsu)
def invSquad(loc, name):
    ktl = maxbots.getChats([loc]).chats[0]
    target = []
    for x in position["squadteam"][name]["list"]:
        if x in ktl.extra.groupExtra.memberMids or x in ktl.extra.groupExtra.inviteeMids:
            continue
        if x not in target:
            target.append(x)
    if target:
        total = 500 - len(ktl.extra.groupExtra.memberMids) - len(ktl.extra.groupExtra.inviteeMids)
        if total != 0: 
            maxbots.inviteIntoChat(loc, target[0:total])
            for xxx in target[0:total]:
                ngelastlist(loc, "lastinvite", xxx)
            position["today"]["invite"] += len(target[0:total])
def lastSEEN(to, sender):
    try:
        group = maxbots.getChats([to]).chats[0].chatName
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
        hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
        bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
        hr = timeNow.strftime("%A")
        bln = timeNow.strftime("%m")
        for i in range(len(day)):
            if hr == day[i]: hasil = hari[i]
        for k in range(0, len(bulan)):
            if bln == str(k): bln = bulan[k-1]
        readTime = timeNow.strftime('%H.%M')
        readTime2 = hr
        readTime3 = timeNow.strftime('%d') + "-" + bln + "-" + timeNow.strftime('%Y')
        lastseen["username"][sender] = f"\n    • In Group: {group}\n    • Time: {readTime} WIB\n    • Day: {readTime2}\n    • Date: {readTime3}"
        lastseen['find'][sender] = True
    except:
        pass                          
def splitdel(text, list):
    mmeks = MySplit(text,range(1,len(list)+1))
    b = []
    for c in mmeks.parse():
        b.append(list[int(c)-1])
    return b
def clearP(to, type, text1, text2):
    if len(position[type]) > 0:
        rahman(to, f"「 {text1} 」\n › Type: {text2} Clear♪ \n    • Amount: {len(position[type])} \n    • Status: Success")
        position[type].clear()                        
    else:
        rahman(to, f"「 {text1} 」\n › Type: {text2} Clear♪ \n    • Status: Nothing♪")            
def delSTC(to, type, text1, text2):
    mmk = "MMK"
    settings[type]["STKID"] = mmk
    settings[type]["STKPKGID"] = mmk
    settings[type]["STKVER"] = mmk
    rahman(to, f"「 {text1} 」\n › Type: Del {text2}♪\n    • Status: Success")
def statW(to, type, text1, text2):
    wait[type] = True
    if settings['setKey']['status'] == True:kalera = settings['setKey']['key']
    else:kalera = ''
    rahman(to, f"「 {text1} 」\n › Type: {text2}♪\n    • Note: Type " + kalera +  "Abort For Cancel \n    • Status: Send Contact") 
def statS1(to, mmk, type, text1, text2):
    if mmk == 'on':
        if settings[type]:
            if settings["stattemp"] == True:
                sendON(to, text2)
            else:
                rahman(to, f'「 {text1} 」\n › Type: {text2}♪\n    • Status: Already Active')                
        else:
            settings[type] = True
            if settings["stattemp"] == True:
                sendON(to, text2)
            else:    	
                rahman(to,f'「 {text1} 」\n › Type: {text2}♪\n    • Status: Active')                                
    elif mmk == 'off':
        if not settings[type]:
            if settings["stattemp"] == True:
                sendOFF(to, text2)
            else:
                rahman(to, f'「 {text1} 」\n › Type: {text2}♪\n    • Status: Already Deactive')                      
        else:
            settings[type] = False
            if settings["stattemp"] == True:
                sendOFF(to, text2)
            else:
                rahman(to,f'「 {text1} 」\n › Type: {text2}♪\n    • Status: Deactive')                                                       
def statS2(to, type, text1, text2, text3):
    settings[type] = True
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    rahman(to, f"「 {text1} 」\n › Type: {text2}♪\n    • Note: Type {kalera}Abort For Cancel \n    • Status: Send {text3}")
def statS3(to, type1, type2, text1, text2):
    settings[type1] = True
    settings[type2] = False
    if settings["stattemp"] == True:
        sendON(to, text2)
    else:
        rahman(to, f"「 {text1} 」\n › Type: {text2}♪\n    • Status: Active")
def statS4(to, type, text1, text2):
    settings[type] = False
    rahman(to, f"「 {text1} 」\n › Type: {text2}♪\n    • Status: Deactive")
def statS5(to, mmk, type, type2, text1, text2):
    if mmk == 'on':
        if settings[type][type2]:
            if settings["stattemp"] == True:
                sendON(to, text2)
            else:	
                rahman(to, f'「 {text1} 」\n › Type: {text2}♪\n    • Status: Already Active')                
        else:
            settings[type][type2] = True
            if settings["stattemp"] == True:
                sendON(to, text2)
            else:
                rahman(to,f'「 {text1} 」\n › Type: {text2}♪\n    • Status: Active')                                
    elif mmk == 'off':
        if not settings[type][type2]:
            if settings["stattemp"] == True:
                sendOFF(to, text2)
            else:
                rahman(to, f'「 {text1} 」\n › Type: {text2}♪\n    • Status: Already Deactive')                
        else:
            settings[type][type2] = False
            if settings["stattemp"] == True:
                sendOFF(to, text2)
            else:
                rahman(to,f'「 {text1} 」\n › Type: {text2}♪\n    • Status: Deactive')                                
def statS6(to, type, type2,type3, text1, text2, text3):
    settings[type][type2][type3] = True
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    rahman(to, f"「 {text1} 」\n › Type: {text2}♪\n    • Note: Type {kalera}Abort For Cancel \n    • Status: Send {text3}")
def statS7(to, mmk, type, type2, type3, text1, text2):
    if mmk == 'on':
        if settings[type][type2][type3]:
            if settings["stattemp"] == True:
                sendON(to, text2)
            else:
                rahman(to, f'「 {text1} 」\n › Type: {text2}♪\n    • Status: Already Active')                
        else:
            settings[type][type2][type3] = True
            if settings["stattemp"] == True:
                sendON(to, text2)
            else:
                rahman(to,f'「 {text1} 」\n › Type: {text2}♪\n    • Status: Active')                                
    elif mmk == 'off':
        if not settings[type][type2][type3]:
            if settings["stattemp"] == True:
                sendOFF(to, text2)
            else:    	
                rahman(to, f'「 {text1} 」\n › Type: {text2}♪\n    • Status: Already Deactive')                
        else:
            settings[type][type2][type3] = False
            if settings["stattemp"] == True:
                sendOFF(to, text2)
            else: 	
                rahman(to,f'「 {text1} 」\n › Type: {text2}♪\n    • Status: Deactive')                                                  
def statS8(to, type, type2, text1, text2, text3):
    settings[type][type2] = True
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    rahman(to, f"「 {text1} 」\n › Type: {text2}♪\n    • Note: Type {kalera}Abort For Cancel \n    • Status: Send {text3}")
def statCCTV(to, mmk):
    if mmk == 'on':
        read2["cctv"][to] = []
        if settings["stattemp"] == True:
            sendON(to, "SIDER")            
        else:
            rahman(to,"「 Group 」\n › Type: Sider♪\n    • In Group: {}\n    • Status: Active".format(maxbots.getChats([to]).chats[0].chatName))                    	
    elif mmk == 'off':
        if to in read2["cctv"]:
            del read2["cctv"][to]           
        if settings["stattemp"] == True:
            sendOFF(to, "SIDER")            
        else:
            rahman(to,"「 Group 」\n › Type: Sider♪\n    • In Group: {}\n    • Status: Deactive".format(maxbots.getChats([to]).chats[0].chatName))                    	
def statMODE(to, type1, type2, type3, type4, type5, type6, type7, type8, text):
     settings[type1] = True
     settings[type2] = False
     settings[type3] = False
     settings[type4] = False
     settings[type5] = False
     settings[type6] = False
     settings[type7] = False
     settings[type8] = False
     sendON(to, text)
def statPro(to, mmk, type, text):
    if mmk == 'on':
        if to in settings[type]:
            msgs = f"「 Protect 」\n › Type: {text}♪\n    • Status: Already Active"                
        else:
             settings[type].append(to)
             ginfo = maxbots.getChats([to]).chats[0]
             msgs = f"「 Protect 」\n › Type: {text}♪\n    • In Group : {ginfo.chatName}\n    • Status: Active"     
        if settings["stattemp"] == True:
            sendON(to, text)            
        else:                         
            rahman(to, msgs)
    elif mmk == 'off':
        if to in settings[type]:
            settings[type].remove(to)
            ginfo = maxbots.getChats([to]).chats[0]
            msgs = f"「 Protect 」\n › Type: {text}♪\n    • In Group : {ginfo.chatName} \n    • Status: Deactive"                                                
        else:
            msgs = "「 Protect 」\n › Type: {text}♪\n    • Status: Already Dective"                  
        if settings["stattemp"] == True:
            sendOFF(to, text)            
        else:                         
            rahman(to, msgs)
def changeMSG(to, mmk, type, text1,text2):
    hmmk = settings[type]
    settings[type] = mmk
    rahman(to,f"「 {text1} 」\n › Type: {text2}♪\n    • Before: {hmmk} \n    • After: {mmk} \n    • Status: Succes")
def changeMSG2(to, mmk, type, type2, text1,text2):
    hmmk = settings[type][type2]
    settings[type][type2] = mmk
    rahman(to,f"「 {text1} 」\n › Type: {text2}♪\n    • Before: {hmmk} \n    • After: {mmk} \n    • Status: Succes")
def changeMSG3(to, mmk, type, type2, type3, text1,text2):
    hmmk = settings[type][type2][type3]
    settings[type][type2][type3] = mmk
    rahman(to,f"「 {text1} 」\n › Type: {text2}♪\n    • Before: {hmmk} \n    • After: {mmk} \n    • Status: Succes")
def printEMO(to, msg, asu, type, type2, type3, cmdnya,text1,text2):
    settings[type][type2] = asu
    REPLACE = {"sticon":{"resources": []}}
    x = eval(msg.contentMetadata["REPLACE"])
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    a = kalera + cmdnya
    for data_rep in x["sticon"]["resources"]:
        REPLACE["sticon"]["resources"].append({"S": str(data_rep["S"] - len(a)), "E": str(data_rep["E"] - len(a)), "productId":data_rep["productId"], "sticonId": data_rep["sticonId"], "version":1, "resourceType": data_rep["resourceType"]})
    contentMetadata = {"REPLACE": json.dumps(REPLACE),"STICON_OWNERSHIP": msg.contentMetadata['STICON_OWNERSHIP']}                                
    settings[type][type3] = contentMetadata
    rahman(to,f"「 {text1} 」\n › Type: {text2}♪\n    • Status: Succes")        
def printSTC(ktl):
    if "STK_MESSAGE" in ktl.contentMetadata:
        mmk = {"STKVER":ktl.contentMetadata["STKVER"],"STKPKGID":ktl.contentMetadata["STKPKGID"],"STKID":ktl.contentMetadata["STKID"],"STK_MESSAGE":ktl.contentMetadata["STK_MESSAGE"]}
    else:
        if "STK_IMG_TXT" in ktl.contentMetadata:
            mmk = {"STKVER":ktl.contentMetadata["STKVER"],"STKPKGID":ktl.contentMetadata["STKPKGID"],"STKID":ktl.contentMetadata["STKID"],"STK_IMG_TXT":ktl.contentMetadata["STK_IMG_TXT"]}
        else:
            mmk = {"STKVER":ktl.contentMetadata["STKVER"],"STKPKGID":ktl.contentMetadata["STKPKGID"],"STKID":ktl.contentMetadata["STKID"]}
    return mmk
def formatNumber(num):
    if len(str(num)) < 7:
        return format_number(num)
    millnames = ['', 'T', 'M', 'B', 'T']
    num = float(num)
    millidx = max(0, min(len(millnames)-1, int(math.floor(0 if num == 0 else math.log10(abs(num))/3))))
    return '{:.0f} {}'.format(num/10**(3*millidx), millnames[millidx])

def help():
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    typenya = "Runtime"
    with open('tmp/menuSB/help.txt', 'r') as f:
        text = f.read()
    help = text.format(kalera=kalera.title(), typenya=typenya, team='®  ' + settings["footerlabel"])
    return help
def modeH():
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    with open('tmp/menuSB/mode.txt', 'r') as f:
        text = f.read()
    modeH = text.format(kalera=kalera.title())
    return modeH
def profileH():
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    with open('tmp/menuSB/profile.txt', 'r') as f:
        text = f.read()
    profileH = text.format(kalera=kalera.title())
    return profileH
def selfH():
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    with open('tmp/menuSB/self.txt', 'r') as f:
        text = f.read()
    selfH = text.format(kalera=kalera.title())
    return selfH
def stealH():
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    with open('tmp/menuSB/steal.txt', 'r') as f:
        text = f.read()
    stealH = text.format(kalera=kalera.title())
    return stealH
def friendH():
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    with open('tmp/menuSB/friend.txt', 'r') as f:
        text = f.read()
    friendH = text.format(kalera=kalera.title())
    return friendH
def groupH():
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    with open('tmp/menuSB/group.txt', 'r') as f:
        text = f.read()
    groupH = text.format(kalera=kalera.title(), bye=settings['leave'].title())
    return groupH
def commandH():
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    with open('tmp/menuSB/command.txt', 'r') as f:
        text = f.read()
    commandH = text.format(kalera=kalera.title())
    return commandH
def mentionH():
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    with open('tmp/menuSB/mention.txt', 'r') as f:
        text = f.read()
    mentionH = text.format(kalera=kalera.title(), xtagall=settings['tagall'].title(), xetagall=settings['emojitagall'].title())
    return mentionH
def protectionH():
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    with open('tmp/menuSB/protect.txt', 'r') as f:
        text = f.read()
    protectionH = text.format(kalera=kalera.title())
    return protectionH
def banningH():
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    with open('tmp/menuSB/banning.txt', 'r') as f:
        text = f.read()
    banningH = text.format(kalera=kalera.title())
    return banningH
def broadcastH():
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    with open('tmp/menuSB/broadcast.txt', 'r') as f:
        text = f.read()
    broadcastH = text.format(kalera=kalera.title())
    return broadcastH
def kicksetH():
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    with open('tmp/menuSB/setkick.txt', 'r') as f:
        text = f.read()
    kicksetH = text.format(kalera=kalera.title(), nkick=settings['kick'].title(), nkill=settings['kill'].title(), nrein=settings['reinvite'].title(), nsl=settings['slain'].title(),nmk=settings['mkick'].title(),ncan=settings['cancel'].title(), nkb=settings['killban'].title(), nkbpy=settings['killbanpy'].title(), nkkpy=settings['kickallpy'].title())
    return kicksetH
def inviteset():
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    with open('tmp/menuSB/setinvite.txt', 'r') as f:
        text = f.read()
    inviteset = text.format(kalera=kalera.title(), nin=settings['invite'].title())
    return inviteset
def funH():
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    with open('tmp/menuSB/funy.txt', 'r') as f:
        text = f.read()
    funH = text.format(kalera=kalera.title())
    return funH
def gameH():
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    with open('tmp/menuSB/game.txt', 'r') as f:
        text = f.read()
    gameH = text.format(kalera=kalera.title())
    return gameH
def javascriptH():
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    with open('tmp/menuSB/javas.txt', 'r') as f:
        text = f.read()
    javascriptH = text.format(kalera=kalera.title(), bp=settings['bypass'].title(),kl=settings['kickall'].title(),cl=settings['cancelall'].title())
    return javascriptH
def spamH():
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    with open('tmp/menuSB/spam.txt', 'r') as f:
        text = f.read()
    spamH = text.format(kalera=kalera.title())
    return spamH
def mediaH():
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    with open('tmp/menuSB/media.txt', 'r') as f:
        text = f.read()
    mediaH = text.format(kalera=kalera.title())
    return mediaH
def settingH():
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    with open('tmp/menuSB/setsb.txt', 'r') as f:
        text = f.read()
    settingH = text.format(kalera=kalera.title())
    return settingH
def autoresponS():
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    with open('tmp/menuSB/autores.txt', 'r') as f:
        text = f.read()
    autoresponS = text.format(kalera=kalera.title(), s1=bool_dict[settings['autoRespondMention']['status']][1],s2=bool_dict[settings['responstickertag']][1],s3=bool_dict[settings['emojirespontag']['status']][1],s4=bool_dict[settings['autoRespond']['status']][1],s5=bool_dict[settings['responstickerchat']][1],s6=bool_dict[settings['emojiresponchat']['status']][1])
    return autoresponS
def lastlisttt():
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    with open('tmp/menuSB/lastlisttt.txt', 'r') as f:
        text = f.read()
    lastlisttt = text.format(kalera=kalera.title())
    return lastlisttt

def autoaddS():
    if settings['setKey']['status'] == True:kalera = settings['setKey']['key']
    else:kalera = ''
    autoaddS =   "「 Autoadd 」" + "\n" + \
             " › Status" +"\n" + \
             "    • Audoadd: " + bool_dict[settings['autoAdd']['status']][1] + "\n" + \
             "    • Autoadd Msg: "  + bool_dict[settings['autoAdd']['reply']][1] + "\n" + \
             "    • Autoadd Sticker: "  + bool_dict[settings['responstickeradd']][1] + "\n" + \
             "    • Autoadd Emoji: "  + bool_dict[settings['emojiautoadd']['status']][1] + "\n" + "\n" + \
             " › Command" +"\n" + \
             "    • " + kalera + "Cek Msgautoadd" + "\n" + \
             "    • " + kalera + "Cek Stickerautoadd" + "\n" + \
             "    • " + kalera + "Changeautoadd ‹Text›" + "\n" + \
             "    • " + kalera + "Add Stickerautoadd" + "\n" + \
             "    • " + kalera + "Add Emojiautoadd ‹Emoji›" + "\n" + \
             "    • " + kalera + "Autoadd ‹On/Off›" + "\n" + \
             "    • " + kalera + "Autoaddmsg ‹On/Off›" + "\n" + \
             "    • " + kalera + "Autoaddstc ‹On/Off›" + "\n" + \
             "    • " + kalera + "Autoaddemoji ‹On/Off›" + "\n" + "\n" + \
             " › Command Reply" +"\n" + \
             "    • " + kalera + "Add Stickerautoadd"              
    return autoaddS
def autojoinS():
    if settings['setKey']['status'] == True:kalera = settings['setKey']['key']
    else:kalera = ''
    autojoinS =   "「 Autojoin 」" + "\n" + \
             " › Status" +"\n" + \
             "    • Autojoin: " + bool_dict[settings['autoJoin']['status']][1] + "\n" + \
             "    • Autojoin Bypass: "  + bool_dict[settings['autojoinbypass']][1] + "\n" + \
             "    • Autojoin Kickall: "  + bool_dict[settings['autojoinkickall']][1]+ "\n" + \
             "    • Autojoin Cancelall: "  + bool_dict[settings['autojoincancelall']][1]+ "\n" + \
             "    • Autojoin Killban: "  + bool_dict[settings['autojoinkillban']][1] + "\n" + \
             "    • Autojoin Kickall PY:"  + bool_dict[settings['autojoinkickallPY']][1] + "\n" + \
             "    • Autojoin Killban PY: "  + bool_dict[settings['autojoinkillbanPY']][1] + "\n" + \
             "    • Autojoin Msg: "  + bool_dict[settings['autoJoin']['reply']][1] + "\n" + \
             "    • Autojoin Sticker: "  + bool_dict[settings['autojoinsticker']][1] + "\n" + "\n" + \
             " › Command" +"\n" + \
             "    • " + kalera + "Cek Msgautojoin" + "\n" + \
             "    • " + kalera + "Cek Stickerautojoin" + "\n" + \
             "    • " + kalera + "Changeautojoin ‹Text›" + "\n" + \
             "    • " + kalera + "Add Stickerautojoin" + "\n" + \
             "    • " + kalera + "Autojoin ‹On/Off›" + "\n" + \
             "    • " + kalera + "Autojoinbypass ‹On/Off›" + "\n" + \
             "    • " + kalera + "Autojoinkickall ‹On/Off›" + "\n" + \
             "    • " + kalera + "Autojoincancelall ‹On/Off›" + "\n" + \
             "    • " + kalera + "Autojoinkillban ‹On/Off›" + "\n" + \
             "    • " + kalera + "Autojoinkickallpy ‹On/Off›" + "\n" + \
             "    • " + kalera + "Autojoinkillbanpy ‹On/Off›" + "\n" + \
             "    • " + kalera + "Autojoinmsg ‹On/Off›" + "\n" + \
             "    • " + kalera + "Autojoinsticker ‹On/Off›" + "\n" + "\n" + \
             " › Command Reply" +"\n" + \
             "    • " + kalera + "Add Stickerautojoin" 
    return autojoinS    
def autoleaveS():
    if settings['setKey']['status'] == True:kalera = settings['setKey']['key']
    else:kalera = ''
    autoleaveS =   "「 Autoleave 」" + "\n" + \
             " › Status" +"\n" + \
             "    • Autoleave Gc: " + bool_dict[settings['autoLeave']['gc']["status"]][1] + "\n" + \
             "    • Autoleave Mc: "  + bool_dict[settings['autoLeave']['mc']["status"]][1] + "\n" + \
             "    • Autoleavemsg Gc: " + bool_dict[settings['autoLeave']['gc']["msg"]][1] + "\n" + \
             "    • Autoleavemsg Mc: "  + bool_dict[settings['autoLeave']['mc']["msg"]][1] + "\n" + \
             "    • Autoleavestc Gc: "  + bool_dict[settings['autoLeave']['gc']["stc"]][1] + "\n" + \
             "    • Autoleavestc Mc: "  + bool_dict[settings['autoLeave']['mc']["stc"]][1] + "\n" + "\n" + \
             " › Command" +"\n" + \
             "    • " + kalera + "Cek Msgautoleave Gc" + "\n" + \
             "    • " + kalera + "Cek Msgautoleave Mc" + "\n" + \
             "    • " + kalera + "Cek Stickerautoleave Gc" + "\n" + \
             "    • " + kalera + "Cek Stickerautoleave Mc" + "\n" + \
             "    • " + kalera + "Changeautoleave Gc ‹Text›" + "\n" + \
             "    • " + kalera + "Changeautoleave Mc ‹Text›" + "\n" + \
             "    • " + kalera + "Add Stickerautoleave Gc" + "\n" + \
             "    • " + kalera + "Add Stickerautoleave Mc" + "\n" + \
             "    • " + kalera + "Autoleave Gc ‹On/Off›" + "\n" + \
             "    • " + kalera + "Autoleave Mc ‹On/Off›" + "\n" + \
             "    • " + kalera + "Autoleavemsg Gc ‹On/Off›" + "\n" + \
             "    • " + kalera + "Autoleavemsg Mc ‹On/Off›" + "\n" + \
             "    • " + kalera + "Autoleavestc Gc ‹On/Off›" + "\n" + \
             "    • " + kalera + "Autoleavestc Mc ‹On/Off›"+ "\n" + "\n" + \
             " › Command Reply" +"\n" + \
             "    • " + kalera + "Add Stickerautoleave Gc" + "\n" + \
             "    • " + kalera + "Add Stickerautoleave Mc"              
    return autoleaveS
def autoreadS():
    if settings['setKey']['status'] == True:kalera = settings['setKey']['key']
    else:kalera = ''
    autoreadS =   "「 Autoread 」" + "\n" + \
             " › Status" +"\n" + \
             "    • Autoread: " + bool_dict[settings['AutoRead']['all']][1] + "\n" + \
             "    • Autoread Pc: " + bool_dict[settings['AutoRead']['pc']][1] + "\n" + \
             "    • Autoread Gc: " + bool_dict[settings['AutoRead']['gc']][1] + "\n" + "\n" + \
             " › Command" +"\n" + \
             "    • " + kalera + "Autoread ‹On/Off›" + "\n" + \
             "    • " + kalera + "Autoreadpc ‹On/Off›" + "\n" + \
             "    • " + kalera + "Autoreadgc ‹On/Off›"
    return autoreadS
def autocommentS():
    if settings['setKey']['status'] == True:kalera = settings['setKey']['key']
    else:kalera = ''
    autocommentS =   "「 Autocomment 」" + "\n" + \
             " › Status" +"\n" + \
             "    • Autocomment Post: " + bool_dict[settings['AutoComment']['post']][1] + "\n" + \
             "    • Autocomennt Story: "  + bool_dict[settings['AutoComment']['story']][1] + "\n" + \
             "    • Autocomennt Sticker Post: "  + bool_dict[settings['AutoComment']['sticker']][1] + "\n" + "\n" + \
             " › Command" +"\n" + \
             "    • " + kalera + "Cek Msgcommentpost" + "\n" + \
             "    • " + kalera + "Cek Msgcommentstory" + "\n" + \
             "    • " + kalera + "Cek Stickercomment" + "\n" + \
             "    • " + kalera + "Changecommentpost ‹Text›" + "\n" + \
             "    • " + kalera + "Changecommentstory ‹Text›" + "\n" + \
             "    • " + kalera + "Add Stickercomment" + "\n" + \
             "    • " + kalera + "Autocommentpost ‹On/Off›" + "\n" + \
             "    • " + kalera + "Autocommentstcpost ‹On/Off›" + "\n" + \
             "    • " + kalera + "Autocommentstory ‹On/Off›" + "\n" + "\n" + \
             " › Command Reply" +"\n" + \
             "    • " + kalera + "Add Stickercomment"
    return autocommentS
def autolikeS():
    if settings['setKey']['status'] == True:kalera = settings['setKey']['key']
    else:kalera = ''
    autolikeS =   "「 Autolike 」" + "\n" + \
             " › Status" +"\n" + \
             "    • Autolike Post: " + bool_dict[settings['AutoLike']['post']][1] + "\n" + \
             "    • Autolike Story: "  + bool_dict[settings['AutoLike']['story']][1] + "\n" + "\n" + \
             " › Command" +"\n" + \
             "    • " + kalera + "Cek Msgautolike" + "\n" + \
             "    • " + kalera + "Changelike ‹Text›" + "\n" + \
             "    • " + kalera + "Autolikepost ‹On/Off›" + "\n" + \
             "    • " + kalera + "Autolikestory ‹On/Off›"
    return autolikeS
def setkeyS():
    setkeyS =   "「 Setkey 」" + "\n"  + \
                    " › Condition " + "\n" + \
                    "    • Status: " + bool_dict[settings['setKey']['status']][1] + "\n" + \
                    "    • Setkey: " + settings['setKey']['key'] + "\n" + "\n" + \
                    " › Command" + "\n" + \
                    "    • Setkey ‹Text›" + "\n" + \
                    "    • Setkey ‹On/Off›"
    return setkeyS
def mimicS():
    if settings['setKey']['status'] == True:kalera = settings['setKey']['key']
    else:kalera = ''
    mimicS =   "「 Mimic 」" + "\n" + \
             " › Condition" +"\n" + \
             "    • Status "  + bool_dict[settings['mimic']['status']][1] + "\n" + "\n" + \
             " › Command" +"\n" + \
             "    • " + kalera + "Mimiclist" + "\n" + \
             "    • " + kalera + "Clearmimic" + "\n" + \
             "    • " + kalera + "Addmimic ‹@›" + "\n" + \
             "    • " + kalera + "Delmimic ‹@›" + "\n" + \
             "    • " + kalera + "Mimic ‹On/Off›"+ "\n" + "\n" + \
             " › Command Reply" +"\n" + \
             "    • " + kalera + "Addmimic" + "\n" + \
             "    • " + kalera + "Delmimic" 
    return mimicS
def greetS():
    if settings['setKey']['status'] == True:kalera = settings['setKey']['key']
    else:kalera = ''
    greetS =   "「 Greet 」" + "\n" + \
             " › Command" +"\n" + \
             "    • " + kalera + "Cek Msggreetjoin" + "\n" + \
             "    • " + kalera + "Cek Msggreetleave" + "\n" + \
             "    • " + kalera + "Cek Stickergreetjoin" + "\n" + \
             "    • " + kalera + "Cek Stickergreetleave" + "\n" + \
             "    • " + kalera + "Add Stickergreetjoin" + "\n" + \
             "    • " + kalera + "Add Stickergreetleave" + "\n" + \
             "    • " + kalera + "Add Emojigreetjoin ‹Emoji›" + "\n" + \
             "    • " + kalera + "Add Emojigreetleave ‹Emoji›" + "\n" + \
             "    • " + kalera + "Greet Join ‹Text›" + "\n" + \
             "    • " + kalera + "Greet Leave ‹Text›" + "\n" + \
             "    • " + kalera + "Greet Join ‹On/Off›" + "\n" + \
             "    • " + kalera + "Greet Leave ‹On/Off›" + "\n" + \
             "    • " + kalera + "Stcgreetjoin ‹On/Off›" + "\n" + \
             "    • " + kalera + "Stcgreetleave ‹On/Off›" + "\n" + \
             "    • " + kalera + "Emojigreetjoin ‹On/Off›" + "\n" + \
             "    • " + kalera + "Emojigreetleave ‹On/Off›" + "\n" + "\n" + \
             " › Command Reply" +"\n" + \
             "    • " + kalera + "Add Stickergreetjoin" + "\n" + \
             "    • " + kalera + "Add Stickergreetleave"              
    return greetS
def detectS():
    if settings['setKey']['status'] == True:kalera = settings['setKey']['key']
    else:kalera = ''
    detectS =   "「 Detect 」" + "\n" + \
             " › Status" +"\n" + \
             "    • Detect Callgroup: " + bool_dict[settings['Detect']['callgroup']][1] + "\n" + \
             "    • Detect Faketag: " + bool_dict[settings['Detect']['faketag']][1] + "\n" + \
             "    • Detect Spamcall: " + bool_dict[settings['Detect']['spamcall']][1] + "\n" + "\n" + \
             " › Command" +"\n" + \
             "    • " + kalera + "Cek Msgdfaketag" + "\n" + \
             "    • " + kalera + "Cek Msgdspamcall" + "\n" + \
             "    • " + kalera + "Changedfaketag ‹Text›" + "\n" + \
             "    • " + kalera + "Changedspamcall ‹Text›" + "\n" + \
             "    • " + kalera + "Detectcallgroup ‹On/Off›" + "\n" + \
             "    • " + kalera + "Detectfaketag ‹On/Off›" + "\n" + \
             "    • " + kalera + "Detectspamcall ‹On/Off›" + "\n" + \
             "    • " + kalera + "Detectunsend"             
    return detectS
def checkS():
    if settings['setKey']['status'] == True:kalera = settings['setKey']['key']
    else:kalera = ''
    checkS =   "「 Check 」" + "\n" + \
             " › Status" +"\n" + \
             "    • Check Post: " + bool_dict[settings['Check']['post']][1] + "\n" + \
             "    • Check Sticker: " + bool_dict[settings['Check']['sticker']][1] + "\n" + "\n" + \
             " › Command" +"\n" + \
             "    • " + kalera + "Checkpost ‹On/Off›" + "\n" + \
             "    • " + kalera + "Checksticker ‹On/Off›"
    return checkS
def lurkS():
    if settings['setKey']['status'] == True:kalera = settings['setKey']['key']
    else:kalera = ''
    lurkS =   "「 Lurk 」" + "\n" + \
             " › Command" +"\n" + \
             "    • " + kalera + "Lurk Result" + "\n" + \
             "    • " + kalera + "Lurk ‹On/Off›"
    return lurkS
def helppublic():
    kalera = settings["setKey"]["rname"].title()
    helppublic =   "「 Help Public 」" + "\n" + "\n" + \
                    " › Command " + "\n" + \
                    "    • Rname" + "\n" + \
                    "    • " + kalera +  " Tagall" + "\n" + \
                    "    • " + kalera +  " Getcall" + "\n" + \
                    "    • " + kalera +  " Openqr" + "\n" + \
                    "    • " + kalera +  " Closeqr" + "\n" + \
                    "    • " + kalera +  " Jodohku" + "\n" + \
                    "    • " + kalera +  " Persen Cinta ‹Name›" + "\n" + \
                    "    • " + kalera +  " Truth Or Dare ‹@›" + "\n" + \
                    "    • " + kalera +  " Getpict ‹@›" + "\n" + \
                    "    • " + kalera +  " Getcover ‹@›" + "\n" + \
                    "    • " + kalera +  " Getvideo ‹@›" + "\n" + \
                    "    • " + kalera +  " Getname ‹@›" + "\n" + \
                    "    • " + kalera +  " Gebio ‹@›" + "\n" + \
                    "    • " + kalera +  " Getmid ‹@›" + "\n" + \
                    "    • " + kalera +  " Getcontact ‹@›" + "\n" + "\n" + \
                    " › Command Reply" + "\n" + \
                    "    • " + kalera +  " Getpict" + "\n" + \
                    "    • " + kalera +  " Getcover" + "\n" + \
                    "    • " + kalera +  " Getvideo" + "\n" + \
                    "    • " + kalera +  " Getname" + "\n" + \
                    "    • " + kalera +  " Gebio" + "\n" + \
                    "    • " + kalera +  " Getmid" + "\n" + \
                    "    • " + kalera +  " Getcontact" + "\n" + "\n" + \
                    " › Command Share Link" +"\n" + \
                    "    • Share Link Tiktok" + "\n" + \
                    "    • Share Link Instagram" + "\n" + \
                    "    • Share Link Youtube" + "\n" + \
                    "    • Share Link Timeline"
    return helppublic
def helpadmin():
    kalera = settings["setKey"]["rname"].title()
    helpadmin =   "「 Help Admin 」" + "\n" + "\n" + \
                    " › Command " + "\n" + \
                    "    • Rname" + "\n" + \
                    "    • " + kalera +  " Tagall" + "\n" + \
                    "    • " + kalera +  " Getcall" + "\n" + \
                    "    • " + kalera +  " Openqr" + "\n" + \
                    "    • " + kalera +  " Closeqr" + "\n" + \
                    "    • " + kalera +  " Jodohku" + "\n" + \
                    "    • " + kalera +  " Persen Cinta ‹Name›" + "\n" + \
                    "    • " + kalera +  " Truth Or Dare ‹@›" + "\n" + \
                    "    • " + kalera +  " Sider ‹On/Off›" + "\n" + \
                    "    • " + kalera +  " Unsend ‹No›" + "\n" + \
                    "    • " + kalera +  " Kick ‹@›" + "\n" + \
                    "    • " + kalera +  " Invite ‹@›" + "\n" + \
                    "    • " + kalera +  " Getpict ‹@›" + "\n" + \
                    "    • " + kalera +  " Getcover ‹@›" + "\n" + \
                    "    • " + kalera +  " Getvideo ‹@›" + "\n" + \
                    "    • " + kalera +  " Getname ‹@›" + "\n" + \
                    "    • " + kalera +  " Gebio ‹@›" + "\n" + \
                    "    • " + kalera +  " Getmid ‹@›" + "\n" + \
                    "    • " + kalera +  " Getcontact ‹@›" + "\n" + "\n" + \
                    " › Command Reply" + "\n" + \
                    "    • " + kalera +  " Kick" + "\n" + \
                    "    • " + kalera +  " Invite" + "\n" + \
                    "    • " + kalera +  " Getpict" + "\n" + \
                    "    • " + kalera +  " Getcover" + "\n" + \
                    "    • " + kalera +  " Getvideo" + "\n" + \
                    "    • " + kalera +  " Getname" + "\n" + \
                    "    • " + kalera +  " Gebio" + "\n" + \
                    "    • " + kalera +  " Getmid" + "\n" + \
                    "    • " + kalera +  " Getcontact" + "\n" + "\n" + \
                    " › Command Share Link" +"\n" + \
                    "    • Share Link Tiktok" + "\n" + \
                    "    • Share Link Instagram" + "\n" + \
                    "    • Share Link Youtube" + "\n" + \
                    "    • Share Link Timeline"
    return helpadmin
def statusH():
    statusH =   "「 Status 」 " + "\n"  + \
                    " › Condition " + "\n" + \
                    "    • Backup Wl: " + bool_dict[settings['backupwl']][1] + "\n" + \
                    "    • Backup Admin: " + bool_dict[settings['backupadmin']][1] + "\n" + \
                    "    • Download Media: " + bool_dict[settings['downloadmedia']][1] + "\n" + \
                    "    • Js: " + bool_dict[settings['javascript']][1] + "\n" + \
                    "    • Mode Public: " + bool_dict[settings['modepublic']][1] + "\n" + \
                    "    • Purge: " + bool_dict[settings["purge"]][1]
    return statusH
def listH():
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    listH =   "「 List Set 」" + "\n" + \
             " › Wordban" +"\n" + \
             "    • " + kalera + "Wordban List" + "\n" + \
             "    • " + kalera + "Wordban Clear" + "\n" + \
             "    • " + kalera + "Wordban Add ‹Text›" + "\n" + \
             "    • " + kalera + "Wordban Del ‹Text›" + "\n" + "\n" + \
             " › Text" +"\n" + \
             "    • " + kalera + "Text List" + "\n" + \
             "    • " + kalera + "Text Clear" + "\n" + \
             "    • " + kalera + "Text Add ‹Text | Text›" + "\n" + \
             "    • " + kalera + "Text Del ‹Text›" + "\n" + "\n" + \
             " › Picture" +"\n" + \
             "    • " + kalera + "Picture List" + "\n" + \
             "    • " + kalera + "Picture Clear" + "\n" + \
             "    • " + kalera + "Picture Add ‹Text›" + "\n" + \
             "    • " + kalera + "Picture Del ‹Text›" + "\n" + "\n" + \
             " › Video" +"\n" + \
             "    • " + kalera + "Video List" + "\n" + \
             "    • " + kalera + "Video Clear" + "\n" + \
             "    • " + kalera + "Video Add ‹Text›" + "\n" + \
             "    • " + kalera + "Video Del ‹Text›" + "\n" + "\n" + \
             " › Audio" +"\n" + \
             "    • " + kalera + "Audio List" + "\n" + \
             "    • " + kalera + "Audio Clear" + "\n" + \
             "    • " + kalera + "Audio Add ‹Text›" + "\n" + \
             "    • " + kalera + "Audio Del ‹Text›" + "\n" + "\n" + \
             " › Sticker" +"\n" + \
             "    • " + kalera + "Sticker List" + "\n" + \
             "    • " + kalera + "Sticker Clear" + "\n" + \
             "    • " + kalera + "Sticker Add ‹Text›" + "\n" + \
             "    • " + kalera + "Sticker Del ‹Text›" + "\n" + "\n" + \
             " › Bigsticker" +"\n" + \
             "    • " + kalera + "Bigsticker List" + "\n" + \
             "    • " + kalera + "Bigsticker Clear" + "\n" + \
             "    • " + kalera + "Bigsticker Add ‹Text›" + "\n" + \
             "    • " + kalera + "Bigsticker Del ‹Text›" + "\n" + "\n" + \
             " › Contact" +"\n" + \
             "    • " + kalera + "Cont List" + "\n" + \
             "    • " + kalera + "Cont Clear" + "\n" + \
             "    • " + kalera + "Cont Add ‹Text›" + "\n" + \
             "    • " + kalera + "Cont Del ‹Text›" + "\n" + "\n" + \
             " › Kibaran" +"\n" + \
             "    • " + kalera + "Kibaran List" + "\n" + \
             "    • " + kalera + "Kibaran Clear" + "\n" + \
             "    • " + kalera + "Kibaran Add ‹Text›" + "\n" + \
             "    • " + kalera + "Kibaran Del ‹Text›"
    return listH
def vpsinfoH():
    if settings['setKey']['status'] == True:kalera = settings['setKey']['key']
    else:kalera = ''
    vpsinfoH =   "「 Vps Info 」" + "\n" + \
             " › Command" +"\n" + \
             "    • " + kalera + "Memory" + "\n" + \
             "    • " + kalera + "System" + "\n" + \
             "    • " + kalera + "Clears" + "\n" + \
             "    • " + kalera + "Clearletsel" + "\n" + \
             "    • " + kalera + "Clearchat"
    return vpsinfoH

def selfsticker():
    a = maxbots.shop.getActivePurchases(start=0, size=1000, language='ID', country='ID').productList
    c = "「 Self 」\n › Type: Mysticker♪"
    no = 0
    for b in a:
       no +=1
       c += "\n    • "+str(no)+". "+b.title[:21]+" ID:"+str(b.packageId)
    k = len(c)//10000
    for aa in range(k+1):
        ret_ = '{}'.format(c[aa*10000 : (aa+1)*10000])
        return ret_
def stealpict(to, mid):
    try:
        rahmanp(to, str("https://obs.line-scdn.net/{}".format(maxbots.getContact(mid).pictureStatus)))
    except:
        rahman(to, "Nothing♪")
def stealcover(to, mid):  
    try:
        if mid is None:
            mid = maxbots.profile.mid
        profileDetail = maxbots.getProfileDetail(mid)
        if 'videoCoverObsInfo' in profileDetail['result']:
            params = {'userid': mid, 'oid': profileDetail['result']['videoCoverObsInfo']['objectId']}
            url = maxbots.server.urlEncode(maxbots.LineObsDomain, '/myhome/vc/download.nhn', params)
            maxbots.sendVideoWithURL(to, url)
        else:
            params = {'userid': mid, 'oid': profileDetail['result']['coverObsInfo']['objectId']}
            url = maxbots.server.urlEncode(maxbots.LineObsDomain, '/myhome/c/download.nhn', params)
            rahmanp(to, url)
    except:
        rahman(to, "Nothing♪")
def coverGroup(to):
    gcnya = maxbots.getChats([to]).chats[0].chatMid
    profileDetail = maxbots.getProfileCoverDetail(gcnya)
    params = {'userid': gcnya, 'oid': profileDetail['result']['coverObsInfo']['objectId']}
    url = maxbots.server.urlEncode(maxbots.LineObsDomain, '/myhome/c/download.nhn', params)
    rahmanp(to, url)
def stealexcover(to, mid):
    try:
        a = maxbots.getProfileDetail(mid)
        b = "https://obs.line-scdn.net/r/stymedia/pf/"
        for data in a["result"]["userStyleMedia"]["components"]:
            if data["type"] == "PFRAME":
                for res in data["data"]:
                    rahmanp(to, b+res["media"]["objectId"]) 
    except:
       rahman(to, "Nothing♪")       
def stealvideo(to, mid):
    try:
        maxbots.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/{}/vp".format(maxbots.getContact(mid).pictureStatus))
    except:
        rahman(to, "Nothing♪")          
def stealname(to, mid, text1):
    maxbots.sendMessage(to, f"「 {text1} 」\n › Type: Name♪\n    • Name:\n{maxbots.getContact(mid).displayName}")        
def stealrename(to, mid):
    maxbots.sendMessage(to, f"「 Steal 」\n › Type: Rename♪\n    • Rename:\n{maxbots.getContact(mid).displayNameOverridden}")         
def stealbio(to, mid, text1):
    try:
        maxbots.sendMessage(to, f"「 {text1} 」\n › Type: Bio♪\n    • Bio:\n{maxbots.getContact(mid).statusMessage}")        
    except:
        rahman(to, "Nothing♪")        
def stealmid(to, mid):
    maxbots.sendMessage(to,"{}".format(maxbots.getContact(mid).mid))
def stealcontact(to, mid):
    maxbots.sendContact(to, maxbots.getContact(mid).mid) 
def stealtimeline(to, mid, text1):
    data = maxbots.getHomeProfile(mid)
    if data['result'] != []:
        try:
            no = 1
            a = f"「 {text1} 」\n › Type: Timeline♪\n"
            for i in data['result']['feeds']:
                gtime = i['post']['postInfo']['createdTime']
                timeCreated = []
                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(gtime) / 1000)))
                try:desc ="    • " + str(no) + ". Caption: "+str(i['post']['contents']['text'])
                except:desc ="    • " + str(no) + ". Caption: None"
                a += str(desc)
                a +="\n    • Total Like : "+str(i['post']['postInfo']['likeCount'])
                a +="\n    • Total Comment : "+str(i['post']['postInfo']['commentCount'])
                a +="\n    • Created on : "+str(timeCreated[0])+"\n"
                no = (no+1)
            a +="\n › Total Post: "+str(data['result']['homeInfo']['postCount'])+" Post."
            rahman(to,str(a))
        except:
            rahman(to, "Nothing♪")        
def stealstory(to, mid):
    try:
        story = maxbots.getStory(mid)
        listnya = []
        if story['message'] == 'success':
            if story['result']['contents']:
                for content in story['result']['contents']:
                    if content['media'][0]['mediaType'] == 'IMAGE':
                        rahmanp(to,str('https://obs.line-scdn.net/' + content['media'][0]['hash']))
                    if content['media'][0]['mediaType'] == 'VIDEO':
                        maxbots.sendVideoWithURL(to,str('https://obs.line-scdn.net/' + content['media'][0]['hash']))
    except:
        rahman(to, "Nothing♪")        
def getcontactcontact():
    wait["getcontactcontact"] = True
    if settings['setKey']['status'] == True:
        kalera = settings['setKey']['key']
    else:
        kalera = ''
    return "「 Steal 」\n › Type: Getcontact♪\n    • Note: Type " + kalera +  "Abort For Cancel \n    • Status: Send Mid"
def changevideopp(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = maxbots.genOBSParams({'oid': myMid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4', 'name': 'Hello_World.mp4'})
        data = {'params': obs_params}
        r_vp = maxbots.server.postContent('{}/talk/vp/upload.nhn'.format(str(maxbots.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        maxbots.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:raise Exception("Error change video and picture profile %s"%str(e))
def covernyaa(mid):  
    if mid is None:
        mid = maxbots.profile.mid
    profileDetail = maxbots.getProfileDetail(mid)
    params = {'userid': mid, 'oid': profileDetail['result']['coverObsInfo']['objectId']}
    url = maxbots.server.urlEncode(maxbots.LineObsDomain, '/myhome/c/download.nhn', params)
    return url
def sendMessageCustom(to, text, icon , name):
    maxbots.sendMessage(to, text, contentMetadata= {'MSG_SENDER_ICON': icon,'MSG_SENDER_NAME':  name})        
def callGet(to):
    try:
        a = maxbots.getGroupCall(to);print(a);k = len(a.memberMids)//20                        
        for i in range(k+1):
            try:
                if i == 0:aa = '「 Group 」\n › Detail: Group Call \n    • In: {}\n    • Call started in: {}\n    • Member Call:'.format(maxbots.getChats([to]).chats[0].chatName,humanize.naturaltime(datetime.fromtimestamp(int(a.started)//1000)));no = i
                else:aa = '「 Group 」\n › Detail: Group Call\n    • In: {}\n    • Call started in: {}\n    • Member Call:'.format(maxbots.getChats([to]).chats[0].chatName,humanize.naturaltime(datetime.fromtimestamp(int(a.starter)//1000)));no=i*20
                ret = aa
                for b in a.memberMids[i*20 : (i+1)*20]:
                    no += 1;c = a.hostMids                        
                    if a.mediaType == 1:typenya = 'Free Call Group'
                    if a.mediaType == 2:typenya = 'Video Call Group'
                    if no == len(a.memberMids):ret+='\n       • {}. @!\n › Type: {}\n    • Host: @!'.format(no,typenya)
                    else:ret+='\n       • {}. @!'.format(no)
                maxbots.sendMentionn(to, ret,"",a.memberMids[i*20 : (i+1)*20]+[c])
            except:
                if a.mediaType == 3:typenya = 'Group Live'
                if i == 0:aa = '「 Group 」\n › Detail: Group Live\n    • In: {}\n    • Live started in: {}\n    • Member Watch:'.format(maxbots.getChats([to]).chats[0].chatName,humanize.naturaltime(datetime.fromtimestamp(int(a.started)//1000)));no = i
                else:aa = '「 Group 」\n › Detail: Group Live\n    • In: {}\n    • Live started in: {}\n    • Member Watch:'.format(maxbots.getChats([to]).chats[0].chatName,humanize.naturaltime(datetime.fromtimestamp(int(a.starter)//1000)));no=i*20
                ret = aa
                for b in a.memberMids[i*20 : (i+1)*20]:
                    no += 1;c = a.hostMids                        
                    if no == len(a.memberMids):ret+='\n       • {}. @!\n › Type: {}\n    • Host: @!'.format(no,typenya)
                    else:ret+='\n       • {}. @!'.format(no)
                maxbots.sendMentionn(to, ret,"",a.memberMids[i*20 : (i+1)*20]+[c])
    except:
        rahman(to,'「 Group 」\n › Detail: Group Call\n    • In: {}\n    • Call: Nothing'.format(maxbots.getChats([to]).chats[0].chatName))        
def cekmember(aping):
    bajingan = [];ktl = maxbots.getChats([aping], True , False).chats[0]    
    if ktl.extra.groupExtra.memberMids != {}:
       for mmk in ktl.extra.groupExtra.memberMids:bajingan.append(mmk)
    return bajingan     
def memberGroup(to, mids=[]):
    parsed_len = len(mids)//20+1;result = '「 Group 」\n › Type: Memberlist♪\n';mention = '@cmdrhmn_ir\n';no = 0            
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*20:(point+1)*20]:
            no += 1;result += '    • %i. %s' % (no, mention);slen = len(result) - 12;elen = len(result) + 3;mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})                                                
            if mid == mids[-1]:result += '\n'                
        if result:
            if result.endswith('\n'): result = result[:-1]
            maxbots.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees})}, 0)
        result = ''
def cekpending(aping):
    bajingan = [];ktl = maxbots.getChats([aping]).chats[0]    
    if ktl.extra.groupExtra.inviteeMids != {}:
       for mmk in ktl.extra.groupExtra.inviteeMids:bajingan.append(mmk)
    return bajingan        
def pendingGroup(to, mids=[]):
    parsed_len = len(mids)//20+1;result = '「 Group 」\n › Type: Pendinglist♪\n';mention = '@cmdrhmn_ir\n';no = 0            
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*20:(point+1)*20]:
            no += 1;result += '    • %i. %s' % (no, mention);slen = len(result) - 12;elen = len(result) + 3;mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})                                                
            if mid == mids[-1]:result += '\n'                
        if result:
            if result.endswith('\n'): result = result[:-1]
            maxbots.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees})}, 0)
        result = ''
def qrOpen(aping):
    group = maxbots.getChats([aping], True , False).chats[0];group.extra.groupExtra.preventedJoinByTicket = False;maxbots.updateChat(group , 4);gurl = maxbots.reissueChatTicket(aping)
    return gurl.ticketId
def qrClose(aping):
    group = maxbots.getChats([aping], True , False).chats[0]
    group.extra.groupExtra.preventedJoinByTicket = True
    maxbots.updateChat(group , 4)
def pictGroup(to ,type, text):
    if to not in settings[type]:
       settings[type].append(to)
    if settings['setKey']['status'] == True:
         kalera = settings['setKey']['key']
    else:
         kalera = ''
    rahman(to, f"「 Group 」\n › Type: Change {text}♪\n    • Note: Type " + kalera +  "Abort For Cancel \n    • Status: Send Image")
def cektagallM(to):
    bajingan = []
    room = maxbots.getCompactRoom(to)
    bajingan = [mem.mid for mem in room.contacts]
def tagallMention(to, mids=[]):
    if myMid in mids:mids.remove(myMid)    
    if thebos in mids:mids.remove(thebos)    
    parsed_len = len(mids)//20+1
    result = '「 M E N T I O N 」\n › Members:\n'
    mention = '@IYUS_SELF™\n'
    no = 0
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*20:(point+1)*20]:
            no += 1
            result += '    • %i. %s' % (no, mention)
            slen = len(result) - 12
            elen = len(result) + 3
            mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
            if mid == mids[-1]:
                result += '\n'
        if result:
            if result.endswith('\n'): result = result[:-1]
            maxbots.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees})}, 0)
        result = ''
def tagallEmot(to, msg, enmy):
    h = [a for a in enmy]
    k = len(h)//20                          
    for aa in range(k+1):
        if msg.toType == 1:
            if aa == 0:
                dd = "「 Mention 」\n › Type: Tagall Emoji♪"
                no=aa
            else:
                dd = '「 Mention 」\n › Type: Tagall Emoji♪'
                no=aa*20
            msgas = dd
            for a in h[aa*20:(aa+1)*20]:
                no+=1
                startcode = 21                                      
                if no == len(h):
                    msgas+='\n    • {}. @!'.format(no)
                else:
                    msgas += '\n    • {}. @!'.format(no)
                if aa % 2 == 0:
                    startcode = 1                                          
            maxbots.sendMentionEmoticon(to, msgas, settings["fakeemoji"]["emoji"], startcode, h[aa*20:(aa+1)*20])
        elif msg.toType == 2:
            if aa == 0:
                dd = "「 Mention 」\n › Type: Tagall Emoji♪"
                no=aa
            else:
                dd = '「 Mention 」\n › Type: Tagall Emoji♪'
                no=aa*20
            msgas = dd
            for a in h[aa*20:(aa+1)*20]:
                no+=1
                startcode = 21                                         
                if no == len(h):
                    msgas+='\n    • {}. @!'.format(no)
                else:
                    msgas += '\n    • {}. @!'.format(no)
                if aa % 2 == 0:
                    startcode = 1                                             
            maxbots.sendMentionEmoticon(to, msgas, settings["fakeemoji"]["emoji"], startcode ,h[aa*20:(aa+1)*20]) 
def NoteCreate(to,cmd,msg):
    h = []
    s = []
    if cmd == 'mentionnote':
        sakui = maxbots.getProfile()
        group = maxbots.getGroup(msg.to);nama = [contact.mid+'||//{}'.format(contact.displayName) for contact in group.members];nama.remove(sakui.mid+'||//{}'.format(sakui.displayName))
        data = nama
        k = len(data)//20
        for aa in range(k+1):
            nos = 0
            if aa == 0:dd = '「 Mention 」\n › Type: Mention Note♪';no=aa
            else:dd = '「 Mention 」\n › Type: Mention Note♪';no=aa*20
            msgas = dd
            for i in data[aa*20 : (aa+1)*20]:
                no+=1
                if no == len(data):msgas+='\n    • {}. @'.format(no)
                else:msgas+='\n    • {}. @'.format(no)
            msgas = msgas
            for i in data[aa*20 : (aa+1)*20]:
                gg = []
                dd = ''
                for ss in msgas:
                    if ss == '@':
                        dd += str(ss)
                        gg.append(dd.index('@'))
                        dd = dd.replace('@',' ')
                    else:
                        dd += str(ss)
                s.append({'type': "RECALL", 'start': gg[nos], 'end': gg[nos]+1,'mid': str(i.split('||//')[0])})
                nos +=1
            h = maxbots.createPostGroup(msgas,msg.to,holdingTime=None,textMeta=s)
def sendfakesticker(to, spkg,sid,sver, mids=[]):
    if myMid in mids:mids.remove(myMid)    
    if thebos in mids:mids.remove(thebos)    
    parsed_len = len(mids)//140+1
    result = '「 Mention 」\n › Type: Fake Sticker♪\n'
    mention = '@IYUS_SELF™\n'
    no = 0
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*140:(point+1)*140]:
            no += 1
            result += ' %i. %s' % (no, mention)
            slen = len(result) - 12
            elen = len(result) + 3
            mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
            if mid == mids[-1]:
                result += ''
        if result:
            maxbots.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees}),'STKPKGID':spkg,"STKID":sid,'STKVER':sver}, 7)
        result = ''
def sendfakecontact(to, datafake, mids=[]):
    if myMid in mids:mids.remove(myMid)    
    if thebos in mids:mids.remove(thebos)    
    parsed_len = len(mids)//140+1
    result = '「 Mention 」\n › Type: Fake Contact♪\n'
    mention = '@IYUS_SELF™\n'
    no = 0
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*140:(point+1)*140]:
            no += 1
            result += ' %i. %s' % (no, mention)
            slen = len(result) - 12
            elen = len(result) + 3
            mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
            if mid == mids[-1]:
                result += ''
        if result:
            maxbots.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees}),'mid': datafake}, 13)
        result = ''
def clpro(to, type, text):
    if len(settings[type]) > 0:
        rahman(to, f"「 Protect 」\n › Type: Clear {text}♪\n    • Group: {len(settings[type])}\n    • Status: Success")
        settings[type].clear()
    else:
        rahman(to, f"「 Protect 」\n › Type: Clear {text}♪\n    • Status: Nothing")
def plist(to, type, text1, text2):
    ma = ""
    a = 0
    for x in settings[type]:
        a = a + 1
        end = '\n'
        ma += "    • " + str(a) + ". " +maxbots.getChats([x]).chats[0].chatName+ "\n"
    blek = "「 Protect 」"
    blek += f"\n › {text1}♪"
    blek += f"\n{ma}"
    blek += "\n\n › Command"
    blek += f"\n    • {text2} ‹On/Off›"
    blek += f"\n    • {text2} Del ‹Num›"
    blek += f"\n    • {text2} Clear"
    rahman(to, blek)  
def banningD(to, type, text):
    group = maxbots.getChats([to]).chats[0]
    lists = []
    for tag in position[type]:
        lists+=filter(lambda str: str == tag, group.extra.groupExtra.memberMids)                
    if lists == []:
        rahman(to,f"「 Banning 」\n › Type: {text} Detect♪ \n    • Status: Not Found")
        return                                
    if len(lists) > 0: 
        h = [a for a in lists]
        k = len(h)//20                
        for aa in range(k+1):
            if aa == 0:dd = f'「 Banning 」\n › Type: {text} Detect♪';no=aa
            else:dd = '';no=aa*20
            msgas = dd
            for a in h[aa*20:(aa+1)*20]:
                no+=1
                if no == len(h):msgas+='\n    • {}.@!\n'.format(no)
                else:msgas += '\n    • {}. @!'.format(no)
            maxbots.sendTag(to, msgas, h[aa*20:(aa+1)*20])     
def appbanning(aping, type, text1):
    ktl = maxbots.getChats([aping]).chats[0]
    mem = ktl.extra.groupExtra.memberMids
    member = [member for member in mem]
    for x in member:
        if x not in position[type] and x not in myMid:
            time.sleep(0.2)
            position[type].append(x)
    rahman(aping, f"「 Banning 」\n › Type: {text1} Add Here♪ \n    • Status: Success")
def rembanning(to, type, text):
    group = maxbots.getChats([to]).chats[0]
    lists = []
    for tag in position[type]:
        lists+=filter(lambda str: str == tag, group.extra.groupExtra.memberMids)                
    if lists == []:
        rahman(to,f"「 Banning 」\n › Type: {text} Del Here♪ \n    • Status: Not Found")
        return                                
    for xx in lists:
        position[type].remove(xx)
    if len(lists) > 0: 
        h = [a for a in lists]
        k = len(h)//20                
        for aa in range(k+1):
            if aa == 0:dd = f'「 Banning 」\n › Type: {text} Del Here♪';no=aa
            else:dd = '';no=aa*20
            msgas = dd
            for a in h[aa*20:(aa+1)*20]:
                no+=1
                if no == len(h):msgas+='\n    • {}.@! Del♪\n'.format(no)
                else:msgas += '\n    • {}. @! Del♪'.format(no)
            maxbots.sendTag(to, msgas, h[aa*20:(aa+1)*20])     
def friendGet(aping):
    teman = maxbots.getAllContactIds()
    target = []
    for sahabat in teman:
        con = maxbots.getContact(sahabat)
        for nama in aping.split(","):
            if con.displayNameOverridden is not None:
                if nama in con.displayNameOverridden:
                    target.append(con.mid)
            else:
                if nama in con.displayName.lower():
                     target.append(con.mid)
    return target
def memberGet(to, aping):
    ktl = maxbots.getChats([to])
    target = []
    for mmk in ktl.chats[0].extra.groupExtra.memberMids:
        con = maxbots.getContact(mmk)
        for nama in aping.split(","):
            if nama in con.statusMessage.lower():
                target.append(con.mid)
            else:
                if con.displayNameOverridden is not None:
                    if nama in con.displayNameOverridden:
                        target.append(con.mid)
                else:
                    if nama in con.displayName.lower():
                        target.append(con.mid)
    return target
def pendingGet(to, aping):
    ktl = maxbots.getChats([to])
    target = []
    for mmk in ktl.chats[0].extra.groupExtra.inviteeMids:
        con = maxbots.getContact(mmk)
        for nama in aping.split(","):
            if nama in con.statusMessage.lower():
                target.append(con.mid)
            else:
                if con.displayNameOverridden is not None:
                    if nama in con.displayNameOverridden:
                        target.append(con.mid)
                else:
                    if nama in con.displayName.lower():
                        target.append(con.mid)
    return target
def purgeJS(aping):
    ktl = maxbots.getChats([aping]).chats[0]
    target = []
    targets = []
    for mmks in position['blacklist']:
        target+=filter(lambda str: str == mmks, ktl.extra.groupExtra.memberMids)
    for mmks in position['blacklist']:
        targets+=filter(lambda str: str == mmks, ktl.extra.groupExtra.inviteeMids)
    canceledJS(aping, targets)    
    kickedJS(aping, target)
def purgePY(aping):
    ktl = maxbots.getChats([aping]).chats[0]
    target = []
    targets = []
    for mmks in position['blacklist']:
        target+=filter(lambda str: str == mmks, ktl.extra.groupExtra.memberMids)
    for mmks in position['blacklist']:
        targets+=filter(lambda str: str == mmks, ktl.extra.groupExtra.inviteeMids)
    for x in targets:
        time.sleep(0.4)
        canceled(aping, x)    
    for x in target:
        time.sleep(0.4)
        kicked(aping, x)

def bypassJS(aping):
    ktl = maxbots.getChats([aping]).chats[0]
    if ktl.extra.groupExtra.inviteeMids == None:pends = []
    else:pends = ktl.extra.groupExtra.inviteeMids
    pending = []
    for x in pends:
        if x not in position["whitelist"] and x not in position["admin"] and x not in myMid:pending.append(x)
    member = []
    for x in ktl.extra.groupExtra.memberMids:
        if x not in position["whitelist"] and x not in position["admin"] and x not in myMid:member.append(x)
    cm = 'kickall.js gid={} type=dual token={} {}'.format(aping, maxbots.authToken, appNameJs)
    for x in pending:
        cm += ' uik={}'.format(x)
        position["today"]["cancel"] += 1
    for x in member:
        cm += ' uid={}'.format(x)
        position["today"]["kick"] += 1
    success = execute_js(cm)
    return success    
def kickallJS(aping):
    ktl = maxbots.getChats([aping]).chats[0];member = []
    for x in ktl.extra.groupExtra.memberMids:
        if x not in position["whitelist"] and x not in position["admin"] and x not in myMid:member.append(x)
    cm = 'kickall.js gid={} type=dual token={} {}'.format(aping, maxbots.authToken, appNameJs)
    for x in member:
        cm += ' uid={}'.format(x)
        position["today"]["kick"] += 1
    success = execute_js(cm)
    return success
def kickallPY(aping):
    ktl = maxbots.getChats([aping]).chats[0]
    mem = ktl.extra.groupExtra.memberMids
    member = [member for member in mem]
    for x in member:
        if x not in position["whitelist"] and x not in position["admin"] and x not in myMid:
            time.sleep(0.4)
            kicked(aping, x)
def cancelallJS(aping):
    ktl = maxbots.getChats([aping]).chats[0]
    if ktl.extra.groupExtra.inviteeMids == None:
        pends = []
    else:
        pends = ktl.extra.groupExtra.inviteeMids
    pending = []
    for x in pends:
        if x not in position["whitelist"] and x not in position["admin"] and x not in myMid:pending.append(x)
    for x in pending:
        time.sleep(0.5)
        canceled(aping, x)

def coronaNotemp():
    data = apiJG.corona()
    blek = " 「 Corona 」"
    blek += "\n › World"
    blek += f'\n    • Case: {data["result"]["world"]["case"]}'
    blek += f'\n    • Fit: {data["result"]["world"]["fit"]}'
    blek += f'\n    • Rip: {data["result"]["world"]["rip"]}'
    blek += "\n\n › Indonesia"
    blek += f'\n    • Case: {data["result"]["indonesia"]["case"]}'
    blek += f'\n    • Fit: {data["result"]["indonesia"]["fit"]}'
    blek += f'\n    • Rip: {data["result"]["indonesia"]["rip"]}'
    return blek
def coroNa(to):
    if settings["stattemp"] == True:
        data = apiJG.corona()
        case1 = data["result"]["world"]["case"]
        rip1 = data["result"]["world"]["rip"]
        fit1 = data["result"]["world"]["fit"]
        case2 = data["result"]["indonesia"]["case"]
        rip2 = data["result"]["indonesia"]["rip"]
        fit2 = data["result"]["indonesia"]["fit"]
        result = flexklr.kaleraCorona(case1, rip1, fit1, case2, rip2, fit2)
        sendTemplate(to,{"type": "flex", "altText": "Top News", "contents": {"type": "carousel", "contents": [result]}})          
    else:
        rahman(to, coronaNotemp())       
def gemPa(to):
    data = apiJG.bmkg()
    rahmanp(to, data["result"]["skema"])
    blek = "「 Gempa 」"
    blek += "\n › Info Gempa BMKG "
    blek += f'\n    • Tanggal: {data["result"]["tanggal"]}'
    blek += f'\n    • Jam: {data["result"]["pukul"]}'
    blek += f'\n    • Lokasi: {data["result"]["lokasi"]}'
    blek += f'\n    • Wilayah: {data["result"]["wilayah"]}'
    blek += f'\n    • Kordinat: {data["result"]["kordinat"]}'
    blek += f'\n    • Kedalaman: {data["result"]["kedalaman"]}'
    blek += f'\n    • Kekuatan: {data["result"]["kekuatan"]}'
    rahman(to, blek)
def hENTAI(to):
    data = json.loads(requests.get("https://mnazria.herokuapp.com/api/picanime?list=lewd").text)
    rahmanp(to, data["gambar"])                      
def pANTUN(to):
    data = json.loads(requests.get(f"https://api.vhtear.com/random_pantun&apikey={apiVH}").text)
    maxbots.sendMessage(to, data["result"]["pantun"])                  
def pUISI(to):
    data = f"https://api.vhtear.com/puisi_image&apikey={apiVH}"
    rahmanp(to, data)                        
def qEN(to):
    data = json.loads(requests.get("https://ibalapi.herokuapp.com/api/quotes").text)
    maxbots.sendMessage(to, data["result"]["quote"])              
def qID(to):
    data = json.loads(requests.get(f"https://api.vhtear.com/quoteid&apikey={apiVH}").text)
    maxbots.sendMessage(to, data["result"]["kata"])                  
def tRIBUN(to):
    data = json.loads(requests.get("https://ibalapi.herokuapp.com/api/tribunnews").text)
    blek = "「 Tribun News 」"
    blek += "\n › Info"
    blek += f'\n    • Title: {data["result"][0]["title"]}'
    blek += f'\n    • Url: {data["result"][0]["url"]}'
    blek += f'\n    • Title: {data["result"][1]["title"]}'
    blek += f'\n    • Url: {data["result"][1]["url"]}'
    blek += f'\n    • Title: {data["result"][2]["title"]}'
    blek += f'\n    • Url: {data["result"][2]["url"]}'
    maxbots.sendMessage(to, blek)
def ytbNotemp(search):
    data = apiJG.youtube(search)
    blek = " 「 Yotube 」"
    blek += "\n › Search"
    blek += f'\n    • Title: {data["result"]["title"]}'
    blek += f'\n    • Author: {data["result"]["author"]}'
    blek += f'\n    • Duration: {data["result"]["duration"]}'
    blek += '\n    • Watched: {}'.format(formatNumber(data["result"]["watched"])) 
    return blek         
def ytb(to, search):
    data = apiJG.youtube(search)
    author = data["result"]["author"]
    duration = data["result"]["duration"]
    thumbnail = data["result"]["thumbnail"]
    title = data["result"]["title"]
    watched = formatNumber(data["result"]["watched"])
    audio = data["result"]["audioUrl"]
    vid = data["result"]["videoUrl"]
    result = flexklr.kaleraYtb(author, duration, thumbnail, title, watched)
    if settings["stattemp"] == True:
        sendTemplate(to,{"type": "flex", "altText": title, "contents": {"type": "carousel", "contents": [result]}})              
    else:
        rahman(to, ytbNotemp(search))               
    sendTemplate(to, {"type": "video", "originalContentUrl": mrt2(vid), "previewImageUrl": thumbnail})    
    sendFooterAudio(to, audio)
def ytbmp4(to, search):
    data = apiJG.youtube(search)
    thumbnail = data["result"]["thumbnail"]
    vid = data["result"]["videoUrl"]
    sendTemplate(to, {"type": "video", "originalContentUrl": mrt2(vid), "previewImageUrl": thumbnail})            
def ytbmp3(to, search):
    data = apiJG.youtube(search)
    audio = data["result"]["audioUrl"]
    sendFooterAudio(to, audio)
def igtemp(username):
    userid = username
    apiKey = requests.get("https://fgmid.xyz/apibe_fgm.php").text
    headers = {"apiKey": apiKey}
    data = apiJG.instagram(userid)
    vh = requests.get('https://api.vhtear.com/igprofile?query={}&apikey={}'.format(userid,apiVH))

    try:
        datavh = vh.json()
    except Exception as e:
        return 'Not Found♪'

    uservh = datavh["result"]
    user = data['result']
    username = user['username']
    biography = user['biography'] if user['biography'] else ' '
    posts = uservh["post_count"]
    followers = user['follower']
    following = user['following']
    full_name = user['fullname'] if user['fullname'] else username
    profile_pic = user['picture']
    profile_pic_hd = user['profile']
    filler = {'type':'filler'}
    link = user['website']
    verified = user['verified']
    flex = {'type':'flex','altText':username,'contents':{'type':'bubble','header':{'type':'box','layout':'horizontal','paddingAll':'10px','contents':[{'type':'box','layout':'vertical','contents':[{'type':'image','url':'https://pluspng.com/img-png/instagram-png-instagram-png-logo-1455.png','size':'full'}],'width':'25px'},{'type':'text','text':username,'gravity':'center','size':'lg','align':'center','weight':'bold'}]},'body':{'type':'box','layout':'vertical','paddingAll':'10px','contents':[{'type':'box','layout':'horizontal','contents':[{'type':'box','layout':'vertical','contents':[{'type':'image','url':profile_pic,'size':'full','aspectMode':'cover'}],'cornerRadius':'100px','width':'70px','action':{'type':'uri','label':'action','uri':'line://app/1584968724-qzg0aR95?auto=yes&type=image&downloadUrl={0}&previewUrl={0}'.format(profile_pic_hd),'altUri':{'desktop':profile_pic_hd}}},{'type':'box','layout':'vertical','contents':[filler,{'type':'text','text':formatNumber(posts),'align':'center','weight':'bold','size':'sm'},{'type':'text','text':'Posts','align':'center','size':'sm'},filler ]},{'type':'box','layout':'vertical','contents':[filler,{'type':'text','text':formatNumber(followers),'align':'center','weight':'bold','size':'sm'},{'type':'text','text':'Followers','align':'center','size':'sm'},filler ]},{'type':'box','layout':'vertical','contents':[filler,{'type':'text','text':formatNumber(following),'align':'center','weight':'bold','size':'sm'},{'type':'text','text':'Following','align':'center','size':'sm'},filler ]}],'spacing':'sm'},{'type':'text','text':full_name,'weight':'bold','margin':'md','size':'sm'},{'type':'text','text':biography,'margin':'md','size':'sm','wrap':True,'maxLines':3 },{'type':'box','layout':'horizontal','contents':[{'type':'text','text':'Follow','color':'#ffffff','gravity':'center','align':'center','weight':'bold'}],'backgroundColor':'#0097e6','margin':'md','height':'30px','cornerRadius':'3px','action':{'type':'uri','label':'action','uri':'https://www.instagram.com/'+username}}]}}}
    if link:
        flex['contents']['body']['contents'].insert(3, {'type':'text','text':link,'size':'sm','wrap':True,'weight':'bold','color':'#0097e6','action':{'type':'uri','label':'action','uri':link}})
    if verified:
        flex['contents']['header']['contents'].append({'type':'box','layout':'vertical','contents':[{'type':'image','url':'https://sczit.xyz/cdnbase/vefired_icon.png','size':'full'}],'width':'25px'})
    if len(uservh['post_picture']) != 0:

        feeds_media = []
        for pict, url in zip(uservh['post_picture'][:6], uservh['post_url'][:6]):
            feeds_media.append({"image":pict, "url":url})

        feeds_media += [filler for _ in range(6-len(feeds_media))]
        feeds_content = {'type':'box','layout':'vertical','spacing':'xs','margin':'md','cornerRadius':'3px','height':'185px','contents':[]}
        parsed_len = len(feeds_media)//3+1
        for point in range(parsed_len):
            contents = {'type':'box','layout':'horizontal','spacing':'xs','contents':[]}
            for feed in feeds_media[point*3:(point+1)*3]:
                if feed == filler:
                    contents['contents'].append(feed)
                else:
                    contents['contents'].append({'type':'image','url':feed['image'],'size':'full','aspectMode':'cover','action':{'type':'uri','label':'action','uri':feed['url']}})
            if contents['contents']:
                feeds_content['contents'].append(contents)
    else:
        feeds_content = {'type':'box','layout':'vertical','spacing':'xs','margin':'md','cornerRadius':'3px','height':'185px','contents':[filler,{'type':'image','url':'https://icon-library.net/images/black-camera-icon/black-camera-icon-3.jpg','size':'xxs'},{'type':'text','text':'No Posts Yet','align':'center','size':'lg'},filler]}
    flex['contents']['body']['contents'].append(feeds_content)
    return flex
def instagramP(to, search):
    data = apiJG.instagram(search)
    blek = "「 Instagram 」"
    blek += "\n › Profile"
    blek += f"\n    • Name: {data['result']['fullname']}"
    blek += f"\n    • Username: {data['result']['username']}"
    blek += f"\n    • Bio: {data['result']['biography']}"
    blek += f"\n    • Website: {data['result']['website']}"
    blek += f"\n    • Private: {data['result']['private']}"
    blek += f"\n    • Verified: {data['result']['verified']}"
    blek += "\n    • Followers: {}".format(data['result']['follower'])
    blek += "\n    • Following: {}".format(data['result']['following'])
    blek += f"\n    • Post: {data['result']['post']}"
    blek += f"\n    • Link: https://www.instagram.com/{data['result']['username']}"
    if settings["stattemp"] == True:
        sendTemplate(to, igtemp(search))
    else:
        rahmanp(to, str(data["result"]["picture"]))
        rahman(to, str(blek))
def igstry(to, search):
    data = apiJG.instastory(search)
    name = data["result"]["username"]
    img = data["result"]["picture"]
    for x in data["result"]["stories"]:
        if x["type"] == "video":
            result = {"type": "video", "originalContentUrl": mrt2(x["url"]), "previewImageUrl": x["thumbnail"]}
            if settings["stattemp"] == True:
                sendTemplate(to, result)
            else:
                 if settings["statfooter"] == True:
                     sendTemplate(to, result)
                 else:
                     time.sleep(0.2)
                     rahmanv(to, x["url"])
        else:
            resultt = {"type": "image", "originalContentUrl": x["url"], "previewImageUrl": x["url"], "sentBy": {"label": name, "iconUrl": img, "linkUrl": "https://instagram.com/{}?utm_medium=copy_link".format(name)}}        
            if settings["stattemp"] == True:
                sendTemplate(to, resultt)
            else:
                if settings["statfooter"] == True:
                    sendTemplate(to, resultt)
                else:
                    time.sleep(0.2)
                    rahmanp(to, x["url"])                                 
def tiktokP(to, search):
    data = json.loads(requests.get(f"https://api.vhtear.com/tiktokprofile?query={search}&apikey={apiVH}").text)        
    profile_pic = str(data['result']['picture'])
    nickname = str(data['result']['title'])
    likes = str(data['result']['like_count'])
    followers = str(data['result']['follower'])
    following = str(data['result']['follow'])
    username = str(data['result']['username'])
    result = flexklr.kaleraTiktok(profile_pic, nickname, likes, followers, following, username)
    blek = "「 Tiktok 」"
    blek += "\n › Profile"
    blek += f"\n    • Name: {nickname}"
    blek += f"\n    • Username: {username}"
    blek += f"\n    • Bio: {data['result']['bio']}"
    blek += f"\n    • Description: {data['result']['description']}"
    blek += "\n    • Followers: {}".format(formatNumber(followers))
    blek += "\n    • Following: {}".format(formatNumber(following))
    blek += f"\n    • Post: {data['result']['video_post']}"
    blek += "\n    • Like: {}".format(formatNumber(likes))
    blek += f"\n    • Private: {data['result']['verified']}"
    blek += f"\n    • Link: {data['result']['url_account']}"
    sendMedias2(to, result, blek, profile_pic)          
def twitterP(to, search):
    data = apiJG.twitter(search)
    profile_pic = data["result"]["avatar"]
    fullname = data["result"]["fullname"]
    if fullname == "" or fullname is None:
        fullname = data["result"]["username"]
    bio = data["result"]["biography"]
    followers = formatNumber(data["result"]["follower"])
    following = formatNumber(data["result"]["following"])
    link = data["result"]["username"]
    banner = data["result"]["banner"]
    joined = data["result"]["tweet"]    
    blek = "「 Twitter 」"
    blek += "\n › Profile"
    blek += f"\n    • Name: {data['result']['fullname']}"
    blek += f"\n    • Username: {data['result']['username']}"
    blek += f"\n    • Bio: {data['result']['biography']}"
    blek += f"\n    • Tweet: {data['result']['tweet']}"
    blek += "\n    • Followers: {}".format(formatNumber(data['result']['follower']))
    blek += "\n    • Following: {}".format(formatNumber(data['result']['following']))
    blek += f"\n    • Link: https://www.twitter.com/{link}"
    result = flexklr.kaleraTwitter(profile_pic, fullname, bio, followers, following, link, banner)
    sendMedias2(to, result, blek, profile_pic)          
def githubP(to, search):
    data = apiJG.github(search)
    avatar = data["result"]["avatar"]
    fullname = data["result"]["fullname"]
    if fullname == "" or fullname is None:
        fullname = data["result"]["username"]
    biography = data["result"]["bio"]
    repo = data["result"]["repositories"]
    followers = data["result"]["followers"]
    following = data["result"]["following"]
    type = data["result"]["type"]
    blog = data["result"]["blog"]
    emaill = data["result"]["email"]
    company = data["result"]["company"]
    crt = data["result"]["created_at"]
    updt = data["result"]["updated_at"]
    loc = data["result"]["location"]
    blek = "「 Github 」"
    blek += "\n › Profile"
    blek += f"\n    • Name: {fullname}"
    blek += f"\n    • Username: {data['result']['username']}"
    blek += f"\n    • Bio: {biography}"
    blek += f"\n    • Blog: {blog}"
    blek += f"\n    • Email: {emaill}"
    blek += f"\n    • Company: {company}"
    blek += f"\n    • Created: {crt}"
    blek += f"\n    • Updated: {updt}"
    blek += f"\n    • Location: {loc}"
    blek += f"\n    • Repositories: {repo}"        
    blek += f"\n    • Follower: {followers}"
    blek += f"\n    • Following: {following}"
    blek += f"\n    • Link: https://github.com/{fullname}"
    result = flexklr.kaleraGithub(fullname, biography, repo, followers, following, avatar)
    sendMedias2(to, result, blek, avatar)      
def pint(to, search):
    data = json.loads(requests.get(f"https://api.vhtear.com/pinterest?query={search}&apikey={apiVH}").text)
    time.sleep(0.4)
    for xx in data["result"]:
        rahmanp(to, xx)        
def porn(to, search):
    data = apiJG.porn(search)
    pict = data["result"]["thumbnail"]
    title = data["result"]["title"].title()
    duration = data["result"]["duration"]
    quality = data["result"]["quality"]
    watched = data["result"]["watched"]
    vids = data["result"]["videoUrl"]
    blek = "「 Porn 」"
    blek += "\n › 18+"
    blek += f"\n    • Title: {title}"
    blek += f"\n    • Duration: {duration}"
    blek += f"\n    • Quality: {quality}"
    blek += f"\n    • Watched: {watched}"
    result = flexklr.kaleraPorn(pict, title, duration, quality, watched, vids)
    sendMedias(to, result, blek)       
    sendTemplate(to, {"type": "video", "originalContentUrl": mrt2(vids), "previewImageUrl": pict})            
def downloadPornhub(to, search):
    r = requests.get(f'https://blay.herokuapp.com/pornhub_search?q={search}')
    data = r .json()
    for a in data['result']:
        r = requests.get(f'https://blay.herokuapp.com/pornhub_dl?url={a["url"]}')
        data = r.json()
        video = data['formats'][-1]['video_url']
        thumbs = data['thumbnail']
        sendTemplate(to, {"type": "video", "originalContentUrl": mrt2(video), "previewImageUrl": thumbs})            
def jooX(to, search):
    data = apiJG.joox(search)
    audio = data["result"]["mp3Url"]
    artist = data["result"]["singer"]
    duration = data["result"]["duration"]
    thumbnail = data["result"]["thumbnail"]
    title = data["result"]["title"]
    blek = "「 Joox 」"
    blek += "\n › Music"
    blek += f"\n    • Singer: {artist}"
    blek += f"\n    • Title: {title}"
    blek += f"\n    • Duration : {duration}"
    result = flexklr.kaleraJoox(artist, duration, thumbnail, title)
    sendMedias(to, result, blek)     
    rahmana(to, audio)
def gglSearch(to, searchh):
    data = apiJG.search(searchh)
    blek = "「 Google 」"
    blek += "\n › Search"
    blek += f'\n    • Title: {data["result"][0]["title"]}'
    blek += f'\n    • Url: {data["result"][0]["url"]}'
    blek += f'\n    • Title: {data["result"][1]["title"]}'
    blek += f'\n    • Url: {data["result"][1]["url"]}'
    blek += f'\n    • Title: {data["result"][2]["title"]}'
    blek += f'\n    • Url: {data["result"][2]["url"]}'
    maxbots.sendMessage(to, blek)
def imageSearch(to, search):
    data = apiJG.image(search)
    time.sleep(0.4)
    rahmanp(to, data["result"][0])
    rahmanp(to, data["result"][1])
    rahmanp(to, data["result"][2])          
def brainlY(to, search):
    data = json.loads(requests.get(f"https://api.vhtear.com/branly?query={search}&apikey={apiVH}").text)
    desc = data["result"]["data"]
    blek = "「 Brainly 」"
    blek += "\n › Search"
    blek += '\n    • Title: {}'.format(search.title())
    blek += f'\n    • Answer: \n{desc}'
    maxbots.sendMessage(to, blek)
def kBBI(to, search):
    data = apiJG.kbbi(search)
    desc = data["result"]["desc"]
    blek = "「 KBBI 」"
    blek += "\n › Search"
    blek += '\n    • Title: {}'.format(search.title())
    blek += f'\n    • Answer: \n{desc}'
    maxbots.sendMessage(to, blek)  
def wikip(to, search):
    data = apiJG.wikipedia(search)
    desc = data["result"]
    blek = "「 Wikipedia 」"
    blek += "\n › Search"
    blek += '\n    • Title: {}'.format(search.title())
    blek += f'\n    • Answer: \n{desc}'
    maxbots.sendMessage(to, blek)  
def artiN(to, search):
    data = apiJG.nama(search)
    query = data["result"]["name"]
    karakter = data["result"]["definition"]
    deskripsi = data["result"]["description"]
    blek = "「 Arti 」"
    blek += "\n › Nama"
    blek += f'\n    • Nama: {query.title()}'
    blek += f'\n    • Karakter: {karakter}'
    blek += f'\n    • Desc: {deskripsi}'
    maxbots.sendMessage(to, blek)  
def artiM(to, search):
    data = apiJG.mimpi(search)
    mimpi = data["result"][0]['dream']
    artimimpi = data["result"][0]['meaning']   
    blek = "「 Arti 」"
    blek += "\n › Mimpi"
    blek += f'\n    • Mimpi: {mimpi.title()}'
    blek += f'\n    • Arti: {artimimpi}'
    maxbots.sendMessage(to, blek)
def adzaN(to, search):
    data = apiJG.adzan(search)
    waktu = data["result"]["tanggal"]
    city = data["result"]["wilayah"]
    imsyak = data["result"]["adzan"]["imsyak"]
    subuh = data["result"]["adzan"]["subuh"]
    terbit = data["result"]["adzan"]["terbit"]
    dhuha = data["result"]["adzan"]["dhuha"]
    dzuhur = data["result"]["adzan"]["dzuhur"]
    ashar = data["result"]["adzan"]["ashar"]
    maghrib = data["result"]["adzan"]["maghrib"]
    isya = data["result"]["adzan"]["isya"]
    blek = "「 Adzan 」"
    blek += f"\n › {city.title()}"    
    blek += f'\n    • Tanggal: {waktu}'
    blek += f'\n    • Imsyak: {imsyak}'
    blek += f'\n    • Terbit: {terbit}'
    blek += f'\n    • Subuh: {subuh}'
    blek += f'\n    • Dhuha: {dhuha}'
    blek += f'\n    • Dzuhur: {dzuhur}'
    blek += f'\n    • Ashar: {ashar}'
    blek += f'\n    • Maghrib: {maghrib}'
    blek += f'\n    • Isya: {isya}'
    result = flexklr.kaleraAdzan(waktu, city, imsyak, subuh, terbit, dhuha, dzuhur, ashar, maghrib, isya)
    sendMedias(to, result, blek)            
def zodiaC(to, search):
    data = apiJG.zodiac(search)
    dateRange = data["result"]["date"]
    sign = data["result"]["zodiac"]
    imageUrl = data["result"]["image"]
    kecocokan = data['result']['couple']
    waktuH = data['result']['time']
    warnaH = data['result']['color']
    nomorH = data['result']['number']
    umum = data['result']['public']
    aJomblo = data['result']['love']['single']
    aPasangan = data['result']['love']['couple']
    keuangan = data['result']['money']
    desc = f"Kecocokan : {kecocokan}"
    desc += f"\nWaktu Hoki : {waktuH}"
    desc += f"\nWarna Hoki : {warnaH}"
    desc += f"\nNomor Hoki : {nomorH}"
    desc += f"\n\nUmum : {umum}"
    desc += f"\n\nAsmara Jomblo : {aJomblo}"
    desc += f"\n\nAsmara Pasangan : {aPasangan}"
    desc += f"\n\nKeuangan : {keuangan}"
    blek = "「 Zodiac 」"
    blek += f"\n › {sign.title()}"    
    blek += f'\n    • Date: {dateRange}'
    blek += f'\n    • Kecocokan: {kecocokan}'
    blek += f'\n    • Waktu Hoki: {waktuH}'
    blek += f'\n    • Warna Hoki: {warnaH}'
    blek += f'\n    • Nomor Hoki: {nomorH}'
    blek += f'\n    • Umum: {umum}'
    blek += f'\n    • Asmara Jomblo: {aJomblo}'
    blek += f'\n    • Asmara Pasangan: {aPasangan}'
    blek += f'\n    • Keuangan: {keuangan}'
    result = flexklr.kaleraZodiac(dateRange, sign, imageUrl, desc)
    sendMedias(to, result, blek)     
def cuacA(to, search):
    data = apiJG.cuaca(search)
    place = data["result"]["location"]
    weather = data["result"]["description"]
    temperature = data["result"]["temperature"]
    humidity = data["result"]["humidity"]
    wind = data["result"]["wind"]
    result = flexklr.kaleraCuaca(place, weather, temperature, humidity, wind)
    blek = "「 Cuaca 」"
    blek += f"\n › {place.title()}"    
    blek += f'\n    • Cuaca: {weather}'
    blek += f'\n    • Suhu: {temperature}'
    blek += f'\n    • Angin: {wind}'
    blek += f'\n    • Kelembapan: {humidity}'
    sendMedias(to, result, blek)     
def lyriC(to, search):
    data = apiJG.lyric(search)
    title = data["result"]["title"]
    artis = data["result"]["artist"]
    lyric = data["result"]["lyric"]    
    blek = "「 Lyric 」"
    blek += f"\n › {artis.title()}"    
    blek += f'\n    • Title: {title}'
    blek += f'\n    • Lyric: \n{lyric}'
    maxbots.sendMessage(to, blek)  
def chorD(to, search):
    data = json.loads(requests.get(f"https://api.vhtear.com/chordguitar?query={search}&apikey={apiVH}").text)          
    chord = data['result']['result']
    blek = "「 Chord Gitar 」"
    blek += f"\n › {search.title()}"    
    blek += f'\n    • Chord: \n{chord}'
    maxbots.sendMessage(to, blek)  
def igPost(to, blek):
    try:
        data = apiJG.instapost(blek)
        username = data["result"]["username"]
        link = f"https://www.instagram.com/{username}"
        pict = data["result"]["picture"]
        number = 0                           
        for ajg in data["result"]["postData"]:
            number += 1
            if ajg["type"] == "image":
                rslt = {"type": "image", "originalContentUrl": ajg["postUrl"], "previewImageUrl": ajg["postUrl"], "sentBy": {"label": username, "iconUrl": pict, "linkUrl": link}}                                                                    	
                if settings["stattemp"] == True:
                    sendTemplate(to, rslt)
                else:
                    if settings["statfooter"] == True:
                        sendTemplate(to, rslt)
                    else:
                        rahmanp(to, ajg["postUrl"])
            if ajg["type"] == "video":
                sendTemplate(to, {"type": "video", "originalContentUrl": mrt2(ajg["postUrl"]), "previewImageUrl": ajg["poster"]})                                   
    except:pass
def ttPost(to, blek):
    try:
        try:
            result = apiBE.tiktokPostV2(blek)            
            sendTemplate(to, {"type": "video", "originalContentUrl": mrt2(result['result']['download']), "previewImageUrl": result['result']['preview']})                   
        except Exception as e:
            result = apiBE.tiktokPost(blek)
            maxbots.sendVideoWithURL(to, result['result']['aweme_detail']['video']['play_addr']['url_list'][0])                              
    except:pass
def trPost(to, blek):
    try:
        req = requests.get(f"https://api.vhtear.com/twitter?link={blek}&apikey={apiVH}")
        mmk = json.loads(req.text) 
        maxbots.sendVideoWithURL(to, mmk['result']['urlVideo'])
    except:pass
def tlPost(to, blek):
    try:
        data = apiJG.timeline(blek)
        name = data["result"]["displayName"]
        pict = data["result"]["pictureUrl"] 
        if data["result"]["timeline"] != []:
            number = 0
            for ajg in data["result"]["timeline"]:
                number += 1
                if ajg["type"] == "image":
                    rslt = {"type": "image", "originalContentUrl": ajg["url"], "previewImageUrl": ajg["url"], "sentBy": {"label": username, "iconUrl": pict, "linkUrl": ajg["url"]}}                                                                    	
                    if settings["stattemp"] == True:
                        sendTemplate(to, rslt)
                    else:
                        if settings["statfooter"] == True:
                            sendTemplate(to, rslt)
                        else:
                            rahmanp(to, ajg["url"])
                if ajg["type"] == "video":
                    sendTemplate(to, {"type": "video", "originalContentUrl": mrt2(ajg["url"]), "previewImageUrl": ajg["thumbnail"]})                                    
    except:pass
def smuleDl(to,link):
    data = apiJG.smuledl(link)
    res = "SMULE DOWNLOADED\nTitle: {}".format(data["result"]["title"])
    res += "\nType: {}".format(data["result"]["type"])
    res += "\n\nCaption: {}".format(data["result"]["caption"])
    maxbots.sendMessage(to,res)
    if data["result"]["type"] == "video":
        sendTemplate(to, {"type": "video", "originalContentUrl": mrt2(data["result"]["mp4Url"]), "previewImageUrl": data["result"]["thumbnail"]})    
    sendFooterAudio(to, data["result"]["mp3Url"])
def ytbPost(to, blek):
    data = apiJG.youtubedl(blek)
    sendTemplate(to, {"type": "video", "originalContentUrl": mrt2(data["result"]["videoUrl"]), "previewImageUrl": data["result"]["thumbnail"]})    
    sendFooterAudio(to, data["result"]["audioUrl"])   
def pinPost(to, blek):
    try:
        data = apiJG.pinterest(blek)
        for x in data["result"]:
            if x["type"] == "mp4":
                maxbots.sendVideoWithURL(to, x["url"])
            if x["type"] == "gif":
                maxbots.sendGift(to, x["url"])
            if x["type"] == "jpg":
                maxbots.sendImageWithURL(to, x["url"])
    except:pass                         
def maker1(to, type, mkr):
    path = f"https://api.vhtear.com/{type}?text={mkr}&apikey={apiVH}"
    maxbots.sendImageWithURL(to, path)                                   
def maker2(to, type, mkr1, mkr2):
    path = f"https://api.vhtear.com/{type}?text1={mkr1}&text2={mkr2}&apikey={apiVH}"
    maxbots.sendImageWithURL(to, path)               
                                    
def timers(secs):
    mins, secs = divmod(secs, 60);hours, mins = divmod(mins, 60);days, hours = divmod(hours, 24);weeks, days = divmod(days, 7);months, weeks = divmod(weeks, 4);text = ""
    if months != 0:text += "%02d Month" % (months)
    if weeks != 0:text += " %02d Week" % (weeks)
    if days != 0:text += " %02d Day" % (days)
    if hours != 0:text += " %02d Hour" % (hours)
    if mins != 0:text += " %02d Min" % (mins)
    if secs != 0:text += " %02d Sec" % (secs)
    if text[0] == " ":text = text[1:]
    return text    

def debugH():
	a = time.time()
	b = maxbots.getProfile()
	c = time.time() - a
	d = time.time() - a
	return "%s ms♪" % (round(c * 1000,2))
def runH():
     runtime = time.time() - programStart
     return '「 Runtime 」\n › Type: Run\n    • Running On: '+ format_timespan(runtime)

def typeList(to, type1, type2):
    no = 0
    arifblek = f"「 List 」\n › Type: {type1}♪\n"
    for ktl in listsett[type2]:
        arifblek += "    • " + ktl.title() + "\n"
    arifblek += " › Total {} {}".format(str(len(listsett[type2])), type1)
    rahman(to, arifblek)

def notif_add(op):
    notifi2(op.param1)    
    if settings['autoAdd']['status']:
        finded(op.param1)                
    if settings['autoAdd']['reply']:
        mentext(op.param1, settings['autoAdd']['message'])
    if settings['emojiautoadd']['status']:
        sendEmo(op.param1, settings['emojiautoadd']['message'], settings['emojiautoadd']['sticons'], "emojiautoadd")
    if settings['responstickeradd']:
        maxbots.sendSticker(op.param1,settings,"stcadd")
def notif_atribut(op):
    if op.param1 in protectqr:
        if maxbots.getChats([op.param1]).chats[0].extra.groupExtra.preventedJoinByTicket == False:
            if op.param2 not in position["whitelist"] and op.param2 not in position["admin"]:
                ngebl(op.param2)
                qrClose(op.param1)   
                kicked(op.param1, op.param2)
    if op.param1 in protectname:
        if op.param2 not in position["whitelist"] and op.param2 not in position["admin"]:
            nama = maxbots.getChats([op.param1]).chats[0].chatName
            if nama != protectname[op.param1]:
                x = maxbots.getChats([op.param1]).chats[0]
                x.chatName = protectname[op.param1]
                maxbots.updateChat(x, 1)    
                kicked(op.param1, op.param2)
                ngebl(op.param2)                 
def notif_join(op):
    if myMid in op.param3:
        notifi(op.param1, op.param2, "Invite")
        position["today"]["invited"] += 1
    if settings['autoLeave']['gc']["status"] and myMid in op.param3:
        if settings['autoLeave']['gc']["msg"]:
            mentext2(op.param1, op.param2, settings['autoLeave']['gc']["message"])           
        if settings['autoLeave']['gc']["stc"]:
            maxbots.sendSticker(op.param1,settings,"stcautoleaveGC")
        leaveed(op.param1)                                                
    if settings['autoJoin']['status'] and myMid in op.param3:
        accepted(op.param1)
        if settings['autoJoin']['reply']:
            mentext2(op.param1, op.param2, settings['autoJoin']['message'])           
        if settings['autojoinsticker']:
            maxbots.sendSticker(op.param1,settings,"stcautojoin")
        if settings['autojoinbypass']:
            bypassJS(op.param1)
        if settings['autojoinkickall']:
            kickallJS(op.param1)
        if settings['autojoinkickallPY']:
            kickallPY(op.param1)
        if settings['autojoincancelall']:
            cancelallJS(op.param1)
        if settings['autojoinkillban']:
            purgeJS(op.param1)           
        if settings['autojoinkillbanPY']:
            purgePY(op.param1)                     
    if settings["purge"]:
      if op.param2 in position["blacklist"]:
        if op.param3 not in position["whitelist"] and op.param2 not in position["bot"] and op.param2 not in position["admin"]:
            tnmbl = op.param3.split('\x1e')
            for x in tnmbl:
                ngebl(x)        
                time.sleep(0.4)
                canceled(op.param1, x)
            kicked(op.param1, op.param2)                   
      if op.param3 in position["blacklist"]:
        if op.param2 not in position["whitelist"] and op.param2 not in position["admin"]:
            tnmbl = op.param3.split('\x1e')
            for x in tnmbl:
                time.sleep(0.4)
                canceled(op.param1, x)
            kicked(op.param1, op.param2)
            ngebl(op.param2)                            
    if op.param1 in protectinvite:
        if op.param2 not in position["whitelist"] and op.param2 not in position["admin"]:
            tnmbl = op.param3.split('\x1e')
            for x in tnmbl:
                ngebl(x)        
                time.sleep(0.4)
                canceled(op.param1, x)
            kicked(op.param1, op.param2)
            ngebl(op.param2)           
    llinviteee = op.param3.split('\x1e')
    for xll in llinviteee:
        ngelastlist(op.param1, "lastinvite", xll)
def notif_leaveMC(op):
    if settings['autoLeave']['mc']["status"] == True:
        if settings['autoLeave']['mc']["msg"]:
            mentext2(op.param1, op.param2, settings['autoLeave']['mc']["message"])           
        if settings['autoLeave']['mc']["stc"]:
            maxbots.sendSticker(op.param1,settings,"stcautoleaveMC")
        maxbots.leaveRoom(op.param1) 
def notif_leaveGC(op):
    if op.param1 not in [a for a in maxbots.getAllChatMids(True, True).memberChatMids]:
        return
    if op.param1 in settings['greet']['leave']['status'] and op.param1 not in position['silent']:
        if op.param1 not in limited["greetlm"]:
            limited["greetlm"][op.param1] = time.time()                    
        if time.time() <= limited["greetlm"][op.param1]:
            pass
        else:
            if settings["stattemp"] == True:
                profile = maxbots.getContact(op.param2)
                username = profile.displayName
                if profile.pictureStatus: picture = "https://obs.line-scdn.net/"+str(profile.pictureStatus)
                else: picture = "https://s20.directupload.net/images/220423/uxdxnp5a.jpg"
                if '@!' in settings['greet']['leave']['message']: message = settings['greet']['leave']['message'].format(name='', gname=maxbots.getChats([op.param1]).chats[0].chatName).replace('@!', profile.displayName)
                else: message = settings['greet']['leave']['message'].format(name='', gname=maxbots.getChats([op.param1]).chats[0].chatName)
                #data = {"type": "bubble", "size": "kilo", "header": {"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": "https://i.ibb.co/Q9FQx3V/perakbiruslow.png", "aspectRatio": "1:3", "aspectMode": "cover", "position": "absolute", "size": "full","animated": True}, {"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": "https://i.ibb.co/jGhB2xR/Moris.png", "aspectMode": "cover", "aspectRatio": "1:3", "size": "full", "animated": True}, {"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": "https://i.ibb.co/vDq3JS1/putar1.png", "size": "full", "aspectMode": "cover", "aspectRatio": "1:1", "animated": True}, {"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": picture, "aspectMode": "cover"}], "position": "absolute", "width": "65px", "height": "65px", "cornerRadius": "100px", "borderWidth": "1px", "borderColor": "#191919", "offsetTop": "2.5px", "offsetStart": "3px"}], "width": "70px", "height": "70px", "position": "absolute", "cornerRadius": "100px", "offsetStart": "2px", "offsetTop": "2px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": username, "size": "14px", "weight": "bold", "color": "#FFFFFF"}], "width": "200px", "height": "17.5px", "position": "absolute", "offsetEnd": "80px", "offsetTop": "22.5px", "justifyContent": "center", "alignItems": "center"}], "paddingAll": "0px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": message, "color": "#fefdfa", "size": "15px", "wrap": True}], "paddingAll": "10px", "backgroundColor": "#191919", "cornerRadius": "0px"}], "paddingTop": "1px","paddingBottom": "2.5px","paddingStart": "2px","paddingEnd": "2px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": "https://i.ibb.co/0GfCjm7/20220520-223702.png", "aspectMode": "cover", "aspectRatio": "9:2", "size": "full", "animated": True}, {"type": "box","layout": "vertical","contents": [{"type": "image","url": "https://i.ibb.co/vDq3JS1/putar1.png","size": "full","aspectMode": "cover","animated": True},{"type": "box","layout": "vertical","contents": [{"type": "image","url": "https://i.ibb.co/DYPLqnV/botjoget.png", "size": "full","aspectMode": "cover","animated": True}],"position": "absolute","width": "62px","height": "62px","offsetBottom": "1.5px","offsetEnd": "1.5px","cornerRadius": "100px"}],"width": "65px","height": "65px","position": "absolute","offsetBottom": "3px","offsetEnd": "3px","cornerRadius": "100px", "borderWidth": "1px", "borderColor": "#191919","backgroundColor": "#000000"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "M O R I S  B O T S", "size": "14px", "align": "center", "color": "#e6c619", "weight": "bold"}], "position": "absolute", "height": "30px", "width": "200px", "justifyContent": "center", "offsetBottom": "22px", "offsetStart": "68px"}], "paddingAll": "0px"}], "paddingAll": "0px"} }
                data = {"type": "bubble", "size": "kilo", "header": {"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": "https://i.ibb.co/Q9FQx3V/perakbiruslow.png", "aspectRatio": "1:3", "aspectMode": "cover", "position": "absolute", "size": "full","animated": True}, {"type": "image", "url": "https://i.ibb.co/Q9FQx3V/perakbiruslow.png", "aspectRatio": "1:3", "aspectMode": "cover", "position": "absolute", "offsetTop": "347.5px", "size": "full","animated": True}, {"type": "image", "url": "https://i.ibb.co/Q9FQx3V/perakbiruslow.png", "aspectRatio": "1:3", "aspectMode": "cover", "position": "absolute", "offsetTop": "647.5px", "size": "full","animated": True}, {"type": "image", "url": "https://i.ibb.co/Q9FQx3V/perakbiruslow.png", "aspectRatio": "1:3", "aspectMode": "cover", "position": "absolute", "offsetTop": "947.5px", "size": "full","animated": True}, {"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": "https://i.ibb.co/jGhB2xR/Moris.png", "aspectMode": "cover", "aspectRatio": "9:2", "size": "full", "animated": True}, {"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": "https://i.ibb.co/vDq3JS1/putar1.png", "size": "full", "aspectMode": "cover", "aspectRatio": "1:1", "animated": True}, {"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": picture, "aspectMode": "cover"}], "position": "absolute", "width": "40px", "height": "40px", "cornerRadius": "100px", "borderWidth": "1px", "borderColor": "#191919", "offsetTop": "3px", "offsetStart": "2.5px"}], "width": "45px", "height": "45px", "position": "absolute", "cornerRadius": "100px", "offsetStart": "3px", "offsetTop": "3px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": username, "size": "12px", "weight": "bold", "color": "#FFFFFF"}], "width": "110px", "height": "17.5px", "position": "absolute", "offsetEnd": "50px", "offsetTop": "13px", "justifyContent": "center", "alignItems": "center"}], "paddingAll": "0px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": message, "color": "#fefdfa", "size": "12px", "wrap": True}], "paddingAll": "4px", "backgroundColor": "#191919", "cornerRadius": "0px"}], "paddingTop": "1px","paddingBottom": "2.5px","paddingStart": "2px","paddingEnd": "2px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": "https://i.ibb.co/0GfCjm7/20220520-223702.png", "aspectMode": "cover", "aspectRatio": "9:2", "size": "full", "animated": True}, {"type": "box","layout": "vertical","contents": [{"type": "image","url": "https://i.ibb.co/vDq3JS1/putar1.png","size": "full","aspectMode": "cover","animated": True},{"type": "box","layout": "vertical","contents": [{"type": "image","url": "https://s20.directupload.net/images/220423/uxdxnp5a.jpg", "size": "full","aspectMode": "cover","animated": True}],"position": "absolute","width": "40px","height": "40px","offsetBottom": "3px","offsetEnd": "2.5px","cornerRadius": "100px"}],"width": "45px","height": "45px","position": "absolute","offsetBottom": "2px","offsetEnd": "1.5px","cornerRadius": "100px","backgroundColor": "#000000"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "M O R I S  B O T S", "size": "12px", "align": "center", "color": "#e6c619", "weight": "bold"}], "position": "absolute", "height": "20px", "width": "120px", "justifyContent": "center", "offsetBottom": "14px", "offsetStart": "45px"}], "paddingAll": "0px"}], "paddingAll": "0px"} }
                sendTemplate(op.param1,{"type": "flex", "altText": settings["footerlabel"], "contents": data})    
                limitGLM[op.param1] = time.time() + 10
            else:
                mentext2(op.param1, op.param2, settings['greet']['leave']['message'].format(name=maxbots.getChats([op.param1]).chats[0].chatName))
                limitGLM[op.param1] = time.time() + 10
    if op.param1 in  settings['greet']['leavestc'] and op.param1 not in position['silent']:
        if op.param1 not in limited["greetls"]:
            limited["greetls"][op.param1] = time.time()                    
        if time.time() <= limited["greetls"][op.param1]:
            pass
        else:
           maxbots.sendSticker2(op.param1,settings, "greet","stcgreetleave")
           limited["greetls"][op.param1] = time.time() + 10
    ngelastlist(op.param1, "lastleave", op.param2)
def notif_kickJoin(op):
  if settings["purge"]:
      for ktl in position["blacklist"]:
          if op.param2 not in position["whitelist"] and op.param2 not in position["admin"]:
              kicked(op.param1, ktl)                      
      else:pass
def notif_joinGC(op):
    if op.param1 not in [a for a in maxbots.getAllChatMids(True, True).memberChatMids]:
        return
    if op.param1 in settings['greet']['join']['status'] and op.param1 not in position['silent']:
        if op.param1 not in limited["greetjm"]:
            limited["greetjm"][op.param1] = time.time()                    
        if time.time() <= limited["greetjm"][op.param1]:
            pass
        else:
            if settings["stattemp"] == True:
                profile = maxbots.getContact(op.param2)
                username = profile.displayName
                if profile.pictureStatus: picture = "https://obs.line-scdn.net/"+str(profile.pictureStatus)
                else: picture = "https://s20.directupload.net/images/220423/uxdxnp5a.jpg"
                if '@!' in settings['greet']['join']['message']: message = settings['greet']['join']['message'].format(name='', gname=maxbots.getChats([op.param1]).chats[0].chatName).replace('@!', profile.displayName)
                else: message = settings['greet']['join']['message'].format(name='', gname=maxbots.getChats([op.param1]).chats[0].chatName)
                data = {"type": "bubble", "size": "kilo", "header": {"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": "https://i.ibb.co/Q9FQx3V/perakbiruslow.png", "aspectRatio": "1:3", "aspectMode": "cover", "position": "absolute", "size": "full","animated": True}, {"type": "image", "url": "https://i.ibb.co/Q9FQx3V/perakbiruslow.png", "aspectRatio": "1:3", "aspectMode": "cover", "position": "absolute", "offsetTop": "347.5px", "size": "full","animated": True}, {"type": "image", "url": "https://i.ibb.co/Q9FQx3V/perakbiruslow.png", "aspectRatio": "1:3", "aspectMode": "cover", "position": "absolute", "offsetTop": "647.5px", "size": "full","animated": True}, {"type": "image", "url": "https://i.ibb.co/Q9FQx3V/perakbiruslow.png", "aspectRatio": "1:3", "aspectMode": "cover", "position": "absolute", "offsetTop": "947.5px", "size": "full","animated": True}, {"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": "https://i.ibb.co/jGhB2xR/Moris.png", "aspectMode": "cover", "aspectRatio": "9:2", "size": "full", "animated": True}, {"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": "https://i.ibb.co/vDq3JS1/putar1.png", "size": "full", "aspectMode": "cover", "aspectRatio": "1:1", "animated": True}, {"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": picture, "aspectMode": "cover"}], "position": "absolute", "width": "40px", "height": "40px", "cornerRadius": "100px", "borderWidth": "1px", "borderColor": "#191919", "offsetTop": "3px", "offsetStart": "2.5px"}], "width": "45px", "height": "45px", "position": "absolute", "cornerRadius": "100px", "offsetStart": "3px", "offsetTop": "3px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": username, "size": "12px", "weight": "bold", "color": "#FFFFFF"}], "width": "110px", "height": "17.5px", "position": "absolute", "offsetEnd": "50px", "offsetTop": "13px", "justifyContent": "center", "alignItems": "center"}], "paddingAll": "0px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": message, "color": "#fefdfa", "size": "12px", "wrap": True}], "paddingAll": "4px", "backgroundColor": "#191919", "cornerRadius": "0px"}], "paddingTop": "1px","paddingBottom": "2.5px","paddingStart": "2px","paddingEnd": "2px"}, {"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": "https://i.ibb.co/0GfCjm7/20220520-223702.png", "aspectMode": "cover", "aspectRatio": "9:2", "size": "full", "animated": True}, {"type": "box","layout": "vertical","contents": [{"type": "image","url": "https://i.ibb.co/vDq3JS1/putar1.png","size": "full","aspectMode": "cover","animated": True},{"type": "box","layout": "vertical","contents": [{"type": "image","url": "https://s20.directupload.net/images/220423/uxdxnp5a.jpg", "size": "full","aspectMode": "cover","animated": True}],"position": "absolute","width": "40px","height": "40px","offsetBottom": "3px","offsetEnd": "2.5px","cornerRadius": "100px"}],"width": "45px","height": "45px","position": "absolute","offsetBottom": "2px","offsetEnd": "1.5px","cornerRadius": "100px","backgroundColor": "#000000"}, {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "M O R I S  B O T S", "size": "12px", "align": "center", "color": "#e6c619", "weight": "bold"}], "position": "absolute", "height": "20px", "width": "120px", "justifyContent": "center", "offsetBottom": "14px", "offsetStart": "45px"}], "paddingAll": "0px"}], "paddingAll": "0px"} }
                sendTemplate(op.param1,{"type": "flex", "altText": settings["footerlabel"], "contents": data})    
                limitGLM[op.param1] = time.time() + 10
            else:
                mentext2(op.param1, op.param2, settings['greet']['join']['message'].format(name=maxbots.getChats([op.param1]).chats[0].chatName))
                limitGLM[op.param1] = time.time() + 10
    if op.param1 in settings['emojigreetjoin']['status'] and op.param1 not in position['silent']:
        if op.param1 not in limited["greetje"]:
            limited["greetje"][op.param1] = time.time()                   
        if time.time() <= limited["greetje"][op.param1]:
            pass
        else:
            sendEmo2(op.param1,op.param2, settings['emojigreetjoin']['message'], settings['emojigreetjoin']['sticons'], "emojigreetjoin")
            limited["greetje"][op.param1] = time.time() + 10                                                                                 
    if op.param1 in settings['greet']['joinstc'] and op.param1 not in position['silent']:
        if op.param1 not in limited["greetjs"]:
            limited["greetjs"][op.param1] = time.time()                    
        if time.time() <= limited["greetjs"][op.param1]:
            pass
        else:
            maxbots.sendSticker2(op.param1,settings, "greet","stcgreetjoin")
            limited["greetjs"][op.param1] = time.time() + 10
    if settings["purge"]:
        if op.param2 in position["blacklist"]:
            kicked(op.param1, op.param2)
            qrClose(op.param1)
    if op.param1 in protectjoin:
        kicked(op.param1, op.param2)
        ngebl(op.param2)           
    ngelastlist(op.param1, "lastjoin", op.param2)
def notif_kick(op):
    if op.param3 in myMid:
        notifi(op.param1, op.param2, "Kick")
        ngebl(op.param2)           
        position["today"]["kicked"] += 1
    if settings["backupwl"]:
        if op.param3 in position["whitelist"]:
            if op.param2 not in position["whitelist"] and op.param2 not in position["admin"]:
                kicked(op.param1, op.param2)
                invited(op.param1, op.param3)
                ngebl(op.param2)           
    for k, v in position['squadteam'].items():            
        if v["status"] == True:
            if op.param3 in v["list"]:
                if op.param2 not in position["whitelist"] and op.param2 not in position["admin"] and op.param2 not in v["list"]:
                    kicked(op.param1, op.param2) 
                    invSquad(op.param1, k)
                    ngebl(op.param2)          
    if settings["backupadmin"]:
        if op.param3 in position["admin"]:
            if op.param2 not in position["whitelist"] and op.param2 not in position["admin"]:
                kicked(op.param1, op.param2)
                invited(op.param1, op.param3)
                ngebl(op.param2)           
    if op.param1 in protectkick:
        if op.param2 not in position["whitelist"] and op.param2 not in position["admin"]:
            kicked(op.param1, op.param2)
            ngebl(op.param2)        
    ngelastlist(op.param1, "lastkick", op.param3)
def notif_cancel(op):
    if op.param3 in myMid:
        notifi(op.param1, op.param2, "Cancel")
        ngebl(op.param2)    
        position["today"]["canceled"] += 1
    if settings["backupwl"]:
        if op.param3 in position["whitelist"]:
            if op.param2 not in position["whitelist"] and op.param2 not in position["admin"]:
                kicked(op.param1, op.param2)
                invited(op.param1, op.param3)
                ngebl(op.param2)           
    for k, v in position['squadteam'].items():            
        if v["status"] == True:
            if op.param3 in v["list"]:
                if op.param2 not in position["whitelist"] and op.param2 not in position["admin"] and op.param2 not in v["list"]:
                    kicked(op.param1, op.param2) 
                    invSquad(op.param1, k)
                    ngebl(op.param2)              
    if settings["backupadmin"]:
        if op.param3 in position["admin"]:
            if op.param2 not in position["whitelist"] and op.param2 not in position["admin"]:
                kicked(op.param1, op.param2)
                invited(op.param1, op.param3)
                ngebl(op.param2)            
    if op.param1 in protectcancel:
        if op.param2 not in position["whitelist"] and op.param2 not in position["admin"]:
            kicked(op.param1, op.param2)
            ngebl(op.param2)        
    ngelastlist(op.param1, "lastcancel", op.param3)
def notif_read(op):
    if op.param1 in read2["cctv"] and op.param1.startswith("c"):
        target = maxbots.getChats([op.param1]).chats[0].extra.groupExtra.memberMids
        if op.param2 in target and op.param2 not in read2["cctv"][op.param1]:
            if settings["stattemp"] == True:
                siderTemplate(op)
                read2["cctv"][op.param1].append(op.param2)  
            else:
                query = settings["sider"]
                text  = "{} @!".format(query)            
                maxbots.sendTag(op.param1,text,[op.param2])
                read2["cctv"][op.param1].append(op.param2)
    if op.param1 in lurk["readPoint"]:
        if op.param2 not in lurk["readMember"][op.param1]:
            lurk["readMember"][op.param1].append(op.param2)
    if settings["purge"]:
      if op.param2 in position["blacklist"]:
          kicked(op.param1, op.param2)                               
    lastSEEN(op.param1, op.param2)
def notif_all(op):
    msg = op.message
    text = msg.text
    msg_id = msg.id
    receiver = msg.to
    sender = msg._from
    s = maxbots.getProfile()
    if msg.toType == 0:
        if sender != maxbots.profile.mid:
            to = sender                    
        else:
            to = receiver                    
    else:
        to = receiver                
    if msg.contentType == 0:
        if text is None:
            return
        else:
            cmd = command(text)
            if sender != s:
                position["today"]["chatrecv"] += 1                        
            if sender == s.mid:
                position["today"]["chatsend"] += 1                        
    if msg.contentType == 16 and to not in position['silent']:
    	if msg.toType in (2,1,0):
            if settings["AutoLike"]["post"]:
                if msg.contentMetadata['serviceType'] in ['GB', 'NT', 'MH']:
                    posturl = msg.contentMetadata['postEndUrl']
                    rep = posturl.replace("line://home/post?userMid=","")
                    sep = rep.split("&postId=")
                    if sep[1] not in position["postId2"]:
                        maxbots.likePost(sender, sep[1], 1001)                                                  
                        position["postId2"].append(sep[1])
                    ktl = settings['AutoLike']["msglike"]
                    mmk = settings['AutoLike']['sticons']                                                        
                    if '(' not in ktl:
                        rahmanlike(to, ktl)
                    else:
                        if '@!' not in ktl:
                            maxbots.sendMessage(to, ktl,mmk, 0)  
                        else:
                             if '(' in ktl:
                                 maxbots.sendMentionEmot(to,ktl, mmk, "AutoLike", settings, [sender])
                             else:
                                 maxbots.sendTag(to, ktl, [sender])         
            if settings["AutoComment"]["post"]:
                if msg.contentMetadata['serviceType'] in ['GB', 'NT', 'MH']:
                    cuk = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=') 
                    if cuk[1] not in position["postId3"]:
                        if settings["AutoComment"]["sticker"]:
                            sid = settings['AutoComment']["stccomment"]["STKID"]
                            spkg = settings['AutoComment']["stccomment"]["STKPKGID"]
                            sver = settings['AutoComment']["stccomment"]["STKVER"]
                            textt = settings['AutoComment']["msgpost"]
                            maxbots.createComment(cuk[0], cuk[1], textt, contentMetadata={"STKID": sid, "STKPKGID": spkg, "STKVER": sver})                                                                                                                                                                       
                        else:
                            textt = settings['AutoComment']["msgpost"]
                            maxbots.createComment(cuk[0], cuk[1], textt)                                                                                 
                        position["postId3"].append(cuk[1])
    if msg.contentType == 13:
        mid = msg.contentMetadata['mid']  
        ngelastlist(to, "lastcontact", mid)
    if msg.contentType == 0 and to not in position['silent']:
        if text is None:
            return
        if 'smule.com/' in text.lower():
            if settings["modepublic"] or settings["downloadmedia"] or msg._from in position["admin"]:
                regex = re.findall(r'(https?://\S+)', text)
                share_link = []                                                   
                for link in regex:
                    if link not in share_link:
                        share_link.append(link)
                for download in share_link:
                    smuleDl(to,download)
        if 'youtu.be/' in text.lower() or 'youtube.com/' in text.lower():
            if settings["modepublic"] or settings["downloadmedia"] or msg._from in position["admin"]:
                regex = re.findall(r'(https?://\S+)', text)
                share_link = []                                                   
                for link in regex:
                    if link not in share_link:
                        share_link.append(link)                                    
                for download in share_link:
                    ytbPost(to, download)                                             
        if 'pin.it/' in text.lower():
            if settings["modepublic"] or settings["downloadmedia"] or msg._from in position["admin"]:
                regex = re.findall(r'(https?://\S+)', text)
                share_link = []                                                  
                for link in regex:
                    if link not in share_link:
                        share_link.append(link)                                    
                for download in share_link:
                    pinPost(to, download)
        if 'linevoom.line.me/' in text.lower():
            if settings["modepublic"] or settings["downloadmedia"] or msg._from in position["admin"]:
                regex = re.findall(r'(https?://\S+)', text)
                share_link = []                                                   
                for link in regex:
                    if link not in share_link:
                        share_link.append(link)                                    
                for download in share_link:
                    tlPost(to, download)                   
        if 'twitter.com/' in text.lower():
            if settings["modepublic"] or settings["downloadmedia"] or msg._from in position["admin"]:
                regex = re.findall(r'(https?://\S+)', text)
                share_link = []                                                   
                for link in regex:
                    if link not in share_link:
                        share_link.append(link)                                    
                for download in share_link:
                    trPost(to, download)                       
        if 'tiktok.com/' in text.lower():
            if settings["modepublic"] or settings["downloadmedia"] or msg._from in position["admin"]:
                regex = re.findall(r'(https?://\S+)', text)
                share_link = []                                                   
                for link in regex:
                    if link not in share_link:
                        share_link.append(link)                                    
                for download in share_link:
                    ttPost(to, download)                                          
        if 'instagram.com/' in text.lower():
            if settings["modepublic"] or settings["downloadmedia"] or msg._from in position["admin"]:
                regex = re.findall(r'(https?://\S+)', text)
                share_link = []                                                   
                for link in regex:
                    if link not in share_link:
                        share_link.append(link)                                    
                for download in share_link:
                    igPost(to, download) 
        if text.lower() in listsett["fakestickerr"]:
            if to not in limited["list1"]:
                limited["list1"][to] = time.time()                    
            if time.time() <= limited["list1"][to]:
                pass
            else:
                sid = listsett["fakestickerr"][text.lower()]["STKID"]
                spkg = listsett["fakestickerr"][text.lower()]["STKPKGID"]
                sver = listsett["fakestickerr"][text.lower()]["STKVER"]                                                            
                if msg.toType == 1:
                    members = cektagallM(to)                             
                elif msg.toType == 2:
                    members = cekmember(to)               
                else:
                    return rahman(to,   "「 Mention 」\n › Type: Fake Sticker♪\n    • Failed Fake Sticker")
                if members:
                    sendfakesticker(to, spkg, sid,sver, members)     
                    limited["list1"][to] = time.time() + 20                             
        if text.lower() in listsett["fakecontactt"]:
            if to not in limited["list2"]:
                limited["list2"][to] = time.time()                    
            if time.time() <= limited["list2"][to]:
                pass
            else:
                if msg.toType == 1:
                    members = cektagallM(to)                             
                elif msg.toType == 2:
                    members = cekmember(to)               
                else:
                    return rahman(to,   "「 Mention 」\n › Type: Fake Contact♪\n    • Failed Fake Contact")      
                if members:
                    sendfakecontact(to, listsett["fakecontactt"][text.lower()],members)                                                                 
                    limited["list2"][to] = time.time() + 20                                                
        if text.lower() in listsett["wordbann"]:
            kicked(msg.to, msg._from)                                                                                        
        if text.lower() in listsett["textt"]:
            if to not in limited["list3"]:
                limited["list3"][to] = time.time()                    
            if time.time() <= limited["list3"][to]:
                pass
            else:
                if "("  in listsett["textt"][text.lower()]:   
                    if "@!" not in listsett["textt"][text.lower()]:   
                        try:
                            maxbots.sendReplyMessage(msg_id,to,listsett["textt"][text.lower()], listsett[text.lower()])
                        except:
                            maxbots.sendReplyMessage(msg_id, to, listsett["textt"][text.lower()])   
                    else:         
                        try:
                            maxbots.sendMentionReplyEmot2(msg_id,to, listsett["textt"][text.lower()],listsett[text.lower()], listsett, text.lower(),[sender])       
                        except:
                            maxbots.sendMentionV2(msg_id,to, listsett["textt"][text.lower()], [sender])                             
                else:            
                    if "@!" not in listsett["textt"][text.lower()]:   
                        maxbots.sendReplyMessage(msg_id, to, listsett["textt"][text.lower()])   
                    else: 
                        maxbots.sendMentionV2(msg_id,to, listsett["textt"][text.lower()], [sender])                                                                   
                limited["list3"][to] = time.time() + 20                     
        if text.lower() in listsett["imagee"]:
            if to not in limited["list4"]:
                limited["list4"][to] = time.time()                    
            if time.time() <= limited["list4"][to]:
                pass
            else:
                try:
                    maxbots.sendImage(msg.to, listsett["imagee"][text.lower()]) 
                    limited["list4"][to] = time.time() + 20                                      
                except:pass
        if text.lower() in listsett["videoo"]:
            if to not in limited["list5"]:
                limited["list5"][to] = time.time()                    
            if time.time() <= limited["list5"][to]:
                pass
            else:
                try:
                    maxbots.sendVideo(msg.to, listsett["videoo"][text.lower()])                               
                    limited["list5"][to] = time.time() + 20                
                except:pass
        if text.lower() in listsett["audioo"]:
            if to not in limited["list6"]:
                limited["list6"][to] = time.time()                    
            if time.time() <= limited["list6"][to]:
                pass
            else:
                maxbots.sendAudio(msg.to, listsett["audioo"][text.lower()])                               
                limited["list6"][to] = time.time() + 20           
        if text.lower() in listsett["stickerr"]:
            if to not in limited["list7"]:
                limited["list7"][to] = time.time()                    
            if time.time() <= limited["list7"][to]:
                pass
            else:
                try:
                    maxbots.sendMessage(msg.to, "", listsett["stickerr"][text.lower()], 7)                                                                                                        
                    limited["list7"][to] = time.time() + 20         
                except:pass
        if text.lower() in listsett["contactt"]:
            if to not in limited["list8"]:
                limited["list8"][to] = time.time()                    
            if time.time() <= limited["list8"][to]:
                pass
            else:
                maxbots.sendContact(msg.to, listsett["contactt"][text.lower()])                              
                limited["list8"][to] = time.time() + 20         
        if text.lower() in listsett["bigstickerr"]:
            if to not in limited["list9"]:
                limited["list9"][to] = time.time()                    
            if time.time() <= limited["list9"][to]:
                pass
            else:
                sid = listsett["bigstickerr"][text.lower()]["STKID"]
                spkg = listsett["bigstickerr"][text.lower()]["STKPKGID"]
                sver = listsett["bigstickerr"][text.lower()]["STKVER"]
                xsex = maxbots.shop.getProduct(packageID=int(spkg), language='ID', country='ID')
                if xsex.hasAnimation == True:data = {"type": "template","altText": "{} sent a sticker.".format(maxbots.getProfile().displayName),"template": {"type": "image_carousel","columns": [{"imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png".format(sid),"size": "full","action": {"type": "uri","uri": "http://line.me/S/sticker/{}".format(spkg)}}]}}
                else:data = {"type": "template","altText": "{} sent a sticker.".format(maxbots.getProfile().displayName),"template": {"type": "image_carousel","columns": [{"imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png".format(sid),"size": "full","action": {"type": "uri","uri": "http://line.me/S/sticker/{}".format(spkg)}}]}}
                sendTemplate(to, data)                        
                limited["list9"][to] = time.time() + 20         
def notif_acount(op):
    msg      = op.message
    text     = str(msg.text)
    msg_id   = msg.id
    receiver = msg.to
    sender   = msg._from
    to       = sender if not msg.toType and sender != myMid else receiver
    txt      = text.lower()
    cmd      = command(txt)
    setKey   = settings['setKey']['key'] if settings['setKey']['status'] else ''           
    if msg.contentType == 0:
        try:
            executeArf(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey)                    
        except TalkException as talk_error:
            logError(talk_error)
            if talk_error.code in [7, 8, 20]:
                sys.exit(1)
            print('「 ✘ Error 」\n' + str(talk_error))
            time.sleep(3)                                   
        except Exception as error:
            print('「 ✘ Error 」\n' + str(error))
            time.sleep(3)
    if msg.contentType == 0:
        if msg.toType == 0 and not msg.toType == 2:
            if text.lower() == 'p':
                maxbots.sendTag(to, "@!", [to])                      
    if msg.contentType == 0:
        if wait['getcontactcontact']:            	
            data= maxbots.server.MID_REGEX.findall(text)
            if data != []:
                for i in data:
                    time.sleep(0.8)
                    maxbots.sendContact(to, i)                                                         
        if text.lower() in listsett["kibarann"]:
            for x in listsett["kibarann"][text.lower()]:                                   
                if "png" in x:
                    maxbots.sendImage(to, x)              
                elif "mp4" in x:
                    maxbots.sendVideo(to, x)              
                elif "mp3" in x:
                    maxbots.sendAudio(to, x)              
                elif len(x) == 33:
                    try:
                        maxbots.sendContact(to, x)
                    except:
                        maxbots.sendMessage(to, x)
                else:                
                    maxbots.sendMessage(to, x)
        if cmd in position["squadteam"]:
            invSquad(to, cmd)
        if settings["Addkibaran"]["status"] == True:
            if "kibaran" in text.lower() or "「" in text.lower() or "abort" in text.lower():
                pass
            else:
                listsett["kibarann"][settings["Addkibaran"]["name"]].append(msg.text)
                maxbots.sendMessage(to, "• Type `"+ setKey +"Abort` For Done")               
        if to in position['timebc']:
            if "broadcast" in text.lower() or "「" in text.lower() or "• Type" in text.lower():
                pass
            else:
                if "(" in msg.text:
                    try:
                        REPLACE = {"sticon":{"resources": []}}
                        x = eval(msg.contentMetadata["REPLACE"])
                        for data_rep in x["sticon"]["resources"]:
                             REPLACE["sticon"]["resources"].append({"S": str(data_rep["S"]), "E": str(data_rep["E"]), "productId":data_rep["productId"], "sticonId": data_rep["sticonId"], "version":1, "resourceType": data_rep["resourceType"]})
                        contentMetadata = {"REPLACE": json.dumps(REPLACE),"STICON_OWNERSHIP": msg.contentMetadata['STICON_OWNERSHIP']}                                
                        name = msg.text
                        position["bot"].append(name)
                        position["multibc"].append(msg.text)
                        position[name] = contentMetadata
                    except:
                        position["multibc"].append(msg.text)
                    maxbots.sendMessage(to, "• Type `"+ setKey +"Send Broadcast` For Done")               

                else:
                    position["multibc"].append(msg.text)
                    maxbots.sendMessage(to, "• Type `"+ setKey +"Send Broadcast` For Done")               
    if msg.contentType == 1:
        if settings['ChangePictFooter']:
            path = maxbots.downloadObjectMsg(msg_id, saveAs=f'user/{usernamee}/picture.jpg')
            data = apiJG.imgurl(path)
            settings["footerpict"] = data["result"]
            rahman(to,   "「 Mode 」\n › Type: Change Picture Label♪\n    • Status: Success")
            settings['ChangePictFooter'] = False                                                                                                    
        if settings['changePictureProfile']:
            path = maxbots.downloadObjectMsg(msg_id, saveAs=f'user/{usernamee}/picture.jpg')
            maxbots.updateProfilePicture(path)
            rahman(to,   "「 Profile 」\n › Type: Change Profile♪\n    • Status: Success")
            settings['changePictureProfile'] = False                                                                                
        if settings['changeCoverProfile']:
            path = maxbots.downloadObjectMsg(msg_id, saveAs=f'user/{usernamee}/cover.jpg')
            maxbots.updateProfileCover(path)
            rahman(to,   "「 Profile 」\n › Type: Change Cover♪\n    • Status: Success")
            settings['changeCoverProfile'] = False                                                                                
        if settings['updatestory']:
            path = maxbots.downloadObjectMsg(msg_id)
            objId, obsHash = maxbots.uploadObjStory(path, type='image')
            maxbots.updateStory(objId, obsHash, mediaType='image')
            rahman(to,   "「 Profile 」\n › Type: Update Story♪\n    • Status: Success")
            settings['updatestory'] = False                                                                                                    
        if to in settings['changeGroupPicture'] and msg.toType == 2:
            path = maxbots.downloadObjectMsg(msg_id, saveAs=f'user/{usernamee}/grouppicture.jpg')
            maxbots.updateGroupPicture(to, path)
            rahman(to,   "「 Group 」\n › Type: Change Gpict♪\n    • Status: Success")
            settings['changeGroupPicture'].remove(to)                                                                                                    
        if to in settings['changeGroupCover'] and msg.toType == 2:
            path = maxbots.downloadObjectMsg(msg_id, saveAs=f'user/{usernamee}/groupcover.jpg')
            maxbots.updateCoverGroup(to, path)
            rahman(to,   "「 Group 」\n › Type: Change Gcover♪\n    • Status: Success")
            settings['changeGroupCover'].remove(to)                                                                              
        if settings["Addimage"]["status"] == True:
            time.sleep(0.8)
            path = maxbots.downloadObjectMsg(msg_id, saveAs=f'user/{usernamee}/{settings["Addimage"]["name"]}.png')
            listsett["imagee"][settings["Addimage"]["name"]] = str(path)
            rahman(to,"「 List 」\n › Type: Picture Add♪\n    • Text : {} \n    • Status: Succes".format(str(settings["Addimage"]["name"])))
            settings["Addimage"]["status"] = False
            settings["Addimage"]["name"] = ""           
        if settings["Addkibaran"]["status"] == True:
            path = maxbots.downloadObjectMsg(msg_id, saveAs=f'user/{usernamee}/{settings["Addkibaran"]["name"]}.png')
            listsett["kibarann"][settings["Addkibaran"]["name"]].append(path)
            maxbots.sendMessage(to, "• Type "+ setKey +"Abort For Done")
        if to in position['timebc']:
            time.sleep(0.8)
            path = maxbots.downloadObjectMsg(msg_id, saveAs=f'user/{usernamee}/bc.png')
            position["multibc"].append(path)
            maxbots.sendMessage(to, "• Type `"+ setKey +"Send Broadcast` For Done")               
    if msg.contentType == 2:
        if settings["changevp"] == True:
            contact = maxbots.getProfile()
            pict = "https://obs.line-scdn.net/{}".format(contact.pictureStatus)
            path = maxbots.downloadFileURL(pict)
            path1 = maxbots.downloadObjectMsg(msg_id)
            settings["changevp"] = False
            changevideopp(path, path1)
            rahman(to,   "「 Profile 」\n › Type: Change Video Profile♪\n    • Status: Succes")                                                                                                                                            
        if settings['changeProfileVideo']:
            pict = covernyaa(sender)
            path = maxbots.downloadFileURL(pict)
            path1 = maxbots.downloadObjectMsg(msg_id)
            maxbots.updateProfileCoverVideo(path, path1)
            rahman(to,   "「 Profile 」\n › Type: Change Video Cover♪\n    • Status: Succes")                                                                     
        if settings['updatestory']:
            path = maxbots.downloadObjectMsg(msg_id)
            objId, obsHash = maxbots.uploadObjStory(path, type='video')
            maxbots.updateStory(objId, obsHash, mediaType='video')
            rahman(to,   "「 Profile 」\n › Type: Update Story♪\n    • Status: Success")
            settings['updatestory'] = False                                                                                                         
        if settings["Addvideo"]["status"] == True:
            time.sleep(0.8)
            path = maxbots.downloadObjectMsg(msg_id, saveAs=f'user/{usernamee}/{settings["Addvideo"]["name"]}.mp4')
            listsett["videoo"][settings["Addvideo"]["name"]] = str(path)
            rahman(to,"「 List 」\n › Type: Video Add♪\n    • Text : {} \n    • Status: Succes".format(str(settings["Addvideo"]["name"])))
            settings["Addvideo"]["status"] = False
            settings["Addvideo"]["name"] = ""                      
        if settings["Addkibaran"]["status"] == True:
            path = maxbots.downloadObjectMsg(msg_id, saveAs=f'user/{usernamee}/{settings["Addkibaran"]["name"]}.mp4')
            listsett["kibarann"][settings["Addkibaran"]["name"]].append(path)
            maxbots.sendMessage(to, "• Type "+ setKey +"Abort For Done")
        if to in position['timebc']:
            time.sleep(0.8)
            path = maxbots.downloadObjectMsg(msg_id, saveAs=f'user/{usernamee}/bc.mp4')
            position["multibc"].append(path)
            maxbots.sendMessage(to, "• Type `"+ setKey +"Send Broadcast` For Done")               
    if msg.contentType == 3:                                                                                          
        if settings["Addaudio"]["status"] == True:
            time.sleep(0.8)
            path = maxbots.downloadObjectMsg(msg_id, saveAs=f'user/{usernamee}/{settings["Addaudio"]["name"]}.mp3')
            listsett["audioo"][settings["Addaudio"]["name"]] = str(path)
            rahman(to,"「 List 」\n › Type: Audio Add♪\n    • Text : {} \n    • Status: Succes".format(str(settings["Addaudio"]["name"])))
            settings["Addaudio"]["status"] = False
            settings["Addaudio"]["name"] = ""                                                                                                      
        if settings["Addkibaran"]["status"] == True:
            path = maxbots.downloadObjectMsg(msg_id, saveAs=f'user/{usernamee}/{settings["Addkibaran"]["name"]}.mp3')
            listsett["kibarann"][settings["Addkibaran"]["name"]].append(path)
            maxbots.sendMessage(to, "• Type "+ setKey +"Abort For Done")
        if to in position['timebc']:
            time.sleep(0.8)
            path = maxbots.downloadObjectMsg(msg_id, saveAs=f'user/{usernamee}/bc.mp3')
            position["multibc"].append(path)
            maxbots.sendMessage(to, "• Type `"+ setKey +"Send Broadcast` For Done")               
    if msg.contentType == 7 and to not in position['silent']:
        if settings['statkick']:
            ktl = printSTC(msg)
            settings["stckick"] = ktl
            rahman(to,   "「 Command 」\n › Type: Add Stickerkick♪\n    • Status: Success")
            settings['statkick'] = False                                                                                                                                                                                                                   
        if settings['statinvite']:
            ktl = printSTC(msg)
            settings["stcinvite"] = ktl
            rahman(to,   "「 Command 」\n › Type: Add Stickerinvite♪\n    • Status: Success")
            settings['statinvite'] = False                                                                                                               
        if settings['statleave']:
            limited["ceks"][to] = time.time() + 2
            ktl = printSTC(msg)
            settings["stcleave"] = ktl
            rahman(to,   "「 Command 」\n › Type: Add Stickerleave♪\n    • Status: Success")
            settings['statleave'] = False                                                                                                               
        if settings['statkickallpy']:
            limited["ceks"][to] = time.time() + 2
            ktl = printSTC(msg)
            settings["stckickallpy"] = ktl
            rahman(to,   "「 Command 」\n › Type: Add Stickerkickallpy♪\n    • Status: Success")
            settings['statkickallpy'] = False                                                                                                               
        if settings['statkillbanpy']:
            limited["ceks"][to] = time.time() + 2
            ktl = printSTC(msg)
            settings["stckillbanpy"] = ktl
            rahman(to,   "「 Command 」\n › Type: Add Stickerkillbanpy♪\n    • Status: Success")
            settings['statkillbanpy'] = False                                                                                                               
        if settings['statkillban']:
            limited["ceks"][to] = time.time() + 2
            ktl = printSTC(msg)
            settings["stckillban"] = ktl
            rahman(to,   "「 Command 」\n › Type: Add Stickerkillban♪\n    • Status: Success")
            settings['statkillban'] = False                                                                                                               
        if settings['statreinvite']:
            ktl = printSTC(msg)
            settings["stcreinvite"] = ktl
            rahman(to,   "「 Command 」\n › Type: Add Stickerreinvite♪\n    • Status: Success")
            settings['statreinvite'] = False                                                                                                               
        if settings['statmkick']:
            ktl = printSTC(msg)
            settings["stcmkick"] = ktl
            rahman(to,   "「 Command 」\n › Type: Add Stickermkick♪\n    • Status: Success")
            settings['statmkick'] = False                                                                                                               
        if settings['statslain']:
            ktl = printSTC(msg)
            settings["stcslain"] = ktl
            rahman(to,   "「 Command 」\n › Type: Add Stickerslain♪\n    • Status: Success")
            settings['statslain'] = False                                                                                                               
        if settings['stattagall']:
            limited["ceks"][to] = time.time() + 2
            ktl = printSTC(msg)
            settings["stctagall"] = ktl
            rahman(to,   "「 Mention 」\n › Type: Add Stickertagall♪\n    • Status: Success")
            settings['stattagall'] = False                                                                                                                                                                                    
        if settings['statemojitagall']:
            limited["ceks"][to] = time.time() + 2
            ktl = printSTC(msg)
            settings["stcemojitagall"] = ktl
            rahman(to,   "「 Mention 」\n › Type: Add Stickeremojitagall♪\n    • Status: Success")
            settings['statemojitagall'] = False                                                                                                            
            settings["statusceksticker"] = True
        if settings['stickerfaketag']:
            limited["ceks"][to] = time.time() + 2
            ktl = printSTC(msg)
            settings["stkfaketag"] = ktl
            rahman(to,   "「 Mention 」\n › Type: Add Stickerfaketag♪\n    • Status: Success")
            settings['stickerfaketag'] = False                                                                                                      
        if settings['statjsbypass']:
            limited["ceks"][to] = time.time() + 2
            ktl = printSTC(msg)
            settings["stcjsbypass"] = ktl
            rahman(to,   "「 Js 」\n › Type: Add Stickerbypass♪\n    • Status: Success")
            settings['statjsbypass'] = False                                                                                                                                                                                    
        if settings['statjskickall']:
            limited["ceks"][to] = time.time() + 2
            ktl = printSTC(msg)
            settings["stcjskickall"] = ktl
            rahman(to,   "「 Js 」\n › Type: Add Stickerkickall♪\n    • Status: Success")
            settings['statjskickall'] = False                                                                                                             
        if settings['statjscancelall']:
            limited["ceks"][to] = time.time() + 2
            ktl = printSTC(msg)
            settings["stcjscancelall"] = ktl
            rahman(to,   "「 Js 」\n › Type: Add Stickercancelall♪\n    • Status: Success")
            settings['statjscancelall'] = False                                                                                                      
        if settings['stickermention']:
            ktl = printSTC(msg)
            settings["stcmention"] = ktl
            rahman(to,   "「 Autorespon 」\n › Type: Add Stickerrespontag♪\n    • Status: Success")
            settings['stickermention'] = False                                                                                                          
        if settings['stickerchat']:
            ktl = printSTC(msg)
            settings["stcchat"] = ktl
            rahman(to,   "「 Autorespon 」\n › Type: Add Stickerresponchat♪\n    • Status: Success")
            settings['stickerchat'] = False                                                                                                       
        if settings['stickeradd']:
            ktl = printSTC(msg)
            settings["stcadd"] = ktl
            rahman(to,   "「 Autoadd 」\n › Type: Add Stickerautoadd♪\n    • Status: Success")
            settings['stickeradd'] = False                                                                                                    
        if settings['statstcautojoin']:
            ktl = printSTC(msg)
            settings["stcautojoin"] = ktl
            rahman(to,   "「 Autojoin 」\n › Type: Add Stickerautojoin♪\n    • Status: Success")
            settings['statstcautojoin'] = False
        if settings['autoLeave']['gc']["setstc"]:
            ktl = printSTC(msg)
            settings["stcautoleaveGC"] = ktl
            rahman(to,   "「 Autoleave 」\n › Type: Add Stickerautoleave GC♪\n    • Status: Success")
            settings['autoLeave']['gc']["setstc"] = False   
        if settings['autoLeave']['mc']["setstc"]:
            ktl = printSTC(msg)
            settings["stcautoleaveMC"] = ktl
            rahman(to,   "「 Autoleave 」\n › Type: Add Stickerautoleave MC♪\n    • Status: Success")
            settings['autoLeave']['mc']["setstc"] = False                                                                                                      
        if settings['AutoComment']['setstccomment']:
            ktl = printSTC(msg)
            settings['AutoComment']["stccomment"] = ktl
            rahman(to,   "「 Autocomment 」\n › Type: Add Stickercomment♪\n    • Status: Success")
            settings['AutoComment']['setstccomment'] = False                                                                                                       
        if settings['greet']['stickergreetjoin']:
            ktl = printSTC(msg)
            settings['greet']["stcgreetjoin"] = ktl
            rahman(to,   "「 Greet 」\n › Type: Add Stickergreetjoin♪\n    • Status: Success")
            settings['greet']['stickergreetjoin'] = False                                                                                                   
        if settings['greet']['stickergreetleave']:
            ktl = printSTC(msg)
            settings['greet']["stcgreetleave"] = ktl
            rahman(to,   "「 Greet 」\n › Type: Add Stickergreetleave♪\n    • Status: Success")
            settings['greet']['stickergreetleave'] = False                                                                                                      
        if settings["Addfakesticker"]["status"] == True:
            listsett["fakestickerr"][settings["Addfakesticker"]["name"]] = printSTC(msg)
            rahman(to,"「 Mention 」\n › Type: Add Fakesticker♪\n    • Name : {}\n    • Status: Success".format(str(settings["Addfakesticker"]["name"])))
            settings["Addfakesticker"]["status"] = False
            settings["Addfakesticker"]["name"] = ""                                                 
        if settings["Addsticker"]["status"] == True:
            listsett["stickerr"][settings["Addsticker"]["name"]] = printSTC(msg)
            rahman(to,"「 List 」\n › Type: Sticker Add♪\n    • Name : {}\n    • Status: Success".format(str(settings["Addsticker"]["name"])))
            settings["Addsticker"]["status"] = False
            settings["Addsticker"]["name"] = ""                       
        if settings["Addbigsticker"]["status"] == True:
            listsett["bigstickerr"][settings["Addbigsticker"]["name"]] = printSTC(msg)
            rahman(to,"「 List 」\n › Type: Bigsticker Add♪\n    • Name : {}\n    • Status: Success".format(str(settings["Addbigsticker"]["name"])))
            settings["Addbigsticker"]["status"] = False
            settings["Addbigsticker"]["name"] = ""                       
        if to in position['timebc']:
            name = msg.contentMetadata["STKID"] + ".stc"
            position["multibc"].append(name)
            position["bot"].append(name)
            position[name] = printSTC(msg)
            maxbots.sendMessage(to, "• Type `"+ setKey +"Send Broadcast` For Done")               
        if settings['Check']['sticker']:
            arifblek = "「 Check 」\n › Type: Sticker♪"
            arifblek += f"\n    • Sticker ID: {msg.contentMetadata['STKID']} "
            arifblek += f"\n    • Sticker Packages ID: {msg.contentMetadata['STKPKGID']} "
            arifblek += f"\n    • Sticker Version: {msg.contentMetadata['STKVER']} "
            arifblek += f"\n    • Sticker Link: line://shop/detail/{msg.contentMetadata['STKPKGID']} "
            rahman(to, arifblek)     
        for k, v in position['squadteam'].items():            
            if v["statusstc"] == True:
                ngentod = printSTC(msg)
                position["squadteam"][k]["stc"] = ngentod
                rahman(to,   "「 Squad 」\n › Type: Sticker Add♪\n    • Status: Success")
                position["squadteam"][k]["statusstc"] = False
        if settings["stckick"]["STKID"] in msg.contentMetadata["STKID"]:
            if msg.relatedMessageId is not None:
                aa = maxbots.getRecentMessagesV2(to, 1001)
                for bb in aa:
                    if bb.id in msg.relatedMessageId:
                        kicked(to, bb._from)                                    
        if settings["stcinvite"]["STKID"] in msg.contentMetadata["STKID"]:
            if msg.relatedMessageId is not None:
                aa = maxbots.getRecentMessagesV2(to, 1001)
                for bb in aa:
                    if bb.id in msg.relatedMessageId:
                        invited(to, bb._from)                                            
        if settings["stcreinvite"]["STKID"] in msg.contentMetadata["STKID"]:
            if msg.relatedMessageId is not None:
                aa = maxbots.getRecentMessagesV2(to, 1001)
                for bb in aa:
                    if bb.id in msg.relatedMessageId:
                        kicked(to, bb._from)            
                        invited(to, bb._from)      
        if settings["stcmkick"]["STKID"] in msg.contentMetadata["STKID"]:
            if msg.relatedMessageId is not None:
                aa = maxbots.getRecentMessagesV2(to, 1001)
                for bb in aa:
                    if bb.id in msg.relatedMessageId:
                        kicked(to, bb._from)
                        invited(to, bb._from)
                        canceled(to, bb._from)
                        invited(to, bb._from)
                        canceled(to, bb._from)                
        if settings["stcslain"]["STKID"] in msg.contentMetadata["STKID"]:
            if msg.relatedMessageId is not None:
                aa = maxbots.getRecentMessagesV2(to, 1001)
                for bb in aa:
                    if bb.id in msg.relatedMessageId:
                        kicked(to, bb._from)
                        invited(to, bb._from)
                        canceled(to, bb._from)
                        invited(to, bb._from)                                                                                                  
        if settings["stctagall"]["STKID"] in msg.contentMetadata["STKID"]:
            if to not in limited["ceks"]:
                limited["ceks"][to] = time.time()                              
            if time.time() <= limited["ceks"][to]:
                pass
            else:
                if msg.toType == 1:
                    members = cektagallM(to)                             
                elif msg.toType == 2:
                    members = cekmember(to)               
                else:
                    return rahman(to,   "「 Mention 」\n › Type: Tagall♪\n    • Status: Failed Tagall")                                     
                if members:
                    tagallMention(to, members)                          
        if settings["stcemojitagall"]["STKID"] in msg.contentMetadata["STKID"]:
            if to not in limited["ceks"]:
                limited["ceks"][to] = time.time()                              
            if time.time() <= limited["ceks"][to]:
                pass
            else:
                if msg.toType == 1:
                    members = cektagallM(to)                             
                elif msg.toType == 2:
                    members = cekmember(to)               
                else:
                     return rahman(to,   "「 Mention 」\n › Type: Tagall♪\n    • Status: Failed Tagall")                                     
                if members:
                    tagallEmot(to, msg, members)                          
        if settings['stkfaketag']["STKID"] in msg.contentMetadata["STKID"]:
            if to not in limited["ceks"]:
                limited["ceks"][to] = time.time()                              
            if time.time() <= limited["ceks"][to]:
                pass
            else:
                sid = settings['stkfaketag']["STKID"]
                spkg = settings['stkfaketag']["STKPKGID"]
                sver = settings['stkfaketag']["STKVER"]                                                                      
                if msg.toType == 1:
                    members = cektagallM(to)                             
                elif msg.toType == 2:
                    members = cekmember(to)               
                else:
                    return rahman(to,   "「 Mention 」\n › Type: Faketag♪\n    • Status: Failed Faketag")
                if members:
                    if to not in limited["fake"]:
                        limited["fake"][to] = time.time()                              
                    if time.time() <= limited["fake"][to]:
                        pass
                    else:
                        sendfakesticker(to, spkg, sid, sver,members)
                        limited["fake"][to] = time.time() + 20                                                                                                   
        if settings["stcjsbypass"]["STKID"] in msg.contentMetadata['STKID']:
            if to not in limited["ceks"]:
                limited["ceks"][to] = time.time()                              
            if time.time() <= limited["ceks"][to]:
                pass
            else:
                if settings["javascript"]:
                    bypassJS(to)
        if settings["stcjskickall"]["STKID"] in msg.contentMetadata['STKID']:
            if to not in limited["ceks"]:
                limited["ceks"][to] = time.time()                              
            if time.time() <= limited["ceks"][to]:
                pass
            else:
                if settings["javascript"]:
                    kickallJS(to)
        if settings["stcjscancelall"]["STKID"] in msg.contentMetadata['STKID']:
            if to not in limited["ceks"]:
                limited["ceks"][to] = time.time()                              
            if time.time() <= limited["ceks"][to]:
                pass
            else:
                if settings["javascript"]:
                    cancelallJS(to)
        if settings["stckickallpy"]["STKID"] in msg.contentMetadata['STKID']:
            if to not in limited["ceks"]:
                limited["ceks"][to] = time.time()                              
            if time.time() <= limited["ceks"][to]:
                pass
            else:
                kickallPY(to)
        if settings["stckillban"]["STKID"] in msg.contentMetadata['STKID']:
            if to not in limited["ceks"]:
                limited["ceks"][to] = time.time()                              
            if time.time() <= limited["ceks"][to]:
                pass
            else:
                purgeJS(to)
        if settings["stckillbanpy"]["STKID"] in msg.contentMetadata['STKID']:
            if to not in limited["ceks"]:
                limited["ceks"][to] = time.time()                              
            if time.time() <= limited["ceks"][to]:
                pass
            else:
                purgePY(to)
        if settings["stcleave"]["STKID"] in msg.contentMetadata['STKID']:
            if to not in limited["ceks"]:
                limited["ceks"][to] = time.time()                              
            if time.time() <= limited["ceks"][to]:
                pass
            else:
                leaveed(to)
        for k, v in position['squadteam'].items():
            try:
               if v["stc"]["STKID"] in msg.contentMetadata['STKID']:
                     invSquad(to, k)
            except:pass
    if msg.contentType == 13:
        for k, v in position['squadteam'].items():            
            if v["statusconadd"] == True:
                mid = msg.contentMetadata['mid']
                if mid not in position["squadteam"][k]["list"]:
                    position["squadteam"][k]["list"].append(mid)
                    maxbots.sendTag(to,"「 Squad 」\n › Type: Add♪\n    • 1. @! Add♪\n › Note: Type "+ setKey +"Abort For Done",[mid])                                  
                else:
                    maxbots.sendTag(to,"「 Squad 」\n › Type: Add♪\n    • 1. @! Already♪\n › Note: Type "+ setKey +"Abort For Done",[mid])                                  
            if v["statuscondel"] == True:
                mid = msg.contentMetadata['mid']
                if mid in position["squadteam"][k]["list"]:
                    position["squadteam"][k]["list"].remove(mid)
                    maxbots.sendTag(to,"「 Squad 」\n › Type: Del♪\n    • 1. @! Del♪\n › Note: Type "+ setKey +"Abort For Done",[mid])                                  
                else:
                    maxbots.sendTag(to,"「 Squad 」\n › Type: Del♪\n    • 1. @! Nothing♪\n › Note: Type "+ setKey +"Abort For Done",[mid])                                  
        if wait['getpictcontact']:
            mid = msg.contentMetadata['mid']
            stealpict(to, mid)
            rahman(to, "「 Steal 」\n › Type: Getpict♪\n    • Note: Type "+ setKey +"Abort For Done \n    • Status: Success")                                                             
        if wait['getcovercontact']:
            mid = msg.contentMetadata['mid']
            stealcover(to, mid)
            rahman(to, "「 Steal 」\n › Type: Getcover♪\n    • Note: Type "+ setKey +"Abort For Done \n    • Status: Success")                                                              
        if wait['getexcovercontact']:
            mid = msg.contentMetadata['mid']
            stealexcover(to, mid)
            rahman(to, "「 Steal 」\n › Type: Getextracover♪\n    • Note: Type "+ setKey +"Abort For Done \n    • Status: Success")                                                              
        if wait['getvideocontact']:
            mid = msg.contentMetadata['mid']  
            stealvideo(to, mid)
            rahman(to, "「 Steal 」\n › Type: Getvideo♪\n    • Note: Type "+ setKey +"Abort For Done \n    • Status: Success")                                        
        if wait['getnamecontact']:
            mid = msg.contentMetadata['mid']
            stealname(to,mid, "Steal")
            rahman(to, "「 Steal 」\n › Type: Getname♪\n    • Note: Type "+ setKey +"Abort For Done \n    • Status: Success")                                                              
        if wait['getrenamecontact']:
            mid = msg.contentMetadata['mid']
            stealrename(to,mid)
            rahman(to, "「 Steal 」\n › Type: Getrename♪\n    • Note: Type "+ setKey +"Abort For Done \n    • Status: Success")                                                              
        if wait['getbiocontact']:
            mid = msg.contentMetadata['mid']
            stealbio(to,mid, "Steal")
            rahman(to, "「 Steal 」\n › Type: Getbio♪\n    • Bio: " + str(contact.statusMessage) + "\n    • Note: Type "+ setKey +"Abort For Done \n    • Status: Success")                                                              
        if wait['getmidcontact']:
            mid = msg.contentMetadata['mid']
            stealmid(to,mid)
            rahman(to, "「 Steal 」\n › Type: Getmid♪\n    • Note: Type "+ setKey +"Abort For Done \n    • Status: Success")                                                            
        if wait['gettimelinecontact']:
            mid = msg.contentMetadata['mid']
            stealtimeline(to,mid, "Steal")
            rahman(to, "「 Steal 」\n › Type: Gettimeline♪\n    • Note: Type "+ setKey +"Abort For Done \n    • Status: Success")                                                              
        if wait['getstorycontact']:
            mid = msg.contentMetadata['mid']
            stealstory(to,mid)
            rahman(to, "「 Steal 」\n › Type: Getstory♪\n    • Note: Type "+ setKey +"Abort For Done \n    • Status: Success")                                                              
        if wait["wfriendlist"] == True:
            mid = msg.contentMetadata['mid']
            n = len(maxbots.getAllContactIds())
            finded(mid)            
            t = len(maxbots.getAllContactIds())
            rahman(to, f"「 Friend 」\n › Type: Friend Add♪\n    • Before: {n} \n    • After: {t}\n    • Note: Type {setKey}Abort For Done\n    • Status: Success")
        if wait["dfriendlist"] == True:
            if msg.contentMetadata["mid"] in maxbots.getAllContactIds():
                maxbots.deleteContact(msg.contentMetadata["mid"])
                maxbots.sendTag(to,"「 Friend 」\n › Type: Friend Del♪\n    • 1. @! Del♪\n › Note: Type "+ setKey +"Abort For Done",[msg.contentMetadata["mid"]])                                  
            else:
                maxbots.sendTag(to,"「 Friend 」\n › Type: Friend Del♪\n    • 1. @! Nothing♪\n › Note: Type "+ setKey +"Abort For Done",[msg.contentMetadata["mid"]])       
        if wait["wblocklist"] == True:
            mid = msg.contentMetadata['mid']
            n = len(maxbots.getAllContactIds())
            maxbots.blockContact(mid)            
            t = len(maxbots.getAllContactIds())
            rahman(to, f"「 Friend 」\n › Type: Block Add♪\n    • Before: {n} \n    • After: {t}\n    • Note: Type {setKey}Abort For Done\n    • Status: Success")
        if wait["dblocklist"] == True:
            mid = msg.contentMetadata['mid']
            n = len(maxbots.getAllContactIds())
            maxbots.unblockContact(mid)            
            t = len(maxbots.getAllContactIds())
            rahman(to, f"「 Friend 」\n › Type: Block Del♪\n    • Before: {n} \n    • After: {t}\n    • Note: Type {setKey}Abort For Done\n    • Status: Success")
        if settings["updateProfile"]:
            mid = msg.contentMetadata['mid']  
            namaa = settings["msgbroadcast"]  
            b = maxbots.getContact(mid).displayName
            finded(mid)
            maxbots.renameContact(mid,namaa)
            maxbots.sendTag(to, f"「 Friend 」\n › Type: Rename♪\n    • Target: @!\n    • Before: {b}\n    • After: {namaa}\n    • Note: Type {setKey}Abort For Done\n    • Status: Succes",[mid])                            
        if wait["wblacklist"] == True:
            if msg.contentMetadata["mid"] in position["blacklist"]:
                maxbots.sendTag(to,"「 Banning 」\n › Type: Bl Add♪\n    • 1. @! Already♪\n › Note: Type "+ setKey +"Abort For Done",[msg.contentMetadata["mid"]])                                     
            else:
                time.sleep(0.5)
                position["blacklist"].append(msg.contentMetadata["mid"])
                maxbots.sendTag(to,"「 Banning 」\n › Type: Bl Add♪\n    • 1. @! Add♪\n › Note: Type "+ setKey +"Abort For Done",[msg.contentMetadata["mid"]])                                     
        if wait["dblacklist"] == True:
            if msg.contentMetadata["mid"] in position["blacklist"]:
                time.sleep(0.5)
                position["blacklist"].remove(msg.contentMetadata["mid"])
                maxbots.sendTag(to,"「 Banning 」\n › Type: Bl Del♪\n    • 1. @! Del♪\n › Note: Type "+ setKey +"Abort For Done",[msg.contentMetadata["mid"]])       
            else:
                maxbots.sendTag(to,"「 Banning 」\n › Type: Bl Del♪\n    • 1. @! Nothing♪\n › Note: Type "+ setKey +"Abort For Done",[msg.contentMetadata["mid"]])       
        if wait["wwhitelist"] == True:
            if msg.contentMetadata["mid"] in position["whitelist"]:
                maxbots.sendTag(to,"「 Banning 」\n › Type: Wl Add♪\n    • 1. @! Already♪\n › Note: Type "+ setKey +"Abort For Done",[msg.contentMetadata["mid"]])       
            else:
                time.sleep(0.5)
                position["whitelist"].append(msg.contentMetadata["mid"])
                maxbots.sendTag(to,"「 Banning 」\n › Type: Wl Add♪\n    • 1. @! Add♪\n › Note: Type "+ setKey +"Abort For Done",[msg.contentMetadata["mid"]])            
        if wait["dwhitelist"] == True:
            if msg.contentMetadata["mid"] in position["whitelist"]:
                time.sleep(0.5)
                position["whitelist"].remove(msg.contentMetadata["mid"])
                maxbots.sendTag(to,"「 Banning 」\n › Type: Wl Del♪\n    • 1. @! Del♪\n › Note: Type "+ setKey +"Abort For Done",[msg.contentMetadata["mid"]])                                  
            else:
                maxbots.sendTag(to,"「 Banning 」\n › Type: Wl Del♪\n    • 1. @! Nothing♪\n › Note: Type "+ setKey +"Abort For Done",[msg.contentMetadata["mid"]])       
        if wait["wadminlist"] == True:
            if msg.contentMetadata["mid"] in position["admin"]:
                maxbots.sendTag(to,"「 Banning 」\n › Type: Admin Add♪\n    • 1. @! Already♪\n › Note: Type "+ setKey +"Abort For Done",[msg.contentMetadata["mid"]])       
            else:
                time.sleep(0.5)
                position["admin"].append(msg.contentMetadata["mid"])
                maxbots.sendTag(to,"「 Banning 」\n › Type: Admin Add♪\n    • 1. @! Add♪\n › Note: Type "+ setKey +"Abort For Done",[msg.contentMetadata["mid"]])                          
        if wait["dadminlist"] == True:
            if msg.contentMetadata["mid"] in position["admin"]:
                time.sleep(0.5)
                position["admin"].remove(msg.contentMetadata["mid"])
                maxbots.sendTag(to,"「 Banning 」\n › Type: Admin Del♪\n    • 1. @! Del♪\n › Note: Type "+ setKey +"Abort For Done",[msg.contentMetadata["mid"]])                                                
            else:
                maxbots.sendTag(to,"「 Banning 」\n › Type: Admin Del♪\n    • 1. @! Nothing♪\n › Note: Type "+ setKey +"Abort For Done",[msg.contentMetadata["mid"]])                                     
        if wait["wtalkbanlist"] == True:
            if msg.contentMetadata["mid"] in position["talkbanlist"]:
                maxbots.sendTag(to,"「 Banning 」\n › Type: Tban Add♪\n    • 1. @! Already♪\n › Note: Type "+ setKey +"Abort For Done",[msg.contentMetadata["mid"]])       
            else:
                time.sleep(0.5)
                position["talkbanlist"].append(msg.contentMetadata["mid"])
                maxbots.sendTag(to,"「 Banning 」\n › Type: Tban Add♪\n    • 1. @! Add♪\n › Note: Type "+ setKey +"Abort For Done",[msg.contentMetadata["mid"]])                                            
        if wait["dtalkbanlist"] == True:
            if msg.contentMetadata["mid"] in position["talkbanlist"]:
                time.sleep(0.5)
                position["talkbanlist"].remove(msg.contentMetadata["mid"])
                maxbots.sendTag(to,"「 Banning 」\n › Type: Tban Del♪\n    • 1. @! Del♪\n › Note: Type "+ setKey +"Abort For Done",[msg.contentMetadata["mid"]])                
            else:
                maxbots.sendTag(to,"「 Banning 」\n › Type: Tban Del♪\n    • 1. @! Nothing♪\n › Note: Type "+ setKey +"Abort For Done",[msg.contentMetadata["mid"]])       
        if settings["Addfakecontact"]["status"] == True:
            listsett["fakecontactt"][settings["Addfakecontact"]["name"]] = msg.contentMetadata["mid"]
            rahman(to,"「 Mention 」\n › Type: Add Fakecontact♪\n    • Name : {}\n    • Status: Success".format(str(settings["Addfakecontact"]["name"])))
            settings["Addfakecontact"]["status"] = False
            settings["Addfakecontact"]["name"] = ""                                                                                                    
        if settings["Addcontact"]["status"] == True:
            listsett["contactt"][settings["Addcontact"]["name"]] = msg.contentMetadata["mid"]
            rahman(to,"「 List 」\n › Type: Contact Add♪\n    • Name : {}\n    • Status: Success".format(str(settings["Addcontact"]["name"])))
            settings["Addcontact"]["status"] = False
            settings["Addcontact"]["name"] = ""                                                                  
        if settings["Addkibaran"]["status"] == True:
            listsett["kibarann"][settings["Addkibaran"]["name"]].append(msg.contentMetadata["mid"])
            maxbots.sendMessage(to, "• Type "+ setKey +"Abort For Done")               
        if to in position['timebc']:
            time.sleep(0.8)
            position["multibc"].append(msg.contentMetadata["mid"])
            maxbots.sendMessage(to, "• Type `"+ setKey +"Send Broadcast` For Done")               
    if msg.contentType == 16:
        if to in position['timebc']:
            time.sleep(0.8)
            mmk = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
            position["multibc"].append(mmk[1])
            maxbots.sendMessage(to, "• Type `"+ setKey +"Send Broadcast` For Done")               
        if settings["Check"]["post"]:
            if msg.contentMetadata['serviceType'] in ['GB', 'NT', 'MH']:
                if msg.contentMetadata['serviceType'] in ['GB', 'NT']:
                    contact = maxbots.getContact(sender)
                    author = contact.displayName                                                        
                else:
                    author = msg.contentMetadata['serviceName']
                arifblek = "「 Check 」\n › Type: Post♪"
                arifblek += f"\n    • Creator : {author}"
                arifblek += f"\n    • Post : {msg.contentMetadata['postEndUrl']}"                                
                rahman(to, arifblek)
def notif_public(op):
    msg      = op.message
    text     = str(msg.text)
    msg_id   = msg.id
    receiver = msg.to
    sender   = msg._from
    to       = sender if not msg.toType and sender != myMid else receiver
    txt      = text.lower()
    pub      = publiccmd(txt)
    if sender in position["talkbanlist"] and to not in position['silent']:
        kicked(to, sender)                
    if msg.contentType in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21] and to not in position['silent']:
        if msg.toType == 0:
            if settings["AutoRead"]["all"]:
                maxbots.sendChatChecked(to, msg_id)                       
        if msg.toType == 0 and not msg.toType == 2:
            if settings["AutoRead"]["pc"]:
                maxbots.sendChatChecked(to, msg_id)                        
        if msg.toType == 2:
            if settings["AutoRead"]["gc"]:
                maxbots.sendChatChecked(to, msg_id)                        
    if msg.contentType != 0:
        if settings['Detect']['faketag']:
            if 'MENTION' in msg.contentMetadata:
                tipenya = {1: "IMAGE",2: "VIDEO",3: "AUDIO",4: "HTML",5: "PDF",6: "CALL",7: "STICKER",8: "PRESENCE",9: "GIFT",10: "GROUPBOARD",11: "APPLINK",12: "LINK",13: "CONTACT",14: "FILE",15: "LOCATION",16: "POSTNOTIFICATION",17: "RICH",18: "CHATEVENT",19: "MUSIC",20: "PAYMENT",21: "EXTIMAGE",22: "FLEX"}
                lahkontol = '「 Detect 」\n ›Type: Faketag♪\n    • Type: {}\n    • Sender: @! \n    • {}'.format(tipenya[msg.contentType],settings['Detect']['msgfaketag'])
                maxbots.sendTag(to, lahkontol, [sender])                                      
    if msg.contentType == 6 and to not in position['silent']:
            if msg.toType == 0:
                if op.type != 50 and settings["Detect"]["spamcall"] == True:
                    if msg.contentMetadata["GC_EVT_TYPE"] == "I":
                        if sender in last_game["spamer"]:
                            if len(last_game["spamer"][sender]["list"]) > 1:
                                try:
                                    ktl = settings['Detect']["msgspamcall"]
                                    mmk = settings['Detect']['sticons']                                                        
                                    if '(' not in ktl:
                                        maxbots.sendMessage(sender, ktl)
                                    else:
                                        if '@!' not in ktl:
                                            maxbots.sendMessage(sender, ktl,mmk, 0)  
                                        else:
                                             if '(' in ktl:
                                                 maxbots.sendMentionEmot(sender,ktl, mmk, "Detect", settings, [sender])
                                             else:
                                                 maxbots.sendTag(sender, ktl, [sender])         
                                except:pass
                                del last_game["spamer"][sender]
                                maxbots.blockContact(sender)
                                last_game["spamertime"][sender] = {"time": str(datetime.now(tz=pytz.timezone("Asia/Jakarta"))+timedelta(minutes=1))}                      
                            else:
                                last_game["spamer"][sender]["list"].append(sender)
                        else:
                            last_game["spamer"][sender] = {"list": []}
                            last_game["spamer"][sender]["list"].append(sender)     
                                                    
            if msg.toType == 2 and sender not in myMid:
                if settings['Detect']['callgroup'] == True:
                    if to not in limited["call"]:
                        limited["call"][to] = time.time()
                    b = msg.contentMetadata['GC_EVT_TYPE']
                    c = msg.contentMetadata["GC_MEDIA_TYPE"]
                    name = maxbots.getChats([to]).chats[0].chatName
                    if c == "VIDEO" and b == "S":
                        a = '「 Detect 」'
                        a += "\n › Type: Callgroup♪"
                        a += "\n    • Started Group {}".format(c)
                        a += "\n    • Type: {}".format(c)
                        a += "\n    • Group: {}".format(name)
                        a += "\n    • Started: {}".format(humanize.naturaltime(datetime.fromtimestamp(msg.createdTime/1000)))
                        a += "\n    • Host: @!"
                        maxbots.sendTag(to, str(a), [sender])
                    if c == 'AUDIO' and b == "S":
                        a = '「 Detect 」'
                        a += "\n › Type: Callgroup♪"
                        a += "\n    • Started Group {}".format(c)
                        a += "\n    • Type: {}".format(c)
                        a += "\n    • Group: {}".format(name)
                        a += "\n    • Started: {}".format(humanize.naturaltime(datetime.fromtimestamp(msg.createdTime/1000)))
                        a += "\n    • Host: @!"
                        pict = "https://obs.line-scdn.net/{}".format(maxbots.getContact(sender).pictureStatus)
                        name2 = maxbots.getContact(sender).displayName
                        nows = "Now"
                        result = flexklr.kalerastartcall(pict, name2, name, nows)
                        if settings["stattemp"] == True:
                            sendTemplate(to,{"type": "flex", "altText": settings["footerlabel"], "contents": {"type": "carousel", "contents": [result]}})
                        elif settings["statfooter"] == True:
                            sendTemplate(to,{"type": "flex", "altText": settings["footerlabel"], "contents": {"type": "carousel", "contents": [result]}})
                        else:
                            maxbots.sendTag(to, str(a), [sender])
                    else:
                        if to in limited["call"]:
                            wktt = time.time() - limited["call"][to]
                        else:wktt = "None"
                        if c == "VIDEO" and b == "E":
                            a = '「 Detect 」'
                            a += "\n › Type: Callgroup♪"
                            a += "\n    • Ended Group {}".format(c)
                            a += "\n    • Type: {}".format(c)
                            a += "\n    • Group: {}".format(name)
                            a += "\n    • Duration: " + format_timespan(wktt)
                            a += "\n    • Host: @!"
                            maxbots.sendTag(to, str(a), [sender])
                        if c == "AUDIO" and b == "E":
                            a = '「 Detect 」'
                            a += "\n › Type: Callgroup♪"
                            a += "\n    • Ended Group {}".format(c)
                            a += "\n    • Type: {}".format(c)
                            a += "\n    • Group: {}".format(name)
                            a += "\n    • Duration: " + format_timespan(wktt)
                            a += "\n    • Host: @!"
                            pict = "https://obs.line-scdn.net/{}".format(maxbots.getContact(sender).pictureStatus)
                            name2 = maxbots.getContact(sender).displayName
                            nows = format_timespan(wktt)
                            result = flexklr.kaleraendcall(pict, name2, name, nows)
                            if settings["stattemp"] == True:
                                sendTemplate(to,{"type": "flex", "altText": settings["footerlabel"], "contents": {"type": "carousel", "contents": [result]}})
                            elif settings["statfooter"] == True:
                                sendTemplate(to,{"type": "flex", "altText": settings["footerlabel"], "contents": {"type": "carousel", "contents": [result]}})
                            else:
                                maxbots.sendTag(to, str(a), [sender])
                        del limited["call"][to]
    if msg.contentType == 0 and to not in position['silent']:
        if msg.toType != 0 and msg.toType == 2:
            if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
                names = re.findall(r'@(\w+)', text);mention = ast.literal_eval(msg.contentMetadata['MENTION']);mentionees = mention['MENTIONEES']                                                
                for mention in mentionees:
                    if myMid in mention["M"]:
                        if maxbots.getProfile().mid in mention["M"]:
                            if to not in position['ROM']:
                                position['ROM'][to] = {}                                        
                            if sender not in position['ROM'][to]:
                                position['ROM'][to][sender] = {}                                       
                            if 'msg.id' not in position['ROM'][to][sender]:
                                position['ROM'][to][sender]['msg.id'] = []                                        
                            if 'waktu' not in position['ROM'][to][sender]:
                                position['ROM'][to][sender]['waktu'] = []                                        
                            position['ROM'][to][sender]['msg.id'].append(msg.id)
                            position['ROM'][to][sender]['waktu'].append(msg.createdTime)                               
            if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys() and sender != myMid and msg.contentType not in [6, 7, 9] and msg.toType in [1, 2]:
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                mentionees = [mention['M'] for mention in mentions['MENTIONEES']]
                if myMid in mentionees:
                    if maxbots.getProfile().displayName in text:
                            if to not in limited["notifi"]:
                               limited["notifi"][to] = time.time()                    
                            if time.time() <= limited["notifi"][to]:
                               pass
                            else:  
                               notifi3(to, sender, text)
                               limited["notifi"][to] = time.time() + 5                               
            if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
                if msg._from not in myMid:
                    if to in position['mentionkick']:   
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            if myMid in mention["M"]:
                                if maxbots.getProfile().mid in mention["M"]:
                                    ktl = settings['mentionkickmsg']["msg"]
                                    mmk = settings['mentionkickmsg']['sticons']                                                        
                                    if '(' not in ktl:
                                        rahman(to, ktl)
                                    else:
                                        if '@!' not in ktl:
                                            maxbots.sendMessage(to, ktl,mmk, 0)  
                                        else:
                                             if '(' in ktl:
                                                 maxbots.sendMentionEmot(to,ktl, mmk, "mentionkickmsg", settings, [sender])
                                             else:
                                                 maxbots.sendTag(to, ktl, [sender])         
                                    kicked(msg.to, msg._from)                                            
                                    break
    if msg.contentType == 0 and to not in position['silent']:               
        if txt == 'rname':
            if settings["modepublic"] or msg._from in position["admin"] or msg._from in position["creator"]:
                maxbots.sendMessage(to, settings["setKey"]["rname"])                                                
        if txt == 'ping':
            if msg._from in position["creator"]:
                maxbots.sendTag(to, "PONG @!", [sender])
        if pub.startswith('say') or commandMen(msg, text, 'say'):
            if msg._from in position["creator"]:
                ktl = text.split("say ")[1]
                maxbots.sendMessage(to, ktl)                                                
        if pub == 'help':
            if settings["modepublic"] and msg._from not in position["admin"]:
                rahman(to, helppublic())                        
        if pub == 'help':
            if msg._from in position["admin"]:
                rahman(to, helpadmin())                        
        if pub == 'tagall':
            if settings["modepublic"] or msg._from in position["admin"]:
                if msg.toType == 1:
                    members = cektagallM(to)                             
                elif msg.toType == 2:
                    members = cekmember(to)               
                else:
                    return rahman(to,   "「 Mention 」\n › Type: Tagall♪\n    • Status: Failed Tagall")                                     
                if members:
                    tagallMention(to, members)
        if pub.startswith('sider'):
            if msg._from in position["admin"]:
                mmk = pub.replace(pub.split(" ")[0] + ' ','')                         
                statCCTV(to, mmk)                                                   
        if pub.startswith('unsend'):
            if msg._from in position["admin"]:
                sep = msg.text.split("send ")
                args = msg.text.replace(sep[0] + "send ","")
                mes = int(sep[1])
                M = maxbots.getRecentMessagesV2(to, 1001)
                MId = []                                            
                for ind,i in enumerate(M):
                    if ind == 0:
                        pass                   
                    else:
                        if i._from == maxbots.profile.mid:
                            MId.append(i.id)
                            if len(MId) == mes:
                                break                           
                def unsMes(id):
                    maxbots.unsendMessage(id)               
                for i in MId:
                    thread1 = threading.Thread(target=unsMes, args=(i,))
                    thread1.daemon = True
                    thread1.start()
                    thread1.join()                                                            
                maxbots.unsendMessage(msg.id)              
        if pub == 'getcall':
            if settings["modepublic"] or msg._from in position["admin"]:
                callGet(to)                            
        if pub == 'openqr':
            if settings["modepublic"] or msg._from in position["admin"]:
                tol = qrOpen(to)
                if tol:
                    maxbots.sendMessage(to,"「 Group 」\n › Type: Openqr♪\n    • Link: line://ti/g/{} \n    • Status: Success".format(tol))       
        if pub == 'closeqr':
            if settings["modepublic"] or msg._from in position["admin"]:
                qrClose(to)
                rahman(to,"「 Group 」\n › Type: Closeqr♪\n    • Status: Success") 
        if pub == 'jodohku':
            if settings["modepublic"] or msg._from in position["admin"]:
                ktl = cekmember(to)
                psntunggu = ["Bentar Ya Kak @!","Wait Bos @!","Oke Bentar Gua Cariin @!","Si Jomblo Nyari Jodoh Bentar @!"]
                psnyangberjdh = ["Nah Gua Jumpa Ni Jodoh Lu @!, Ni Jodoh Lu @! Silakan Callan","Waduh Bre @! Nah Jodohlu @!, Gih Ngewe","Semoga lu @! Dengan @! Langgeng Ya,Kalian Berjodoh","Ni Gua Dapat Bre @! Ni Lu Kenalan Dulu Sama @!, Mana Tau Nyaman"]
                yangberjodoh = random.choice(ktl)
                kautunggu = random.choice(psntunggu)
                akhirnyadapat = random.choice(psnyangberjdh)
                maxbots.sendMentionV2(msg_id,to, kautunggu,[sender])
                time.sleep(0.5)
                maxbots.sendMentionV2(msg_id,to,akhirnyadapat,[sender,yangberjodoh])  
                maxbots.sendContact(to, yangberjodoh) 
        if pub.startswith('persen cinta'):
            if settings["modepublic"] or msg._from in position["admin"]:
                tanya = pub.replace(pub.split(" ")[0] + ' ','')                
                jawab = ("0%","25%","50%","75%","100%")
                jawaban = random.choice(jawab)
                time.sleep(0.8)
                maxbots.sendMessage(to,jawaban)
        if pub.startswith('truth or dare'):
            if settings["modepublic"] or msg._from in position["admin"]:
                hotel = geTmention(msg)
                for ngewe in hotel:
                    ktl = ["Hai @! Kamu Harus Truth","Hai @! Kamu Harus Dare","Truth Aja Deh Lu @!","Mending Lu Dare @!","Yahahah Kamu Kena Truth @!","Hayolo @! Kena Truth Deh lu","Harus Terima Ya Kamu Kena Truth @!","Yahahah Kamu Kena Dare @!","Hayolo @! Kena Dare Deh lu","Harus Terima Ya Kamu Kena Dare @!","Dar Der Dor @! Truth Ya Bukan Dare"]
                    mmk = random.choice(ktl)
                    maxbots.sendTag(to,mmk,[ngewe])
        if pub.startswith('invite'):
            if msg._from in position["admin"]:
                if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
                    lists = geTmention(msg)
                    for ls in lists:
                        invited(to, ls)                                                                        
                else:
                    if msg.relatedMessageId is not None:
                        aa = maxbots.getRecentMessagesV2(to, 1001)
                        for bb in aa:
                            if bb.id in msg.relatedMessageId:
                                invited(to, bb._from)                                                                                                                                	
        if pub.startswith('kick'):
            if msg._from in position["admin"]:
                if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
                    lists = geTmention(msg)
                    for ls in lists:
                        kicked(to, ls)                                    
                else:
                    if msg.relatedMessageId is not None:
                        aa = maxbots.getRecentMessagesV2(to, 1001)
                        for bb in aa:
                            if bb.id in msg.relatedMessageId:
                                kicked(to, bb._from)                                            
        if pub.startswith('getpict'):
            if settings["modepublic"] or msg._from in position["admin"]:
                if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
                    lists = geTmention(msg)
                    for ls in lists:
                        stealpict(to, ls)
                else:
                    if msg.relatedMessageId is not None:
                        aa = maxbots.getRecentMessagesV2(to, 1001)
                        for bb in aa:
                            if bb.id in msg.relatedMessageId:
                                stealpict(to, bb._from)                                                                                                                                                                                                                     
        if pub.startswith('getcover'):
            if settings["modepublic"] or msg._from in position["admin"]:
                if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
                    lists = geTmention(msg)
                    for ls in lists:
                        stealcover(to, ls)
                else:
                    if msg.relatedMessageId is not None:
                        aa = maxbots.getRecentMessagesV2(to, 1001)
                        for bb in aa:
                            if bb.id in msg.relatedMessageId:
                                stealcover(to, bb._from)
        if pub.startswith('getname'):
            if settings["modepublic"] or msg._from in position["admin"]:
                if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
                    lists = geTmention(msg)
                    for ls in lists:
                        stealname(to, ls, "Steal")
                else:
                    if msg.relatedMessageId is not None:
                        aa = maxbots.getRecentMessagesV2(to, 1001)
                        for bb in aa:
                            if bb.id in msg.relatedMessageId:
                                stealname(to, bb._from, "Steal")       
        if pub.startswith('getbio'):
            if settings["modepublic"] or msg._from in position["admin"]:
                if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
                    lists = geTmention(msg)
                    for ls in lists:
                        stealbio(to, ls, "Steal")
                else:
                    if msg.relatedMessageId is not None:
                        aa = maxbots.getRecentMessagesV2(to, 1001)
                        for bb in aa:
                            if bb.id in msg.relatedMessageId:
                                stealbio(to, bb._from, "Steal")
        if pub.startswith('getmid'):
            if settings["modepublic"] or msg._from in position["admin"]:
                if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
                    lists = geTmention(msg)
                    for ls in lists:
                        stealmid(to, ls)
                else:
                    if msg.relatedMessageId is not None:
                        aa = maxbots.getRecentMessagesV2(to, 1001)
                        for bb in aa:
                            if bb.id in msg.relatedMessageId:
                                stealmid(to, bb._from)                     
        if pub.startswith('getcontact'):
            if settings["modepublic"] or msg._from in position["admin"]:
                if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
                    lists = geTmention(msg)
                    for ls in lists:
                        stealcontact(to, ls)
                else:
                    if msg.relatedMessageId is not None:
                        aa = maxbots.getRecentMessagesV2(to, 1001)
                        for bb in aa:
                            if bb.id in msg.relatedMessageId:
                                stealcontact(to, bb._from)
        if pub.startswith('getvideo'):
            if settings["modepublic"] or msg._from in position["admin"]:
                if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
                    lists = geTmention(msg)
                    for ls in lists:
                        stealvideo(to, ls)	
                else:
                    if msg.relatedMessageId is not None:
                        aa = maxbots.getRecentMessagesV2(to, 1001)
                        for bb in aa:
                            if bb.id in msg.relatedMessageId:
                                stealvideo(to, bb._from)                             
        if settings['mimic']['status']:
            if sender in settings['mimic']['target'] and settings['mimic']['target'][sender]:
                try:
                    maxbots.sendMessage(to, text, msg.contentMetadata);tmp_text.append(text)
                except:
                    pass
        if settings['autoRespond']['status']:
            if msg.toType == 0:
                contact = maxbots.getContact(sender)
                if contact.attributes != 32 and 'MENTION' not in msg.contentMetadata.keys():
                    mentext2(to, sender, settings['autoRespond']['message'])           
        if settings['emojiresponchat']['status']:
            if msg.toType == 0:
                contact = maxbots.getContact(sender)
                if contact.attributes != 32:
                    sendEmo2(to,sender, settings['emojiresponchat']['message'], settings['emojiresponchat']['sticons'], "emojiresponchat")
        if settings['responstickerchat']:
            if msg.toType == 0:
                contact = maxbots.getContact(sender)
                if contact.attributes != 32:
                    maxbots.sendSticker(to,settings,"stcchat")
        if settings['autoRespondMention']['status']:
             if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION']);mentionees = [mention['M'] for mention in mentions['MENTIONEES']]                        
                if myMid in mentionees:
                    if to not in limited:limited[to] = time.time()                                
                    if time.time() <= limited[to]:
                        pass
                    else:
                        if settings["stattemp"] == True:
                            profile = maxbots.getContact(sender)
                            username = profile.displayName
                            if profile.pictureStatus:
                                picture = "https://obs.line-scdn.net/"+str(profile.pictureStatus)
                            else:
                                picture = "https://s20.directupload.net/images/220423/uxdxnp5a.jpg"
                            if "@!" in settings['autoRespondMention']['message']:
                                message = settings['autoRespondMention']['message'].replace("@!",username)
                            else:
                                message = settings['autoRespondMention']['message']
                            data = {
                              "type": "bubble",
                              "size": "kilo",
                              "header": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                  {
                                    "type": "image",
                                    "url": "https://www.linkpicture.com/q/ryansLamp.png",
                                    "aspectRatio": "190:35",
                                    "size": "full",
                                    "aspectMode": "cover",
                                    "animated": True
                                  },
                                  {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                      {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                          {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "offsetStart": "15px",
                                            "width": "1px",
                                            "backgroundColor": "#ffffff",
                                            "height": "85%",
                                            "offsetTop": "7.5%"
                                          },
                                          {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                              {
                                                "type": "text",
                                                "text": message.upper(), #YOUR TEXT
                                                "weight": "bold",
                                                "size": "8px",
                                                "color": "#FFFFFF",
                                                "wrap": True,
                                                "maxLines": 3
                                              }
                                            ],
                                            "paddingEnd": "2.5px",
                                            "paddingStart": "25px",
                                            "position": "absolute",
                                            "width": "100%",
                                            "height": "85%",
                                            "offsetTop": "7.5%",
                                            "justifyContent": "center"
                                          }
                                        ],
                                        "offsetTop": "4px",
                                        "offsetEnd": "5px",
                                        "offsetStart": "40px",
                                        "offsetBottom": "4px",
                                        "position": "absolute",
                                        "cornerRadius": "6px",
                                        "backgroundColor": "#50505095"
                                      },
                                      {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                          {
                                            "type": "image",
                                            "url": "https://i.ibb.co/WD3bWv4/kalera-circle-1.png",
                                            "aspectMode": "cover",
                                            "size": "full",
                                            "animated": True
                                          },
                                          {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                              {
                                                "type": "image",
                                                "url": picture,
                                                "size": "full",
                                                "aspectRatio": "1:1",
                                                "aspectMode": "cover"
                                              }
                                            ],
                                            "width": "80%",
                                            "height": "80%",
                                            "paddingAll": "0px",
                                            "cornerRadius": "100px",
                                            "position": "absolute",
                                            "offsetTop": "10%",
                                            "offsetStart": "10%"
                                          }
                                        ],
                                        "width": "45px",
                                        "height": "45px",
                                        "paddingAll": "0px",
                                        "cornerRadius": "100px",
                                        "offsetTop": "1.275px",
                                        "offsetStart": "5px",
                                        "backgroundColor": "#000000"
                                      }
                                    ],
                                    "position": "absolute",
                                    "width": "100%",
                                    "height": "100%",
                                    "backgroundColor": "#00000050"
                                  }
                                ],
                                "paddingAll": "0px"
                              },
                              "styles": {
                                "header": {
                                  "backgroundColor": "#000000"
                                }
                              }
                            }
                            sendTemplate(to,{"type": "flex", "altText": "Auto Respone", "contents": data})
                            limited[to] = time.time() + 15
                        else:
                            if '@!' not in settings['autoRespondMention']['message']:
                                maxbots.sendReplyMessage(msg_id,to, settings['autoRespondMention']['message'])
                                limited[to] = time.time() + 15                                                                                    
                            else:
                                maxbots.sendMentionV2(msg_id,to, settings['autoRespondMention']['message'], [sender])
                                limited[to] = time.time() + 15
        if settings['emojirespontag']['status']:
             if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
                mentions = ast.literal_eval(msg.contentMetadata['MENTION']);mentionees = [mention['M'] for mention in mentions['MENTIONEES']]                       
                if myMid in mentionees:
                    if to not in limited["respontagemo"]:
                        limited["respontagemo"][to] = time.time()                                
                    if time.time() <= limited["respontagemo"][to]:
                        pass
                    else:
                        ktl = settings['emojirespontag']['message']
                        mmk = settings['emojirespontag']['sticons']                                                                        
                        if '(' not in ktl:
                            maxbots.sendReplyMessage(msg_id,to,'',mmk)                                                     
                        else:
                            if '@!' not in ktl:
                                maxbots.sendReplyMessage(msg_id,to, ktl,mmk)                                                    
                            else:
                                maxbots.sendMentionReplyEmot(msg_id,to, ktl,mmk, settings, [sender])
                        limited["respontagemo"][to] = time.time() + 15                                                                                        
        if settings['responstickertag']:
             if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
                mentions = ast.literal_eval(msg.contentMetadata['MENTION']);mentionees = [mention['M'] for mention in mentions['MENTIONEES']]                        
                if myMid in mentionees:
                    if to not in limited["respontagstc"]:
                        limited["respontagstc"][to] = time.time()                                
                    if time.time() <= limited["respontagstc"][to]:
                        pass
                    else:
                        try:
                            if "STK_MESSAGE" in settings['stcmention']: 
                                maxbots.sendReplyMessage(msg_id,to, "", settings['stcmention'], 7)
                            else:
                                if "STK_IMG_TXT" in settings['stcmention']:
                                    maxbots.sendReplyMessage(msg_id,to, "", settings['stcmention'], 7)
                                else:
                                   maxbots.sendReplyMessage(msg_id,to, "", settings['stcmention'], 7)
                            limited["respontagstc"][to] = time.time() + 15                                	                                                                                                                                                                                                
                        except:pass
    lastSEEN(to, sender)             
def notif_saveunsend(op):
    msg = op.message
    text = str(msg.text)
    msg_id = msg.id
    receiver = msg.to
    sender = msg._from
    to = msg.to
    cmd = command(text)
    if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
        if msg.toType == 0 and sender != myMid: to = sender
        else:to = receiver
        if to in position['detectunsend']:   
           try:
               msg = op.message
               if msg.contentType == 1 or msg.contentType == 2 or msg.contentType == 3 or msg.contentType == 14:
                   print(msg.contentMetadata)
                   if 'DOWNLOAD_URL' in msg.contentMetadata:
                       linkus = maxbots.downloadFileURL(msg.contentMetadata['DOWNLOAD_URL'])
                       last_game["msg_dict"][msg.id] = {"text": msg.text, "from": msg._from, "to": to, "createdTime": time.time(), "contentType": msg.contentType, "contentMetadata": msg.contentMetadata, "path": linkus}
                   else:
                       linkus = maxbots.downloadObjectMsg(msg_id)
                       last_game["msg_dict"][msg.id] = {"text": msg.text, "from": msg._from, "to": to, "createdTime": time.time(), "contentType": msg.contentType, "contentMetadata": msg.contentMetadata, "path": linkus}
               else:
                   last_game["msg_dict"][msg.id] = {"text": msg.text, "from": msg._from, "to": to, "createdTime": time.time(), "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
           except Exception as e:print(e)
        elif msg.toType == 1:
            to = receiver
            if to in position['detectunsend']:   
                try:
                    msg = op.message
                    if msg.contentType == 1 or msg.contentType == 2 or msg.contentType == 3 or msg.contentType == 14:
                        if 'DOWNLOAD_URL' in msg.contentMetadata:
                            linkus = maxbots.downloadFileURL(msg.contentMetadata['DOWNLOAD_URL'])
                            last_game["msg_dict"][msg.id] = {"text": msg.text, "from": msg._from, "to": to, "createdTime": time.time(), "contentType": msg.contentType, "contentMetadata": msg.contentMetadata, "path": linkus}
                        else:
                            linkus = maxbots.downloadObjectMsg(msg_id)
                            last_game["msg_dict"][msg.id] = {"text": msg.text, "from": msg._from, "to": to, "createdTime": time.time(), "contentType": msg.contentType, "contentMetadata": msg.contentMetadata, "path": linkus}
                    else:
                        last_game["msg_dict"][msg.id] = {"text": msg.text, "from": msg._from, "to": to, "createdTime": time.time(), "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                except Exception as e:print(e)
        elif msg.toType == 2:
            to = receiver
            if to in position['detectunsend']:   
                try:
                    msg = op.message
                    if msg.contentType == 1 or msg.contentType == 2 or msg.contentType == 3 or msg.contentType == 14:
                        if 'DOWNLOAD_URL' in msg.contentMetadata:
                            linkus = maxbots.downloadFileURL(msg.contentMetadata['DOWNLOAD_URL'])
                            last_game["msg_dict"][msg.id] = {"text": msg.text, "from": msg._from, "to": to, "createdTime": time.time(), "contentType": msg.contentType, "contentMetadata": msg.contentMetadata, "path": linkus}
                        else:
                            linkus = maxbots.downloadObjectMsg(msg_id)
                            last_game["msg_dict"][msg.id] = {"text": msg.text, "from": msg._from, "to": msg.to, "createdTime": time.time(), "contentType": msg.contentType, "contentMetadata": msg.contentMetadata, "path": linkus}
                    else:
                        last_game["msg_dict"][msg.id] = {"text": msg.text, "from": msg._from, "to": msg.to, "createdTime": time.time(), "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                except Exception as e:print(e)       
def notif_unsend(op):
    if op.param1 not in position['silent']:               
        if op.param1 in position['detectunsend']:   
            try:
                try:
                    msg = op.message
                    at = op.param1
                    msg_id = op.param2
                    if at not in limited["uns"]:
                        limited["uns"][at] = time.time()
                    if time.time() <= limited["uns"][at]:pass
                    else:
                        if msg_id in last_game["msg_dict"]:
                            contact = maxbots.getContact(last_game["msg_dict"][msg_id]["from"])
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.fromtimestamp(last_game["msg_dict"][msg_id]["createdTime"], tz=tz)
                            waktuunsend = datetime.strftime(timeNow,"%H:%M:%S")
                            ret_ = "「 Detect 」\n › Unsend Message"
                            ret_ += "\n    • Sender: @!"
                            ret_ += "\n    • Send Time: {} WIB".format(str(waktuunsend))
                            if last_game["msg_dict"][msg_id]["contentType"] == 0:
                                ret_ += "\n    • Type: Text"
                                ret_ += "\n    • Text: {}".format(str(last_game["msg_dict"][msg_id]["text"]))
                                maxbots.sendTag(at, str(ret_), [contact.mid])
                            elif last_game["msg_dict"][msg_id]["contentType"] == 1:
                                ret_ += "\n    • Type: Image"
                                maxbots.sendTag(at, str(ret_), [contact.mid])
                                maxbots.sendImage(at, last_game["msg_dict"][msg_id]["path"])
                                maxbots.deleteFile(last_game["msg_dict"][msg_id]["path"])
                            elif last_game["msg_dict"][msg_id]["contentType"] == 2:
                                ret_ += "\n    • Type: VIDEO"
                                maxbots.sendVideo(at, last_game["msg_dict"][msg_id]["path"])
                                maxbots.deleteFile(last_game["msg_dict"][msg_id]["path"])
                                maxbots.sendMentionv2(at, str(ret_), [contact.mid])
                            elif last_game["msg_dict"][msg_id]["contentType"] == 3:
                                ret_ += "\n    • Type: Audio"
                                maxbots.sendTag(at, str(ret_), [contact.mid])
                                maxbots.sendAudio(at, last_game["msg_dict"][msg_id]["path"])
                                maxbots.deleteFile(last_game["msg_dict"][msg_id]["path"])
                            elif last_game["msg_dict"][msg_id]["contentType"] == 4:
                                ret_ += "\n    • Type: Template"
                                maxbots.sendTag(at, str(ret_), [contact.mid])
                            elif last_game["msg_dict"][msg_id]["contentType"] == 7:
                                ret_ += "\n    • Type: Sticker"
                                ret_ += "\n    • ID : {}".format(str(last_game["msg_dict"][msg_id]["contentMetadata"]["STKID"]))
                                ret_ += "\n    • Package ID : {}".format(str(last_game["msg_dict"][msg_id]["contentMetadata"]["STKPKGID"]))
                                ret_ += "\n    • Version: {}".format(str(last_game["msg_dict"][msg_id]["contentMetadata"]["STKVER"]))
                                maxbots.sendTag(at, str(ret_), [contact.mid])
                                maxbots.sendImageWithURL(at, "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png".format(str(last_game["msg_dict"][msg_id]["contentMetadata"]["STKID"])))
                            elif last_game["msg_dict"][msg_id]["contentType"] == 13:
                                ret_ += "\n    • Type: Contact"
                                ret_ += "\n    • Mid: {}".format(str(last_game["msg_dict"][msg_id]["contentMetadata"]["mid"]))
                                maxbots.sendTag(at, str(ret_), [contact.mid])
                                maxbots.sendContact(at, last_game["msg_dict"][msg_id]["contentMetadata"]["mid"])
                            elif last_game["msg_dict"][msg_id]["contentType"] == 14:
                                ret_ += "\n    • Type: File"
                                ret_ += "\n    • Filename: {}".format(str(last_game["msg_dict"][msg_id]["contentMetadata"]["FILE_NAME"]))
                                ret_ += "\n    • Size: {}".format(str(last_game["msg_dict"][msg_id]["contentMetadata"]["FILE_SIZE"]))
                                maxbots.sendTag(at, str(ret_), [contact.mid])
                                maxbots.sendFile(at, last_game["msg_dict"][msg_id]["path"], last_game["msg_dict"][msg_id]["contentMetadata"]["FILE_NAME"])
                                maxbots.deleteFile(last_game["msg_dict"][msg_id]["path"])
                            else:
                                ret_ += "\n    • Type: Not found"
                                ret_ += "\n    • Teks: {}".format(str(last_game["msg_dict"][msg_id]["text"]))
                                if "path" in last_game["msg_dict"][msg_id]:
                                    maxbots.deleteFile(last_game["msg_dict"][msg_id]["path"])
                                maxbots.sendTag(at, str(ret_), [contact.mid])
                            del last_game["msg_dict"][msg_id]
                            limited["uns"][at] = time.time() + 0.3
                        else:
                            maxbots.sendMessage(at,"Not found")
                            limited["uns"][at] = time.time() + 0.3
                except Exception as error:print(error)
            except Exception as error:
                print("{}".format(str(error)))
def executeArf(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey):
 for cmd in cmd.split(" & "):
    if cmd == 'mute':
        if to in position['silent']:
            maxbots.sendMessage(to, 'Already♪')
        else:
            position['silent'].append(to)
            maxbots.sendMessage(to, 'Succes♪')
    elif cmd == 'unmute':
        if to not in position['silent']:
            maxbots.sendMessage(to, 'Already♪')
        else:
            position['silent'].remove(to)
            maxbots.sendMessage(to, 'Succes♪')
    if to in position['silent']:
        return
    if cmd == 'help':
        rahmanH(to)
    elif cmd == 'mode':
        rahman(to, modeH())
    elif cmd == 'self':
        rahman(to, selfH())
    elif cmd == 'steal':
        rahman(to, stealH())
    elif cmd == 'profile':
        rahman(to, profileH())
    elif cmd == 'friend':
        rahman(to, friendH())
    elif cmd == 'group':
        rahman(to, groupH())
    elif cmd == 'command':
        rahman(to, commandH())
    elif cmd == 'mention':
        rahman(to, mentionH())
    elif cmd == 'protect':
        rahman(to, protectionH())
    elif cmd == 'banning':
        rahman(to, banningH())

    elif cmd == 'setkick':
        rahman(to, kicksetH())
    elif cmd == 'setinvite':
        rahman(to, inviteset())
    elif cmd == 'js':
        rahman(to, javascriptH())
    elif cmd == 'spam':
        rahman(to, spamH())
    elif cmd == 'media':
        rahman(to, mediaH())
    elif cmd == 'fun':
        rahman(to, funH())
    elif cmd == 'setting':
        rahman(to, settingH())
    elif cmd == 'lastlist':
        rahman(to, lastlisttt())
    elif cmd == 'about':
        mids = []
        lita = ["u1f32ad104615e29d7561f0b4298f037d"]
        for aping in lita:mids.append(aping)
        kalera = ["u1f32ad104615e29d7561f0b4298f037d"]
        for red in kalera:mids.append(red)
        gantengkontol = maxbots.getSettings().privacySearchByUserid
        ewbanget = maxbots.getSettings().privacyReceiveMessagesFromNotFriend
        sangeee = maxbots.getSettings().e2eeEnable
        if gantengkontol == True:tllsngentod = "Addfromline ID: True"
        else:tllsngentod = "Addfromline ID: False"                            
        if sangeee == True:letsel = "Lettersealing: True"
        if sangeee == False:letsel = "Lettersealing: False"
        if ewbanget == True:fpes = "Filterchat: False"
        if ewbanget == False:fpes = "Filterchat: True"
        ajg = subprocess.getoutput('lsb_release -a')
        babi = subprocess.getoutput('cat /proc/meminfo')
        tll = subprocess.getoutput('lscpu')
        asu  = subprocess.getoutput('grep -c ^processor /proc/cpuinfo ')
        ngewe = platform.python_implementation()
        ngentod = platform.python_version()
        for bego in ajg.splitlines():
           if 'Description:' in bego:telaso = bego.split('Description:')[1].replace(' ','')
        for bego in tll.splitlines():
           if 'Architecture:' in bego:architecture =  bego.split('Architecture:')[1].replace(' ','')
        for bego in babi.splitlines():
           if 'MemTotal:' in bego:memor = bego.split('MemTotal:')[1].replace(' ','')
           if 'MemFree:' in bego:free = bego.split('MemFree:')[1].replace(' ','')  
        sygaping =  "「  About 」"
        sygaping +=  "\n › Type: Selfbot"        
        sygaping +=  "\n    • Version: 5"
        sygaping +=  "\n    • Library: Linepy"
        sygaping +=  "\n    • Rework: @!"  
        sygaping +=  "\n    • Store: @!"
        sygaping +=  f"\n    • Name: {maxbots.getContact(myMid).displayName}"  
        sygaping +=  f"\n    • Friend: {len(maxbots.getAllContactIds())}"  
        sygaping +=  f"\n    • Favorite: {len(maxbots.getFavoriteMids())}"  
        sygaping +=  f"\n    • Bloked: {len(maxbots.getBlockedContactIds())}"  
        sygaping +=  f"\n    • Group: {len([a for a in maxbots.getAllChatMids(True, True).memberChatMids])}"  
        sygaping +=  f"\n    • {tllsngentod}"
        sygaping +=  f"\n    • {letsel}"
        sygaping +=  f"\n    • {fpes}"
        sygaping +=  "\n\n › Account Activity Today"    
        sygaping +=  f"\n    • Chatsend: {str(position['today']['chatsend'])}"  
        sygaping +=  f"\n    • Chatrecived: {str(position['today']['chatrecv'])}"
        sygaping +=  f"\n    • Kick: {str(position['today']['kick'])}"  
        sygaping +=  f"\n    • Kicked: {str(position['today']['kicked'])}"  
        sygaping +=  f"\n    • Invite: {str(position['today']['invite'])}"  
        sygaping +=  f"\n    • Invited: {str(position['today']['invited'])}"  
        sygaping +=  f"\n    • Cancel: {str(position['today']['cancel'])}"  
        sygaping +=  f"\n    • Canceled: {str(position['today']['canceled'])}"  
        sygaping +=  f"\n    • Add: {str(position['today']['add'])}"  
        sygaping +=  f"\n    • Added: {str(position['today']['added'])}"  
        sygaping +=  "\n\n › Spesial Thanks"                
        sygaping +=  "\n    • MAXBOTS"
        sygaping +=  "\n    • Alm. Zero Cool"
        sygaping +=  "\n    • Team Hello Word"
        sygaping +=  "\n    • Kyuza"
        sygaping +=  "\n    • Haku (Pyshcopumpum)"
        sygaping +=  "\n    • Yehezkiel Bagas (VnnyL)"
        sygaping +=  "\n    • Fahmi Andrean (A-Code44)"
        sygaping +=  "\n    • Ben (Project Beta)"
        sygaping +=  "\n    • Bobby (WBB Corps™)"
        sygaping +=  "\n    • Ibl (Eighty Thousand)"
        maxbots.sendTag(to, sygaping, mids)
    elif cmd == 'speed':
        maxbots.sendMessage(to, debugH())             
    elif cmd == 'runtime':
        rahman(to, runH())             
    elif cmd == 'cekbot':
       try:
           maxbots.inviteIntoChat(to, ["u1f32ad104615e29d7561f0b4298f037d"]);has = "OK"
       except:
           has = "NOT"
       try:
           maxbots.inviteIntoChat(to, ["u1f32ad104615e29d7561f0b4298f037d"]);has1 = "OK"
       except:
           has1 = "NOT"
       try:
           maxbots.cancelChatInvitation(to, ["u1f32ad104615e29d7561f0b4298f037d"]);has2 = "OK"
       except:
           has2 = "NOT"
       crott = maxbots.getProfile().userid
       try:
           maxbots.findContactsByUserid(crott);has3 = "OK"
       except:
           has3 = "NOT"
       if has == "OK":
           sil = "✓"
       else:
           sil = "✘"
       if has1 == "OK":
           sil1 = "✓"
       else:
           sil1 = "✘"
       if has2 == "OK":
           sil2 = "✓"
       else:
           sil2 = "✘"
       if has3 == "OK":
           sil3 = "✓"
       else:
          sil3 = "✘"
       ret = "「 Status Bot 」\n › Type: Cek♪"
       ret += f"\n    • Kick: {sil1}"
       ret += f"\n    • Invite: {sil}"
       ret += f"\n    • Cancel: {sil2}"
       ret += f"\n    • Add: {sil3}"       
       rahman(to, ret)
    elif cmd == 'status':
        rahmanSTAT(to)
    elif cmd == 'listset':
        rahman(to, listH())
    elif cmd == 'vpsinfo':
        rahman(to, vpsinfoH())
    elif cmd == 'logout':
       rahman(to, 'Succes♪')
       sys.exit('##----- PROGRAM STOPPED -----##')
    elif cmd == 'restart':
       rahman(to, 'Wait♪')
       settings['restartPoint'] = to
       restartProgram()      	

    elif cmd == 'changepictlabel':
        ktl = geTreply(msg)
        if ktl == None:
            statS2(to, "ChangePictFooter","Mode","Change","Image")              
        else:
            if ktl.contentType == 1:
                path = maxbots.downloadObjectMsg(ktl.id)
                data = apiJG.imgurl(path)
                settings["footerpict"] = data["result"]
                rahman(to,   "「 Mode 」\n › Type: Change Picture Label♪\n    • Status: Success")            
    elif cmd == "temp on":
        statS3(to, "stattemp", "statfooter", "Mode", "Template")
    elif cmd == "temp off":
        settings["stattemp"] = False
        statS4(to, "stattemp", "Mode", "Tamplate")
    elif cmd == "footer on":
        statS3(to, "statfooter", "stattemp", "Mode", "Footer")
    elif cmd == "footer off":
        statS4(to, "statfooter", "Mode", "Footer")
    elif cmd == "tempblue on":    	
        statMODE(to, "tempRyansbot","invitekontak","tempyans", "statigtempnormal", "statigtempblack", "yansnew", "statlinetempblack", "temprobot", "Temp Blue")
    elif cmd == "tempdefult on":    	
        statMODE(to, "invitekontak","tempyans", "statigtempnormal", "statigtempblack", "yansnew", "statlinetempblack", "temprobot", "tempRyansbot", "Defult")
    elif cmd == "tempbot on":    	
        statMODE(to, "tempyans","invitekontak", "statigtempnormal", "statigtempblack", "yansnew", "statlinetempblack", "temprobot", "tempRyansbot", "Temp bot")
    elif cmd == "temprobot on":
        statMODE(to, "temprobot", "invitekontak","statigtempnormal", "statigtempblack", "yansnew", "statlinetempblack", "tempyans", "tempRyansbot", "Temp Robot")
    elif cmd == "templineblack on":
        statMODE(to, "statlinetempblack","invitekontak", "statigtempnormal", "statigtempblack", "yansnew", "temprobot", "tempyans", "tempRyansbot", "Line Black")
    elif cmd == "temp1 on":
        statMODE(to, "yansnew", "invitekontak","statigtempnormal", "statigtempblack", "statlinetempblack", "temprobot", "tempyans", "tempRyansbot", "Temp1")
    elif cmd == "tempigblack on":
        statMODE(to, "statigtempblack", "invitekontak","statigtempnormal", "yansnew", "statlinetempblack", "temprobot", "tempyans", "tempRyansbot", "Instagram Black")
    elif cmd == "tempignormal on":
        statMODE(to, "statigtempnormal","invitekontak", "statigtempblack", "yansnew", "statlinetempblack", "temprobot", "tempyans", "tempRyansbot", "Instagram Normal")
    elif cmd.startswith("changelink"):
        mmk = removeCmd("changelink", text)
        changeMSG(to, mmk, "idline", "Mode" , "Link")   
    elif cmd.startswith("changelabel"):
        mmk = removeCmd("changelabel", text)
        changeMSG(to, mmk, "footerlabel", "Mode" , "Label")           
    elif cmd.startswith("changecolor"):
        mmk = removeCmd("changecolor", text)
        changeMSG(to, mmk, "colorlabel", "Mode" , "Color")           
    elif cmd.startswith("changeurlplabel"):
        mmk = removeCmd("changeurlplabel", text)
        changeMSG(to, mmk, "footerpict", "Mode" , "Url Pict Label")           

    elif cmd == "me":
        sendTemplate(to, {"type":"flex","altText":"maxbots","contents":{"type":"bubble",'styles': {"body":{"backgroundColor":"#000000"}},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":" "},{"type":"image","url":"https://obs.line-scdn.net/{}".format(maxbots.getContact(sender).pictureStatus),"size":"lg"},{"type":"text","text":" "},{"type":"text","text":"{}".format(maxbots.getContact(sender).displayName),"size":"xl","weight":"bold","color":"#FFFFFF","align":"center"},{"type":"text","text":" "},{"type":"text","text":"{}".format(maxbots.getContact(sender).statusMessage),"align":"center","size":"xs","color":"#FFFFFF","wrap":True},{"type":"text","text":" "},{"type":"button","style":"primary","color":"#000000","action":{"type":"uri","label":"maxbots","uri":"https://line.me/ti/p/~max.panupong.sawaeng"}}]}}}) 
    elif cmd == 'mypict':
       stealpict(to, sender)
    elif cmd == "mycover":
       stealcover(to, sender)
    elif cmd == "myextracover":
       stealexcover(to, sender)
    elif cmd == "myvideo":
       stealvideo(to, sender)
    elif cmd == 'myname':
       stealname(to, sender,"Self")
    elif cmd == 'mybio':
       stealbio(to, sender, "Self")
    elif cmd == 'mymid':
       stealmid(to, sender)
    elif cmd == 'mycontact':
       stealcontact(to, sender)
    elif cmd == "myid":
       maxbots.sendMessage(to, "https://line.me/ti/p/~" + maxbots.profile.userid)     
    elif cmd == "myticket":
       maxbots.sendMessage(to,"https://line.me/ti/p/" + maxbots.reissueUserTicket())
    elif cmd == "mytimeline":
       stealtimeline(to, sender, "Self")
    elif cmd == "mystory":
       stealstory(to, sender)
    elif cmd == 'mysticker':
       maxbots.sendMessage(to, selfsticker())   

    elif cmd.startswith("getpict"):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            lists = geTmention(msg)
            for ls in lists:
                stealpict(to, ls)
        else: 
            mmk = removeCmd("getpict", text)
            if mmk == "on":
                statW(to, "getpictcontact","Steal","Getpict")          
            elif mmk != " ":
                if msg.relatedMessageId is not None:
                    bb = geTreply(msg)
                    if cmd == "getpict":
                        stealpict(to, bb._from)
    elif cmd.startswith("getcover"):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            lists = geTmention(msg)
            for ls in lists:
                stealcover(to, ls)
        else: 
            mmk = removeCmd("getcover", text)
            if mmk == "on":
                statW(to, "getcovercontact","Steal","Getcover")          
            elif mmk != " ":
                if msg.relatedMessageId is not None:
                    bb = geTreply(msg)
                    if cmd == "getcover":
                        stealcover(to, bb._from)
    elif cmd.startswith("getextracover"):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            lists = geTmention(msg)
            for ls in lists:
                stealexcover(to, ls)
        else: 
            mmk = removeCmd("getextracover", text)     
            if mmk == "on":
                statW(to, "getexcovercontact","Steal","Getextracover")          
            elif mmk != " ":
                if msg.relatedMessageId is not None:
                    bb = geTreply(msg)
                    if cmd == "getextracover":
                        stealexcover(to, bb._from)
    elif cmd.startswith("getvideo"):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            lists = geTmention(msg) 
            for ls in lists:
                stealvideo(to, ls)
        else: 
            mmk = removeCmd("getvideo", text)             
            if mmk == "on":
                statW(to, "getvideocontact","Steal","Getvideo")  
            elif mmk != " ":
                if msg.relatedMessageId is not None:
                    bb = geTreply(msg)
                    if cmd == "getvideo":
                        stealvideo(to, bb._from)
    elif cmd.startswith("getname"):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            lists = geTmention(msg)
            for ls in lists:
                stealname(to, ls,"Steal")                                        
        else: 
            mmk = removeCmd("getname", text)  
            if mmk == "on":
                statW(to, "getnamecontact","Steal","Getname")                   
            elif mmk != " ":
                if msg.relatedMessageId is not None:
                    bb = geTreply(msg)
                    if cmd == "getname":
                        stealname(to, bb._from,"Steal")                                
    elif cmd.startswith("getrename"):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            lists = geTmention(msg)
            for ls in lists:
                stealrename(to, ls)                   
        else: 
            mmk = removeCmd("getrename", text)      
            if mmk == "on":
                statW(to, "getrenamecontact","Steal","Getrename")  
            elif mmk != " ":
                if msg.relatedMessageId is not None:
                    bb = geTreply(msg)
                    if cmd == "getrename":
                        stealrename(to, bb._from)                                
    elif cmd.startswith("getbio"):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            lists = geTmention(msg)
            for ls in lists:
                stealbio(to, ls, "Steal")     
        else: 
            mmk = removeCmd("getbio", text)      
            if mmk == "on":
                statW(to, "getbiocontact","Steal","Getbio")                 
            elif mmk != " ":
                if msg.relatedMessageId is not None:
                    bb = geTreply(msg)
                    if cmd == "getbio":
                        stealbio(to, bb._from, "Steal")                        
    elif cmd.startswith("getmid"):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            lists = geTmention(msg)
            for ls in lists:
                stealmid(to, ls)                  
        else: 
            mmk = removeCmd("getmid", text)      
            if mmk == "on":
                statW(to, "getmidcontact","Steal","Getmid")                 
            elif mmk != " ":
                if msg.relatedMessageId is not None:
                    bb = geTreply(msg)
                    if cmd == "getmid":
                        stealmid(to, bb._from)                               
    elif cmd.startswith("getcontact"):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            lists = geTmention(msg)
            for ls in lists:
                stealcontact(to, ls)                   
        else: 
            mmk = removeCmd("getcontact", text)      
            if mmk == "on":
                rahman(to,getcontactcontact())                   
            elif mmk != " ":
                if msg.relatedMessageId is not None:
                    bb = geTreply(msg)
                    if cmd == "getcontact":
                        stealcontact(to, bb._from)                                
    elif cmd.startswith("gettimeline"):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            lists = geTmention(msg)
            for ls in lists:
                stealtimeline(to, ls, "Steal")              
        else: 
            mmk = removeCmd("gettimeline", text)      
            if mmk == "on":
                statW(to, "gettimelinecontact","Steal","Gettimeline")    
            elif mmk != " ":
                if msg.relatedMessageId is not None:
                    bb = geTreply(msg)
                    if cmd == "gettimeline":
                        stealtimeline(to, bb._from, "Steal")                                                                                           
    elif cmd.startswith("getstory"):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            lists = geTmention(msg)
            for ls in lists:
                stealstory(to, ls)                                    
        else: 
            mmk = removeCmd("getstory", text)      
            if mmk == "on":
                statW(to, "getstorycontact","Steal","Getstory")                                
            elif mmk != " ":
                if msg.relatedMessageId is not None:
                    bb = geTreply(msg)
                    if cmd == "getstory":
                        stealstory(to, bb._from)                                
    elif cmd.startswith("lastseen"):
        if 'MENTION' in msg.contentMetadata.keys() != None:
            names = re.findall(r'@(\w+)', msg.text)
            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
            mentionees = mention['MENTIONEES']                                
            for mention in mentionees:
                if mention['M'] in lastseen["find"]:
                    maxbots.sendTag(to, " 「 Steal 」\n › Type: Lastseen♪\n    • User: @! {}".format(lastseen["username"][mention['M']]), [mention['M']])                       
                else:
                    maxbots.sendTag(to, " 「 Steal 」\n › Type: Lastseen♪\n    • User: @! \n    • Oops!! I can't found",[mention['M']])                        
        else:
          if msg.relatedMessageId is not None:
              bb = geTreply(msg)
              if cmd == "lastseen":
                  if bb._from in lastseen["find"]:
                      maxbots.sendTag(to, " 「 Steal 」\n › Type: Lastseen♪\n    • User: @! {}".format(lastseen["username"][bb._from]), [bb._from])                             
                  else:
                      maxbots.sendTag(to, " 「 Steal 」\n › Type: Lastseen♪\n    • User: @! \n    • Oops!! I can't found".format(lastseen["username"][bb._from]), [bb._from])                             
    elif cmd.startswith("find"):
        if 'MENTION' in msg.contentMetadata.keys():
            mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
            for mention in mentions['MENTIONEES']:
                profile = maxbots.getContact(mention['M'])
                aa = [a for a in maxbots.getAllChatMids(True, True).memberChatMids]
                target = profile.mid
                lacak = ""
                num = 1                                                
                for x in aa:
                    member = maxbots.getChats([x]).chats[0].extra.groupExtra.memberMids
                    if target in member:
                        lacak += "\n      • {}. {}".format(num,maxbots.getChats([x]).chats[0].chatName)
                        num = (num+1)                                                
                if lacak == "":
                    rahman(to, " 「 Steal 」\n › Type: Find♪\n    • Not Fund")      
                else:
                    rahman(to, "「 Steal 」\n › Type: Find♪ \n    • User : {}\n    • Group Joined:{}".format(maxbots.getContact(target).displayName, lacak))                   
        else:
            if msg.relatedMessageId is not None:
                bb = geTreply(msg)
                if cmd == "find":
                   profile = maxbots.getContact(bb._from)
                   aa = [a for a in maxbots.getAllChatMids(True, True).memberChatMids]
                   target = profile.mid
                   lacak = ""
                   num = 1                                                                     
                   for x in aa:
                       member = maxbots.getChats([x]).chats[0].extra.groupExtra.memberMids
                       if target in member:
                           lacak += "\n      • {}. {}".format(num,maxbots.getChats([x]).chats[0].chatName)
                           num = (num+1)                        
                   if lacak == "":
                       rahman(to, " 「 Steal 」\n › Type: Find♪\n    • Not Fund")      
                   else:
                       rahman(to, "「 Steal 」\n › Type: Find♪ \n    • User : {}\n    • Group Joined:{}".format(maxbots.getContact(target).displayName, lacak))                            
    elif cmd.startswith("faketweet"):
       if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
           lists = geTmention(msg)         
           for ls in lists:
               ret_ = "{}".format(str(ls))               
           ppk = removeCmd("faketweet", text)      
           asyu = ppk.split(" | ")
           ktl = asyu[1]
           text = "{}".format(ktl)
           profile = maxbots.getContact(ls)
           userpict = "https://obs.line-scdn.net/"+str(profile.pictureStatus)
           if profile.pictureStatus is None:userpict = "https://s20.directupload.net/images/220423/uxdxnp5a.jpg"                                      
           sendTemplate(to, flexklr.kaleraFaketweet(userpict, maxbots.getContact(ls).displayName, text))                                            
       else:
           if msg.relatedMessageId is not None:
               aa = maxbots.getRecentMessagesV2(to, 1001)
               lists = []               
               for bb in aa:
                   if bb.id in msg.relatedMessageId:
                       lists.append(bb._from)                       
               for ls in lists:
                   ret_ = "{}".format(str(ls))                                                         
               ppk = removeCmd("faketweet", text)      
               asyu = ppk.split("| ")
               ktl = asyu[1]
               text = "{}".format(ktl)       
               profile = maxbots.getContact(ls)
               userpict = "https://obs.line-scdn.net/"+str(profile.pictureStatus)
               if profile.pictureStatus is None:userpict = "https://s20.directupload.net/images/220423/uxdxnp5a.jpg"                                                                                    
               sendTemplate(to, flexklr.kaleraFaketweet(userpict, maxbots.getContact(ls).displayName, text))                                   
           else:
               ktl = removeCmd("faketweet", text)      
               text = "{}".format(ktl)
               profile = maxbots.getContact(sender)
               userpict = "https://obs.line-scdn.net/"+str(profile.pictureStatus)
               if profile.pictureStatus is None:userpict = "https://s20.directupload.net/images/220423/uxdxnp5a.jpg"                                
               sendTemplate(to, flexklr.kaleraFaketweet(userpict, maxbots.getContact(sender).displayName, text))       
    elif cmd.startswith("fakeline"):
       if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
           lists = geTmention(msg)         
           for ls in lists:
               ret_ = "{}".format(str(ls))               
           ppk = removeCmd("fakeline", text)      
           asyu = ppk.split(" | ")
           ktl = asyu[1]
           text = "{}".format(ktl) 
           profile = maxbots.getContact(ls)
           userpict = "https://obs.line-scdn.net/"+str(profile.pictureStatus)
           if profile.pictureStatus is None:userpict = "https://s20.directupload.net/images/220423/uxdxnp5a.jpg"                             
           sendTemplate(to, flexklr.kaleraFakeline(userpict, maxbots.getContact(ls).displayName, text))                                                
       else:
           if msg.relatedMessageId is not None:
               aa = maxbots.getRecentMessagesV2(to, 1001)
               lists = []               
               for bb in aa:
                   if bb.id in msg.relatedMessageId:
                       lists.append(bb._from)                       
               for ls in lists:
                   ret_ = "{}".format(str(ls))                   
               ppk = removeCmd("fakeline", text)      
               asyu = ppk.split("| ")
               ktl = asyu[1]
               text = "{}".format(ktl)                                                                   
               profile = maxbots.getContact(ls)
               userpict = "https://obs.line-scdn.net/"+str(profile.pictureStatus)
               if profile.pictureStatus is None:userpict = "https://s20.directupload.net/images/220423/uxdxnp5a.jpg"                             
               sendTemplate(to, flexklr.kaleraFakeline(userpict, maxbots.getContact(ls).displayName, text))                                                              
           else:
               ktl = removeCmd("fakeline", text)      
               text = "{}".format(ktl)                              
               profile = maxbots.getContact(sender)
               userpict = "https://obs.line-scdn.net/"+str(profile.pictureStatus)
               if profile.pictureStatus is None:userpict = "https://s20.directupload.net/images/220423/uxdxnp5a.jpg"   
               sendTemplate(to, flexklr.kaleraFakeline(userpict, maxbots.getContact(sender).displayName, text))                                                       
    elif cmd.startswith("fakefb"):
       if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
           lists = geTmention(msg)         
           for ls in lists:
               ret_ = "{}".format(str(ls))               
           ppk = removeCmd("fakefb", text)      
           asyu = ppk.split(" | ")
           ktl = asyu[1]
           text = "{}".format(ktl) 
           profile = maxbots.getContact(ls)
           userpict = "https://obs.line-scdn.net/"+str(profile.pictureStatus)
           if profile.pictureStatus is None:userpict = "https://s20.directupload.net/images/220423/uxdxnp5a.jpg"                             
           sendTemplate(to, flexklr.kaleraFakefb(userpict, maxbots.getContact(ls).displayName, text))                                                                                                                       
       else:
           if msg.relatedMessageId is not None:
               aa = maxbots.getRecentMessagesV2(to, 1001)
               lists = []               
               for bb in aa:
                   if bb.id in msg.relatedMessageId:
                       lists.append(bb._from)                       
               for ls in lists:
                   ret_ = "{}".format(str(ls))                                      
               ppk = removeCmd("fakefb", text)      
               asyu = ppk.split("| ")
               ktl = asyu[1]
               text = "{}".format(ktl)                                                                   
               profile = maxbots.getContact(ls)
               userpict = "https://obs.line-scdn.net/"+str(profile.pictureStatus)
               if profile.pictureStatus is None:userpict = "https://s20.directupload.net/images/220423/uxdxnp5a.jpg"                             
               sendTemplate(to, flexklr.kaleraFakefb(userpict, maxbots.getContact(ls).displayName, text))                                                                                     
           else:
               ktl = removeCmd("fakefb", text)      
               text = "{}".format(ktl)                              
               profile = maxbots.getContact(sender)
               userpict = "https://obs.line-scdn.net/"+str(profile.pictureStatus)
               if profile.pictureStatus is None:userpict = "https://s20.directupload.net/images/220423/uxdxnp5a.jpg"   
               sendTemplate(to, flexklr.kaleraFakefb(userpict, maxbots.getContact(sender).displayName, text))                                                                                            
    elif cmd.startswith("sim"):
       if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            lists = geTmention(msg)
            for ls in lists:
                profile = maxbots.getContact(ls)
                userpict = "https://obs.line-scdn.net/"+str(profile.pictureStatus)
                if profile.pictureStatus is None:userpict = "https://s20.directupload.net/images/220423/uxdxnp5a.jpg"   
                path = f"https://some-random-api.ml/canvas/horny?avatar={userpict}"
                maxbots.sendImageWithURL(to, path)                                    
       else:
           if msg.relatedMessageId is not None:
                bb = geTreply(msg)
                if cmd == "sim":
                    profile = maxbots.getContact(bb._from)
                    userpict = "https://obs.line-scdn.net/"+str(profile.pictureStatus)
                    if profile.pictureStatus is None:userpict = "https://s20.directupload.net/images/220423/uxdxnp5a.jpg"   
                    path = f"https://some-random-api.ml/canvas/horny?avatar={userpict}"
                    maxbots.sendImageWithURL(to, path)                                                         
           else:
               profile = maxbots.getContact(sender)
               userpict = "https://obs.line-scdn.net/"+str(profile.pictureStatus)
               if profile.pictureStatus is None:userpict = "https://s20.directupload.net/images/220423/uxdxnp5a.jpg"   
               path = f"https://some-random-api.ml/canvas/horny?avatar={userpict}"
               maxbots.sendImageWithURL(to, path)                                                   
    elif cmd.startswith("fakecall"):
       if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
           lists = geTmention(msg)    
           target1 = lists[int("1")-1]    
           target2 = lists[int("2")-1]   
           profile1 = maxbots.getContact(target1)
           profile2 = maxbots.getContact(target2)
           name1 = profile1.displayName
           name2 = profile2.displayName
           userpict1 = "https://obs.line-scdn.net/"+str(profile1.pictureStatus)
           if profile1.pictureStatus is None:userpict1 = "https://s20.directupload.net/images/220423/uxdxnp5a.jpg"   
           userpict2 = "https://obs.line-scdn.net/"+str(profile2.pictureStatus)
           if profile2.pictureStatus is None:userpict2 = "https://s20.directupload.net/images/220423/uxdxnp5a.jpg"   
           pictgc = "https://obs.line-scdn.net/{}".format(maxbots.getChats([to]).chats[0].picturePath)
           sendTemplate(to,{"type":"flex","altText":settings["footerlabel"],"contents": flexklr.media_fakecall(userpict1,userpict2,name1,name2,pictgc)})                                      

    elif cmd == 'changepict':
        ktl = geTreply(msg)
        if ktl == None:
            statS2(to, "changePictureProfile","Profile","Profile","Image")                    
        else:
            if ktl.contentType == 1:
                path = maxbots.downloadObjectMsg(ktl.id)
                maxbots.updateProfilePicture(path)
                rahman(to,   "「 Profile 」\n › Type: Change Profile♪\n    • Status: Success")                                                
    elif cmd == 'changecover':
        ktl = geTreply(msg)
        if ktl == None:
            statS2(to, "changeCoverProfile","Profile","Cover","Image")                     
        else:
            if ktl.contentType == 1:
                path = maxbots.downloadObjectMsg(ktl.id)
                maxbots.updateProfileCover(path)
                rahman(to,   "「 Profile 」\n › Type: Change Cover♪\n    • Status: Success")                                                
    elif cmd == 'changevp':
        ktl = geTreply(msg)
        if ktl == None:
            statS2(to, "changevp","Profile","Vp","Video")                     
        else:
            if ktl.contentType == 2:
                pict = "https://obs.line-scdn.net/{}".format(maxbots.getProfile().pictureStatus)
                path = maxbots.downloadFileURL(pict)
                path1 = maxbots.downloadObjectMsg(ktl.id)
                changevideopp(path, path1)
                rahman(to,   "「 Profile 」\n › Type: Change Video Profile♪\n    • Status: Success")                                                                                
    elif cmd == "changevc":
        ktl = geTreply(msg)
        if ktl == None:
            statS2(to, "changeProfileVideo","Profile","Vc","Video")                     
        else:
            if ktl.contentType == 2:
                pict = covernyaa(sender)
                path = maxbots.downloadFileURL(pict)
                path1 = maxbots.downloadObjectMsg(ktl.id)
                maxbots.updateProfileCoverVideo(path, path1)
                rahman(to,   "「 Profile 」\n › Type: Change Video Cover♪\n    • Status: Succes")                                                                       
    elif cmd == 'updatestory':
        ktl = geTreply(msg)
        if ktl == None:
            statS2(to, "updatestory","Profile","Story","Image/Video")                     
        else:
            path = maxbots.downloadObjectMsg(ktl.id)
            if ktl.contentType == 1:
                objId, obsHash = maxbots.uploadObjStory(path, type='image')
                maxbots.updateStory(objId, obsHash, mediaType='image')                                
            elif ktl.contentType == 2:
                objId, obsHash = maxbots.uploadObjStory(path, type='video')
                maxbots.updateStory(objId, obsHash, mediaType='video')                                
            rahman(to,   "「 Profile 」\n › Type: Update Story♪\n    • Status: Success")
    elif cmd.startswith("changename"):
        mmk = removeCmd("changename", text)      
        asu = maxbots.getProfile().displayName
        profile = maxbots.getProfile()
        profile.displayName = str(mmk)
        maxbots.updateProfile(profile)
        rahman(to,   "「 Profile 」\n › Type: Name♪\n    • Before: %s \n    • After: %s\n    • Status: Success"%(asu,mmk))                                                        
    elif cmd.startswith("changebio "):
        mmk = removeCmd("changebio", text)      
        asu = maxbots.getProfile().statusMessage
        profile = maxbots.getProfile()
        profile.statusMessage = str(mmk)
        maxbots.updateProfile(profile)
        rahman(to,   "「 Profile 」\n › Type: Change Bio♪\n    • Before: %s \n    • After: %s\n    • Status: Success"%(asu,mmk))                                                        
    elif cmd.startswith("changername"):
        mmk = removeCmd("changername", text)  
        changeMSG2(to, mmk.lower(), "setKey","rname", "Profile" , "Rname")   

    elif cmd == 'friendlist':
        maxbots.sendlistFriend(to)
    elif cmd == 'favoritelist':
        if len(maxbots.getFavoriteMids()) > 0:
            h = [a for a in maxbots.getFavoriteMids()];k = len(h)//20            
            for aa in range(k+1):
                if aa == 0:dd = '「 Friend 」\n › Type: Favoritelist♪';no=aa
                else:dd = '';no=aa*20
                msgas = dd
                for a in h[aa*20:(aa+1)*20]:
                    no+=1
                    if no == len(h):msgas+='\n    • {}.@!\n'.format(no)
                    else:msgas += '\n    • {}.@!'.format(no)
                maxbots.sendTag(to, msgas, h[aa*20:(aa+1)*20])
        else:rahman(to,"「 Friend 」\n › Type: Favoritelist♪\n    • Not Found")                            
    elif cmd == 'blocklist':
        maxbots.sendlistBlock(to, rahman)
    elif cmd == 'friend clear':
        ktl = len(maxbots.getAllContactIds())
        try:
            maxbots.clearContacts()
        except:
            pass
        mmk = len(maxbots.getAllContactIds())
        rahman(to,"「 Friend 」\n › Type: Friend Clear♪\n    • Amount: {} \n    • Status: Success".format(ktl-mmk))
    elif cmd.startswith("contact "):
        name = removeCmd("contact", text)  
        user = maxbots.getAllContactIds()
        ahay = maxbots.getContacts(user)
        targets = []                                
        for contact in ahay:
            if contact.displayNameOverridden is not None:
                if name in contact.displayNameOverridden:
                    targets.append(contact.mid)                                                     	
            else:
                if name in contact.displayName.lower():
                    targets.append(contact.mid)                   
        for target in targets:
            try:
                M = Message()
                M.to = to
                M.contentType = 13
                M.contentMetadata = {'mid': target}
                maxbots.sendContact(to,target)                                                                                
            except:
                rahman(to,"「 Friend 」\n › Type: Contact♪\n    • Status: Not Found")                        
    elif cmd.startswith("idline "):
        mmk = removeCmd("idline", text)  
        lonte = maxbots.findContactsByUserid(mmk)
        ktl = lonte.mid
        maxbots.sendMessage(to,"http://line.me/ti/p/~" + mmk)
        maxbots.sendContact(to, ktl)         
    elif cmd.startswith("friend add"):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            lists = geTmention(msg)
            n = len(maxbots.getAllContactIds())
            for ls in lists:                
                finded(ls)
            t = len(maxbots.getAllContactIds())
            rahman(to, f"「 Friend 」\n › Type: Friend Add♪\n    • Before: {n} \n    • After: {t}\n    • Status: Succes")
        else: 
            mmk = removeCmd("friend add", text)
            if mmk == "on":
                statW(to, "wfriendlist","Friend","Friend Add")          
            elif mmk != " ":
                if msg.relatedMessageId is not None:
                    bb = geTreply(msg)
                    if cmd == "friend add":
                        n = len(maxbots.getAllContactIds())
                        finded(bb._from)
                        t = len(maxbots.getAllContactIds())
                        rahman(to, f"「 Friend 」\n › Type: Friend Add♪\n    • Before: {n} \n    • After: {t}\n    • Status: Succes")
    elif cmd.startswith("friend del"):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            list = geTmention(msg)
            n = len(maxbots.getAllContactIds())
            for ls in list:
                maxbots.deleteContact(ls)
            t = len(maxbots.getAllContactIds())
            rahman(to, f"「 Friend 」\n › Type: Friend Del♪\n    • Before: {n} \n    • After: {t}\n    • Status: Succes")
        else:
            mmk = removeCmd("friend del", text)
            if mmk == "on":
                statW(to, "dfriendlist","Friend","Friend Del")                        
            elif mmk != " ":
                if msg.relatedMessageId is not None:
                    bb = geTreply(msg)
                    if cmd == "friend del":
                        if bb._from in maxbots.getAllContactIds():
                            maxbots.deleteContact(bb._from)
                            maxbots.sendTag(to,"「 Friend 」\n › Type: Friend Del♪\n    • 1. @! Del♪",[bb._from])                                                                             
                        else:
                            maxbots.sendTag(to,"「 Friend 」\n › Type: Friend Del♪\n    • 1. @! Nothing♪",[bb._from])                                                                                           
                else:
                    anu = maxbots.refreshContacts()
                    maxbots.deletefriendnum(to, wait, cmd)
    elif cmd.startswith("block add"):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            lists = geTmention(msg)
            n = len(maxbots.getBlockedContactIds())
            for ls in lists:                
                maxbots.blockContact(ls)
            t = len(maxbots.getBlockedContactIds())
            rahman(to, f"「 Friend 」\n › Type: Block Add♪\n    • Before: {n} \n    • After: {t}\n    • Status: Succes")
        else: 
            mmk = removeCmd("block add", text)
            if mmk == "on":
                statW(to, "wblocklist","Friend","Block Add")          
            elif mmk != " ":
                if msg.relatedMessageId is not None:
                    bb = geTreply(msg)
                    if cmd == "block add":
                        n = len(maxbots.getBlockedContactIds())
                        maxbots.blockContact(bb._from)
                        t = len(maxbots.getBlockedContactIds())
                        rahman(to, f"「 Friend 」\n › Type: Block Add♪\n    • Before: {n} \n    • After: {t}\n    • Status: Succes")
    elif cmd.startswith("block del"):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            lists = geTmention(msg)
            n = len(maxbots.getBlockedContactIds())
            for ls in lists:                
                maxbots.unblockContact(ls)
            t = len(maxbots.getBlockedContactIds())
            rahman(to, f"「 Friend 」\n › Type: Block Del♪\n    • Before: {n} \n    • After: {t}\n    • Status: Succes")
        else: 
            mmk = removeCmd("block del", text)
            if mmk == "on":
                statW(to, "dblocklist","Friend","Block Del")          
            elif mmk != " ":
                if msg.relatedMessageId is not None:
                    bb = geTreply(msg)
                    if cmd == "block del":
                        n = len(maxbots.getBlockedContactIds())
                        maxbots.unblockContact(bb._from)
                        t = len(maxbots.getBlockedContactIds())
                        rahman(to, f"「 Friend 」\n › Type: Block Del♪\n    • Before: {n} \n    • After: {t}\n    • Status: Succes")
    elif cmd == "backup profile":
        rahman(to, maxbots.backupProfile(settings, usernamee))
    elif cmd == "restore":
        rahman(to, maxbots.restoreProfile(settings, usernamee))
    elif cmd.startswith("clone"): 
        if settings["backupProfile"]:       
            a = geTmention(msg)
            if a:
                for x in a:                 
                    rahman(to, maxbots.cloneProfile(x))
            else:
                if cmd == "clone":
                    b = geTreply(msg)
                    if b.id != "":
                        rahman(to, maxbots.cloneProfile(b._from))                            
        else:
            rahman(to, "「 Friend 」\n › Type: Clone♪ \n    • Note: Type `Backup Profile` For Backup You Profile")
    elif cmd.startswith("chat "):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            key = eval(msg.contentMetadata["MENTION"])
            key1 = key["MENTIONEES"][0]["M"]
            nama = maxbots.getContact(key1).displayName
            anu = maxbots.getContact(key1)                                    
            if len(cmd.split(" | ")) >= 2:
                mid  = "{}".format(key1)
                text = "{}".format(str(cmd.replace(cmd.split(" | ")[0]+" | ","")))
                icon = "http://dl.profile.maxbots.naver.jp/{}".format(anu.pictureStatus)
                name = "{}".format(anu.displayName)
                b = [sendMessageCustom(key1, text, icon, name)]
                maxbots.sendTag(to,"「 Friend 」\n › Type: Chat♪\n    • Target : @! \n    • Status: Success",[key1])                                                                                                
        else: 
            if msg.relatedMessageId is not None:
                aa = maxbots.getRecentMessagesV2(to, 1001)
                for bb in aa:
                    if bb.id in msg.relatedMessageId:
                        nama = maxbots.getContact(bb._from).displayName
                        anu = maxbots.getContact(bb._from)                           
                        if len(cmd.split(" | ")) >= 2:
                            mid  = "{}".format(bb._from)
                            text = "{}".format(str(cmd.replace(cmd.split(" | ")[0]+" | ","")))
                            icon = "http://dl.profile.maxbots.naver.jp/{}".format(anu.pictureStatus)
                            name = "{}".format(anu.displayName)
                            b = [sendMessageCustom(bb._from, text, icon, name)]
                            maxbots.sendTag(to,"「 Friend 」\n › Type: Chat♪\n    • Target : @! \n    • Status: Success",[bb._from])
    if cmd.startswith("rename "):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            lists = geTmention(msg)
            for ls in lists:
                ret_ = "{}".format(str(ls))                
            s = removeCmd("rename", text)
            sam = s.split("| ")
            namauser = sam[1]
            b = maxbots.getContact(ls).displayName
            finded(ls)
            maxbots.renameContact(ls,namauser)
            rahman(to,"「 Friend 」\n › Type: Rename Contact♪\n    • Before: %s \n    • After: %s \n    • Status: Succes"%(b,namauser))                                                                                             
    if cmd.startswith("rename"):
        if msg.relatedMessageId is not None:
            aa = maxbots.getRecentMessagesV2(to, 1001)
            lists = []            
            for bb in aa:
               if bb.id in msg.relatedMessageId:
                   lists.append(bb._from)
            for ls in lists:
                ret_ = "{}".format(str(ls))               
            s = removeCmd("rename", text)
            sam = s.split("| ")
            namauser = sam[1]
            b = maxbots.getContact(ls).displayName
            finded(ls)
            maxbots.renameContact(ls,namauser)
            rahman(to,"「 Friend 」\n › Type: Rename Contact♪\n    • Before: %s \n    • After: %s \n    • Status: Succes"%(b,namauser))                                                                                                                  
    if cmd.startswith("renamecontact "):
        name = removeCmd("renamecontact", text)
        settings['msgbroadcast'] = str(name)
        statS2(to, "updateProfile","Friend","Rename","Contact")          

    elif cmd.startswith("getcall"):
        mmk = removeCmd("getcall", text)
        if mmk == "all":
            yb = []
            a = maxbots.getAllChatMids(True, True).memberChatMids
            for x in a:
                b = maxbots.getGroupCall(x).online
                if b == True:
                   c = maxbots.getGroupCall(x).chatMid
                   yb.append(c)
            ma = ""
            d = 0
            for group in yb:
                d = d + 1
                ma += "    • " + str(d) + ". " + maxbots.getChats([group]).chats[0].chatName + "\n"             
            rahman(to,"「 Getcall 」\n › Type: All♪\n"+ ma +"\n › Command\n    • " + setKey + "Getcall ‹Num›")
        else:   
            number = removeCmd("getcall", text)
            for ajg in number.split(","):
                yb = []
                a = maxbots.getAllChatMids(True, True).memberChatMids
                for x in a:
                    b = maxbots.getGroupCall(x).online
                    if b == True:
                       c = maxbots.getGroupCall(x).chatMid
                       yb.append(c)
                try:
                    group = yb[int(ajg)-1]
                    G = maxbots.getChats([group], True , False).chats[0]                    
                    try:
                        a = maxbots.getGroupCall(G.chatMid);print(a);k = len(a.memberMids)//20                        
                        for i in range(k+1):
                            if i == 0:aa = '「 Group 」\n › Detail: Group Call \n    • In: {}\n    • Call started in: {}\n    • Member Call:'.format(maxbots.getChats([G.chatMid]).chats[0].chatName,humanize.naturaltime(datetime.fromtimestamp(int(a.started)//1000)));no = i
                            else:aa = '「 Group 」\n › Detail: Group Call\n    • In: {}\n    • Call started in: {}\n    • Member Call:'.format(maxbots.getChats([G.chatMid]).chats[0].chatName,humanize.naturaltime(datetime.fromtimestamp(int(a.starter)//1000)));no=i*20
                            ret = aa
                            for b in a.memberMids[i*20 : (i+1)*20]:
                                no += 1;c = a.hostMids                        
                                if a.mediaType == 1:typenya = 'Free Call Group'
                                if a.mediaType == 2:typenya = 'Video Call Group'
                                if no == len(a.memberMids):ret+='\n       • {}. @!\n › Type: {}\n    • Host: @!'.format(no,typenya)
                                else:ret+='\n       • {}. @!'.format(no)
                            maxbots.sendMentionn(to, ret,"",a.memberMids[i*20 : (i+1)*20]+[c])
                    except:
                        rahman(to,'「 Group 」\n › Detail: Group Call\n    • In: {}\n    • Call: Nothing'.format(maxbots.getChats([to]).chats[0].chatName))        
                except:
                    callGet(to)
                          
 


    elif cmd == 'groupinfo':
        group = maxbots.getChats([to]).chats[0]
        try:ccreator = group.extra.groupExtra.creator;gcreator = maxbots.getContact(ccreator).displayName
        except:ccreator = None;gcreator = 'Not found'
        if not group.extra.groupExtra.inviteeMids:pendings = 0
        else:pendings = len(group.extra.groupExtra.inviteeMids)
        qr = 'Close' if group.extra.groupExtra.preventedJoinByTicket else 'Open'
        if group.extra.groupExtra.preventedJoinByTicket:ticket = 'Not found'
        else:ticket = 'https://line.me/R/ti/g/' + str(maxbots.reissueChatTicket(group.chatMid).ticketId)
        created = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(group.createdTime) / 1000))
        rahmanp(to, "https://obs.line-scdn.net/{}".format(maxbots.getChats([to]).chats[0].picturePath))
        if ccreator:maxbots.sendMessage(to, None, contentMetadata={'mid': ccreator}, contentType=13)
        rahman(to,'「 Group 」\n › Type: Group Info♪\n    • ID : ' + group.chatMid + '\n    • Name : ' + group.chatName + '\n    • Creator : ' + gcreator + '\n    • Created Time : ' + created + '\n    • Group Member : ' + str(len(group.extra.groupExtra.memberMids)) + '\n    • Group Pending : ' + str(pendings) + '\n    • QR Status : ' + qr)                              
    elif cmd.startswith("groupinfo "):
        sep = msg.text.split(" ");num = msg.text.replace(sep[0] + " ","");gids = [a for a in maxbots.getAllChatMids(True, True).memberChatMids];gid = gids[int(num) - 1];group = maxbots.getChats([gid], True , False).chats[0]
        try:ccreator = group.extra.groupExtra.creator;gcreator = maxbots.getContact(ccreator).displayName
        except:ccreator = None;gcreator = 'Not found'
        if not group.extra.groupExtra.inviteeMids:pendings = 0
        else:pendings = len(group.extra.groupExtra.inviteeMids)
        qr = 'Close' if group.extra.groupExtra.preventedJoinByTicket else 'Open'
        if group.extra.groupExtra.preventedJoinByTicket:ticket = 'Not found'
        else:ticket = 'https://line.me/R/ti/g/' + str(maxbots.reissueChatTicket(group.chatMid).ticketId)
        created = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(group.createdTime) / 1000))
        rahmanp(to, "https://obs.line-scdn.net/{}".format(maxbots.getChats([gid]).chats[0].picturePath))
        if ccreator:maxbots.sendMessage(to, None, contentMetadata={'mid': ccreator}, contentType=13)
        maxbots.sendMessage(to,'「 Group 」\n › Type: Remote Group Info♪\n    • ID : ' + group.chatMid + '\n    • Name : ' + group.chatName + '\n    • Creator : ' + gcreator + '\n    • Created Time : ' + created + '\n    • Group Member : ' + str(len(group.extra.groupExtra.memberMids)) + '\n    • Group Pending : ' + str(pendings) + '\n    • QR Status : ' + qr)                            
    elif cmd == 'groupcreator':
        try:
            maxbots.sendContact(to, maxbots.getChats([to]).chats[0].extra.groupExtra.creator)          
        except:
            rahman(to,'「 Group 」\n › Type: Group Creator♪\n    • In: {}\n    • Not Found'.format(maxbots.getChats([to]).chats[0].chatName))          
    elif cmd == 'groupid':
        maxbots.sendMessage(to, "「 Group 」\n › Type: Group Id♪\n    • Id: {}".format(maxbots.getChats([to]).chats[0].chatMid))
    elif cmd == 'groupname':
        maxbots.sendMessage(to, "「 Group 」\n › Type: Group Name♪\n    • Name: {}".format(maxbots.getChats([to]).chats[0].chatName))           
    elif cmd == 'grouppict':
        rahmanp(to, "https://obs.line-scdn.net/{}".format(maxbots.getChats([to]).chats[0].picturePath))
    elif cmd == 'groupcover':
        coverGroup(to)
    elif cmd == 'grouplist':
        if settings['setKey']['status'] == True:kalera = settings['setKey']['key']
        else:kalera = ''
        if len(maxbots.getAllChatMids(True, True).memberChatMids) > 0:
            h = [a for a in maxbots.getAllChatMids(True, True).memberChatMids];k = len(h)//100     
            for aa in range(k+1):
                if aa == 0:dd = '「 Group 」\n › Type: Grouplist♪';no=aa
                else:dd = '';no=aa*100
                msgas = dd 
                for a in h[aa*100:(aa+1)*100]:
                    cuk = maxbots.getChats([a], True , False).chats[0]
                    no+=1
                    if no == len(h):msgas+="\n    • {}. {} {}".format(no , cuk.chatName[0:25], len(cuk.extra.groupExtra.memberMids))                    
                    else:msgas += "\n    • {}. {} {}".format(no , cuk.chatName[0:25], len(cuk.extra.groupExtra.memberMids))                   
                rahman(to, msgas +"\n\n › Type: Remote♪\n    • " + kalera + "Leave ‹No›\n    • " + kalera + "Groupinfo ‹No›\n    • " + kalera + settings['tagall'] + " ‹No›\n    • " + kalera + "Respamcall ‹No› ‹No›\n    • " + kalera + "Reunsend ‹No› ‹No›\n    • " + kalera + "Memberlist ‹No›\n    • " + kalera + "Pendinglist ‹No›\n    • " + kalera + "Openqr ‹No›\n    • " + kalera + "Closeqr ‹No›\n    • " + kalera + "Addbcmute ‹No›\n    • " + kalera + "Delbcmute ‹No›\n    • " + kalera + settings["kickallpy"] + " ‹No›\n    • " + kalera + settings['bypass'] + " ‹No›\n    • " + kalera + settings['kickall'] + " ‹No›\n    • " + kalera + settings['cancelall'] + " ‹No›")
        else:rahman(to,"「 Group 」\n › Type: Grouplist♪ \n   • Status: Not List")  
    if cmd.startswith("leave "):
        gid = [a for a in maxbots.getAllChatMids(True, True).memberChatMids]
        if len(cmd.split(" ")) == 2:
            selection = MySplit(cmd.split(' ')[1],range(1,len(gid)+1));k = len(gid)//100             
            for a in range(k+1):
                if a == 0:ajg='「 Group 」\n › Type: Remote Leave♪'
                else:ajg='「 Group 」\n › Type: Remote Leave♪\n    • Nothing Group'
                babi = '';no = 0                 
                for i in selection.parse()[a*100 : (a+1)*100]:
                    maxbots.deleteSelfFromChat(gid[i - 1]);time.sleep(0.4);no+=1;gC = maxbots.getChats([gid[i - 1]], True , False).chats[0]                                         
                    if no == len(selection.parse()):babi+= "\n    • {}. {}\n    • Status: Success".format(i,gC.chatName)
                    else:babi+= "\n    • {}. {}".format(i,gC.chatName)
                rahman(to,ajg+babi)
    elif cmd.startswith('respamcall '):
        sep = text.split(" ");num = int(sep[1]);numb = int(sep[2]);sep2 = text.replace(sep[0] + ' ','');text = sep2.replace(sep[1] + ' ','');groups = [a for a in maxbots.getAllChatMids(True, True).memberChatMids];group = groups[int(num) - 1];G = maxbots.getChats([group], True , False).chats[0]                                             
        for var in range(0,numb):G = maxbots.getChats([group]).chats[0];members = G.extra.groupExtra.memberMids;maxbots.acquireGroupCallRoute(group);time.sleep(0.4);maxbots.inviteIntoGroupCall(group, contactIds=members)      
        rahman(to, '「 Group 」\n › Type: Remote Spamcall♪\n    • In Group: {} \n    • Amount: {} \n    • Status: Success'.format(G.chatName, numb))             
    elif cmd.startswith('reunsend '):
        sep = text.split(" ")
        num = int(sep[1])
        numb = int(sep[2])
        sep2 = text.replace(sep[0] + ' ','')
        text = sep2.replace(sep[1] + ' ','')
        groups = [a for a in maxbots.getAllChatMids(True, True).memberChatMids]
        group = groups[int(num) - 1]
        G = maxbots.getChats([group], True , False).chats[0]
        M = maxbots.getRecentMessagesV2(group, 1001)
        MId = []                                                                                                        
        for ind,i in enumerate(M):
            if ind == 0:pass                
            else: 
                if i._from == maxbots.profile.mid:
                    MId.append(i.id)
                    if len(MId) == numb:
                        break
        def unsMes(id):maxbots.unsendMessage(id)
        for i in MId:thread1 = threading.Thread(target=unsMes, args=(i,));thread1.daemon = True;thread1.start();thread1.join()
        rahman(to, '「 Group 」\n › Type: Remote Unsend♪\n    • Amount: {} '.format(len(MId)) + '\n    • In Group : ' + G.chatName + '\n    • Status: Success')
    elif cmd == 'grouppendinglist':
        if settings['setKey']['status'] == True:
            kalera = settings['setKey']['key']
        else:
            kalera = ''
        ktl = ""
        no = 0
        mypen = [a for a in maxbots.getAllChatMids(True, True).invitedChatMids]
        if mypen != []:
            for asu in mypen:
                cuk = maxbots.getChats([asu], True , False).chats[0]
                no = no + 1
                ktl += "    • {}. {} {}\n".format(str(no) , cuk.chatName[0:25], len(cuk.extra.groupExtra.memberMids))                                    
            rahman(to, "「 Group 」\n › Type: Invationlist♪\n"+ktl+"\n › Type: Remote♪\n    • " + kalera + "Accept「No/All」\n    • " + kalera + "Reject「No/All」")
    elif cmd.startswith("reject"):
        mmk = removeCmd("reject", text)
        if mmk == "all":
            ginvited = [a for a in maxbots.getAllChatMids(True, True).invitedChatMids]
            if ginvited != [] and ginvited != None:
                for gid in ginvited:
                    time.sleep(0.4)
                    maxbots.rejectChatInvitation(gid)
                rahman(to, "「 Group 」\n › Type: Remote Reject Invation♪ \n    • Amount: {} \n    • Status: Success".format(str(len(ginvited))))
            else:
                rahman(to, "「 Group 」\n › Type: Remote Reject Invation♪\n    • Not Invation")
        else:   
            number = removeCmd("reject", text)
            for ajg in number.split(","):
                groups = [a for a in maxbots.getAllChatMids(True, True).invitedChatMids]
                try:
                    group = groups[int(ajg)-1]
                    G = maxbots.getChats([group], True , False).chats[0]                    
                    try:
                        time.sleep(0.4)
                        maxbots.rejectChatInvitation(G.chatMid)
                    except:
                        time.sleep(0.4)
                        maxbots.rejectChatInvitation(G.chatMid)
                    rahman(to, "「 Group 」\n › Type: Remote Reject Invation♪\n    • Group : " + G.chatName)
                except:
                    rahman(to, "「 Group 」\n › Type: Remote Reject Invation♪\n    • Not Invation")
    elif cmd.startswith("accept"):
        mmk = removeCmd("accept", text)
        if mmk == "all":
            ginvited = [a for a in maxbots.getAllChatMids(True, True).invitedChatMids]
            if ginvited != [] and ginvited != None:
                for gid in ginvited:
                    time.sleep(0.4)
                    maxbots.acceptChatInvitation(gid)                    
                rahman(to, "「 Group 」\n › Type: Remote Accept Invation♪ \n    • Amount: {} \n    • Status: Success".format(str(len(ginvited))))
            else:
                rahman(to, "「 Group 」\n › Type: Remote Accept Invation♪\n    • Not Invation")                
        else:   
            number = removeCmd("accept", text)
            for ajg in number.split(","):
                groups = [a for a in maxbots.getAllChatMids(True, True).invitedChatMids]
                try:
                    group = groups[int(ajg)-1]
                    G = maxbots.getChats([group], True , False).chats[0]                                        
                    try:
                        time.sleep(0.4)
                        maxbots.acceptChatInvitation(G.chatMid)                        
                    except:
                        time.sleep(0.4)
                        maxbots.acceptChatInvitation(G.chatMid)                        
                    rahman(to, "「 Group 」\n › Type: Remote Accept Invation♪\n    • Group : " + G.chatName)
                except:
                    rahman(to, "「 Group 」\n › Type: Remote Accept Invation♪\n    • Not Invation")                   
    elif cmd == 'memberlist':
        if msg.toType == 2:
            tol = cekmember(to)
            if tol:memberGroup(to,tol)               
    elif cmd.startswith("memberlist "):
        sep = msg.text.split(" ");num = msg.text.replace(sep[0] + " ","");gids = [a for a in maxbots.getAllChatMids(True, True).memberChatMids];gid = gids[int(num) - 1];tol = cekmember(gid)
        if tol:memberGroup(to,tol);rahman(to, '「 Group 」\n › Type: Remote Memberlist♪\n    • In Group: {} \n    • Status: Success'.format(maxbots.getChats([gid], True , False).chats[0].chatName))        
    elif cmd == 'pendinglist':
        try:
            if msg.toType == 2:
                tol = cekpending(to)
                if tol:pendingGroup(to,tol)     
        except:rahman(to, '「 Group 」\n › Type: Pendinglist♪ \n    • Nothing Pendinglist')
    elif cmd.startswith("pendinglist "):
        try:
            sep = msg.text.split(" ");num = msg.text.replace(sep[0] + " ","");gids = [a for a in maxbots.getAllChatMids(True, True).memberChatMids];gid = gids[int(num) - 1];tol = cekpending(gid)
            if tol:pendingGroup(to,tol);rahman(to, '「 Group 」\n › Type: Remote Pendinglist♪\n    • In Group: {} \n    • Status: Success'.format(maxbots.getChats([gid], True , False).chats[0].chatName))        
        except:rahman(to, '「 Group 」\n › Type: Remote Pendinglist♪\n    • In Group: {} \n    • Status: Nothing Pendinglist'.format(maxbots.getChats([gid], True , False).chats[0].chatName))   
    elif cmd == 'openqr':
        tol = qrOpen(to)
        if tol:maxbots.sendMessage(to,"「 Group 」\n › Type: Openqr♪\n    • Link: line://ti/g/{} \n    • Status: Success".format(tol))       
    elif cmd.startswith("openqr "):
        sep = msg.text.split(" ");num = msg.text.replace(sep[0] + " ","");gids = [a for a in maxbots.getAllChatMids(True, True).memberChatMids];gid = gids[int(num) - 1];tol = qrOpen(gid)
        if tol:maxbots.sendMessage(to,"「 Group 」\n › Type: Openqr♪\n    • In Group: {}\n    • Link: line://ti/g/{} \n    • Status: Success".format(maxbots.getChats([gid], True , False).chats[0].chatName,tol))       
    elif cmd == 'closeqr':qrClose(to);rahman(to,"「 Group 」\n › Type: Closeqr♪\n    • Status: Success") 
    elif cmd.startswith("closeqr "):sep = msg.text.split(" ");num = msg.text.replace(sep[0] + " ","");gids = [a for a in maxbots.getAllChatMids(True, True).memberChatMids];gid = gids[int(num) - 1];qrClose(gid);rahman(to,"「 Group 」\n › Type: Closeqr♪\n    • In Group: {}\n    • Status: Success".format(maxbots.getChats([gid], True , False).chats[0].chatName))
    elif cmd.startswith('changegname '):
        if msg.toType != 2:return rahman(to,"「 Group 」\n › Type: Change Gname♪\n    • Status: Failed") 
        group = maxbots.getChats([to], True , False).chats[0];ktl = text.split(' ');mmk = text.replace(ktl[0] + ' ','');a = maxbots.getChats([to]).chats[0].chatName
        if len(mmk) > 50:return rahman(to,"「 Group 」\n › Type: Change Gname♪\n    • Status: Failed") 
        group.chatName = mmk;maxbots.updateChat(group, 1);rahman(to,"「 Group 」\n › Type: Change Gname ♪\n    • Before: %s \n    • After: %s \n    • Status: Succes"%(a,mmk))
    elif cmd == 'changegpict':
        if msg.toType != 2: return rahman(to,"「 Group 」\n › Type: Change Gpict♪\n    • Status: Failed") 
        ktl = geTreply(msg)
        if ktl == None:
            pictGroup(to ,"changeGroupPicture","Gpict")         
        else:
            if ktl.contentType == 1:
                path = maxbots.downloadObjectMsg(ktl.id)
                maxbots.updateGroupPicture(to,path)
                rahman(to,   "「 Group 」\n › Type: Change Gpict♪\n    • Status: Success")                                                
    elif cmd == 'changegcover':
        if msg.toType != 2: return rahman(to,"「 Group 」\n › Type: Change Gpict♪\n    • Status: Failed") 
        ktl = geTreply(msg)
        if ktl == None:
            pictGroup(to ,"changeGroupCover","Gcover")         
        else:
            if ktl.contentType == 1:
                path = maxbots.downloadObjectMsg(ktl.id)
                maxbots.updateCoverGroup(to,path)
                rahman(to,   "「 Group 」\n › Type: Change Gcover♪\n    • Status: Success")                  
    elif cmd == 'clear mention':
        try:del position['ROM'][to];rahman(to,"「 Group 」\n › Type: Clear Mention♪\n    • In Group: {}\n    • Status: Success".format(maxbots.getChats([to]).chats[0].chatName))
        except:rahman(to, '「 Group 」\n › Type: Clear Mention♪\n    • In Group: {} \n    • Status: Nothing Mention'.format(maxbots.getChats([to]).chats[0].chatName))
    elif cmd == "who tag":
        if to in position['ROM']:
            moneys = {};msgas = ''            
            for a in position['ROM'][to].items():moneys[a[0]] = [a[1]['msg.id'],a[1]['waktu']] if a[1] is not None else idnya                
            sort = sorted(moneys);sort.reverse();sort = sort[0:];msgas = '「 Group 」\n › Type: Tagme♪';h = [];no = 0                                                
            for m in sort:
                has = '';nol = -1                
                for kucing in moneys[m][0]:nol+=1;has+= '\nline://nv/chatMsg?chatId={}&messageId={} \n{}'.format(to,kucing,humanize.naturaltime(datetime.fromtimestamp(moneys[m][1][nol]/1000)))                                        
                h.append(m);no+=1                
                if m == sort[0]:msgas+= '\n    • {}. @!{}x{}'.format(no,len(moneys[m][0]),has)                    
                else:msgas+= '\n\n    • {}. @!{}x{}'.format(no,len(moneys[m][0]),has)                    
            maxbots.sendTag(to, msgas, h)
        else:msgas = '「 Group 」\n › Type: Tagme♪ \n    • Sorry @! In {} nothink get a mention'.format(maxbots.getChats([to]).chats[0].chatName);maxbots.sendTag(to, msgas, [sender])                        
    elif cmd == settings["leave"].lower():
        leaveed(to)                          
    elif cmd.startswith('sider '):
        mmk = removeCmd("sider", text)
        statCCTV(to, mmk)

    elif cmd == 'cmdlist':
        if settings['setKey']['status'] == True:
            kalera = settings['setKey']['key'].title()
        else:
            kalera = ''
        arifblek = "「 Command 」\n › Type: Cmdlist♪"
        arifblek += f"\n    • Tagall: {settings['tagall']}"
        arifblek += f"\n    • Emojitagall: {settings['emojitagall']}"
        arifblek += f"\n    • Kick: {settings['kick']}"
        arifblek += f"\n    • Kickallpy: {settings['kickallpy']}"
        arifblek += f"\n    • Kill: {settings['kill']}"
        arifblek += f"\n    • Killban: {settings['killban']}"
        arifblek += f"\n    • Killbanpy: {settings['killbanpy']}"
        arifblek += f"\n    • Invite: {settings['invite']}"
        arifblek += f"\n    • Reinvite: {settings['reinvite']}"
        arifblek += f"\n    • Cancel: {settings['cancel']}"
        arifblek += f"\n    • Mkick: {settings['mkick']}"
        arifblek += f"\n    • Slain: {settings['slain']}"
        arifblek += f"\n    • Leave: {settings['leave']}"
        arifblek += f"\n    • Msgsider: {settings['sider']}"
        arifblek += f"\n\n › Type: Cek Sticker♪"
        arifblek += f"\n    • {kalera}Cek Stickerkick"
        arifblek += f"\n    • {kalera}Cek Stickerinvite"
        arifblek += f"\n    • {kalera}Cek Stickerleave"
        arifblek += f"\n    • {kalera}Cek Stickerkickallpy"
        arifblek += f"\n    • {kalera}Cek Stickerkillbanpy"
        arifblek += f"\n    • {kalera}Cek Stickerkillban"
        arifblek += f"\n    • {kalera}Cek Stickerreinvite"
        arifblek += f"\n    • {kalera}Cek Stickermkick"
        arifblek += f"\n    • {kalera}Cek Stickerslain"
        rahman(to, arifblek)
    elif cmd.startswith("changekick "):
        mmk = removeCmd("changekick", text.lower())
        changeMSG(to, mmk.lower(), "kick", "Command" , "Set Kick")                
    elif cmd.startswith("changekill "):
        mmk = removeCmd("changekill", text)
        changeMSG(to, mmk.lower(), "kill", "Command" , "Set Kill")           
    elif cmd.startswith("changekillban "):
        mmk = removeCmd("changekillban", text)
        changeMSG(to, mmk.lower(), "killban", "Command" , "Set Killban")           
    elif cmd.startswith("changekillbanpy "):
        mmk = removeCmd("changekillbanpy", text)
        changeMSG(to, mmk.lower(), "killbanpy", "Command" , "Set Killban PY")           
    elif cmd.startswith("changekickallpy "):
        mmk = removeCmd("changekickallpy", text)
        changeMSG(to, mmk.lower(), "kickallpy", "Command" , "Set Kickall PY")           
    elif cmd.startswith("changeinvite "):
        mmk = removeCmd("changeinvite", text)
        changeMSG(to, mmk.lower(), "invite", "Command" , "Set Invite")                 
    elif cmd.startswith("changereinvite "):
        mmk = removeCmd("changereinvite", text)
        changeMSG(to, mmk.lower(), "reinvite", "Command" , "Set Reinvite")
    elif cmd.startswith("changecancel"):
        mmk = removeCmd("changecancel", text)
        changeMSG(to, mmk.lower(), "cancel", "Command" , "Set Cancel")       
    elif cmd.startswith("changemkick "):
        mmk = removeCmd("changemkick", text)
        changeMSG(to, mmk.lower(), "mkick", "Command" , "Set Mkick")                       
    elif cmd.startswith("changeslain "):
        mmk = removeCmd("changeslain", text)
        changeMSG(to, mmk.lower(), "slain", "Command" , "Set Slain")                                      
    elif cmd.startswith("changeleave "):
        mmk = removeCmd("changeleave", text)
        changeMSG(to, mmk.lower(), "leave", "Command" , "Set Leave")                                      
    elif cmd.startswith("changemsgsider "):
        mmk = removeCmd("changemsgsider", text)
        changeMSG(to, mmk, "sider", "Command" , "Set Msg Sider")                      
    elif cmd.startswith("changemsgleave "):
        mmk = removeCmd("changemsgleave", text)
        changeMSG(to, mmk, "msgleave", "Command" , "Set Msg Leave")             
    elif cmd == 'cek stickerkick':
        try:
            maxbots.sendSticker(to,settings, "stckick")
        except:
            rahman(to, '「 Command 」\n › Type: Cek Stickerkick♪\n    • Nothing Sticker')
    elif cmd == 'cek stickerinvite':
        try:
            maxbots.sendSticker(to,settings, "stcinvite")
        except:
            rahman(to, '「 Command 」\n › Type: Cek Stickerinvite♪\n    • Nothing Sticker')
    elif cmd == 'cek stickerleave':
        try:
            limited["ceks"][to] = time.time() + 1         
            maxbots.sendSticker(to,settings, "stcleave")
        except:
            rahman(to, '「 Command 」\n › Type: Cek Stickerleave♪\n    • Nothing Sticker')
    elif cmd == 'cek stickerkickallpy':
        try:
            limited["ceks"][to] = time.time() + 1         
            maxbots.sendSticker(to,settings, "stckickallpy")
        except:
            rahman(to, '「 Command 」\n › Type: Cek Stickerkickallpy♪\n    • Nothing Sticker')
    elif cmd == 'cek stickerkillbanpy':
        try:
            limited["ceks"][to] = time.time() + 1         
            maxbots.sendSticker(to,settings, "stckillbanpy")
        except:
            rahman(to, '「 Command 」\n › Type: Cek Stickerkillbanpy♪\n    • Nothing Sticker')
    elif cmd == 'cek stickerkillban':
        try:
            limited["ceks"][to] = time.time() + 1         
            maxbots.sendSticker(to,settings, "stckillban")
        except:
            rahman(to, '「 Command 」\n › Type: Cek Stickerkillban♪\n    • Nothing Sticker')
    elif cmd == 'cek stickerreinvite':
        try:
            maxbots.sendSticker(to,settings, "stcreinvite")
        except:
            rahman(to, '「 Command 」\n › Type: Cek Stickerreinvite♪\n    • Nothing Sticker')
    elif cmd == 'cek stickermkick':
        try:
            maxbots.sendSticker(to,settings, "stcmkick")
        except:
            rahman(to, '「 Command 」\n › Type: Cek Stickermkick♪\n    • Nothing Sticker')
    elif cmd == 'cek stickerslain':
        try:
            maxbots.sendSticker(to,settings, "stcslain")
        except:
            rahman(to, '「 Command 」\n › Type: Cek Stickerslain♪\n    • Nothing Sticker')
    elif cmd == 'add stickerkick':
        ktl = geTreply(msg)
        if ktl == None:
            statS2(to, "statkick","Command","Add Stickerkick","Sticker")          
        else:
            if ktl.contentType == 7:
                mmk = printSTC(ktl)
                settings["stckick"] = mmk
                rahman(to,   "「 Command 」\n › Type: Add Stickerkick♪\n    • Status: Success")
    elif cmd == 'add stickerinvite':
        ktl = geTreply(msg)
        if ktl == None:
            statS2(to, "statinvite","Command","Add Stickerinvite","Sticker")          
        else:
            if ktl.contentType == 7:
                mmk = printSTC(ktl)
                settings["stcinvite"] = mmk
                rahman(to,   "「 Command 」\n › Type: Add Stickerinvite♪\n    • Status: Success")
    elif cmd == 'add stickerleave':
        ktl = geTreply(msg)
        if ktl == None:
            statS2(to, "statleave","Command","Add Stickerleave","Sticker")          
        else:
            if ktl.contentType == 7:
                mmk = printSTC(ktl)
                settings["stcleave"] = mmk
                rahman(to,   "「 Command 」\n › Type: Add Stickerleave♪\n    • Status: Success")
    elif cmd == 'add stickerkickallpy':
        ktl = geTreply(msg)
        if ktl == None:
            statS2(to, "statkickallpy","Command","Add Stickerkickallpy","Sticker")          
        else:
            if ktl.contentType == 7:
                mmk = printSTC(ktl)
                settings["stckickallpy"] = mmk
                rahman(to,   "「 Command 」\n › Type: Add Stickerkickallpy♪\n    • Status: Success")
    elif cmd == 'add stickerkillbanpy':
        ktl = geTreply(msg)
        if ktl == None:
            statS2(to, "statkillbanpy","Command","Add Stickerkillbanpy","Sticker")          
        else:
            if ktl.contentType == 7:
                mmk = printSTC(ktl)
                settings["stckillbanpy"] = mmk
                rahman(to,   "「 Command 」\n › Type: Add Stickerkillbanpy♪\n    • Status: Success")
    elif cmd == 'add stickerkillban':
        ktl = geTreply(msg)
        if ktl == None:
            statS2(to, "statkillban","Command","Add Stickerkillban","Sticker")          
        else:
            if ktl.contentType == 7:
                mmk = printSTC(ktl)
                settings["stckillban"] = mmk
                rahman(to,   "「 Command 」\n › Type: Add Stickerkillban♪\n    • Status: Success")
    elif cmd == 'add stickerreinvite':
        ktl = geTreply(msg)
        if ktl == None:
            statS2(to, "statreinvite","Command","Add Stickerreinvite","Sticker")          
        else:
            if ktl.contentType == 7:
                mmk = printSTC(ktl)
                settings["stcreinvite"] = mmk
                rahman(to,   "「 Command 」\n › Type: Add Stickerreinvite♪\n    • Status: Success")
    elif cmd == 'add stickermkick':
        ktl = geTreply(msg)
        if ktl == None:
            statS2(to, "statmkick","Command","Add Stickermkick","Sticker")          
        else:
            if ktl.contentType == 7:
                mmk = printSTC(ktl)
                settings["stcmkick"] = mmk
                rahman(to,   "「 Command 」\n › Type: Add Stickermkick♪\n    • Status: Success")
    elif cmd == 'add stickerslain':
        ktl = geTreply(msg)
        if ktl == None:
            statS2(to, "statslain","Command","Add Stickerslain","Sticker")          
        else:
            if ktl.contentType == 7:
                mmk = printSTC(ktl)
                settings["stcslain"] = mmk
                rahman(to,   "「 Command 」\n › Type: Add Stickerslain♪\n    • Status: Success")
    elif cmd == 'del stickerkick':
        delSTC(to, "stckick","Command","Stickerkick")          
    elif cmd == 'del stickerinvite':
        delSTC(to, "stcinvite","Command","Stickerinvite")          
    elif cmd == 'del stickerleave':
        delSTC(to, "stcleave","Command","Stickerleave")          
    elif cmd == 'del stickerkickallpy':
        delSTC(to, "stckickallpy","Command","Stickerkickallpy")          
    elif cmd == 'del stickerkillbanpy':
        delSTC(to, "stckillbanpy","Command","Stickerkillbanpy")          
    elif cmd == 'del stickerkillban':
        delSTC(to, "stckillban","Command","Stickerkillban")          
    elif cmd == 'del stickerreinvite':
        delSTC(to, "stcreinvite","Command","Stickerreinvite")          
    elif cmd == 'del stickermkick':
        delSTC(to, "stcmkick","Command","Stickermkick")          
    elif cmd == 'del stickerslain':
        delSTC(to, "stcslain","Command","Stickerslain")          

    elif cmd == settings["tagall"].lower():
        if msg.toType == 1:
            members = cektagallM(to)                             
        elif msg.toType == 2:
            members = cekmember(to)               
        else:
            return rahman(to,   "「 Mention 」\n › Type: Tagall♪\n    • Status: Failed Tagall")                                     
        if members:
            tagallMention(to, members)                      
    elif cmd.startswith(settings["tagall"]):
        ppk = removeCmd(settings["tagall"], text)
        num = ppk.replace(ppk.split(" ")[0] + ' ','')
        gids = [a for a in maxbots.getAllChatMids(True, True).memberChatMids]
        gid = gids[int(num) - 1]
        tol = cekmember(gid)
        if tol:
            tagallMention(gid, tol)
            rahman(to, '「 Group 」\n ›Type: Remote Tagall♪\n    • In Group: {} \n    • Status: Success'.format(maxbots.getChats([gid], True , False).chats[0].chatName))                            
    elif cmd.startswith(settings["emojitagall"].lower()):
        try:
            if msg.toType == 1:
                members = cektagallM(to)                             
            elif msg.toType == 2:
                members = cekmember(to)               
            else:
                return rahman(to,   "「 Mention 」\n › Type: Tagall♪\n    • Status: Failed Tagall")                                     
            if members:
                tagallEmot(to, msg, members)           
        except:
            rahman(to, '「 Mention 」\n › Type: Emoji Tagall♪\n    • Nothing Emoji')
    elif cmd == 'mentionnote':
        NoteCreate(to,cmd,msg)         
    elif cmd == 'fakestickerlist':
        typeList(to, "Fake Sticker","fakestickerr")
    elif cmd == 'fakecontactlist':
        typeList(to, "Fake Contact","fakecontactt")
    elif cmd.startswith("addfakesticker"):
        mmk = removeCmd("addfakesticker", text)
        mmk = mmk.lower()    
        if mmk not in listsett["fakestickerr"]:
            settings["Addfakesticker"]["status"] = True
            settings["Addfakesticker"]["name"] = str(mmk.lower())
            listsett["fakestickerr"][str(mmk.lower())] = ""
            rahman(to,"「 List 」\n › Type: Fake Sticker Add♪\n    • Text : {} \n    • Status: Send Sticker".format(str(mmk.lower())))                                                            
        else:
            rahman(to,"「 List 」\n › Type: Fake Sticker Add♪\n    • Status:    • Sticker Already")                                        
    elif cmd.startswith("delfakesticker"):
        mmk = removeCmd("delfakesticker", text)
        mmk = ppk.replace(ppk.split(" ")[0] + ' ','')
        if mmk in listsett["fakestickerr"]:
            del listsett["fakestickerr"][str(mmk.lower())]
            rahman(to,"「 List 」\n › Type: Fake Sticker Del♪\n    • Text : {} \n    • Status: Success".format(str(mmk.lower())))                                            
        else:
            rahman(to,"「 List 」\n › Type: Fake Sticker Del♪\n    • Status: Fake Sticker Not In List")                 
    elif cmd.startswith("addfakecontact"):
        mmk = removeCmd("addfakecontact", text)
        mmk = mmk.lower()    
        if mmk not in listsett["fakecontactt"]:
            settings["Addfakecontact"]["status"] = True
            settings["Addfakecontact"]["name"] = str(mmk.lower())
            listsett["fakecontactt"][str(mmk.lower())] = ""
            rahman(to,"「 List 」\n › Type: Fake Contact Add♪\n    • Text : {} \n    • Status: Send Contact".format(str(mmk.lower())))                                                            
        else:
            rahman(to,"「 List 」\n › Type: Fake Contact Add♪\n    • Status:    • Fake Contact Already")                                        
    elif cmd.startswith("delfakecontact"):
        mmk = removeCmd("delfakecontact", text)
        mmk = mmk.lower()    
        if mmk in listsett["fakecontactt"]:
            del listsett["fakecontactt"][str(mmk.lower())]
            rahman(to,"「 List 」\n › Type: Fake Contact Del♪\n    • Text : {} \n    • Status: Success".format(str(mmk.lower())))                                            
        else:
            rahman(to,"「 List 」\n › Type: Fake Contact Del♪\n    • Status: Fake Contact Not In List")          
    elif cmd.startswith("changetagall "):
        mmk = removeCmd("changetagall", text)
        changeMSG(to, mmk.lower(), "tagall", "Mention" , "Set Tagall")                      
    elif cmd.startswith("changeemojitagall "):
        mmk = removeCmd("changeemojitagall", text)
        changeMSG(to, mmk.lower(), "emojitagall", "Mention" , "Set Emojitagall")                      
    elif cmd.startswith("add emojitagall"):
        jing = text.split(' ')
        ktl = text.replace(jing[2] + ' ','')
        if 'STICON_OWNERSHIP' in msg.contentMetadata:
            settings["fakeemoji"]["emoji"] = json.loads(msg.contentMetadata["STICON_OWNERSHIP"])[0]
            rahman(to,"「 Mention 」\n › Type: Add Emoji Tagall♪\n    • Status: Succes")
        else:
            try:
                mmk = ktl.split("id=")[1].split("&lang")[0]
            except:
                pass
            settings["fakeemoji"]["emoji"] = str(mmk)
            rahman(to,"「 Mention 」\n › Type: Add Emoji Tagall♪\n    • Status: Succes")
    elif cmd == 'cek stickeremojitagall':
        try:
            limited["ceks"][to] = time.time() + 1         
            maxbots.sendSticker(to,settings, "stcemojitagall")
        except:
            rahman(to, '「 Mention 」\n › Type: Cek Stickeremojitagall♪\n    • Nothing Sticker')
    elif cmd == 'cek stickertagall':
        try:
            limited["ceks"][to] = time.time() + 1                  
            maxbots.sendSticker(to,settings,  "stctagall")
        except:
            rahman(to, '「 Mention 」\n › Type: Cek Stickertagall♪\n    • Nothing Sticker')
    elif cmd == 'cek stickerfaketag':
        try:
            limited["ceks"][to] = time.time() + 1         
            maxbots.sendSticker(to,settings, "stkfaketag")
        except:
            rahman(to, '「 Mention 」\n › Type: Cek Stickerfaketag♪\n    • Nothing Sticker')
    elif cmd == 'add stickerfaketag':
        ktl = geTreply(msg)
        if ktl == None:
            statS2(to, "stickerfaketag","Mention","Add Stickerfaketag","Sticker")            
        else:
            if ktl.contentType == 7:
                mmk = printSTC(ktl)
                settings["stkfaketag"] = mmk
                rahman(to,   "「 Mention 」\n › Type: Add Stickerfaketag♪\n    • Status: Success")                                                       
    elif cmd == 'add stickertagall':
        ktl = geTreply(msg)
        if ktl == None:
            statS2(to, "stattagall","Mention","Add Stickertagall","Sticker")                   
        else:
            if ktl.contentType == 7:
                mmk = printSTC(ktl)
                settings["stctagall"] = mmk
                rahman(to,   "「 Mention 」\n › Type: Add Stickertagall♪\n    • Status: Success")                                                                     
    elif cmd == 'add stickeremojitagall':
        ktl = geTreply(msg)
        if ktl == None:
            statS2(to, "statemojitagall","Mention","Add Stickeremojitagall","Sticker")            
        else:
            if ktl.contentType == 7:
                mmk = printSTC(ktl)
                settings["stcemojitagall"] = mmk
                rahman(to,   "「 Mention 」\n › Type: Add Stickeremojitagall♪\n    • Status: Success")                                                          
    elif cmd == 'del stickerfaketag':
        delSTC(to, "stkfaketag","Mention","Stickerfaketag")          
    elif cmd == 'del stickertagall':
        delSTC(to, "stctagall","Mention","Stickertagall")          
    elif cmd == 'del stickeremojitagall':
        delSTC(to, "stcemojitagall","Mention","Stickeremojitagall")                      

    elif cmd == 'prokick list':
        plist(to, "protectkick","Protect Kick", "Prokick")
    elif cmd == 'prokick clear':
        clpro(to, "protectkick","Protect Kick")
    elif cmd.startswith("prokick"):
         mmk = removeCmd("prokick", text)
         statPro(to, mmk, "protectkick", "Protect Kick")
    if cmd.startswith("prokick del"):
         gid = [a for a in settings["protectkick"]]
         if len(cmd.split(" ")) == 3:
             selection = MySplit(cmd.split(' ')[2],range(1,len(gid)+1))
             k = len(gid)//100
             for a in range(k+1):
                 if a == 0:ajg='「 Protect 」\n › Type: Protect Kick♪'
                 else:ajg='「 Protect 」\n › Type: Protect Kick♪\n    • Nothing Group'
                 babi = ''
                 no = 0
                 for i in selection.parse()[a*100 : (a+1)*100]:
                     settings["protectkick"].remove(gid[i - 1])
                     time.sleep(0.4)
                     no+=1
                     gC = maxbots.getChats([gid[i - 1]], True , False).chats[0]                                         
                     if no == len(selection.parse()):
                         babi+= "\n    • {}. {}\n    • Status: Success".format(i,gC.chatName)
                     else:
                         babi+= "\n    • {}. {}".format(i,gC.chatName)
                 rahman(to,ajg+babi)
    elif cmd == 'proinvite list':
        plist(to, "protectinvite","Protect Invite", "Proinvite")
    elif cmd == 'proinvite clear':
        clpro(to, "protectinvite","Protect Invite")
    elif cmd.startswith("proinvite"):
         mmk = removeCmd("proinvite", text)
         statPro(to, mmk, "protectinvite", "Protect Invite")
    if cmd.startswith("proinvite del"):
         gid = [a for a in settings["protectinvite"]]
         if len(cmd.split(" ")) == 3:
             selection = MySplit(cmd.split(' ')[2],range(1,len(gid)+1))
             k = len(gid)//100
             for a in range(k+1):
                 if a == 0:ajg='「 Protect 」\n › Type: Protect Invite♪'
                 else:ajg='「 Protect 」\n › Type: Protect Invite♪\n    • Nothing Group'
                 babi = ''
                 no = 0
                 for i in selection.parse()[a*100 : (a+1)*100]:
                     settings["protectinvite"].remove(gid[i - 1])
                     time.sleep(0.4)
                     no+=1
                     gC = maxbots.getChats([gid[i - 1]], True , False).chats[0]                                         
                     if no == len(selection.parse()):
                         babi+= "\n    • {}. {}\n    • Status: Success".format(i,gC.chatName)
                     else:
                         babi+= "\n    • {}. {}".format(i,gC.chatName)
                 rahman(to,ajg+babi)     
    elif cmd == 'procancel list':
        plist(to, "protectcancel","Protect Cancel", "Procancel")
    elif cmd == 'procancel clear':
        clpro(to, "protectcancel","Protect Cancel")
    elif cmd.startswith("procancel"):
         mmk = removeCmd("procancel", text)
         statPro(to, mmk, "protectcancel", "Protect Cancel")
    if cmd.startswith("procancel del"):
         gid = [a for a in settings["protectcancel"]]
         if len(cmd.split(" ")) == 3:
             selection = MySplit(cmd.split(' ')[2],range(1,len(gid)+1))
             k = len(gid)//100
             for a in range(k+1):
                 if a == 0:ajg='「 Protect 」\n › Type: Protect Cancel♪'
                 else:ajg='「 Protect 」\n › Type: Protect Cancel♪\n    • Nothing Group'
                 babi = ''
                 no = 0
                 for i in selection.parse()[a*100 : (a+1)*100]:
                     settings["protectcancel"].remove(gid[i - 1])
                     time.sleep(0.4)
                     no+=1
                     gC = maxbots.getChats([gid[i - 1]], True , False).chats[0]                                         
                     if no == len(selection.parse()):
                         babi+= "\n    • {}. {}\n    • Status: Success".format(i,gC.chatName)
                     else:
                         babi+= "\n    • {}. {}".format(i,gC.chatName)
                 rahman(to,ajg+babi)         
    elif cmd == 'proqr list':
        plist(to, "protectqr","Protect Qr", "Proqr")
    elif cmd == 'proqr clear':
        clpro(to, "protectqr","Protect Qr")
    elif cmd.startswith("proqr"):
         mmk = removeCmd("proqr", text)
         statPro(to, mmk, "protectqr", "Protect Qr")
    if cmd.startswith("proqr del"):
         gid = [a for a in settings["protectqr"]]
         if len(cmd.split(" ")) == 3:
             selection = MySplit(cmd.split(' ')[2],range(1,len(gid)+1))
             k = len(gid)//100
             for a in range(k+1):
                 if a == 0:ajg='「 Protect 」\n › Type: Protect Qr♪'
                 else:ajg='「 Protect 」\n › Type: Protect Qr♪\n    • Nothing Group'
                 babi = ''
                 no = 0
                 for i in selection.parse()[a*100 : (a+1)*100]:
                     settings["protectqr"].remove(gid[i - 1])
                     time.sleep(0.4)
                     no+=1
                     gC = maxbots.getChats([gid[i - 1]], True , False).chats[0]                                         
                     if no == len(selection.parse()):
                         babi+= "\n    • {}. {}\n    • Status: Success".format(i,gC.chatName)
                     else:
                         babi+= "\n    • {}. {}".format(i,gC.chatName)
                 rahman(to,ajg+babi)     
    elif cmd == 'projoin list':
        plist(to, "protectjoin","Protect Join", "Projoin")
    elif cmd == 'projoin clear':
        clpro(to, "protectjoin","Protect Join")
    elif cmd.startswith("projoin"):
         mmk = removeCmd("projoin", text)
         statPro(to, mmk, "protectjoin", "Protect Join")
    if cmd.startswith("projoin del"):
         gid = [a for a in settings["protectjoin"]]
         if len(cmd.split(" ")) == 3:
             selection = MySplit(cmd.split(' ')[2],range(1,len(gid)+1))
             k = len(gid)//100
             for a in range(k+1):
                 if a == 0:ajg='「 Protect 」\n › Type: Protect Join♪'
                 else:ajg='「 Protect 」\n › Type: Protect Join♪\n    • Nothing Group'
                 babi = ''
                 no = 0
                 for i in selection.parse()[a*100 : (a+1)*100]:
                     settings["protectjoin"].remove(gid[i - 1])
                     time.sleep(0.4)
                     no+=1
                     gC = maxbots.getChats([gid[i - 1]], True , False).chats[0]                                         
                     if no == len(selection.parse()):
                         babi+= "\n    • {}. {}\n    • Status: Success".format(i,gC.chatName)
                     else:
                         babi+= "\n    • {}. {}".format(i,gC.chatName)
                 rahman(to,ajg+babi)   
    elif cmd == 'proname list':
        plist(to, "protectname","Protect Name", "Proname")
    elif cmd == 'proname clear':
        clpro(to, "protectname","Protect Name")                  
    elif cmd.startswith("proname "):
       spl = removeCmd("proname", text)
       z = maxbots.getChats([to]).chats[0].chatName
       if spl == 'on':
           if to in protectname:
               msgs = "「 Protect 」\n › Type: Protect Name♪\n    • Status: Already Active"                
           else:
               protectname[to] = z
               ginfo = maxbots.getChats([to]).chats[0]
               msgs = "「 Protect 」\n › Type: Protect Name♪\n    • In Group : {}\n    • Status: Active".format(str(ginfo.chatName))                                              
           if settings["stattemp"] == True:
               sendON(to, "Protect Name")            
           else:                        
               rahman(to, msgs)
       elif spl == 'off':
             if msg.to in protectname:
                 del protectname[to]
                 ginfo = maxbots.getChats([msg.to]).chats[0]
                 msgs = "「 Protect 」\n › Type: Protect Name♪\n    • In Group : {} \n    • Status: Deactive".format(str(ginfo.chatName))                                                      
             else:
                 msgs = "「 Protect 」\n › Type: Protect Name♪\n    • Status: Already Dective"                  
             if settings["stattemp"] == True:
                 sendOFF(to, "Protect Name")            
             else:                        
               rahman(to, msgs)                                   
    if cmd.startswith("proname del"):
         gid = [a for a in settings["protectname"]]
         if len(cmd.split(" ")) == 3:
             selection = MySplit(cmd.split(' ')[2],range(1,len(gid)+1))
             k = len(gid)//100
             for a in range(k+1):
                 if a == 0:ajg='「 Protect 」\n › Type: Protect Name♪'
                 else:ajg='「 Protect 」\n › Type: Protect Name♪\n    • Nothing Group'
                 babi = ''
                 no = 0
                 for i in selection.parse()[a*100 : (a+1)*100]:
                     del settings["protectname"][gid[i - 1]]
                     time.sleep(0.4)
                     no+=1
                     gC = maxbots.getChats([gid[i - 1]], True , False).chats[0]                                         
                     if no == len(selection.parse()):
                         babi+= "\n    • {}. {}\n    • Status: Success".format(i,gC.chatName)
                     else:
                         babi+= "\n    • {}. {}".format(i,gC.chatName)
                 rahman(to,ajg+babi)       
    elif cmd.startswith("proall "):
        spl = removeCmd("proall", text)
        z = maxbots.getChats([receiver]).chats[0].chatName
        if spl == "on":
            if to in settings["protectkick"]:
                msgs = ""                
            else:
                settings["protectkick"].append(to) 
            if to in settings["protectname"]:
                msgs = ""                
            else:
                protectname[to] = z
            if to in settings["protectqr"]:
                msgs = ""                
            else:
                settings["protectqr"].append(to)                
            if to in settings["protectjoin"]:
                msgs = ""               
            else:
                settings["protectjoin"].append(to)                
            if to in settings["protectcancel"]:
                msgs = ""               
            else:
                settings["protectcancel"].append(to)                
            if to in settings["protectinvite"]:
                msgs = "「 Protect 」\n › Type: Protect All♪\n    • Status: Already Active"                
            else:
                settings["protectinvite"].append(to)
                info = maxbots.getChats([msg.to]).chats[0]
                msgs = "「 Protect 」\n › Type: Protect All♪\n    • In Group : {}\n    • Status: Active".format(str(info.chatName))                                               
            if settings["stattemp"] == True:
                sendON(to, "Protect All")            
            else:                        
                rahman(to, msgs)   
        if spl == "off":
            if to in settings["protectkick"]:
                settings["protectkick"].remove(to)
                msgs = ""                                
            else:
                msgs = "" 
            if to in settings["protectname"]:
                del protectname[msg.to]
                msgs = ""                                
            else:
                msgs = ""         
            if to in settings["protectinvite"]:
                settings["protectinvite"].remove(to)
                msgs = ""                           
            else:
                msgs = ""              
            if to in settings["protectqr"]:
                settings["protectqr"].remove(to)
                msgs = ""                           
            else:
                msgs = ""              
            if to in settings["protectjoin"]:
                settings["protectjoin"].remove(to)
                msgs = ""                           
            else:
                msgs = ""              
            if to in settings["protectcancel"]:
                settings["protectcancel"].remove(to)
                info = maxbots.getChats([to]).chats[0]
                msgs = "「 Protect 」\n › Type: Protect All♪\n    • In Group : {}\n    • Status: Deactive".format(str(info.chatName))                                          
            else:
                msgs = "「 Protect 」\n › Type: Protect All♪\n    • Status: Already Dective"              
            if settings["stattemp"] == True:
                sendOFF(to, "Protect All")            
            else:                        
                rahman(to, msgs)      

    elif cmd == 'blacklist':
        maxbots.sendlistBanning(to, setKey, position,"blacklist","Blacklist","Bl")  
    elif cmd == 'whitelist':
        maxbots.sendlistBanning(to, setKey, position,"whitelist","Whitelist","Wl")
    elif cmd == 'adminlist':
        maxbots.sendlistBanning(to, setKey, position,"admin","Adminlist","Admin")
    elif cmd == 'talkbanlist':
        maxbots.sendlistBanning(to, setKey, position,"talkbanlist","Talkbanlist","Tban")
    elif cmd == 'wl clear':
        clearP(to, "whitelist","Banning","Wl")
    elif cmd == 'bl clear':
        clearP(to, "blacklist","Banning","Bl")
    elif cmd == 'admin clear':
        clearP(to, "admin","Banning","Admin")
    elif cmd == 'tban clear':
        clearP(to, "talkbanlist","Banning","Tban")
    elif cmd == "tban detect":
        if msg.toType == 2:
            banningD(to, "talkbanlist","Tban")
    elif cmd == "wl detect":
        if msg.toType == 2:
            banningD(to, "whitelist","Wl")
    elif cmd == "admin detect":
        if msg.toType == 2:
            banningD(to, "admin","Admin")
    elif cmd == "bl detect":
        if msg.toType == 2:
            banningD(to, "blacklist","Bl")
    elif cmd.startswith('purge '):
        ktl = text.split(' ')
        mmk = text.replace(ktl[0] + ' ','')    
        statS1(to, mmk, "purge","Banning","Purge")           
    elif cmd.startswith('backupwl '):
        ktl = text.split(' ')
        mmk = text.replace(ktl[0] + ' ','')    
        statS1(to, mmk, "backupwl","Banning","Backupwl")                   
    elif cmd.startswith('backupadmin '):
        ktl = text.split(' ')
        mmk = text.replace(ktl[0] + ' ','')    
        statS1(to, mmk, "backupadmin","Banning","Backupadmin")                          
    elif cmd.startswith("wl add"):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            list = geTmention(msg)
            maxbots.datamentions(to,'Banning',list,'ADDWL',position,ps='\n › Type: Wl Add♪')
        else: 
            mmk = removeCmd("wl add", text)
            if mmk == "on":
                statW(to, "wwhitelist","Banning","Wl Add")          
            elif mmk == "here":
                appbanning(to, "whitelist", "Wl")
            elif mmk != " ":
                if msg.relatedMessageId is not None:
                    bb = geTreply(msg)
                    if cmd == "wl add":
                        if bb._from not in position["whitelist"]:
                            finded(bb._from)
                            position["whitelist"].append(bb._from)
                            maxbots.sendTag(to,"「 Banning 」\n › Type: Wl Add♪\n    • 1. @! Add♪",[bb._from])                                                                
                        else:
                            maxbots.sendTag(to,"「 Banning 」\n › Type: Wl Add♪\n    • 1. @! Already♪",[bb._from])                                
    elif cmd.startswith("wl del"):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            list = geTmention(msg)
            maxbots.datamentions(to,'Banning',list,'DELWL',position,ps='\n › Type: Wl Del♪')
        else: 
            mmk = removeCmd("wl del", text)
            if mmk == "on":
                statW(to, "dwhitelist","Banning","Wl Del")          
            elif mmk == "here":
                rembanning(to, "whitelist", "Wl")
            elif mmk != " ":
                if msg.relatedMessageId is not None:
                    bb = geTreply(msg)
                    if cmd == "wl del":
                        if bb._from in position["whitelist"]:
                            position["whitelist"].remove(bb._from)
                            maxbots.sendTag(to,"「 Banning 」\n › Type: Wl Del♪\n    • 1. @! Del♪",[bb._from])                                                                
                        else:
                            maxbots.sendTag(to,"「 Banning 」\n › Type: Wl Del♪\n    • 1. @! Nothing♪",[bb._from])                                             
                else:
                    try:
                        x = splitdel(str(mmk), position["whitelist"])
                        z = len(position["whitelist"])//100
                        for c in range(z+1):
                            if c == 0:
                                maxbots.datamentions(to,'Banning',x[:100],'DELWL',position,ps='\n › Type: Wl Del♪')
                            else:
                                maxbots.datamentions(to,'Banning',x[c*100 : (c+1)*100],'DELWL',position,ps='\n › Type: Wl Del♪')
                    except:
                        rahman(to,"「 Banning 」\n › Type: Wl Del♪\n   • Please Command @/Reply/Num")                   
    elif cmd.startswith("admin add"):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            list = geTmention(msg)
            maxbots.datamentions(to,'Banning',list,'ADDADMIN',position,ps='\n › Type: Admin Add♪')
        else: 
            mmk = removeCmd("admin add", text)
            if mmk == "on":
                statW(to, "wadminlist","Banning","Admin Add")          
            elif mmk == "here":
                appbanning(to, "admin", "Admin")
            elif mmk != " ":
                if msg.relatedMessageId is not None:
                    bb = geTreply(msg)
                    if cmd == "admin add":
                        if bb._from not in position["admin"]:
                            finded(bb._from)
                            position["admin"].append(bb._from);maxbots.sendTag(to,"「 Banning 」\n › Type: Admin Add♪\n    • 1. @! Add♪",[bb._from])                                                                
                        else:
                            maxbots.sendTag(to,"「 Banning 」\n › Type: Admin Add♪\n    • 1. @! Already♪",[bb._from])                                
    elif cmd.startswith("admin del"):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            list = geTmention(msg)
            maxbots.datamentions(to,'Banning',list,'DELADMIN',position,ps='\n › Type: Admin Del♪')
        else: 
            mmk = removeCmd("admin del", text)
            if mmk == "on":
                statW(to, "dadminlist","Banning","Admin Del")          
            elif mmk == "here":
                rembanning(to, "admin", "Admin")
            elif mmk != " ":
                if msg.relatedMessageId is not None:
                    bb = geTreply(msg)
                    if cmd == "admin del":
                        if bb._from in position["admin"]:
                            position["admin"].remove(bb._from)
                            maxbots.sendTag(to,"「 Banning 」\n › Type: Admin Del♪\n    • 1. @! Del♪",[bb._from])                                                                
                        else:maxbots.sendTag(to,"「 Banning 」\n › Type: Admin Del♪\n    • 1. @! Nothing♪",[bb._from])                                             
                else:
                    try:
                        x = splitdel(str(mmk), position["admin"])
                        z = len(position["admin"])//100
                        for c in range(z+1):
                            if c == 0:
                                maxbots.datamentions(to,'Banning',x[:100],'DELADMIN',position,ps='\n › Type: Admin Del♪')
                            else:
                                maxbots.datamentions(to,'Banning',x[c*100 : (c+1)*100],'DELADMIN',position,ps='\n › Type: Admin Del♪')
                    except:
                        rahman(to,"「 Banning 」\n › Type: Admin Del♪\n   • Please Command @/Reply/Num")                   
    elif cmd.startswith("bl add"):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            list = geTmention(msg)
            maxbots.datamentions(to,'Banning',list,'ADDBL',position,ps='\n › Type: Bl Add♪')
        else: 
            mmk = removeCmd("bl add", text)
            if mmk == "on":
                statW(to, "wblacklist","Banning","Bl Add")          
            elif mmk == "here":
                appbanning(to, "blacklist", "Bl")
            elif mmk != " ":
                if msg.relatedMessageId is not None:
                    bb = geTreply(msg)
                    if cmd == "bl add":
                        if bb._from not in position["blacklist"]:
                            position["blacklist"].append(bb._from)
                            maxbots.sendTag(to,"「 Banning 」\n › Type: Bl Add♪\n    • 1. @! Add♪",[bb._from])                                                                
                        else:
                            maxbots.sendTag(to,"「 Banning 」\n › Type: Bl Add♪\n    • 1. @! Already♪",[bb._from])                                
    elif cmd.startswith("bl del"):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            list = geTmention(msg)
            maxbots.datamentions(to,'Banning',list,'DELBL',position,ps='\n › Type: Bl Del♪')
        else: 
            mmk = removeCmd("bl del", text)
            if mmk == "on":
                statW(to, "dblacklist","Banning","Bl Del")          
            elif mmk == "here":
                rembanning(to, "blacklist", "Bl")
            elif mmk != " ":
                if msg.relatedMessageId is not None:
                    bb = geTreply(msg)
                    if cmd == "bl del":
                        if bb._from in position["blacklist"]:
                            position["blacklist"].remove(bb._from)
                            maxbots.sendTag(to,"「 Banning 」\n › Type: Bl Del♪\n    • 1. @! Del♪",[bb._from])                                                                
                        else:
                            maxbots.sendTag(to,"「 Banning 」\n › Type: Bl Del♪\n    • 1. @! Nothing♪",[bb._from])                                             
                else:
                    try:
                        x = splitdel(str(mmk), position["blacklist"])
                        z = len(position["blacklist"])//100
                        for c in range(z+1):
                            if c == 0:
                                maxbots.datamentions(to,'Banning',x[:100],'DELBL',position,ps='\n › Type: Bl Del♪')
                            else:
                                maxbots.datamentions(to,'Banning',x[c*100 : (c+1)*100],'DELBL',position,ps='\n › Type: Bl Del♪')
                    except:rahman(to,"「 Banning 」\n › Type: Bl Del♪\n   • Please Command @/Reply/Num")                   
    elif cmd.startswith("tban add"):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            list = geTmention(msg)
            maxbots.datamentions(to,'Banning',list,'ADDTBAN',position,ps='\n › Type: Tban Add♪')
        else: 
            mmk = removeCmd("tban add", text)
            if mmk == "on":
                statW(to, "wtalkbanlist","Banning","Tban Add")          
            elif mmk == "here": 
                appbanning(to, "talkbanlist", "Tban")
            elif mmk != " ":
                if msg.relatedMessageId is not None:
                    bb = geTreply(msg)
                    if cmd == "tban add":
                        if bb._from not in position["talkbanlist"]:
                            position["talkbanlist"].append(bb._from)
                            maxbots.sendTag(to,"「 Banning 」\n › Type: Tban Add♪\n    • 1. @! Add♪",[bb._from])                                                                
                        else:
                            maxbots.sendTag(to,"「 Banning 」\n › Type: Tban Add♪\n    • 1. @! Already♪",[bb._from])                                
    elif cmd.startswith("tban del"):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            list = geTmention(msg)
            maxbots.datamentions(to,'Banning',list,'DELTBAN',position,ps='\n › Type: Tban Del♪')
        else: 
            mmk = removeCmd("tban del", text)
            if mmk == "on":
                statW(to, "dtalkbanlist","Banning","Tban Del")          
            elif mmk == "here":
                rembanning(to, "talkbanlist", "Tban")
            elif mmk != " ":
                if msg.relatedMessageId is not None:
                    bb = geTreply(msg)
                    if cmd == "tban del":
                        if bb._from in position["talkbanlist"]:
                            position["talkbanlist"].remove(bb._from)
                            maxbots.sendTag(to,"「 Banning 」\n › Type: Tban Del♪\n    • 1. @! Del♪",[bb._from])                                                                
                        else:
                            maxbots.sendTag(to,"「 Banning 」\n › Type: Tban Del♪\n    • 1. @! Nothing♪",[bb._from])                                             
                else:
                    try:
                        x = splitdel(str(mmk), position["talkbanlist"])
                        z = len(position["talkbanlist"])//100
                        for c in range(z+1):
                            if c == 0:
                                maxbots.datamentions(to,'Banning',x[:100],'DELTBAN',position,ps='\n › Type: Tban Del♪')
                            else:
                                maxbots.datamentions(to,'Banning',x[c*100 : (c+1)*100],'DELTBAN',position,ps='\n › Type: Tban Del♪')
                    except:
                        rahman(to,"「 Banning 」\n › Type: Tban Del♪\n   • Please Command @/Reply/Num")                   

    if cmd.startswith("addbcmute "):
     if msg.toType in [0,1,2]:
         gid = [a for a in maxbots.getAllChatMids(True, True).memberChatMids]
         if len(cmd.split(" ")) == 2:
             selection = MySplit(cmd.split(' ')[1],range(1,len(gid)+1))
             k = len(gid)//100
             for a in range(k+1):
                 if a == 0:ajg='「 Broadcast 」\n › Type: Addbcmute♪'
                 else:ajg='「 Broadcast 」\n › Type: Addbcmute♪\n    • Nothing Group'
                 babi = ''
                 no = 0
                 for i in selection.parse()[a*100 : (a+1)*100]:
                     position["bcfilter"].append(gid[i - 1])
                     time.sleep(0.4)
                     no+=1
                     gC = maxbots.getChats([gid[i - 1]], True , False).chats[0]                                         
                     if no == len(selection.parse()):
                         babi+= "\n    • {}. {}\n    • Status: Success".format(i,gC.chatName)
                     else:
                         babi+= "\n    • {}. {}".format(i,gC.chatName)
                 rahman(to,ajg+babi)
    if cmd.startswith("delbcmute "):
     if msg.toType in [0,1,2]:
         gid = [a for a in position["bcfilter"]]
         if len(cmd.split(" ")) == 2:
             selection = MySplit(cmd.split(' ')[1],range(1,len(gid)+1))
             k = len(gid)//100
             for a in range(k+1):
                 if a == 0:ajg='「 Broadcast 」\n › Type: Delbcmute♪'
                 else:ajg='「 Broadcast 」\n › Type: Delbcmute♪\n    • Nothing Group'
                 babi = ''
                 no = 0
                 for i in selection.parse()[a*100 : (a+1)*100]:
                     position["bcfilter"].remove(gid[i - 1])
                     time.sleep(0.4)
                     no+=1
                     gC = maxbots.getChats([gid[i - 1]], True , False).chats[0]                                         
                     if no == len(selection.parse()):
                         babi+= "\n    • {}. {}\n    • Status: Success".format(i,gC.chatName)
                     else:
                         babi+= "\n    • {}. {}".format(i,gC.chatName)
                 rahman(to,ajg+babi)
    elif cmd == 'bcmutelist':
        ma = ""
        a = 0
        for group in position["bcfilter"]:
            a = a + 1
            ma += "    • " + str(a) + ". " + maxbots.getChats([group]).chats[0].chatName + "\n"
        rahman(to,"「 Broadcast 」\n › Type: Bcfilterlist♪\n"+ ma)

    elif cmd == 'clearbcmute':
        clearP(to, "bcfilter","Broadcast","Bcmute")        

    elif cmd.startswith("broadcast"):
        mmk = removeCmd("broadcast", text)
        if cmd == 'broadcast':
            rahman(to, broadcastH())
        elif mmk == "1":
            settings["mltbc1"] = True
            if to not in position["timebc"]:
                position["timebc"].append(to)
            rahman(to,   "「 Broadcast 」\n › Type: Broadcast♪\n    • Status: Send Text/Image/Video/Audio/Contact/Sticker/Emoji/Post \n    • Type `Abort` For Cancel")
        elif mmk == "2":
            settings["mltbc2"] = True
            if to not in position["timebc"]:
                position["timebc"].append(to)
            rahman(to,   "「 Broadcast 」\n › Type: Broadcast♪\n    • Status: Send Text/Image/Video/Audio/Contact/Sticker/Emoji/Post \n    • Type `Abort` For Cancel")
        elif mmk == "0":
            settings["mltbc0"] = True
            if to not in position["timebc"]:
                position["timebc"].append(to)
            rahman(to,   "「 Broadcast 」\n › Type: Broadcast♪\n    • Status: Send Text/Image/Video/Audio/Contact/Sticker/Emoji/Post \n    • Type `Abort` For Cancel")

    elif cmd.startswith("send broadcast"):
        position["timebc"].clear()
        if settings["mltbc2"]:
            asu = [a for a in maxbots.getAllChatMids(True, True).memberChatMids]
            bcan = position["multibc"]
            hotel = []
            for x in asu:
                if x not in position['bcfilter']:
                    hotel.append(x)
            rahman(to,"「 Broadcast 」\n › Type: Broadcast Multi♪\n    • Status: Send Broadcast ")
            for ngewe in hotel:
                try:
                    time.sleep(0.5)
                    for bc in bcan:
                        if "png" in bc:
                            time.sleep(0.5)
                            maxbots.sendImage(ngewe, bc)              
                        elif "mp4" in bc:
                            time.sleep(0.5)
                            maxbots.sendVideo(ngewe, bc)              
                        elif "mp3" in bc:
                            time.sleep(0.5)
                            maxbots.sendAudio(ngewe, bc)              
                        elif "stc" in bc:
                            time.sleep(0.5)
                            maxbots.sendMessage(ngewe, "", position[bc], 7)
                        elif "(" in bc:
                            time.sleep(0.5)
                            try:
                                maxbots.sendMessage(ngewe, bc,position[bc])
                            except:
                                maxbots.sendMessage(ngewe, bc)
                        elif len(bc) == 33:
                            try:
                                time.sleep(0.5)
                                maxbots.sendContact(ngewe, bc)
                            except:
                                maxbots.sendMessage(ngewe, bc)
                        elif len(bc) == 19:
                            try:
                                time.sleep(0.5)
                                maxbots.sendPostToTalk(ngewe, bc)
                            except:
                                maxbots.sendMessage(ngewe, bc)
                        else:                  
                            time.sleep(0.5)
                            maxbots.sendMessage(ngewe, bc)
                except:
                    hotel.remove(ngewe)
                    continue
                time.sleep(0.8)
            for x in position["bot"]:
                del position[x]
            settings["mltbc2"] = False
            position["timebc"].clear()
            position["multibc"].clear()
            position["bot"].clear()
            rahman(to,"「 Broadcast 」\n › Type: Broadcast♪\n    • Group: {}    \n    • Status: Succes".format(len(hotel)))                                  
        if settings["mltbc1"]:
            bcan = position["multibc"]
            hotel = maxbots.getAllContactIds()
            rahman(to,"「 Broadcast 」\n › Type: Broadcast♪\n    • Status: Send Broadcast ")
            for ngewe in hotel:
                try:
                    time.sleep(0.5)
                    for bc in bcan:
                        if "png" in bc:
                            time.sleep(0.5)
                            maxbots.sendImage(ngewe, bc)              
                        elif "mp4" in bc:
                            time.sleep(0.5)
                            maxbots.sendVideo(ngewe, bc)              
                        elif "mp3" in bc:
                            time.sleep(0.5)
                            maxbots.sendAudio(ngewe, bc)              
                        elif "stc" in bc:
                            time.sleep(0.5)
                            maxbots.sendMessage(ngewe, "", position[bc], 7)
                        elif "(" in bc:
                            time.sleep(0.5)
                            maxbots.sendMessage(ngewe, bc,position[bc])
                        elif len(bc) == 33:
                            try:
                                time.sleep(0.5)
                                maxbots.sendContact(ngewe, bc)
                            except:
                                maxbots.sendMessage(ngewe, bc)
                        elif len(bc) == 19:
                            try:
                                time.sleep(0.5)
                                maxbots.sendPostToTalk(ngewe, bc)
                            except:
                                maxbots.sendMessage(ngewe, bc)
                        else:                  
                            time.sleep(0.5)
                            maxbots.sendMessage(ngewe, bc)
                except:
                    hotel.remove(ngewe)
                    continue
                time.sleep(0.8)
            for x in position["bot"]:
                del position[x]
            settings["mltbc1"] = False
            position["timebc"].clear()
            position["multibc"].clear()
            position["bot"].clear()
            rahman(to,"「 Broadcast 」\n › Type: Broadcast♪\n    • Friend: {}    \n    • Status: Succes".format(len(hotel)))                                  
        if settings["mltbc0"]:
            bcan = position["multibc"]
            open = maxbots.getAllContactIds()
            bo = [a for a in maxbots.getAllChatMids(True, True).memberChatMids]
            hotel = open + bo
            rahman(to,"「 Broadcast 」\n › Type: Broadcast♪\n    • Status: Send Broadcast ")
            for ngewe in hotel:
                try:
                    time.sleep(0.5)
                    for bc in bcan:
                        if "png" in bc:
                            time.sleep(0.5)
                            maxbots.sendImage(ngewe, bc)              
                        elif "mp4" in bc:
                            time.sleep(0.5)
                            maxbots.sendVideo(ngewe, bc)              
                        elif "mp3" in bc:
                            time.sleep(0.5)
                            maxbots.sendAudio(ngewe, bc)              
                        elif "stc" in bc:
                            time.sleep(0.5)
                            maxbots.sendMessage(ngewe, "", position[bc], 7)
                        elif "(" in bc:
                            time.sleep(0.5)
                            maxbots.sendMessage(ngewe, bc,position[bc])
                        elif len(bc) == 33:
                            try:
                                time.sleep(0.5)
                                maxbots.sendContact(ngewe, bc)
                            except:
                                maxbots.sendMessage(ngewe, bc)
                        elif len(bc) == 19:
                            try:
                                time.sleep(0.5) 
                                maxbots.sendPostToTalk(ngewe, bc)
                            except:
                                maxbots.sendMessage(ngewe, bc)
                        else:                  
                            time.sleep(0.5)
                            maxbots.sendMessage(ngewe, bc)
                except:
                    hotel.remove(ngewe)
                    continue
                time.sleep(0.8)
            for x in position["bot"]:
                del position[x]
            settings["mltbc0"] = False
            position["timebc"].clear()
            position["multibc"].clear()
            position["bot"].clear()
            rahman(to,"「 Broadcast 」\n › Type: Broadcast♪\n    • Friend: {}\n    • Group: {}    \n    • Status: Succes".format(len(open),len(bo)))

    elif cmd.startswith(settings["invite"]):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            lists = geTmention(msg)
            ktl = maxbots.getChats([to]).chats[0]
            target = []
            for x in lists:
                if x not in ktl.extra.groupExtra.memberMids and x not in ktl.extra.groupExtra.inviteeMids and x not in target:
                    target.append(x)
            if target:
                total = 500 - len(ktl.extra.groupExtra.memberMids) - len(ktl.extra.groupExtra.inviteeMids)
                if total != 0: 
                    maxbots.inviteIntoChat(to, target[0:total]) 
                    for xxx in target[0:total]:
                        ngelastlist(to, "lastinvite", xxx)
                    position["today"]["invite"] += len(target[0:total])
        else: 
            if msg.relatedMessageId is not None:
                bb = geTreply(msg)
                if cmd == settings["invite"].lower():
                    try:
                        invited(to, bb._from)
                    except:pass              
            else:
                mmk = removeCmd(settings["invite"], text)
                if mmk == "lcon":
                    try:
                        ls = last_game["ROM"][to]["lastcontact"]["last"]
                        invited(to, ls)                                            
                    except:pass 
                elif mmk == "lkick":
                    try:
                        ls = last_game["ROM"][to]["lastkick"]["last"]
                        invited(to, ls)                                            
                    except:pass 
                elif mmk == "lcancel":
                    try:
                        ls = last_game["ROM"][to]["lastcancel"]["last"]
                        invited(to, ls)                                            
                    except:pass   
                elif mmk == "lleave":
                    try:
                        ls = last_game["ROM"][to]["lastleave"]["last"]
                        invited(to, ls)                                            
                    except:pass   
                elif mmk == "ljoin":
                    try:
                        ls = last_game["ROM"][to]["lastjoin"]["last"]
                        invited(to, ls)                                            
                    except:pass      

                else:
                    if mmk == '':
                        return     
                    lists= friendGet(mmk)
                    ktl = maxbots.getChats([to]).chats[0]
                    target = []
                    for x in lists:
                        if x in ktl.extra.groupExtra.memberMids or x in ktl.extra.groupExtra.inviteeMids:
                            continue
                        if x not in target:
                            target.append(x)
                    if target:
                        total = 500 - len(ktl.extra.groupExtra.memberMids) - len(ktl.extra.groupExtra.inviteeMids)
                        if total != 0: 
                            maxbots.inviteIntoChat(to, target[0:total]) 
                            for xxx in target[0:total]:
                                ngelastlist(to, "lastinvite", xxx)
                            position["today"]["invite"] += len(target[0:total])


    elif cmd.startswith(settings["reinvite"]):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            lists = geTmention(msg)
            for ls in lists:
                kicked(to, ls)          
                invited(to, ls)                   
        else:
            if msg.relatedMessageId is not None:
                bb = geTreply(msg)
                if cmd == settings["reinvite"].lower():
                    kicked(to, bb._from)          
                    invited(to, bb._from)       
            else:
                name = removeCmd(settings["reinvite"], text)
                if name == '':
                    return                      
                lists = memberGet(to,name)
                for ls in lists:
                    kicked(to, ls)          
                    invited(to, ls)    
    elif cmd.startswith(settings["kick"]):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            lists = geTmention(msg)
            for ls in lists:
                kicked(to, ls)                 
        else:
            if msg.relatedMessageId is not None:
                bb = geTreply(msg)
                if cmd == settings["kick"].lower():
                    kicked(to, bb._from)          
            else:
                name = removeCmd(settings["kick"], text)
                if name == "":
                    pass
                else:                     
                    lists = memberGet(to,name)
                    for ls in lists:
                        kicked(to, ls)          
    elif cmd.startswith(settings["mkick"]):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            lists = geTmention(msg)
            for ls in lists:
                kicked(to, ls)
                invited(to, ls)
                canceled(to, ls)
                invited(to, ls)
                canceled(to, ls)                
        else:
            if msg.relatedMessageId is not None:
                bb = geTreply(msg)
                if cmd == settings["mkick"].lower():
                    kicked(to, bb._from)
                    invited(to, bb._from)
                    canceled(to, bb._from)
                    invited(to, bb._from)
                    canceled(to, bb._from)     
            else:
                name = removeCmd(settings["mkick"], text)   
                if name == '':
                    return                      
                lists = memberGet(to,name)
                for ls in lists:
                    kicked(to, ls)
                    invited(to, ls)
                    canceled(to, ls)
                    invited(to, ls)
                    canceled(to, ls)                                        
    elif cmd.startswith(settings["slain"]):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            lists = geTmention(msg)
            for ls in lists:
                kicked(to, ls)
                invited(to, ls)
                canceled(to, ls)
                invited(to, ls)
        else:
            if msg.relatedMessageId is not None:
                bb = geTreply(msg)
                if cmd == settings["slain"].lower():
                    kicked(to, bb._from)
                    invited(to, bb._from)
                    canceled(to, bb._from)
                    invited(to, bb._from)               
            else:
                name = removeCmd(settings["slain"], text)  
                if name == '':
                  return                      
                lists = memberGet(to,name)
                for ls in lists:
                    kicked(to, ls)
                    invited(to, ls)
                    canceled(to, ls)
                    invited(to, ls)                                                                                 
    elif cmd.startswith(settings["kill"]):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            lists = geTmention(msg)
            cm = 'kickall.js gid={} type=dual token={} {}'.format(to, maxbots.authToken, appNameJs)
            for ls in lists:
                cm += ' uid={}'.format(ls)
                position["today"]["kick"] += 1
            success = execute_js(cm)          
        else:
            name = removeCmd(settings["kill"], text)
            if name == "":
                return              
            list = pendingGet(to,name)
            lists = memberGet(to,name)
            cm = 'kickall.js gid={} type=dual token={} {}'.format(to, maxbots.authToken, appNameJs)
            for x in list:
                cm += ' uik={}'.format(x)
                position["today"]["cancel"] += 1
            for x in lists:
                cm += ' uid={}'.format(x)
                position["today"]["kick"] += 1
            success = execute_js(cm)        
    elif cmd.startswith(settings["cancel"]):
        name = removeCmd(settings["cancel"], text)
        if name == "":
            pass
        else:
            list = pendingGet(to,name)
            for ls in list:
                maxbots.cancelChatInvitation(to, [ls])
                position["today"]["cancel"] += 1
    elif cmd == settings["killban"].lower():          
        purgeJS(to)         
    elif cmd == settings["killbanpy"].lower():          
        purgePY(to)         
    elif cmd == settings["kickallpy"].lower():          
        kickallPY(to)
    elif cmd.startswith(settings["kickallpy"]):
      num = removeCmd(settings["kickallpy"], text)
      groups = [a for a in maxbots.getAllChatMids(True, True).memberChatMids]
      groupp = groups[int(num) - 1]
      success = kickallPY(groupp) 
      if success:
          rahman(to,"「 Group 」\n › Type: Remote Kickall PY♪\n    • In group: {} \n    • Status: Failed".format(maxbots.getChats([groupp]).chats[0].chatName))
      else:
          rahman(to,"「 Group 」\n › Type: Remote Kickall PY♪\n    • In group: {} \n    • Status: Success".format(maxbots.getChats([groupp]).chats[0].chatName))

    elif cmd == 'del stickerbypass':
        delSTC(to, "stcjsbypass","Js","Stickerbypass")          
    elif cmd == 'del stickerkickall':
        delSTC(to, "stcjskickall","Js","Stickerkickall")          
    elif cmd == 'del stickercancelall':
        delSTC(to, "stcjscancelall","Js","Stickercancelall")          
    elif cmd.startswith('js'):
        mmk = removeCmd("js", text)
        statS1(to, mmk, "javascript","Js","Java Script")                   
    elif cmd.startswith("changebypass"):
        mmk = removeCmd("changebypass", text)
        changeMSG(to, mmk.lower(), "bypass", "Js" , "Set Bypass")           
    elif cmd.startswith("changekickall"):
        mmk = removeCmd("changekickall", text)
        changeMSG(to, mmk.lower(),"kickall", "Js" , "Set Kickall")           
    elif cmd.startswith("changecancelall"):
        mmk = removeCmd("changecancelall", text)
        changeMSG(to, mmk.lower(), "cancelall", "Js" , "Set Cancelall")           
    elif cmd == settings["bypass"]:
      if settings["javascript"]:
          success = bypassJS(to) 
          if success:
              rahman(to,"「 Js 」\n › Type: Bypass♪\n    • In group: {} \n    • Status: Success".format(maxbots.getChats([to]).chats[0].chatName))
          else:
              rahman(to,"「 Js 」\n › Type: Bypass♪\n    • In group: {} \n    • Status: Failed".format(maxbots.getChats([to]).chats[0].chatName))
    elif cmd == settings["kickall"]:
      if settings["javascript"]:
          success = kickallJS(to)
          if success:
              rahman(to,"「 Js 」\n › Type: Kickall♪\n    • In group: {} \n    • Status: Success".format(maxbots.getChats([to]).chats[0].chatName))
          else:
              rahman(to,"「 Js 」\n › Type: Kickall♪\n    • In group: {} \n    • Status: Failed".format(maxbots.getChats([to]).chats[0].chatName))
    elif cmd == settings["cancelall"]:
      if settings["javascript"]:
          success = cancelallJS(to)
          if success:
              rahman(to,"「 Js 」\n › Type: Cancelall♪\n    • In group: {} \n    • Status: Failed".format(maxbots.getChats([to]).chats[0].chatName))
          else:
              rahman(to,"「 Js 」\n › Type: Cancelall♪\n    • In group: {} \n    • Status: Success".format(maxbots.getChats([to]).chats[0].chatName))
    elif cmd.startswith(settings["bypass"]):
      if settings["javascript"]:
          num = removeCmd(settings["bypass"], text)
          groups = [a for a in maxbots.getAllChatMids(True, True).memberChatMids]
          groupp = groups[int(num) - 1]
          success = bypassJS(groupp) 
          if success:
              rahman(to,"「 Group 」\n › Type: Remote Bypass♪\n    • In group: {} \n    • Status: Success".format(maxbots.getChats([groupp]).chats[0].chatName))
          else:
              rahman(to,"「 Group 」\n › Type: Remote Bypass♪\n    • In group: {} \n    • Status: Failed".format(maxbots.getChats([groupp]).chats[0].chatName))
    elif cmd.startswith(settings["kickall"]):
      if settings["javascript"]:
          num = removeCmd(settings["kickall"], text)
          groups = [a for a in maxbots.getAllChatMids(True, True).memberChatMids]
          groupp = groups[int(num) - 1]
          success = kickallJS(groupp) 
          if success:
              rahman(to,"「 Group 」\n › Type: Remote Kickall♪\n    • In group: {} \n    • Status: Success".format(maxbots.getChats([groupp]).chats[0].chatName))
          else:
              rahman(to,"「 Group 」\n › Type: Remote Kickall♪\n    • In group: {} \n    • Status: Failed".format(maxbots.getChats([groupp]).chats[0].chatName))
    elif cmd.startswith(settings["cancelall"]):
      if settings["javascript"]:
          num = removeCmd(settings["cancelall"], text)
          groups = [a for a in maxbots.getAllChatMids(True, True).memberChatMids]
          groupp = groups[int(num) - 1]
          success = cancelallJS(groupp) 
          if success:
              rahman(to,"「 Group 」\n › Type: Remote Cancellall♪\n    • In group: {} \n    • Status: Success".format(maxbots.getChats([groupp]).chats[0].chatName))
          else:
              rahman(to,"「 Group 」\n › Type: Remote Cancellall♪\n    • In group: {} \n    • Status: Failed".format(maxbots.getChats([groupp]).chats[0].chatName))       
    elif cmd == 'cek stickerbypass':
        try:
            limited["ceks"][to] = time.time() + 1         
            maxbots.sendSticker(to,settings, "stcjsbypass")
        except:
            rahman(to, '「 Js 」\n › Type: Cek Stickerbypass♪\n    • Nothing Sticker')
    elif cmd == 'cek stickerkickall':
        try:
            limited["ceks"][to] = time.time() + 1         
            maxbots.sendSticker(to,settings, "stcjskickall")
        except:
            rahman(to, '「 Js 」\n › Type: Cek Stickerkickall♪\n    • Nothing Sticker')
    elif cmd == 'cek stickercancelall':
        try:
            limited["ceks"][to] = time.time() + 1         
            maxbots.sendSticker(to,settings, "stcjscancelall")
        except:
            rahman(to, '「 Js 」\n › Type: Cek Stickercancelall♪\n    • Nothing Sticker')
    elif cmd == 'add stickerbypass':
        ktl = geTreply(msg)
        if ktl == None:
            statS2(to, "statjsbypass","Js","Add Stickerbypass","Sticker")          
        else:
            if ktl.contentType == 7:
                mmk = printSTC(ktl)
                settings["stcjsbypass"] = mmk
                rahman(to,   "「 Js 」\n › Type: Add Stickerbypass♪\n    • Status: Success")
    elif cmd == 'add stickerkickall':
        ktl = geTreply(msg)
        if ktl == None:
            statS2(to, "statjskickall","Js","Add Stickerkickall","Sticker")          
        else:
            if ktl.contentType == 7:
                mmk = printSTC(ktl)
                settings["stcjskickall"] = mmk
                rahman(to,   "「 Js 」\n › Type: Add Stickerkickall♪\n    • Status: Success")
    elif cmd == 'add stickercancelall':
        ktl = geTreply(msg)
        if ktl == None:
            statS2(to, "statjscancelall","Js","Add Stickerkickall","Sticker")          
        else:
            if ktl.contentType == 7:
                mmk = printSTC(ktl)
                settings["stcjscancelall"] = mmk
                rahman(to,   "「 Js 」\n › Type: Add Stickercancelall♪\n    • Status: Success")

    elif cmd.startswith("spamtag"):
        dan = text.split(" ")
        num = int(dan[1])        
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            lists = geTmention(msg)
            for ls in lists:
                for var in range(0,num):
                    maxbots.sendTag(to, "@!", [ls])                    
            rahman(to, "「 Spam 」\n › Type: Spamtag♪ \n    • Amount : {}\n    • Status: Success".format(str(dan[1]))) 
        else:
            if msg.relatedMessageId is not None:
                aa = maxbots.getRecentMessagesV2(to, 1001)
                dan = text.split(" ")
                num = int(dan[1])                                
                for bb in aa:
                    if bb.id in msg.relatedMessageId:
                        for var in range(0,num):
                            maxbots.sendTag(to, "@!", [bb._from])                                
                rahman(to, "「 Spam 」\n › Type: Spamtag♪ \n    • Amount : {}\n    • Status: Success".format(str(dan[1]))) 
    elif cmd.startswith("spamcallto"):
       dan = text.split(" ")
       num = int(dan[1])
       ret_ = "「 Spam 」\n › Type: Spamcall Target♪"              
       if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
           lists = geTmention(msg)
           for ls in lists:
               for var in range(0,num):
                   group = maxbots.getChats([to]).chats[0]
                   members = [ls]
                   maxbots.acquireGroupCallRoute(to)
                   time.sleep(0.2)
                   maxbots.inviteIntoGroupCall(to, contactIds=members)                                                                                               
               ret_ += "\n    • Target: @!"
           ret_ += "\n    • Amount: {} \n    • Status: Succes".format(str(dan[1]))
           maxbots.sendTag(to, ret_, lists)               
       else:
           if msg.relatedMessageId is not None:
               aa = maxbots.getRecentMessagesV2(to, 1001)
               dan = text.split(" ")
               num = int(dan[1])
               ret_ = "「 Spam 」\n › Type: Spamcall Target♪"                                             
               for bb in aa:
                   if bb.id in msg.relatedMessageId:
                       for var in range(0,num):
                           group = maxbots.getChats([to]).chats[0]
                           members = [bb._from]
                           maxbots.acquireGroupCallRoute(to)
                           time.sleep(0.2)
                           maxbots.inviteIntoGroupCall(to, contactIds=members)                                                                                                                                                           
                       ret_ += "\n    • Target: @!"                         
               ret_ += "\n    • Amount: {} \n    • Status: Succes".format(str(dan[1]))
               maxbots.sendTag(to, ret_, members)                   
    elif cmd.startswith("spamcall "):
        if msg.toType == 2:
            strnum = removeCmd("spamcall", text)
            num = int(strnum)                        
            for var in range(0,num):
                group = maxbots.getChats([to]).chats[0]
                maxbots.acquireGroupCallRoute(to)
                time.sleep(0.2)
                maxbots.inviteIntoGroupCall(to, contactIds=group.extra.groupExtra.memberMids)                                                                 
            rahman(to, '「 Spam 」\n › Type: Spamcall Group♪\n    • In Group: {}\n    • Amount: {}\n    • Status: Success'.format(group.chatName, strnum))  
    elif cmd.startswith("spamtext "):
        sange = text.split(" ")[1]
        noneny = text.split(sange+" ")[1]  
        for ngentod in range(int(sange)):
            maxbots.sendMessage(to, str(noneny))       

    elif cmd == 'corona':      
        coroNa(to)
    elif cmd == 'gempa':      
        gemPa(to)
    elif cmd == 'hentai':      
        hENTAI(to)
    elif cmd == 'pantun':      
        pANTUN(to)
    elif cmd == 'puisi':      
        pUISI(to)
    elif cmd == 'quotes en':      
        qEN(to)
    elif cmd == 'quotes id':      
        qID(to)
    elif cmd == 'tribun news':      
        tRIBUN(to)
    elif cmd.startswith("youtube"):
        search = removeCmd("youtube", text)
        ytb(to, search)        
    elif cmd.startswith("ytbmp4"):
        search = removeCmd("ytbmp4", text)
        ytbmp4(to, search)   
    elif cmd.startswith("ytbmp3"):
        search = removeCmd("ytbmp3", text)
        ytbmp3(to, search)       
    elif cmd.startswith("instagram"):
        search = removeCmd("instagram", text)
        instagramP(to, search) 
    elif cmd.startswith("instastory"):
        search = removeCmd("instastory", text)
        igstry(to, search) 
    elif cmd.startswith("tiktok"):
        search = removeCmd("tiktok", text)
        tiktokP(to, search)    
    elif cmd.startswith("twitter"):
        search = removeCmd("twitter", text)
        twitterP(to, search)   
    elif cmd.startswith("github"):
        search = removeCmd("github", text)
        githubP(to, search)    
    elif cmd.startswith("pinterest"):
        search = removeCmd("pinterest", text)
        pint(to, search)  
    elif cmd.startswith("porn"):
        search = removeCmd("porn", text)
        porn(to, search)
    elif cmd.startswith("pornhub"):
        search = removeCmd("pornhub", text)
        downloadPornhub(to, search)    
    elif cmd.startswith("joox"):
        search = removeCmd("joox", text)
        jooX(to, search)    
    elif cmd.startswith("google"):
        search = removeCmd("google", text)
        gglSearch(to, search)    
    elif cmd.startswith("image"):
        search = removeCmd("image", text)
        imageSearch(to, search)    
    elif cmd.startswith("brainly"):
        search = removeCmd("brainly", text)
        brainlY(to, search)    
    elif cmd.startswith("kbbi"):
        search = removeCmd("kbbi", text)
        kBBI(to, search)    
    elif cmd.startswith("wikipedia"):
        search = removeCmd("wikipedia", text)
        wikip(to, search)    
    elif cmd.startswith("artinama"):
        search = removeCmd("artinama", text)
        artiN(to, search)   
    elif cmd.startswith("artimimpi"):
        search = removeCmd("artimimpi", text)
        artiM(to, search)  
    elif cmd.startswith("adzan"):
        search = removeCmd("adzan", text)
        adzaN(to, search)  
    elif cmd.startswith("zodiac"):
        search = removeCmd("zodiac", text)
        zodiaC(to, search)  
    elif cmd.startswith("cuaca"):
        search = removeCmd("cuaca", text)
        cuacA(to, search)  
    elif cmd.startswith("lyric"):
        search = removeCmd("lyric", text)
        lyriC(to, search)  
    elif cmd.startswith("chordgitar"):
        search = removeCmd("chordgitar", text)
        chorD(to, search)  
    elif cmd.startswith('downloadmedia '):
        mmk = removeCmd("downloadmedia", text)
        statS1(to, mmk, "downloadmedia","Media","Download Media")                                                                         

    elif cmd == 'game':
        rahman(to, gameH())
    elif cmd.startswith("jodohku"):
        ktl = cekmember(to)
        psntunggu = ["Bentar Ya Kak @!","Wait Bos @!","Oke Bentar Gua Cariin @!","Si Jomblo Nyari Jodoh Bentar @!"]
        psnyangberjdh = ["Nah Gua Jumpa Ni Jodoh Lu @!, Ni Jodoh Lu @! Silakan Callan","Waduh Bre @! Nah Jodohlu @!, Gih Ngewe","Semoga lu @! Dengan @! Langgeng Ya,Kalian Berjodoh","Ni Gua Dapat Bre @! Ni Lu Kenalan Dulu Sama @!, Mana Tau Nyaman"]
        yangberjodoh = random.choice(ktl)
        kautunggu = random.choice(psntunggu)
        akhirnyadapat = random.choice(psnyangberjdh)
        maxbots.sendMentionV2(msg_id,to, kautunggu,[sender])
        time.sleep(0.5)
        maxbots.sendMentionV2(msg_id,to,akhirnyadapat,[sender,yangberjodoh])  
        maxbots.sendContact(to, yangberjodoh) 
    elif cmd.startswith("persen cinta"):            
       tanya = removeCmd("persen cinta", text)
       jawab = ("0%","25%","50%","75%","100%")
       jawaban = random.choice(jawab)
       time.sleep(0.8)
       maxbots.sendMessage(to,jawaban)
    elif cmd.startswith("truth or dare "):
       hotel = geTmention(msg)
       for ngewe in hotel:
           ktl = ["Hai @! Kamu Harus Truth","Hai @! Kamu Harus Dare","Truth Aja Deh Lu @!","Mending Lu Dare @!","Yahahah Kamu Kena Truth @!","Hayolo @! Kena Truth Deh lu","Harus Terima Ya Kamu Kena Truth @!","Yahahah Kamu Kena Dare @!","Hayolo @! Kena Dare Deh lu","Harus Terima Ya Kamu Kena Dare @!","Dar Der Dor @! Truth Ya Bukan Dare"]
           mmk = random.choice(ktl)
           maxbots.sendTag(to,mmk,[ngewe])
    elif cmd.startswith("fancy"):
        font = removeCmd("fancy", text)
        data   = apiJG.fancy(font)
        arifblek = " 「 Fun 」\n › Type: Fancy♪\n    • Fancy:\n"
        for x in data["result"]:
            arifblek += f"      \n{x}"
        maxbots.sendMessage(to, str(arifblek))
    elif cmd.startswith("translate "):
        apl = removeCmd("translate", text)
        sam = apl.split(" | ")
        tr = sam[0]
        sn = sam[1]
        data = apiJG.translate(tr, sn)
        arifblek = f" 「 Fun 」\n › Type: Translate♪\n    • Translate To: {tr}"
        arifblek += f"\n {data['result']['translate']}"
        maxbots.sendMessage(to,str(arifblek))                                                
    elif cmd.startswith("calculator "):
        cmmk = removeCmd("calculator", text)
        data = apiJG.calc(cmmk)
        maxbots.sendMessage(to, str("「 Fun 」\n › Calculator  \n    • Answer: \n{}".format(data["result"])))                                            
    elif cmd.startswith("hartatahta "):
        mkr = removeCmd("hartatahta", text)
        maker1(to, "hartatahta", mkr)          
    elif cmd.startswith("blackpink "):
        mkr = removeCmd("blackpink", text)
        maker1(to, "blackpinkicon", mkr)          
    elif cmd.startswith("thunder "):
        mkr = removeCmd("thunder", text)
        maker1(to, "thundertext", mkr)          
    elif cmd.startswith("logogame "):
        mkr = removeCmd("logogame", text)
        maker1(to, "gamelogo", mkr)          
    elif cmd.startswith("mlsnulis "):
        mkr = removeCmd("mlsnulis", text)
        maker1(to, "write", mkr)       
    elif cmd.startswith("glowtext "):
        mkr = removeCmd("glowtext", text)
        maker1(to, "glowtext", mkr)  
    elif cmd.startswith("galaxytext "):
        mkr = removeCmd("galaxytext", text)
        maker1(to, "galaxytext", mkr)  
    elif cmd.startswith("hackavatar "):
        mkr = removeCmd("hackavatar", text)
        maker1(to, "hacker_avatar", mkr)  
    elif cmd.startswith("glowmetallic "):
        mkr = removeCmd("glowmetallic", text)
        maker1(to, "glow_metallic", mkr)  
    elif cmd.startswith("coverbanner "):
        mkr = removeCmd("coverbanner", text)
        maker1(to, "cover_banner", mkr)  
    elif cmd.startswith("thewall "):
        mkr = removeCmd("thewall", text)
        maker1(to, "the_wall", mkr)  
    elif cmd.startswith("wings "):
        mkr = removeCmd("wings", text)
        maker1(to, "wings_galaxy", mkr)  
    elif cmd.startswith("matrix "):
        mkr = removeCmd("matrix", text)
        maker1(to, "matrix_text", mkr)  
    elif cmd.startswith("mememaker "):
        apl = removeCmd("mememaker", text)
        sam = apl.split(" | ")
        tr = sam[0]
        sn = sam[1]
        maker2(to, "genmeme", tr, sn)
    elif cmd.startswith("glitchtext "):
        apl = removeCmd("glitchtext", text)
        sam = apl.split(" | ")
        tr = sam[0]
        sn = sam[1]
        maker2(to, "glitchtext", tr, sn)
    elif cmd.startswith("logoporn "):
        apl = removeCmd("logoporn", text)
        sam = apl.split(" | ")
        tr = sam[0]
        sn = sam[1]
        maker2(to, "pornlogo", tr, sn)
    elif cmd.startswith("graffiti "):
        apl = removeCmd("graffiti", text)
        sam = apl.split(" | ")
        tr = sam[0]
        sn = sam[1]
        maker2(to, "girl_graffiti", tr, sn)  
    elif cmd.startswith("avengers "):
        apl = removeCmd("avengers", text)
        sam = apl.split(" | ")
        tr = sam[0]
        sn = sam[1]
        maker2(to, "avengers_text", tr, sn)  

    elif cmd == 'autorespon':
        rahman(to, autoresponS())
    elif cmd == 'autoadd':
        rahman(to, autoaddS())
    elif cmd == 'autojoin':
        rahman(to, autojoinS())
    elif cmd == 'cek msgrespontag':
        rahman(to, settings['autoRespondMention']['message'])
    elif cmd == 'cek msgresponchat':
        rahman(to, settings['autoRespond']['message'])
    elif cmd == 'cek msgautoadd':
        rahman(to, settings['autoAdd']['message'])
    elif cmd == 'cek msgautojoin':
        rahman(to, settings['autoJoin']['message'])
    elif cmd == 'autoleave':
        rahman(to, autoleaveS())
    elif cmd == 'cek msgautoleave gc':
        rahman(to, settings['autoLeave']['gc']["message"])
    elif cmd == 'cek msgautoleave mc':
        rahman(to, settings['autoLeave']['mc']["message"])
    elif cmd == 'autoread':
        rahman(to, autoreadS())        
    elif cmd == 'autocomment':
        rahman(to, autocommentS())
    elif cmd == 'cek msgautocommentpost':
        rahman(to, settings['AutoComment']['msgpost'])
    elif cmd == 'cek msgautocommentstory':
        rahman(to, settings['AutoComment']['msgstory'])
    elif cmd == 'autolike':
        rahman(to, autolikeS())
    elif cmd == 'cek msgautolike':
        rahman(to, settings['AutoLike']['msglike'])
    elif cmd == 'mimic':
        rahman(to, mimicS())
    elif cmd == 'greet':
        rahman(to, greetS())        
    elif cmd == 'cek msggreetjoin':
        rahman(to, settings['greet']['join']['message'])        
    elif cmd == 'cek msggreetleave':
        rahman(to, settings['greet']['leave']['message'])        
    elif cmd == 'detect':
        rahman(to, detectS())        
    elif cmd == 'cek msgdfaketag':
        rahman(to, settings['Detect']['msgfaketag'])        
    elif cmd == 'cek msgdspamcall':
        rahman(to, settings['Detect']['msgspamcall'])                 
    elif cmd == 'check':
        rahman(to, checkS())        
    elif cmd == 'lurk':
        rahman(to, lurkS())         
    elif cmd == 'cek stickerrespontag':
        try:
            maxbots.sendSticker(to,settings, "stcmention")
        except:
           rahman(to, '「 Autorespon 」\n › Type: Cek Stickerrespontag♪\n    • Nothing Sticker')
    elif cmd == 'cek stickerresponchat':
        try:
            maxbots.sendSticker(to,settings, "stcchat")
        except:
            rahman(to, '「 Autorespon 」\n › Type: Cek Stickerresponchat♪\n    • Nothing Sticker')      
    elif cmd == 'cek stickerautoadd':
        try:
            maxbots.sendSticker(to,settings, "stcadd")
        except:
            rahman(to, '「 Autoadd 」\n › Type: Cek Stickerautoadd♪\n    • Nothing Sticker')            
    elif cmd == 'cek stickerautojoin':
        try:
            maxbots.sendSticker(to,settings, "stcautojoin")
        except:
            rahman(to, '「 Autojoin 」\n › Type: Cek Stickerautojoin♪\n    • Nothing Sticker')    
    elif cmd == 'cek stickerautoleave gc':
        try:
            maxbots.sendSticker(to,settings, "stcautoleaveGC")
        except:
            rahman(to, '「 Autoleave 」\n › Type: Cek Stickerautoleave GC♪\n    • Nothing Sticker')
    elif cmd == 'cek stickerautoleave mc':
        try:
            maxbots.sendSticker(to,settings, "stcautoleaveMC")
        except:
            rahman(to, '「 Autoleave 」\n › Type: Cek Stickerautoleave MC♪\n    • Nothing Sticker')        
    elif cmd == 'cek stickercomment':
        try:
            maxbots.sendSticker2(to,settings, "AutoComment","stccomment")            
        except:
            rahman(to, '「 Autocomment 」\n › Type: Cek Stickercomment♪\n    • Nothing Sticker')
    elif cmd == 'cek stickergreetjoin':
        try:
            maxbots.sendSticker2(to,settings, "greet", "stcgreetjoin")
        except:
           rahman(to, '「 Greet 」\n › Type: Cek Stickergreetjoin♪\n    • Nothing Sticker')            
    elif cmd == 'cek stickergreetleave':
        try:
            maxbots.sendSticker2(to,settings, "greet", "stcgreetleave")
        except:
           rahman(to, '「 Greet 」\n › Type: Cek Stickergreetjoin♪\n    • Nothing Sticker')        
    elif cmd == 'add stickerrespontag':
        ktl = geTreply(msg)
        if ktl == None:
            statS2(to, "stickermention","Autorespon","Add Stickerrespontag","Sticker")           
        else:
            if ktl.contentType == 7:
                mmk = printSTC(ktl)
                settings["stcmention"] = mmk
                rahman(to,   "「 Autorespon 」\n › Type: Add Stickerrespontag♪\n    • Status: Success")
    elif cmd == 'add stickerresponchat':
        ktl = geTreply(msg)
        if ktl == None:
            statS2(to, "stickerchat","Autorespon","Add Stickerresponchat","Sticker")           
        else:
            if ktl.contentType == 7:
                mmk = printSTC(ktl)
                settings["stcchat"] = mmk
                rahman(to,   "「 Autorespon 」\n › Type: Add Stickerresponchat♪\n    • Status: Success")
    elif cmd == 'add stickerautoadd':
        ktl = geTreply(msg)
        if ktl == None:
            statS2(to, "stickeradd","Autoadd","Add Stickerautoadd","Sticker")           
        else:
            if ktl.contentType == 7:
                mmk = printSTC(ktl)
                settings["stcadd"] = mmk
                rahman(to,   "「 Autoadd 」\n › Type: Add Stickerautoadd♪\n    • Status: Success")
    elif cmd == 'add stickerautojoin':
        ktl = geTreply(msg)
        if ktl == None:
            statS2(to, "statstcautojoin","Autojoin","Add Stickerautojoin","Sticker")           
        else:
            if ktl.contentType == 7:
                mmk = printSTC(ktl)
                settings["stcautojoin"] = mmk
                rahman(to,   "「 Autojoin 」\n › Type: Add Stickerautojoin♪\n    • Status: Success")
    elif cmd == 'add stickerautoleave gc':
        ktl = geTreply(msg)
        if ktl == None:
            statS6(to, "autoLeave","gc","setstc","Autoleave","Add Stickerautoleave Gc","Sticker")                  
        else:
            if ktl.contentType == 7:
                mmk = printSTC(ktl)
                settings["stcautoleaveGC"] = mmk
                rahman(to,   "「 Autoleave 」\n › Type: Add Stickerautoleave Gc♪\n    • Status: Success")
    elif cmd == 'add stickerautoleave mc':
        ktl = geTreply(msg)
        if ktl == None:
            statS6(to, "autoLeave","mc","setstc","Autoleave","Add Stickerautoleave Mc","Sticker")                  
        else:
            if ktl.contentType == 7:
                mmk = printSTC(ktl)
                settings["stcautoleaveMC"] = mmk
                rahman(to,   "「 Autoleave 」\n › Type: Add Stickerautoleave Mc♪\n    • Status: Success")
    elif cmd == 'add stickercomment':
        ktl = geTreply(msg)
        if ktl == None:
            statS8(to, "AutoComment","setstccomment","Autocomment","Add Stickercomment","Sticker")                    
        else:
            if ktl.contentType == 7:
                mmk = printSTC(ktl)
                settings['AutoComment']["stccomment"] = mmk
                rahman(to,   "「 Autocomment 」\n › Type: Add Stickercomment♪\n    • Status: Success")
    elif cmd == 'add stickergreetjoin':
        ktl = geTreply(msg)
        if ktl == None:
            statS8(to, "greet","stickergreetjoin","Greet","Add Stickergreetjoin","Sticker")                                   
        else:
            if ktl.contentType == 7:
                mmk = printSTC(ktl)
                settings['greet']["stcgreetjoin"] = mmk
                rahman(to,   "「 Greet 」\n › Type: Add Stickergreetjoin♪\n    • Status: Success")                                                                 
    elif cmd == 'add stickergreetleave':
        ktl = geTreply(msg)
        if ktl == None:
            statS8(to, "greet","stickergreetleave","Greet","Add Stickergreetleave","Sticker")                                       
        else:
            if ktl.contentType == 7:
                mmk = printSTC(ktl)
                settings['greet']["stcgreetleave"] = mmk
                rahman(to,   "「 Greet 」\n › Type: Add Stickergreetleave♪\n    • Status: Success")                                                
    elif txt.startswith("setkey"):
        ktl = text.split(' ')
        mmk = text.replace(ktl[0] + ' ','')         
        if txt == 'setkey':
            rahman(to, setkeyS())
        elif mmk == "on":
            statS5(to, mmk, "setKey","status","Setkey","Setkey")            
        elif mmk == "off":
            statS5(to, mmk, "setKey","status","Setkey","Setkey")            
        else:
            changeMSG2(to, mmk.lower(), "setKey","key", "Setkey" , "Set Setkey")                                                           
    elif cmd == 'mimiclist':
        if len(settings['mimic']['target']) > 0:
            h = [a for a in settings['mimic']['target']]
            k = len(h)//20            
            for aa in range(k+1):
                if aa == 0:
                    dd = '「 Mimic 」\n › Type: Mimiclist♪';no=aa
                else:
                    dd = ''
                    no=aa*20
                msgas = dd
                for a in h[aa*20:(aa+1)*20]:
                    no+=1
                    if no == len(h):
                        msgas+='\n    • {}.@!\n'.format(no)
                    else:
                        msgas += '\n    • {}.@!'.format(no)
                maxbots.sendTag(to, msgas, h[aa*20:(aa+1)*20])
        else:rahman(to,"「 Mimic 」\n › Type: Mimiclist♪ \n    • Status: Not List")             
    elif cmd == 'clearmimic':
        if len(settings['mimic']['target']) > 0:
            rahman(to, "「 Mimic 」\n › Type: Clearmimic♪ \n    • Amount: {} \n    • Status: Success".format(len(settings['mimic']['target'])));settings['mimic']['target'].clear()                        
        else:
            rahman(to, "「 Mimic 」\n › Type: Clearmimic♪ \n    • Status: Not List")           
    elif cmd.startswith("addmimic"):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            lists = geTmention(msg)
            for ls in lists:
                if ls not in settings['mimic']['target']:
                    settings['mimic']['target'][ls] = True
                    maxbots.sendTag(to,"「 Mimic 」\n › Type: Addmimic♪\n    • Target : @! \n    • Status: Success",[ls])                                                  
                else:
                    maxbots.sendTag(to,"「 Mimic 」\n › Type: Addmimic♪\n    • Target : @! \n    • Status: Already In List",[ls])                         
        else:
             if msg.relatedMessageId is not None:
                 bb = geTreply(msg)
                 if cmd == "addmimic":
                     if bb._from not in settings['mimic']['target']:
                         settings['mimic']['target'][bb._from] = True
                         maxbots.sendTag(to,"「 Mimic 」\n › Type: Addmimic♪\n    • Target : @! \n    • Status: Success",[bb._from])                                                            
                     else:
                         maxbots.sendTag(to,"「 Mimic 」\n › Type: Addmimic♪\n    • Target : @! \n    • Status: Already In List",[bb._from])                                         
    elif cmd.startswith("delmimic"):
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            lists = geTmention(msg)
            for ls in lists:
                if ls in settings['mimic']['target']:
                    settings['mimic']['target'][bb._from] = False
                    maxbots.sendTag(to,"「 Mimic 」\n › Type: Delmimic♪\n    • Target : @! \n    • Status: Success",[ls])                                                    
                else:
                    maxbots.sendTag(to,"「 Mimic 」\n › Type: Delmimic♪\n    • Target : @! \n    • Status: Not In List",[ls])                          
        else:
            if msg.relatedMessageId is not None:
                bb = geTreply(msg)
                if cmd == "delmimic":
                    if bb._from in settings['mimic']['target']:
                        settings['mimic']['target'][bb._from] = False
                        maxbots.sendTag(to,"「 Mimic 」\n › Type: Delmimic♪\n    • Target : @! \n    • Status: Success",[bb._from])                                                            
                    else:
                        maxbots.sendTag(to,"「 Mimic 」\n › Type: Delmimic♪\n    • Target : @! \n    • Status: Not In List",[bb._from])                              
    elif cmd.startswith("changelike "):
        try:
            asu = removeCmd("changelike", text)
            printEMO(to, msg, asu, "AutoLike", "msglike", "sticons", "changelike ","Autolike","Set Autolike Msg")
        except:
             asu = removeCmd("changelike", text)
             changeMSG2(to, asu, "AutoLike","msglike", "Autolike" , "Set Autolike Msg")           
    elif cmd.startswith("changedspamcall "):
        try:
            asu = removeCmd("changedspamcall", text)
            printEMO(to, msg, asu, "Detect", "msgspamcall", "sticons", "changedspamcall ","Detect","Msg Spamcall")
        except:
             asu = removeCmd("changedspamcall", text)
             changeMSG2(to, asu, "Detect","msgspamcall", "Detect" , "Msg Spamcall")           

    elif cmd.startswith('greet'):
        mmk = removeCmd("greet", text)
        if mmk.startswith('join '):
            texts = mmk[5:]
            textsl = texts      
            if textsl == 'on':
                if to in settings["greet"]["join"]["status"]:
                    rahman(to,"「 Greet 」\n › Type: Join♪\n    • Status: Already")
                else:
                    settings["greet"]["join"]["status"].append(to)
                    rahman(to,"「 Greet 」\n › Type: Join♪\n    • Status: Active")
            elif textsl == 'off':
                if to not in settings["greet"]["join"]["status"]:
                    rahman(to,"「 Greet 」\n › Type: Join♪\n    • Status: Already")
                else:
                    settings["greet"]["join"]["status"].remove(to)
                    rahman(to,"「 Greet 」\n › Type: Join♪\n    • Status: Deactive")                              
            else:
                changeMSG3(to, texts, "greet","join","message", "Greet" , "Greet Join Msg")                   
        elif mmk.startswith('leave '):
            texts = mmk[6:]
            textsl = texts
            if textsl == 'on':
                if to in settings["greet"]["leave"]["status"]:
                    rahman(to,"「 Greet 」\n › Type: Leave♪\n    • Status: Already")
                else:
                    settings["greet"]["leave"]["status"].append(to)
                    rahman(to,"「 Greet 」\n › Type: Leave♪\n    • Status: Active")
            elif textsl == 'off':
                if to not in settings["greet"]["leave"]["status"]:
                    rahman(to,"「 Greet 」\n › Type: Leave♪\n    • Status: Already")
                else:
                    settings["greet"]["leave"]["status"].remove(to)
                    rahman(to,"「 Greet 」\n › Type: Leave♪\n    • Status: Deactive")                                                            
            else:
                changeMSG3(to, texts, "greet","leave","message", "Greet" , "Greet Join Leave")                        
    elif cmd.startswith("lurk"):
        mmk = removeCmd("lurk", text)   
        if mmk == "on":
            if to in lurk["readPoint"]:
                mssg = "「 Lurk 」\n › Type: Status♪\n    • Status: Already Active"
            else:
                try:
                    del lurk['readPoint'][to]
                    del lurk['readMember'][to]
                except:pass
                lurk["readPoint"][to] = msg.id
                lurk["readMember"][to] = []
                mssg = "「 Lurk 」\n › Type: Status♪\n    • Status: Active"
            if settings["stattemp"] == True:
            	sendON(to, "Lurk")                
            else:
                rahman(to, mssg)
        elif mmk == "off":
            if to not in lurk["readPoint"]:
                mssg = "「 Lurk 」\n › Type: Status♪\n    • Status: Already Deactive"
            else:
                del lurk['readPoint'][to]
                del lurk['readMember'][to]
                mssg = "「 Lurk 」\n › Type: Status♪\n    • Status: Deactive"
            if settings["stattemp"] == True:
            	sendOFF(to, "Lurk")                
            else:
                rahman(to, mssg)
        elif mmk == "result":
            if to in lurk['readPoint']:
                if lurk["readMember"][to] == []:
                    return rahman(to, "「 Lurk 」\n › Type: Result♪\n    • Status: Not Found")
                else:
                    no = 0
                    result = "「 Lurk 」\n  › Type: Result♪"
                    for dataRead in lurk["readMember"][to]:
                        no += 1
                        result += "\n    • {}. @!".format(str(no))
                    result += "\n › Result: {}♪".format(str(len(lurk["readMember"][to])))
                    maxbots.sendTag(to, result, lurk["readMember"][to])
                    lurk['readMember'][to] = []             
    elif cmd.startswith('notifline '):
        mmk = removeCmd("notifline", text)
        if mmk == 'on':
            maxbots.updateSettingsAttribute(65536, 'false')
            if settings["stattemp"] == True:
            	sendON(to, "Notif Line")                
            else:
                rahman(to, '「 Notif 」\n › Type: Notif Line♪\n    • Status: Active')                
        elif mmk == 'off':
            maxbots.updateSettingsAttribute(65536, 'true')
            if settings["stattemp"] == True:
                sendOFF(to, "Notif Line")      
            else:     	
                rahman(to, '「 Notif 」\n › Type: Notif Line♪\n    • Status: Deactive')                
    elif cmd.startswith("add emojirespontag "):
        asu = removeCmd("add emojirespontag", text)
        printEMO(to, msg, asu, "emojirespontag", "message", "sticons", "add emojirespontag ","Autorespon","Emoji Respontag")
    elif cmd.startswith("add emojiresponchat "):
        asu = removeCmd("add emojiresponchat", text)
        printEMO(to, msg, asu, "emojiresponchat", "message", "sticons", "add emojiresponchat ","Autorespon","Emoji Responchat")
    elif cmd.startswith("add emojiautoadd "):
        asu = removeCmd("add emojiautoadd", text)
        printEMO(to, msg, asu, "emojiautoadd", "message", "sticons", "add emojiautoadd ","Autoadd","Emoji Autoadd")
    elif cmd.startswith("changerespontag "):
        mmk = removeCmd("changerespontag", text)
        changeMSG2(to, mmk, "autoRespondMention","message", "Autorespon" , "Set Respontag")   
    elif cmd.startswith("changeresponchat "):
        mmk = removeCmd("changeresponchat", text)
        changeMSG2(to, mmk, "autoRespond","message", "Autorespon" , "Set Responchat")           
    elif cmd.startswith('respontag '):
        mmk = removeCmd("respontag", text)
        statS5(to, mmk, "autoRespondMention","status","Autorespon","Respontag")                                        
    elif cmd.startswith('responchat '):
        mmk = removeCmd("responchat", text)
        statS5(to, mmk, "autoRespond","status","Autorespon","Responchat")                                                                                             
    elif cmd.startswith('responstctag '):
        mmk = removeCmd("responstctag", text)
        statS1(to, mmk, "responstickertag","Autorespon","Respon Stickertag")                                                                              
    elif cmd.startswith('responstcchat '):
        mmk = removeCmd("responstcchat", text)
        statS1(to, mmk, "responstickerchat","Autorespon","Respon Stickerchat")                                                             
    elif cmd.startswith('responemojitag '):
        mmk = removeCmd("responemojitag", text)
        statS5(to, mmk, "emojirespontag","status","Autorespon","Respon Emojitag")                                                                                  
    elif cmd.startswith('responemojichat '):
        mmk = removeCmd("responemojichat", text)
        statS5(to, mmk, "emojiresponchat","status","Autorespon","Respon Emojichat")                                                                    
    elif cmd.startswith("changeautoadd "):
        mmk = removeCmd("changeautoadd", text)
        changeMSG2(to, mmk, "autoAdd","message", "Autoadd" , "Set Autoadd")           
    elif cmd.startswith('autoadd '):
        mmk = removeCmd("autoadd", text)
        statS5(to, mmk, "autoAdd","status","Autoadd","Autoadd")                                                                                  
    elif cmd.startswith('autoaddmsg '):
        mmk = removeCmd("autoaddmsg", text)
        statS5(to, mmk, "autoAdd","reply","Autoadd"," Autoadd Msg")                                                                                         
    elif cmd.startswith('autoaddstc '):
        mmk = removeCmd("autoaddstc", text)
        statS1(to, mmk, "responstickeradd","Autoadd","Autoadd Sticker")                                                                                      
    elif cmd.startswith('autoaddemoji '):
        mmk = removeCmd("autoaddemoji", text)
        statS5(to, mmk, "emojiautoadd","status","Autoadd"," Autoadd Emoji")                                                                                             
    elif cmd.startswith("changeautojoin "):
        mmk = removeCmd("changeautojoin", text)
        changeMSG2(to, mmk, "autoJoin","message", "Autojoin" , "Set Autojoin")           
    elif cmd.startswith('autojoin '):
        mmk = removeCmd("autojoin", text)
        statS5(to, mmk, "autoJoin","status","Autojoin","Autojoin")                                                                                             
    elif cmd.startswith('autojoinbypass '):
        mmk = removeCmd("autojoinbypass", text)
        statS1(to, mmk, "autojoinbypass","Autojoin","Autojoin Bypass")        
    elif cmd.startswith('autojoinkickall '):
        mmk = removeCmd("autojoinkickall", text)
        statS1(to, mmk, "autojoinkickall","Autojoin","Autojoin Kickall")                                                  
    elif cmd.startswith('autojoincancelall '):
        mmk = removeCmd("autojoinkickall", text)
        statS1(to, mmk, "autojoincancelall","Autojoin","Autojoin Canceall")                                                  
    elif cmd.startswith('autojoinkillban '):
        mmk = removeCmd("autojoinkillban", text)
        statS1(to, mmk, "autojoinkillban","Autojoin","Autojoin Killban")                                                     
    elif cmd.startswith('autojoinkickallpy'):
        mmk = removeCmd("autojoinkickallpy", text)
        statS1(to, mmk, "autojoinkickallPY","Autojoin","Autojoin Kickall PY")                                                     
    elif cmd.startswith('autojoinkillbanpy '):
        mmk = removeCmd("autojoinkillbanpy", text)
        statS1(to, mmk, "autojoinkillbanPY","Autojoin","Autojoin Killban PY")                                                     
    elif cmd.startswith('autojoinmsg '):
        mmk = removeCmd("autojoinmsg", text)
        statS5(to, mmk, "autoJoin","reply","Autojoin","Autojoin Msg")                    
    elif cmd.startswith('autojoinsticker '):
        mmk = removeCmd("autojoinsticker", text)
        statS1(to, mmk, "autojoinsticker","Autojoin","Autojoin Sticker")                                                                                       
    elif cmd.startswith("changeautoleave gc "):
        mmk = removeCmd("changeautoleave gc", text)
        changeMSG3(to, mmk, "autoLeave","gc","message", "Autoleave" , "Set Autoleave Msg Gc")   
    elif cmd.startswith("changeautoleave mc "):
        mmk = removeCmd("changeautoleave mc", text)
        changeMSG3(to, mmk, "autoLeave","mc","message", "Autoleave" , "Set Autoleave Msg Mc")                   
    elif cmd.startswith("autoleave gc "):
        mmk = removeCmd("autoleave gc", text)
        statS7(to, mmk, "autoLeave","gc","status","Autoleave","Autoleave Gc")                    
    elif cmd.startswith("autoleave mc "):
        mmk = removeCmd("autoleave mc", text)
        statS7(to, mmk, "autoLeave","mc","status","Autoleave","Autoleave Mc")                                       
    elif cmd.startswith("autoleavemsg gc "):
        mmk = removeCmd("autoleavemsg gc", text)
        statS7(to, mmk, "autoLeave","gc","msg","Autoleave","Autoleave Msg Gc")                                                                               
    elif cmd.startswith("autoleavemsg mc "):
        mmk = removeCmd("autoleavemsg mc ", text)
        statS7(to, mmk, "autoLeave","mc","msg","Autoleave","Autoleave Msg Mc")                                                                               
    elif cmd.startswith("autoleavestc gc "):
        mmk = removeCmd("autoleavestc gc", text)
        statS7(to, mmk, "autoLeave","gc","stc","Autoleave","Autoleave Stc Gc")                                                         
    elif cmd.startswith("autoleavestc mc "):
        mmk = removeCmd("autoleavestc mc", text)
        statS7(to, mmk, "autoLeave","mc","stc","Autoleave","Autoleave Stc Mc")                                                         
    elif cmd.startswith('autoread '):
        mmk = removeCmd("autoread", text)
        statS5(to, mmk, "AutoRead","all","Autoread","Autoread All")                                                                                             
    elif cmd.startswith('autoreadpc '):
        mmk = removeCmd("autoreadpc", text)
        statS5(to, mmk, "AutoRead","pc","Autoread","Autoread Pc")                                            
    elif cmd.startswith('autoreadgc '):
        mmk = removeCmd("autoreadgc", text)
        statS5(to, mmk, "AutoRead","gc","Autoread","Autoread Gc")                                       
    elif cmd.startswith("changecommentpost "):
        mmk = removeCmd("changecommentpost", text)
        changeMSG2(to, mmk, "AutoComment","msgpost", "Autocomment" , "Set Autocomment Post")                                    
    elif cmd.startswith("changecommentstory "):
        mmk = removeCmd("changecommentstory", text)
        changeMSG2(to, mmk, "AutoComment","msgstory", "Autocomment" , "Set Autocomment Story")                                                           
    elif cmd.startswith('autocommentpost '):
        mmk = removeCmd("autocommentpost", text)
        statS5(to, mmk, "AutoComment","post","Autocomment","Autocomment Post")                                            
    elif cmd.startswith('autocommentstcpost '):
        mmk = removeCmd("autocommentstcpost", text)
        statS5(to, mmk, "AutoComment","sticker","Autocomment","Autocomment Sticker Post")                                             
    elif cmd.startswith('autocommentstory '):
        mmk = removeCmd("autocommentstory", text)
        statS5(to, mmk, "AutoComment","story","Autocomment","Autocomment Story")                                                                             
    elif cmd.startswith('autolikepost '):
        mmk = removeCmd("autolikepost", text)
        statS5(to, mmk, "AutoLike","post","Autolike","Autolike Post")     
    elif cmd.startswith('autolikestory '):
        mmk = removeCmd("autolikestory", text)
        statS5(to, mmk, "AutoLike","story","Autolike","Autolike Story")                                                
    elif cmd.startswith('mimic '):
        mmk = removeCmd("mimic", text)
        statS5(to, mmk, "mimic","status","Mimic","Mimic")                                                 
    elif cmd.startswith("add emojigreetjoin "):
        asu = removeCmd("add emojigreetjoin", text)
        printEMO(to, msg, asu, "emojigreetjoin", "message", "sticons", "add emojigreetjoin ","Greet","Emoji Greet Join")
    elif cmd.startswith("add emojigreetleave "):
        asu = removeCmd("add emojigreetleave", text)
        printEMO(to, msg, asu, "emojigreetleave", "message", "sticons", "add emojigreetleave ","Greet","Emoji Greet Leave")
    elif cmd.startswith('liff '):
        mmk = removeCmd("liff", text)
        if mmk == "1":
            listsett["liff1"] = "1655623470"
            listsett["liff2"] = "1655623470-81eDd9kM"
            maxbots.sendMessage(to,"Type This Link: line://app/"+listsett["liff2"])
            maxbots.sendMessage(to,"Wait for Restart and Try Used Temp or Flex")
            settings['restartPoint'] = to
            restartProgram()
        elif mmk == "2":
            listsett["liff1"] = "1656453408"
            listsett["liff2"] = "1656453408-8YbRJm45"
            maxbots.sendMessage(to,"Type This Link: line://app/"+listsett["liff2"])
            maxbots.sendMessage(to,"Wait for Restart and Try Used Temp or Flex")
            settings['restartPoint'] = to
            restartProgram()
        elif mmk == "3":
            listsett["liff1"] = "1656210528"
            listsett["liff2"] = "1656210528-6XJ8oAZg"
            maxbots.sendMessage(to,"Type This Link: line://app/"+listsett["liff2"])
            maxbots.sendMessage(to,"Wait for Restart and Try Used Temp or Flex")
            settings['restartPoint'] = to
            restartProgram()
        elif mmk == "4":
            listsett["liff1"] = "1656210537"
            listsett["liff2"] = "1656210537-4LMogKjp"
            maxbots.sendMessage(to,"Type This Link: line://app/"+listsett["liff2"])
            maxbots.sendMessage(to,"Wait for Restart and Try Used Temp or Flex")
            settings['restartPoint'] = to
            restartProgram()
        elif mmk == "5":
            listsett["liff1"] = "1656300882"
            listsett["liff2"] = "1656300882-x2YX9VB5"
            maxbots.sendMessage(to,"Type This Link: line://app/"+listsett["liff2"])
            maxbots.sendMessage(to,"Wait for Restart and Try Used Temp or Flex")
            settings['restartPoint'] = to
            restartProgram()
        elif mmk == "6":
            listsett["liff1"] = "1656300892"
            listsett["liff2"] = "1656300892-ROVnxmrB"
            maxbots.sendMessage(to,"Type This Link: line://app/"+listsett["liff2"])
            maxbots.sendMessage(to,"Wait for Restart and Try Used Temp or Flex")
            settings['restartPoint'] = to
            restartProgram()
    elif cmd.startswith('stcgreetjoin '):
        mmk = removeCmd("stcgreetjoin", text)
        if mmk == "on":
            if to in settings["greet"]["joinstc"]:
                rahman(to,"「 Greet 」\n › Type: Sticker Join♪\n    • Status: Already")
            else:
                settings["greet"]["joinstc"].append(to)
                rahman(to,"「 Greet 」\n › Type: Sticker Join♪\n    • Status: Deactive")
        elif mmk == "off":
            if to not in settings["greet"]["joinstc"]:
                rahman(to,"「 Greet 」\n › Type: Sticker Join♪\n    • Status: Already")
            else:
                settings["greet"]["joinstc"].remove(to)
                rahman(to,"「 Greet 」\n › Type: Sticker Join♪\n    • Status: Deactive")
    elif cmd.startswith('stcgreetleave '):
        mmk = removeCmd("stcgreetleave", text)
        if mmk == "on":
            if to in settings["greet"]["leavestc"]:
                rahman(to,"「 Greet 」\n › Type: Sticker Leave♪\n    • Status: Already")
            else:
                settings["greet"]["leavestc"].append(to)
                rahman(to,"「 Greet 」\n › Type: Sticker Leave♪\n    • Status: Deactive")
        elif mmk == "off":
            if to not in settings["greet"]["leavestc"]:
                rahman(to,"「 Greet 」\n › Type: Sticker Leave♪\n    • Status: Already")
            else:
                settings["greet"]["leavestc"].remove(to)
                rahman(to,"「 Greet 」\n › Type: Sticker Leave♪\n    • Status: Deactive")
    elif cmd.startswith('emojigreetjoin '):
        mmk = removeCmd("emojigreetjoin", text)
        if mmk == "on":
            if to in settings["emojigreetjoin"]["status"]:
                rahman(to,"「 Greet 」\n › Type: Emoji Join♪\n    • Status: Already")
            else:
                settings["emojigreetjoin"]["status"].append(to)
                rahman(to,"「 Greet 」\n › Type: Emoji Join♪\n    • Status: Deactive")
        elif mmk == "off":
            if to not in settings["emojigreetjoin"]["status"]:
                rahman(to,"「 Greet 」\n › Type: Emoji Join♪\n    • Status: Already")
            else:
                settings["emojigreetjoin"]["status"].remove(to)
                rahman(to,"「 Greet 」\n › Type: Emoji Join♪\n    • Status: Deactive")
    elif cmd.startswith('emojigreetleave '):
        mmk = removeCmd("emojigreetleave", text)
        if mmk == "on":
            if to in settings["emojigreetleave"]["status"]:
                rahman(to,"「 Greet 」\n › Type: Emoji Leave♪\n    • Status: Already")
            else:
                settings["emojigreetleave"]["status"].append(to)
                rahman(to,"「 Greet 」\n › Type: Emoji Leave♪\n    • Status: Deactive")
        elif mmk == "off":
            if to not in settings["emojigreetleave"]["status"]:
                rahman(to,"「 Greet 」\n › Type: Emoji Leave♪\n    • Status: Already")
            else:
                settings["emojigreetleave"]["status"].remove(to)
                rahman(to,"「 Greet 」\n › Type: Emoji Leave♪\n    • Status: Deactive")                                                                            
    elif cmd.startswith("changedfaketag "):
        mmk = removeCmd("changedfaketag", text)
        changeMSG2(to, mmk, "Detect","msgfaketag", "Detect" , "Msg Faketag")   
    elif cmd.startswith('detectcallgroup '):
        mmk = removeCmd("detectcallgroup", text)
        statS5(to, mmk, "Detect","callgroup","Detect","Detect Callgroup")                        
    elif cmd.startswith('detectfaketag '):
        mmk = removeCmd("detectfaketag", text)
        statS5(to, mmk, "Detect","faketag","Detect","Detect Faketag")                          
    elif cmd.startswith('detectspamcall '):
        mmk = removeCmd("detectspamcall", text)
        statS5(to, mmk, "Detect","spamcall","Detect","Detect Spamcall")                          
    elif cmd.startswith('checkpost '):
        mmk = removeCmd("checkpost", text)
        statS5(to, mmk, "Check","post","Check","Check Post")                                
    elif cmd.startswith('checksticker '):
        mmk = removeCmd("checksticker", text)
        statS5(to, mmk, "Check","sticker","Check","Check Sticker")                                                                                                            
    elif cmd.startswith('modepublic '):
        mmk = removeCmd("modepublic", text)
        statS1(to, mmk, "modepublic","Mode Public","Mode Public")                                              
    elif cmd.startswith("basenotif"):
        mmk = removeCmd("basenotif", text)
        if cmd == 'basenotif':
            ma = ""
            a = 0
            for x in position["basenotif"]:
                a = a + 1
                end = '\n'
                ma += "    • " + str(a) + ". " +maxbots.getChats([x]).chats[0].chatName+ "\n"
            blek = "「 Basenotif 」"
            blek += f"\n › List♪"
            blek += f"\n{ma}"
            blek += "\n\n › Command"
            blek += f"\n    • Basenotif Add"
            blek += f"\n    • Basenotif Del"
            blek += f"\n    • Basenotif Clear"
            rahman(to, blek)  
        elif mmk == "add":
            if to in position['basenotif']:
                rahman(to, '「 Basenotif 」\n  › Type: Add♪\n    • Status: Already')
            else:
                position['basenotif'].append(to)
                rahman(to, '「 Basenotif 」\n  › Type: Add♪\n    • Status: Success')
        elif mmk == "del":
            if to not in position['basenotif']:
                rahman(to, '「 Basenotif 」\n  › Type: Del♪\n    • Status: Nothing')
            else:
                position['basenotif'].remove(to)
                rahman(to, '「 Basenotif 」\n  › Type: Del♪\n    • Status: Success')
        elif mmk == "clear":
            if len(position['basenotif']) > 0:
                rahman(to, f"「 Basenotif 」\n › Type: Clear♪\n    • Amount: {len(position['basenotif'])}\n    • Status: Success")
                position['basenotif'].clear()
            else:
                rahman(to, "「 Basenotif 」\n › Type: Clear♪\n    • Status: Nothing")           
    elif cmd.startswith("detectunsend"):
        mmk = removeCmd("detectunsend", text)
        if cmd == 'detectunsend':
            ma = ""
            a = 0
            for x in position["detectunsend"]:
                a = a + 1
                end = '\n'
                try:
                    name = maxbots.getChats([x]).chats[0].chatName
                except:
                    name = maxbots.getContact(x).displayName
                ma += "    • " + str(a) + ". " + name + "\n"
            blek = "「 Detectunsend 」"
            blek += f"\n › List♪"
            blek += f"\n{ma}"
            blek += "\n\n › Command"
            blek += f"\n    • Detectunsend ‹On/Off›"
            blek += f"\n    • Detectunsend Clear"
            rahman(to, blek)  
        elif mmk == "on":
            if to in position['detectunsend']:
                rahman(to, '「 Detectunsend 」\n  › Type: On♪\n    • Status: Already')
            else:
                position['detectunsend'].append(to)
                rahman(to, '「 Detectunsend 」\n  › Type: On♪\n    • Status: Success')
        elif mmk == "off":
            if to not in position['detectunsend']:
                rahman(to, '「 Detectunsend 」\n  › Type: Off♪\n    • Status: Nothing')
            else:
                position['detectunsend'].remove(to)
                rahman(to, '「 Detectunsend 」\n  › Type: Off♪\n    • Status: Success')
        elif mmk == "clear":
            if len(position['detectunsend']) > 0:
                rahman(to, f"「 Detectunsend 」\n › Type: Clear♪\n    • Amount: {len(position['detectunsend'])}\n    • Status: Success")
                position['detectunsend'].clear()
            else:
                rahman(to, "「 Detectunsend 」\n › Type: Clear♪\n    • Status: Nothing")           

    elif cmd.startswith("mentionkick"):
        mmk = removeCmd("mentionkick", text)
        if cmd == 'mentionkick':
            ma = ""
            a = 0
            for x in position["mentionkick"]:
                a = a + 1
                end = '\n'
                name = maxbots.getChats([x]).chats[0].chatName   
                ma += "    • " + str(a) + ". " + name + "\n"
            blek = "「 Mentionkick 」"
            blek += f"\n › List♪"
            blek += f"\n{ma}"
            blek += "\n\n › Command"
            blek += f"\n    • Mentionkick ‹On/Off›"
            blek += f"\n    • Mentionkick Cekmsg"
            blek += f"\n    • Mentionkick Clear"
            rahman(to, blek)  
        elif mmk == "on":
            if to in position['mentionkick']:
                rahman(to, '「 Mentionkick 」\n  › Type: On♪\n    • Status: Already')
            else:
                position['mentionkick'].append(to)
                rahman(to, '「 Mentionkick 」\n  › Type: On♪\n    • Status: Success')
        elif mmk == "off":
            if to not in position['mentionkick']:
                rahman(to, '「 Mentionkick 」\n  › Type: Off♪\n    • Status: Nothing')
            else:
                position['mentionkick'].remove(to)
                rahman(to, '「 Mentionkick 」\n  › Type: Off♪\n    • Status: Success')
        elif mmk == "clear":
            if len(position['mentionkick']) > 0:
                rahman(to, f"「 Mentionkick 」\n › Type: Clear♪\n    • Amount: {len(position['mentionkick'])}\n    • Status: Success")
                position['mentionkick'].clear()
            else:
                rahman(to, "「 Mentionkick 」\n › Type: Clear♪\n    • Status: Nothing")           
        elif mmk == "cekmsg":
            rahman(to, settings["mentionkickmsg"]["msg"])           
        else:
            try:
                asu = removeCmd("idline", text)
                printEMO(to, msg, asu, "mentionkickmsg", "msg", "sticons", "mentionkick ","Mentionkick","Set Mentionkick Msg")
            except:
                 asu = removeCmd("idline", text)
                 changeMSG2(to, asu, "mentionkickmsg","msg", "Mentionkick" , "Set Mentionkick Msg")           

    elif cmd == 'wordban list':
        typeList(to, "Wordban","wordbann")
    elif cmd == 'text list':
        typeList(to, "Text","textt")
    elif cmd == 'picture list':
        typeList(to, "Picture","imagee")
    elif cmd == 'video list':
        typeList(to, "Video","videoo")
    elif cmd == 'audio list':
        typeList(to, "Audio","audioo")
    elif cmd == 'sticker list':
        typeList(to, "Sticker","stickerr")
    elif cmd == 'bigsticker list':
        typeList(to, "Bigsticker","bigstickerr")
    elif cmd == 'cont list':
        typeList(to, "Contact","contactt")
    elif cmd == 'kibaran list':
        typeList(to, "Kibaran","kibarann")
    elif cmd == 'wordban clear':        
        listsett["wordbann"] = {}
        rahman(to,"「 List 」\n › Type: Wordban Clear♪\n    • Status: Success")            
    elif cmd == 'text clear':
        for x in listsett["namaemot"]:
            del listsett[x]
        listsett["namaemot"].clear()        
        listsett["textt"] = {}
        rahman(to,"「 List 」\n › Type: Text Clear♪\n    • Status: Success")            
    elif cmd == 'picture clear':        
        listsett["imagee"] = {}
        rahman(to,"「 List 」\n › Type: Picture Clear♪\n    • Status: Success")            
    elif cmd == 'video clear':        
        listsett["videoo"] = {}
        rahman(to,"「 List 」\n › Type: Video Clear♪\n    • Status: Success")            
    elif cmd == 'audio clear':        
        listsett["audioo"] = {}
        rahman(to,"「 List 」\n › Type: Audio Clear♪\n    • Status: Success")            
    elif cmd == 'cont clear':        
        listsett["contactt"] = {}
        rahman(to,"「 LIST 」\n › Type: Contact Clear♪\n    • Status: Success")            
    elif cmd == 'sticker clear':        
        listsett["stickerr"] = {}
        rahman(to,"「 LIST 」\n › Type: Sticker Clear♪\n    • Status: Success")            
    elif cmd == 'bigsticker clear':        
        listsett["bigstickerr"] = {}
        rahman(to,"「 LIST 」\n › Type: Bigsticker Clear♪\n    • Status: Success")            
    elif cmd == 'kibaran clear':        
        listsett["kibarann"] = {}
        rahman(to,"「 LIST 」\n › Type: Kibaran Clear♪\n    • Status: Success")            
    elif cmd.startswith("wordban add"):
        mmk = removeCmd("wordban add", text)
        mmk = mmk.lower()                 
        if mmk not in listsett["wordbann"]:
            settings["Addwordban"]["status"] = True
            settings["Addwordban"]["name"] = str(mmk.lower())
            listsett["wordbann"][str(mmk.lower())] = ""
            rahman(to,"「 List 」\n › Type: Wordban Add♪\n    • Text : {} \n    • Status: Success".format(str(mmk.lower())))                                                       
        else:
            rahman(to,"「 List 」\n › Type: Wordban Add♪\n    • Status: Wordban Already")                      
    elif cmd.startswith("wordban del"):
        mmk = removeCmd("wordban del", text)
        mmk = mmk.lower()       
        if mmk in listsett["wordbann"]:
            del listsett["wordbann"][str(mmk.lower())]
            rahman(to,"「 List 」\n › Type: Wordban Del♪\n    • Text : {} \n    • Status: Success".format(str(mmk.lower())))                                 
        else:
            rahman(to,"「 List 」\n › Type: Wordban Del♪\n    • Status: Wordban Not In List")                 
    elif cmd.startswith("text add"):
        try:
            apl = removeCmd("text add", text)
            sam = apl.split(" | ")
            chat1 = sam[0]
            chat2 = sam[1]
            REPLACE = {"sticon":{"resources": []}}
            x = eval(msg.contentMetadata["REPLACE"])
            if settings['setKey']['status'] == True:
                kalera = settings['setKey']['key']
            else:
                kalera = ''
            a = kalera + "text add " + chat1 + " | "
            for data_rep in x["sticon"]["resources"]:
                REPLACE["sticon"]["resources"].append({"S": str(data_rep["S"] - len(a)), "E": str(data_rep["E"] - len(a)), "productId":data_rep["productId"], "sticonId": data_rep["sticonId"], "version":1, "resourceType": data_rep["resourceType"]})
            contentMetadata = {"REPLACE": json.dumps(REPLACE),"STICON_OWNERSHIP": msg.contentMetadata['STICON_OWNERSHIP']}                                
            apk = ""+chat1
            listsett["textt"][apk] = chat2
            listsett[apk] = contentMetadata
            listsett["namaemot"].append(apk)
            last_game["addText"] = chat1
            anu = last_game["addText"]+'.'
            rahman(to, "「 List 」\n › Type: Text Add\n    • Text: %s\n    • Status: Success"%chat1)
            last_game["addText"] = {}        
        except:
            apl = removeCmd("text add", text)
            sam = apl.split(" | ")
            chat1 = sam[0]
            chat2 = sam[1]
            apk = ""+chat1
            listsett["textt"][apk] = chat2
            last_game["addText"] = chat1
            anu = last_game["addText"]+'.'
            rahman(to, "「 List 」\n › Type: Text Add\n    • Text: %s\n    • Status: Success"%chat1)
            last_game["addText"] = {}        

    elif cmd.startswith("text del"):
        mmk = removeCmd("text del", text)
        mmk = mmk.lower()       
        if mmk in listsett["textt"]:
            if mmk in listsett["namaemot"]:
               del listsett[str(mmk.lower())]
               listsett["namaemot"].remove(mmk)
            else:pass
            del listsett["textt"][str(mmk.lower())]
            rahman(to,"「 List 」\n › Type: Text Del♪\n    • Text : {} \n    • Status: Success".format(str(mmk.lower())))                                 
        else:
            rahman(to,"「 List 」\n › Type: Text Del♪\n    • Status: Text Not In List")                 

    elif cmd.startswith("picture add"):
        mmk = removeCmd("picture add", text)
        mmk = mmk.lower()    
        if mmk not in listsett["imagee"]:
            settings["Addimage"]["status"] = True
            settings["Addimage"]["name"] = str(mmk.lower())
            listsett["imagee"][str(mmk.lower())] = ""
            rahman(to,"「 List 」\n › Type: Picture Add♪\n    • Text : {} \n    • Status: Send Picture".format(str(mmk.lower())))                                                            
        else:
            rahman(to,"「 List 」\n › Type: Picture Add♪\n    • Status:    • Picture Already")                                        
    elif cmd.startswith("picture del"):
        mmk = removeCmd("picture del", text)
        mmk = mmk.lower()   
        if mmk in listsett["imagee"]:
            maxbots.deleteFile(listsett["imagee"][str(mmk.lower())])
            del listsett["imagee"][str(mmk.lower())]
            rahman(to,"「 List 」\n › Type: Picture Del♪\n    • Text : {} \n    • Status: Success".format(str(mmk.lower())))                                            
        else:
            rahman(to,"「 List 」\n › Type: Picture Del♪\n    • Status: Picture Not In List")                 
    elif cmd.startswith("video add"):
        mmk = removeCmd("video add", text)
        mmk = mmk.lower()    
        if mmk not in listsett["videoo"]:
            settings["Addvideo"]["status"] = True
            settings["Addvideo"]["name"] = str(mmk.lower())
            listsett["videoo"][str(mmk.lower())] = ""
            rahman(to,"「 List 」\n › Type: Video Add♪\n    • Text : {} \n    • Status: Send Video".format(str(mmk.lower())))                                                            
        else:
            rahman(to,"「 List 」\n › Type: Video Add♪\n    • Status:    • Video Already")                                        
    elif cmd.startswith("video del"):
        mmk = removeCmd("video del", text)
        mmk = mmk.lower()   
        if mmk in listsett["videoo"]:
            maxbots.deleteFile(listsett["videoo"][str(mmk.lower())])
            del listsett["videoo"][str(mmk.lower())]
            rahman(to,"「 List 」\n › Type: Video Del♪\n    • Text : {} \n    • Status: Success".format(str(mmk.lower())))                                            
        else:
            rahman(to,"「 List 」\n › Type: Video Del♪\n    • Status: Video Not In List")                 
    elif cmd.startswith("audio add"):
        mmk = removeCmd("audio add", text)
        mmk = mmk.lower()    
        if mmk not in listsett["audioo"]:
            settings["Addaudio"]["status"] = True
            settings["Addaudio"]["name"] = str(mmk.lower())
            listsett["audioo"][str(mmk.lower())] = ""
            rahman(to,"「 List 」\n › Type: Audio Add♪\n    • Text : {} \n    • Status: Send Audio".format(str(mmk.lower())))                                                            
        else:
            rahman(to,"「 List 」\n › Type: Audio Add♪\n    • Status:    • Audio Already")                                        
    elif cmd.startswith("audio del"):
        mmk = removeCmd("audio del", text)
        mmk = mmk.lower()   
        if mmk in listsett["audioo"]:
            maxbots.deleteFile(listsett["audioo"][str(mmk.lower())])
            del listsett["audioo"][str(mmk.lower())]
            rahman(to,"「 List 」\n › Type: Audio Del♪\n    • Text : {} \n    • Status: Success".format(str(mmk.lower())))                                            
        else:
            rahman(to,"「 List 」\n › Type: Audio Del♪\n    • Status: Audio Not In List")                 
    elif cmd.startswith("sticker add"):
        mmk = removeCmd("sticker add", text)
        mmk = mmk.lower()    
        if mmk not in listsett["stickerr"]:
            settings["Addsticker"]["status"] = True
            settings["Addsticker"]["name"] = str(mmk.lower())
            listsett["stickerr"][str(mmk.lower())] = ""
            rahman(to,"「 List 」\n › Type: Sticker Add♪\n    • Text : {} \n    • Status: Send Sticker".format(str(mmk.lower())))                                                            
        else:
            rahman(to,"「 List 」\n › Type: Sticker Add♪\n    • Status:    • Sticker Already")                                        
    elif cmd.startswith("sticker del"):
        mmk = removeCmd("sticker del", text)
        mmk = mmk.lower()    
        if mmk in listsett["stickerr"]:
            del listsett["stickerr"][str(mmk.lower())]
            rahman(to,"「 List 」\n › Type: Sticker Del♪\n    • Text : {} \n    • Status: Success".format(str(mmk.lower())))                                            
        else:
            rahman(to,"「 List 」\n › Type: Sticker Del♪\n    • Status: Sticker Not In List")                 
    elif cmd.startswith("bigsticker add"):
        mmk = removeCmd("bigsticker add", text)
        mmk = mmk.lower()    
        ktl = geTreply(msg)
        if ktl == None:
            if mmk not in listsett["bigstickerr"]:
                settings["Addbigsticker"]["status"] = True
                settings["Addbigsticker"]["name"] = str(mmk.lower())
                listsett["bigstickerr"][str(mmk.lower())] = ""
                rahman(to,"「 List 」\n › Type: Bigsticker Add♪\n    • Text : {} \n    • Status: Send Sticker".format(str(mmk.lower())))                                                            
            else:
                rahman(to,"「 List 」\n › Type: Bigsticker Add♪\n    • Status:    • Sticker Already")                                            
        else:
            if ktl.contentType == 7:
                if mmk not in listsett["bigstickerr"]:
                    listsett["bigstickerr"][str(mmk.lower())] = printSTC(ktl)
                    rahman(to,"「 List 」\n › Type: Bigsticker Add♪\n    • Name : {}\n    • Status: Success".format(str(mmk.lower())))                         
                else:
                    rahman(to,"「 List 」\n › Type: Bigsticker Add♪\n    • Status:    • Sticker Already")                                            
    elif cmd.startswith("bigsticker del"):
        mmk = removeCmd("bigsticker del", text)
        mmk = mmk.lower()    
        if mmk in listsett["bigstickerr"]:
            del listsett["bigstickerr"][str(mmk.lower())]
            rahman(to,"「 List 」\n › Type: Bigsticker Del♪\n    • Text : {} \n    • Status: Success".format(str(mmk.lower())))                                            
        else:
            rahman(to,"「 List 」\n › Type: Bigsticker Del♪\n    • Status: Sticker Not In List")                 
    elif cmd.startswith("cont add"):
        mmk = removeCmd("cont add", text)
        mmk = mmk.lower()    
        if mmk not in listsett["contactt"]:
            settings["Addcontact"]["status"] = True
            settings["Addcontact"]["name"] = str(mmk.lower())
            listsett["contactt"][str(mmk.lower())] = ""
            rahman(to,"「 List 」\n › Type: Contact Add♪\n    • Text : {} \n    • Status: Send Contact".format(str(mmk.lower())))                                                            
        else:
            rahman(to,"「 List 」\n › Type: Contact Add♪\n    • Status:    • Contact Already")                                        
    elif cmd.startswith("cont del"):
        mmk = removeCmd("cont del", text)
        mmk = mmk.lower()    
        if mmk in listsett["contactt"]:
            del listsett["contactt"][str(mmk.lower())]
            rahman(to,"「 List 」\n › Type: Contact Del♪\n    • Text : {} \n    • Status: Success".format(str(mmk.lower())))                                            
        else:
            rahman(to,"「 List 」\n › Type: Contact Del♪\n    • Status: Contact Not In List")                 
    elif cmd.startswith("kibaran add"):
        mmk = removeCmd("kibaran add", text)
        mmk = mmk.lower()    
        if mmk not in listsett["kibarann"]:
            settings["Addkibaran"]["status"] = True
            settings["Addkibaran"]["name"] = str(mmk.lower())
            listsett["kibarann"][str(mmk.lower())] = []
            rahman(to,"「 List 」\n › Type: Kibaran Add♪\n    • Text : {} \n    • Status: Send Kibaran".format(str(mmk.lower())))                                                            
        else:
            rahman(to,"「 List 」\n › Type: Kibaran Add♪\n    • Status:    • Kibaran Already")                                        
    elif cmd.startswith("kibaran del"):
        mmk = removeCmd("kibaran del", text)
        mmk = mmk.lower()    
        if mmk in listsett["kibarann"]:
            del listsett["kibarann"][str(mmk.lower())]
            rahman(to,"「 List 」\n › Type: Kibaran Del♪\n    • Text : {} \n    • Status: Success".format(str(mmk.lower())))                                            
        else:
            rahman(to,"「 List 」\n › Type: Kibaran Del♪\n    • Status: Kibaran Not In List")                 

    elif cmd == "memory":
       am = subprocess.getoutput('cat /proc/meminfo');core = subprocess.getoutput('grep -c ^processor /proc/cpuinfo ')           
       for anu in am.splitlines():
           if 'MemTotal:' in anu:mem = anu.split('MemTotal:')[1].replace(' ','')                   
           if 'MemFree:' in anu:fr = anu.split('MemFree:')[1].replace(' ','')                   
       rahman(to, '「 Vps Info 」\n › Type: Memory♪\n    • Cpu Core: {}\n    • Total Memory: {}\n    • Free Memory: {}'.format(core,mem,fr))
    elif cmd == 'system':
       ajg = subprocess.getoutput('lsb_release -a');babi = subprocess.getoutput('cat /proc/meminfo');tll = subprocess.getoutput('lscpu');ngewe = platform.python_implementation();ngentod = platform.python_version()                                 
       for bego in ajg.splitlines():
          if 'Description:' in bego:telaso = bego.split('Description:')[1].replace(' ','')                  
       for bego in tll.splitlines():
          if 'Architecture:' in bego:architecture =  bego.split('Architecture:')[1].replace(' ','')                  
       rahman(to, '「 Vps Info 」\n › Type: Sytem♪\n    • Architecture: {}\n    • OS: {}\n    • Language: {}\n    • Version: {}'.format(architecture,telaso,ngewe,ngentod))
    elif cmd == "clears":
        os.popen('echo 1 | sudo tee /proc/sys/vm/drop_caches\necho 2 | sudo tee /proc/sys/vm/drop_caches\necho 3 | sudo tee /proc/sys/vm/drop_caches\n').read()
        position['ROM'] = {}
        position["postId2"].clear()
        last_game['ROM'] = {}
        rahman(to,"「 Vps Info 」\n › Type: Clear Data♪\n    • Status: Success")                     
    elif cmd == "clearchat":
        maxbots.removeAllMessages(msg.id)
        rahman(to,"「 Vps Info 」\n › Type: Clear Chat ♪\n    • Status: Succes")           
    elif cmd == "clearletsel":
        try:
            a = maxbots.talk.negotiateE2EEPublicKey(myMid)
            b = maxbots.talk.removeE2EEPublicKey(a.publicKey)
            rahman(to,"「 Vps Info 」\n › Type: Clear Publickey♪\n    • Status: Succes")           
        except:                         
            rahman(to,"「 Vps Info 」\n › Type: Clear Publickey♪\n    • Status: Nothing")           

    elif cmd == 'squadlist':        
        no = 0
        arifblek = "「 Squad 」\n › Type: List♪\n"
        for ktl in position["squadteam"]:
            arifblek += "    • " + ktl.title() + "\n"
        arifblek += "\n\n › Command"
        arifblek += f"\n    • {setKey}Squadlist ‹Name›"
        arifblek += f"\n    • {setKey}Squad Del ‹Name›  "
        arifblek += f"\n    • {setKey}Squad Clear "
        arifblek += f'\n    • {setKey}Sl Add ‹Name› ‹@/On/Here› '
        arifblek += "\n\n › Command Reply"
        arifblek += f'\n    • {setKey}Sl Add ‹Name› '
        rahman(to, arifblek)        
    elif cmd.startswith("squadlist"):
        name = removeCmd("squadlist", text)
        mids = eval(str(position["squadteam"][name]["list"]))
        result = '「 Squad 」 \n'
        no = 0
        for i in range(len(mids)//20+1):                                        
            target = []
            for mid in mids[i*20:(i+1)*20]:
                no += 1
                if mid == position["squadteam"][name]["list"][0]:
                    result += ' › Type: List♪\n'
                result += f'    • {no}. @!\n'
                if mid == mids[-1]:
                    result += '\n › Condition'
                    result += '\n    • Status: ' + bool_dict[position["squadteam"][name]["status"]][1]
                    result += '\n    • Cmd: {}{}'.format(setKey, name.title()) 
                    result += '\n\n › Command Set'
                    result += f'\n    • {setKey}Sl Add {name} ‹@/On/Here› '
                    result += f'\n    • {setKey}Sl Del {name} ‹@/On/Num/Here› '
                    result += f'\n    • {setKey}Sl Detect {name}'
                    result += f'\n    • {setKey}Sl Stc Add {name}'
                    result += f'\n    • {setKey}Sl Stc Del {name}'
                    result += f'\n    • {setKey}Sl Stc Cek {name}'
                    result += f'\n    • {setKey}Sl Backup {name} ‹On/Off›'
                    result += '\n\n › Command Reply'
                    result += f'\n    • {setKey}Sl Add {name}'
                    result += f'\n    • {setKey}Sl Del {name}'
                    result += f'\n    • {setKey}Sl Stc Add {name}'
                    result += f'\n    • {setKey}Sl Stc Del {name}'
                target.append(mid)
            if result.startswith('\n'): result = result[1:]
            if result.endswith('\n'): result = result[:-1]
            maxbots.sendTag(to, result, target)
            result = ''
    elif cmd.startswith("squad del"):
        asu = removeCmd("squad del", text)
        if asu in position["squadteam"]:
            del position["squadteam"][asu]
            rahman(to,"「 Squad 」\n › Type: List Del♪\n    • Text : {} \n    • Status: Success".format(str(asu)))                                            
    elif cmd == 'squad clear':        
        position["squadteam"] = {}
        rahman(to,"「 Squad 」\n › Type: List Clear♪\n    • Status: Success")            
    elif cmd.startswith("sl add"):
        mmk = removeCmd("sl add", text)
        tol = mmk.split(" ")
        name = tol[0]
        asu = mmk.replace(mmk.split(" ")[0] + ' ','')
        cpkajg = {"status": False,"statusconadd": False,"statuscondel": False,"statusstc": False,"stc": {}, "list": []}
        if name not in position["squadteam"]:
            position["squadteam"][name] = cpkajg
        if asu == "on":
            position["squadteam"][name]["statusconadd"] = True
            rahman(to,"「 Squad 」\n › Type: Add♪\n    • Squad Name : {} \n    • Status: Send Contact".format(name))           
        if asu == "here":
            ktl = maxbots.getChats([to]).chats[0]
            mem = ktl.extra.groupExtra.memberMids
            member = [member for member in mem]
            for x in member:
                if x not in position["squadteam"][name]["list"] and x not in myMid:
                    time.sleep(0.2)
                    position["squadteam"][name]["list"].append(x)
            rahman(to,"「 Squad 」\n › Type: Add Here♪\n    • Squad Name : {} \n    • Status: Success".format(name))       
        if asu != " ":
            if msg.relatedMessageId is not None:
                bb = geTreply(msg)
                if cmd == "sl add " + name:
                    if bb._from not in position["squadteam"][name]["list"]:
                        finded(bb._from) 
                        position["squadteam"][name]["list"].append(bb._from)
                        maxbots.sendTag(to,"「 Squad 」\n › Type: Add♪\n    • 1. @! Add♪",[bb._from])   
                    else:                                                             
                        maxbots.sendTag(to,"「 Squad 」\n › Type: Add♪\n    • 1. @! Already♪",[bb._from])  
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            list = geTmention(msg)
            if(list == [] or list == {}):pass
            k = len(list)//20
            for aa in range(k+1):
                if aa == 0:dd = '「 Squad 」\n › Type: Add♪';no=aa
                else:dd = '「 Squad 」\n › Type: Add♪';no=aa*20
                msgas = dd
                for i in list[aa*20 : (aa+1)*20]:
                    no+=1
                    if i in position["squadteam"][name]["list"]:
                        a = 'Already♪'
                    else:
                        if i not in myMid:
                            a = 'Add♪'
                            finded(i) 
                            position["squadteam"][name]["list"].append(i)
                        else:a = 'Self♪'   
                    if no == len(list):msgas+='\n    • {}. @! {}'.format(no,a)
                    else:msgas+='\n    • {}. @! {}'.format(no,a)
                maxbots.sendMentionn(to, msgas,' 「 Squad 」', list[aa*20 : (aa+1)*20])
    elif cmd.startswith("sl del"):
        mmk = removeCmd("sl del", text)
        tol = mmk.split(" ")
        name = tol[0]
        asu = mmk.replace(mmk.split(" ")[0] + ' ','')
        if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata.keys():                                
            list = geTmention(msg)
            if(list == [] or list == {}):pass
            k = len(list)//20
            for aa in range(k+1):
                if aa == 0:dd = '「 Squad 」\n › Type: Del♪';no=aa
                else:dd = '「 Squad 」\n › Type: Del♪';no=aa*20
                msgas = dd
                for i in list[aa*20 : (aa+1)*20]:
                    no+=1
                    if i in position["squadteam"][name]["list"]:
                        a = 'Del♪'
                        position["squadteam"][name]["list"].remove(i)
                    else:
                        a = 'Nothing♪'                            
                    if no == len(list):msgas+='\n    • {}. @! {}'.format(no,a)
                    else:msgas+='\n    • {}. @! {}'.format(no,a)
                maxbots.sendMentionn(to, msgas,' 「 Squad 」', list[aa*20 : (aa+1)*20])
        if asu == "on":
            position["squadteam"][name]["statuscondel"] = True
            rahman(to,"「 Squad 」\n › Type: Del♪\n    • Squad Name : {} \n    • Status: Send Contact".format(name))           
        if asu == "here":
            group = maxbots.getChats([to]).chats[0]
            lists = []
            for tag in position["squadteam"][name]["list"]:
                lists+=filter(lambda str: str == tag, group.extra.groupExtra.memberMids)                
            if lists == []:
                rahman(to,"「 Squad 」\n › Type: Del Here♪ \n    • Status: Not Found")
                return                                
            for xx in lists:
                position["squadteam"][name]["list"].remove(xx)
            if len(lists) > 0: 
                h = [a for a in lists]
                k = len(h)//20                
                for aa in range(k+1):
                    if aa == 0:dd = '「 Squad 」\n › Type: Del Here♪';no=aa
                    else:dd = '';no=aa*20
                    msgas = dd
                    for a in h[aa*20:(aa+1)*20]:
                        no+=1
                        if no == len(h):msgas+='\n    • {}.@! Del♪\n'.format(no)
                        else:msgas += '\n    • {}. @! Del♪'.format(no)
                    maxbots.sendTag(to, msgas, h[aa*20:(aa+1)*20])     
        if asu != " ":
            if msg.relatedMessageId is not None:
                bb = geTreply(msg)
                if cmd == "sl del " + name:
                    if bb._from in position["squadteam"][name]["list"]:
                        position["squadteam"][name]["list"].remove(bb._from)
                        maxbots.sendTag(to,"「 Squad 」\n › Type: Del♪\n    • 1. @! Del♪",[bb._from])   
                    else:                                                             
                        maxbots.sendTag(to,"「 Squad 」\n › Type: Del♪\n    • 1. @! Nothing♪",[bb._from])  
            else:
                    x = splitdel(str(asu), position["squadteam"][name]["list"])
                    z = len(position["squadteam"][name]["list"])//100
                    for c in range(z+1):
                        if c == 0:
                            list = x[:100]
                            if(list == [] or list == {}):pass
                            k = len(list)//20
                            for aa in range(k+1):
                                if aa == 0:dd = '「 Squad 」\n › Type: Del♪';no=aa
                                else:dd = '「 Squad 」\n › Type: Del♪';no=aa*20
                                msgas = dd
                                for i in list[aa*20 : (aa+1)*20]:
                                    no+=1
                                    if i in position["squadteam"][name]["list"]:
                                        a = 'Del♪'
                                        position["squadteam"][name]["list"].remove(i)
                                    else:
                                        a = 'Nothing♪'                            
                                    if no == len(list):msgas+='\n    • {}. @! {}'.format(no,a)
                                    else:msgas+='\n    • {}. @! {}'.format(no,a)
                                maxbots.sendMentionn(to, msgas,' 「 Squad 」', list[aa*20 : (aa+1)*20])
                        else:
                            list = x[c*100 : (c+1)*100]
                            if(list == [] or list == {}):pass
                            k = len(list)//20
                            for aa in range(k+1):
                                if aa == 0:dd = '「 Squad 」\n › Type: Del♪';no=aa
                                else:dd = '「 Squad 」\n › Type: Del♪';no=aa*20
                                msgas = dd
                                for i in list[aa*20 : (aa+1)*20]:
                                    no+=1
                                    if i in position["squadteam"][name]["list"]:
                                        a = 'Del♪'
                                        position["squadteam"][name]["list"].remove(i)
                                    else:
                                        a = 'Nothing♪'                            
                                    if no == len(list):msgas+='\n    • {}. @! {}'.format(no,a)
                                    else:msgas+='\n    • {}. @! {}'.format(no,a)
                                maxbots.sendMentionn(to, msgas,' 「 Squad 」', list[aa*20 : (aa+1)*20])
    elif cmd.startswith("sl detect"):
        mmk = removeCmd("sl detect", text)
        group = maxbots.getChats([to]).chats[0]
        lists = []
        for tag in position["squadteam"][mmk]["list"]:
            lists+=filter(lambda str: str == tag, group.extra.groupExtra.memberMids)                
        if lists == []:
            rahman(to,f"「 Squad 」\n › Type: {mmk} Detect♪ \n    • Status: Not Found")
            return                                
        if len(lists) > 0: 
            h = [a for a in lists]
            k = len(h)//20                
            for aa in range(k+1):
                if aa == 0:dd = f'「 Squad 」\n › Type: {mmk} Detect♪';no=aa
                else:dd = '';no=aa*20
                msgas = dd
                for a in h[aa*20:(aa+1)*20]:
                    no+=1
                    if no == len(h):msgas+='\n    • {}.@!\n'.format(no)
                    else:msgas += '\n    • {}. @!'.format(no)
                maxbots.sendTag(to, msgas, h[aa*20:(aa+1)*20])     
    elif cmd.startswith("sl stc add"):        
        asu = removeCmd("sl stc add", text)
        ktl = geTreply(msg)
        if ktl == None:               
            position["squadteam"][asu]["statusstc"] = True
            rahman(to,"「 Squad 」\n › Type: Sticker♪\n    • Squad Name : {} \n    • Status: Send Sticker".format(asu))           
        else:
            if ktl.contentType == 7:
                ngentod = printSTC(ktl)
                position["squadteam"][asu]["stc"] = ngentod
                rahman(to,   "「 Squad 」\n › Type: Sticker Add♪\n    • Status: Success")                                                
    elif cmd.startswith("sl stc del"):
        asu = removeCmd("sl stc del", text)
        position["squadteam"][asu]["stc"] = {}
        rahman(to,   "「 Squad 」\n › Type: Sticker Del♪\n    • Status: Success")                                                
    elif cmd.startswith("sl stc cek"):
        asu = removeCmd("sl stc cek", text)
        tikelnyaa = position["squadteam"][asu]["stc"]
        try:
            maxbots.sendMessage(to, '', tikelnyaa, 7)
        except:
            rahman(to,   "「 Squad 」\n › Type: Sticker Cek♪\n    • Status: Nothing")                                                
    elif cmd.startswith("sl backup"):
        mmk = removeCmd("sl backup", text)
        tol = mmk.split(" ")
        name = tol[0]
        asu = mmk.replace(mmk.split(" ")[0] + ' ','')
        if asu == "on":
            if position["squadteam"][name]["status"]:
                if settings["stattemp"] == True:
                    sendON(to, f"Backup {name.title()}")
                else:	
                    rahman(to, f'「 Squad 」\n › Type: {name.title()} Backul♪\n    • Status: Already Active')                        
            else:
                position["squadteam"][name]["status"] = True
                if settings["stattemp"] == True:
                    sendON(to, f"Backup {name.title()}")
                else:	
                    rahman(to, f'「 Squad 」\n › Type: {name.title()} Backul♪\n    • Status: Active')                          
        elif asu == 'off':
            if not position["squadteam"][name]["status"]:
                if settings["stattemp"] == True:
                    sendOFF(to, f"Backup {name.title()}")
                else:	
                    rahman(to, f'「 Squad 」\n › Type: {name.title()} Backul♪\n    • Status: Already Dctive')                        
            else:
                position["squadteam"][name]["status"] = False
                if settings["stattemp"] == True:
                    sendOFF(to, f"Backup {name.title()}")
                else:	
                    rahman(to, f'「 Squad 」\n › Type: {name.title()} Backul♪\n    • Status: Deactive')                          

    elif cmd == "lastjoin list":
        maxbots.sendlastlist(to, setKey, last_game, "lastjoin", "Join", "Ljoin" ,settings["kill"].title(),settings["invite"].title(), settings["cancel"].title())
    elif cmd == "ljoin clear":
        ngeclearlast(to, "lastjoin", "Join")
    elif cmd.startswith("ljoin del"):
        mmk = removeCmd("ljoin del", text)
        deldellast(to,mmk, "lastjoin",'DELLJOIN',"Join")
    elif cmd.startswith(f"ljoin {settings['invite']}"):
        mmk = removeCmd(f"ljoin {settings['invite']}", text)
        iilast(to, mmk, "lastjoin")
    elif cmd.startswith(f"ljoin {settings['kill']}"):
        mmk = removeCmd(f"ljoin {settings['kill']}", text)
        kklast(to, mmk, "lastjoin")
    elif cmd.startswith(f"ljoin {settings['cancel']}"):
        mmk = removeCmd(f"ljoin {settings['cancel']}", text)
        cclast(to, mmk, "lastjoin")

    elif cmd == "lastleave list":
        maxbots.sendlastlist(to, setKey, last_game, "lastleave", "Leave", "Lleave" ,settings["kill"].title(),settings["invite"].title(), settings["cancel"].title())
    elif cmd == "lleave clear":
        ngeclearlast(to, "lastleave", "Leave")
    elif cmd.startswith("lleave del"):
        mmk = removeCmd("lleave del", text)
        deldellast(to,mmk, "lastleave",'DELLLEAVE',"Leave")
    elif cmd.startswith(f"lleave {settings['invite']}"):
        mmk = removeCmd(f"lleave {settings['invite']}", text)
        iilast(to, mmk, "lastleave")
    elif cmd.startswith(f"lleave {settings['kill']}"):
        mmk = removeCmd(f"lleave {settings['kill']}", text)
        kklast(to, mmk, "lastleave")
    elif cmd.startswith(f"lleave {settings['cancel']}"):
        mmk = removeCmd(f"lleave {settings['cancel']}", text)
        cclast(to, mmk, "lastleave")

    elif cmd == "lastcontact list":
        maxbots.sendlastlist(to, setKey, last_game, "lastcontact", "Contact", "Lcon" ,settings["kill"].title(),settings["invite"].title(), settings["cancel"].title())
    elif cmd == "lcon clear":
        ngeclearlast(to, "lastcontact", "Contact")
    elif cmd.startswith("lcon del"):
        mmk = removeCmd("lcon del", text)
        deldellast(to,mmk, "lastcontact",'DELLCONTACT',"Contact")
    elif cmd.startswith(f"lcon {settings['invite']}"):
        mmk = removeCmd(f"lcon {settings['invite']}", text)
        iilast(to, mmk, "lastcontact")
    elif cmd.startswith(f"lcon {settings['kill']}"):
        mmk = removeCmd(f"lcon {settings['kill']}", text)
        kklast(to, mmk, "lastcontact")
    elif cmd.startswith(f"lcon {settings['cancel']}"):
        mmk = removeCmd(f"lcon {settings['cancel']}", text)
        cclast(to, mmk, "lastcontact")

    elif cmd == "lastkick list":
        maxbots.sendlastlist(to, setKey, last_game, "lastkick", "Kick", "Lkick" ,settings["kill"].title(),settings["invite"].title(), settings["cancel"].title())
    elif cmd == "lkick clear":
        ngeclearlast(to, "lastkick", "Kick")
    elif cmd.startswith("lkick del"):
        mmk = removeCmd("lkick del", text)
        deldellast(to,mmk, "lastkick",'DELLKICK',"Kick")
    elif cmd.startswith(f"lkick {settings['invite']}"):
        mmk = removeCmd(f"lkick {settings['invite']}", text)
        iilast(to, mmk, "lastkick")
    elif cmd.startswith(f"lkick {settings['kill']}"):
        mmk = removeCmd(f"lkick {settings['kill']}", text)
        kklast(to, mmk, "lastkick")
    elif cmd.startswith(f"lkick {settings['cancel']}"):
        mmk = removeCmd(f"lkick {settings['cancel']}", text)
        cclast(to, mmk, "lastkick")

    elif cmd == "lastinvite list":
        maxbots.sendlastlist(to, setKey, last_game, "lastinvite", "Invite", "Linvite" ,settings["kill"].title(),settings["invite"].title(), settings["cancel"].title())
    elif cmd == "linvite clear":
        ngeclearlast(to, "lastinvite", "Invite")
    elif cmd.startswith("linvite del"):
        mmk = removeCmd("linvite del", text)
        deldellast(to,mmk, "lastinvite",'DELLINVITE',"Invite")
    elif cmd.startswith(f"linvite {settings['invite']}"):
        mmk = removeCmd(f"linvite {settings['invite']}", text)
        iilast(to, mmk, "lastinvite")
    elif cmd.startswith(f"linvite {settings['kill']}"):
        mmk = removeCmd(f"linvite {settings['kill']}", text)
        kklast(to, mmk, "lastinvite")
    elif cmd.startswith(f"linvite {settings['cancel']}"):
        mmk = removeCmd(f"linvite {settings['cancel']}", text)
        cclast(to, mmk, "lastinvite")

    elif cmd == "lastcancel list":
        maxbots.sendlastlist(to, setKey, last_game, "lastcancel", "Cancel", "Lcancel" ,settings["kill"].title(),settings["invite"].title(), settings["cancel"].title())
    elif cmd == "lcancel clear":
        ngeclearlast(to, "lastcancel", "Cancel")
    elif cmd.startswith("lcancel del"):
        mmk = removeCmd("lcancel del", text)
        deldellast(to,mmk, "lastcancel",'DELLCANCEL',"Cancel")
    elif cmd.startswith(f"lcancel {settings['invite']}"):
        mmk = removeCmd(f"lcancel {settings['invite']}", text)
        iilast(to, mmk, "lastcancel")
    elif cmd.startswith(f"lcancel {settings['kill']}"):
        mmk = removeCmd(f"lcancel {settings['kill']}", text)
        kklast(to, mmk, "lastcancel")
    elif cmd.startswith(f"lcancel {settings['cancel']}"):
        mmk = removeCmd(f"lcancel {settings['cancel']}", text)
        cclast(to, mmk, "lastcancel")

    elif cmd.startswith("uns "):
           sep = msg.text.split(" ");args = msg.text.replace(sep[0] + " ","");mes = int(sep[1]);M = maxbots.getRecentMessagesV2(to, 1001);MId = []                                            
           for ind,i in enumerate(M):
               if ind == 0:pass                   
               else:
                   if i._from == maxbots.profile.mid:
                       MId.append(i.id)
                       if len(MId) == mes:break                           
           def unsMes(id):maxbots.unsendMessage(id)               
           for i in MId:thread1 = threading.Thread(target=unsMes, args=(i,));thread1.daemon = True;thread1.start();thread1.join()                                                            
           maxbots.unsendMessage(msg.id)    
    elif cmd.startswith("unsend "):
           sep = msg.text.split("d ")
           args = msg.text.replace(sep[0] + "d ","")
           mes = int(sep[1])
           M = maxbots.getRecentMessagesV2(to, 1001)
           MId = []                                            
           for ind,i in enumerate(M):
               if ind == 0:
                   pass                  
               else: 
                   if i._from == maxbots.profile.mid:
                       MId.append(i.id)
                       if len(MId) == mes:
                           break                           
           def unsMes(id):
               maxbots.unsendMessage(id)               
           for i in MId:
               thread1 = threading.Thread(target=unsMes, args=(i,))
               thread1.daemon = True
               thread1.start()
               thread1.join()                                                            
           maxbots.unsendMessage(msg.id)                
    elif cmd.startswith("exec"):
       try:sep = text.split("\n");txt = text.replace(sep[0] + "\n","");exec(txt)                                             
       except Exception as e:rahman(to, str(e))                               
    elif cmd == 'abort':
        aborted = False
        if settings['ChangePictFooter']:
            settings['ChangePictFooter'] = False
            rahman(to,"「 Mode 」\n › Type: Change Picture Label♪ \n    • Status: Aborted")
            aborted = True                                   
        if wait["getpictcontact"]:
            wait["getpictcontact"] = False
            rahman(to,"「 Steal 」\n › Type: Getpict♪ \n    • Status: Aborted")
            aborted = True                                 
        if wait["getcovercontact"]:
            wait["getcovercontact"] = False
            rahman(to,"「 Steal 」\n › Type: Getcover♪ \n    • Status: Aborted")
            aborted = True                                     
        if wait["getexcovercontact"]:
            wait["getexcovercontact"] = False
            rahman(to,"「 Steal 」\n › Type: Getextracover♪ \n    • Status: Aborted")
            aborted = True                                 
        if wait["getvideocontact"]:
            wait["getvideocontact"] = False
            rahman(to,"「 Steal 」\n › Type: Getvideo♪ \n    • Status: Aborted")
            aborted = True                                      
        if wait["getnamecontact"]:
            wait["getnamecontact"] = False
            rahman(to,"「 Steal 」\n › Type: Getname♪ \n    • Status: Aborted")
            aborted = True                                     
        if wait["getrenamecontact"]:
            wait["getrenamecontact"] = False
            rahman(to,"「 Steal 」\n › Type: Getrename♪ \n    • Status: Aborted")
            aborted = True                                     
        if wait["getbiocontact"]:
            wait["getbiocontact"] = False
            rahman(to,"「 Steal 」\n › Type: Getbio♪ \n    • Status: Aborted")
            aborted = True                                 
        if wait["getmidcontact"]:
            wait["getmidcontact"] = False
            rahman(to,"「 Steal 」\n › Type: Getmid♪ \n    • Status: Aborted")
            aborted = True                                   
        if wait["getcontactcontact"]:
            wait["getcontactcontact"] = False
            rahman(to,"「 Steal 」\n › Type: Getcontact♪ \n    • Status: Aborted")
            aborted = True                                 
        if wait["gettimelinecontact"]:
            wait["gettimelinecontact"] = False
            rahman(to,"「 Steal 」\n › Type: Gettimeline♪ \n    • Status: Aborted")
            aborted = True                                 
        if wait["getstorycontact"]:
            wait["getstorycontact"] = False
            rahman(to,"「 Steal 」\n › Type: Getstory♪ \n    • Status: Aborted")
            aborted = True                                  
        if settings['changePictureProfile']:
            settings['changePictureProfile'] = False
            rahman(to,"「 Profile 」\n › Type: Change Profile♪ \n    • Status: Aborted")
            aborted = True                                 
        if settings['changeCoverProfile']:
            settings['changeCoverProfile'] = False
            rahman(to,"「 Profile 」\n › Type: Change Cover♪ \n    • Status: Aborted")
            aborted = True                               
        if settings["changevp"]:
            settings["changevp"] = False
            rahman(to,"「 Profile 」\n › Type: Change Video Profile♪ \n    • Status: Aborted")
            aborted = True                                 
        if settings['changeProfileVideo']:
            settings['changeProfileVideo'] = False
            rahman(to,"「 Profile 」\n › Type: Change Video Cover♪ \n    • Status: Aborted")
            aborted = True                                 
        if settings["updatestory"]:
            settings["updatestory"] = False
            rahman(to,"「 Profile 」\n › Type: Change Video Profile♪ \n    • Status: Aborted")
            aborted = True                                 
        if wait["wfriendlist"]:
            wait["wfriendlist"] = False
            rahman(to,"「 Friend 」\n › Type: Friend Add♪ \n    • Status: Aborted")
            aborted = True                                 
        if wait["dfriendlist"]:
            wait["dfriendlist"] = False
            rahman(to,"「 Friend 」\n › Type: Friend Del♪ \n    • Status: Aborted")
            aborted = True                                 
        if wait["wblocklist"]:
            wait["wblocklist"] = False
            rahman(to,"「 Friend 」\n › Type: Block Add♪ \n    • Status: Aborted")
            aborted = True                                 
        if wait["dblocklist"]:
            wait["dblocklist"] = False
            rahman(to,"「 Friend 」\n › Type: Block Del♪ \n    • Status: Aborted")
            aborted = True                                 
        if to in settings['changeGroupPicture']:
            settings['changeGroupPicture'].remove(to)
            rahman(to,"「 Group 」\n › Type: Change Gpict♪ \n    • Status: Aborted")
            aborted = True
        if to in settings['changeGroupCover']:
            settings['changeGroupCover'].remove(to)
            rahman(to,"「 Group 」\n › Type: Change Gcover♪ \n    • Status: Aborted")
            aborted = True                                                               
        if settings['statkick']:
            settings['statkick'] = False
            rahman(to,"「 Command 」\n › Type: Add Stickerkick♪ \n    • Status: Aborted")
            aborted = True                                 
        if settings['statinvite']:
            settings['statinvite'] = False
            rahman(to,"「 Command 」\n › Type: Add Stickerinvite♪ \n    • Status: Aborted")
            aborted = True
        if settings['statleave']:
            settings['statleave'] = False
            rahman(to,"「 Command 」\n › Type: Add Stickerleave♪ \n    • Status: Aborted")
            aborted = True 
        if settings['statkickallpy']:
            settings['statkickallpy'] = False
            rahman(to,"「 Command 」\n › Type: Add Stickerkickallpy♪ \n    • Status: Aborted")
            aborted = True 
        if settings['statkillbanpy']:
            settings['statkillbanpy'] = False
            rahman(to,"「 Command 」\n › Type: Add Stickerkillbanpy♪ \n    • Status: Aborted")
            aborted = True 
        if settings['statkillban']:
            settings['statkillban'] = False
            rahman(to,"「 Command 」\n › Type: Add Stickerkillban♪ \n    • Status: Aborted")
            aborted = True 
        if settings['statreinvite']:
            settings['statreinvite'] = False
            rahman(to,"「 Command 」\n › Type: Add Stickerreinvite♪ \n    • Status: Aborted")
            aborted = True 
        if settings['statmkick']:
            settings['statmkick'] = False
            rahman(to,"「 Command 」\n › Type: Add Stickermkick♪ \n    • Status: Aborted")
            aborted = True 
        if settings['statslain']:
            settings['statslain'] = False
            rahman(to,"「 Command 」\n › Type: Add Stickerslain♪ \n    • Status: Aborted")
            aborted = True 
        if settings["stattagall"]:
            settings["stattagall"] = False
            rahman(to,"「 Mention 」\n › Type: Add Stickertagall♪ \n    • Status: Aborted")
            aborted = True                                 
        if settings['stickerfaketag']:
            settings['stickerfaketag'] = False
            rahman(to,"「 Mention 」\n › Type: Add Stickerfaketag♪ \n    • Status: Aborted")
            aborted = True                                 
        if settings["statemojitagall"]:
            settings["statemojitagall"] = False
            rahman(to,"「 Mention 」\n › Type: Add Stickeremojitagall♪ \n    • Status: Aborted")
            aborted = True                                 
        if wait["wblacklist"]:
            wait["wblacklist"] = False
            rahman(to,"「 Banning 」\n › Type: Bl Add♪ \n    • Status: Aborted")
            aborted = True                                 
        if wait["dblacklist"]:
            wait["dblacklist"] = False
            rahman(to,"「 Banning 」\n › Type: Bl Del♪ \n    • Status: Aborted")
            aborted = True                                 
        if wait["wadminlist"]:
            wait["wadminlist"] = False
            rahman(to,"「 Banning 」\n › Type: Admin Add♪ \n    • Status: Aborted")
            aborted = True                                 
        if wait["dadminlist"]:
            wait["dadminlist"] = False
            rahman(to,"「 Banning 」\n › Type: Admin Del♪ \n    • Status: Aborted")
            aborted = True                                     
        if wait["wwhitelist"]:
            wait["wwhitelist"] = False
            rahman(to,"「 Banning 」\n › Type: Wl Add♪ \n    • Status: Aborted")
            aborted = True                                 
        if wait["dwhitelist"]:
            wait["dwhitelist"] = False
            rahman(to,"「 Banning 」\n › Type: Wl Del♪ \n    • Status: Aborted")
            aborted = True                                                      
        if wait["wtalkbanlist"]:
            wait["wtalkbanlist"] = False
            rahman(to,"「 Banning 」\n › Type: Tban Add♪ \n    • Status: Aborted")
            aborted = True                                    
        if wait["dtalkbanlist"]:
            wait["dtalkbanlist"] = False
            rahman(to,"「 Banning 」\n › Type: Tban Del♪ \n    • Status: Aborted")
            aborted = True
        if settings["updateProfile"]:
            settings["updateProfile"] = False
            settings["msgbroadcast"] = ""
            rahman(to,"「 Friend 」\n › Type: Rename♪ \n    • Status: Aborted")
            aborted = True                          
        if to in position['timebc']:
            position["timebc"].clear()    
            try:
                for x in position["bot"]:
                    del position[x]
            except:pass
            position["multibc"].clear()
            position["bot"].clear()    
            aborted = True        
        if settings['mltbc1']:
            settings['mltbc1'] = False
            try:
                for x in position["bot"]:
                    del position[x]
            except:pass
            position["timebc"].clear()
            position["multibc"].clear()
            position["bot"].clear()    
            rahman(to,"「 Broadcast 」\n › Type: Broadcast Multi♪ \n    • Status: Aborted")
            aborted = True        
        if settings['mltbc2']:
            settings['mltbc2'] = False
            try:
                for x in position["bot"]:
                    del position[x]
            except:pass
            position["timebc"].clear()
            position["multibc"].clear()
            position["bot"].clear() 
            rahman(to,"「 Broadcast 」\n › Type: Broadcast Multi♪ \n    • Status: Aborted")
            aborted = True        
        if settings['mltbc0']:
            settings['mltbc0'] = False
            try:
                for x in position["bot"]:
                    del position[x]
            except:pass
            position["timebc"].clear()
            position["multibc"].clear()
            position["bot"].clear() 
            rahman(to,"「 Broadcast 」\n › Type: Broadcast Multi♪ \n    • Status: Aborted")
            aborted = True                                                   
        if wait['inviteContact']:wait['inviteContact'] = False;rahman(to,"「 Setinvite 」\n › Type: Invite Contact♪ \n    • Status: Aborted");aborted = True                                        
        if settings['statjsbypass']:settings['statjsbypass'] = False;rahman(to,"「 Js 」\n › Type: Add Stickerbypass♪ \n    • Status: Aborted");aborted = True                                       
        if settings['statjskickall']:settings['statjskickall'] = False;rahman(to,"「 Js 」\n › Type: Add Stickerkickall♪ \n    • Status: Aborted");aborted = True                                             
        if settings['statjscancelall']:settings['statjscancelall'] = False;rahman(to,"「 Js 」\n › Type: Add Stickercancelall♪ \n    • Status: Aborted");aborted = True                                       
        if settings['stickermention']:settings['stickermention'] = False;rahman(to,"「 Autorespon 」\n › Type: Add Stickerrespontag♪ \n    • Status: Aborted");aborted = True                                               
        if settings['stickerchat']:settings['stickerchat'] = False;rahman(to,"「 Autorespon 」\n › Type: Add Stickerresponchat♪ \n    • Status: Aborted");aborted = True                                        
        if settings['stickeradd']:settings['stickeradd'] = False;rahman(to,"「 Autoadd 」\n › Type: Add Stickerautoadd♪ \n    • Status: Aborted");aborted = True                                      
        if settings['statstcautojoin']:settings['statstcautojoin'] = False;rahman(to,"「 Autojoin 」\n › Type: Add Stickerautojoin♪ \n    • Status: Aborted");aborted = True                                      
        if settings['autoLeave']['gc']["setstc"]:settings['autoLeave']['gc']["setstc"] = False;rahman(to,"「 Autoleave 」\n › Type: Add Stickerautoleave Gc♪ \n    • Status: Aborted");aborted = True                                      
        if settings['autoLeave']['mc']["setstc"]:settings['autoLeave']['mc']["setstc"] = False;rahman(to,"「 Autoleave 」\n › Type: Add Stickerautoleave Mc♪ \n    • Status: Aborted");aborted = True                        
        if settings['AutoComment']['setstccomment']:settings['AutoComment']['setstccomment'] = False;rahman(to,"「 Autocomment 」\n › Type: Add Stickercomment♪ \n    • Status: Aborted");aborted = True                                 
        if settings['greet']['stickergreetjoin']:settings['greet']['stickergreetjoin'] = False;rahman(to,"「 Greet 」\n › Type: Add Stickergreetjoin♪ \n    • Status: Aborted");aborted = True                                 
        if settings['greet']['stickergreetleave']:settings['greet']['stickergreetleave'] = False;rahman(to,"「 Greet 」\n › Type: Add Stickergreetleave♪ \n    • Status: Aborted");aborted = True                                      
        if settings['Addkibaran']['status']:settings['Addkibaran']['status'] = False;settings["Addkibaran"]["name"] = "";rahman(to,"「 List 」\n › Type: Kibaran Add♪ \n    • Status: Aborted");aborted = True                                            
        for k, v in position['squadteam'].items():            
            if v["statusconadd"]:
                position["squadteam"][k]["statusconadd"] = False
                rahman(to,"「 Squad 」\n › Type: Add♪ \n    • Status: Aborted")
                aborted = True                                      
            if v["statuscondel"]:
                position["squadteam"][k]["statuscondel"] = False
                rahman(to,"「 Squad 」\n › Type: Del♪ \n    • Status: Aborted")
                aborted = True  
            if v["statusstc"]:
                position["squadteam"][k]["statusstc"] = False
                rahman(to,"「 Squad 」\n › Type: Sticker♪ \n    • Status: Aborted")
                aborted = True 
        if not aborted:rahman(to,"「 Abort 」\n › Detail: Done/Cancel \n    • Status: Failed")                

def executeOp(op):
    try:
        print ('› Operation: %i %s' % (op.type, OpType._VALUES_TO_NAMES[op.type].replace('_', ' ')))
        if op.type in [5]:
            notif_add(op)
        if op.type in [11, 122]:
            notif_atribut(op)
        if op.type in [13, 124]:
            notif_join(op)
        if op.type in [22,24]:
            notif_leaveMC(op)                                          
        if op.type in [15,128]:
            notif_leaveGC(op)        
        if op.type in [16,129]:
            notif_kickJoin(op)        
        if op.type in [17,130]:
            notif_joinGC(op)
        if op.type in [19,133]:
            notif_kick(op)
        if op.type in [32,126]:
            notif_cancel(op) 
        if op.type in [55]:
            notif_read(op)   
        if op.type in [25,26]:
            notif_all(op)            
        if op.type in [25]: 
            notif_acount(op)                                    
        if op.type in [26]: 
            notif_public(op)   
        if op.type in [26]: 
            notif_saveunsend(op)   
        if op.type in [65]: 
            notif_unsend(op)         
    except TalkException as talk_error:
        logError(talk_error)
        if talk_error.code in [7, 8, 20]:
            sys.exit(1)
    except KeyboardInterrupt:
        sys.exit('##---- KEYBOARD INTERRUPT -----##')
    except Exception as error:
        logError(error)
lastcheckstory = 0
def story():
    global lastcheckstory
    try:
        recent = []
        if settings["AutoLike"]["story"] == True or settings['AutoComment']['story'] == True:
            if time.time() > lastcheckstory:recent = maxbots.getRecentStory();lastcheckstory= time.time() + 10                                
        if recent != []:
            likeType = [1001, 1002, 1003, 1004, 1005, 1006]
            if recent['message'] == 'success':
                if recent['result']['recentStories']:
                    for recentStory in recent['result']['recentStories']:
                        story = maxbots.getStory(recentStory['mid'])
                        for content in story['result']['contents']:
                            if not content['viewReaction']['reaction']['liked']:
                                if settings["AutoLike"]["story"] == True:
                                    maxbots.likeStory(content['contentId'], random.choice(likeType))
                                    time.sleep(0.2)
                            if settings['AutoComment']['story']:
                                if content['contentId'] not in position["storyId"]:
                                    maxbots.commentStory(recentStory['mid'], content['contentId'], settings['AutoComment']['msgstory'])
                                    position["storyId"].append(content['contentId'])
                                    time.sleep(0.2)
    except Exception as e:print(e)
def runningProgram():
    if settings['restartPoint'] is not None:
        try:
            maxbots.sendMessage(settings['restartPoint'], 'Done♪')
        except TalkException:
            pass
        settings['restartPoint'] = None
    while True:
        story()
        try:
            timeRESET()
            spamerunbloked()
            ops = maxbots.poll.fetchOps(oepoll.localRev, 15, oepoll.globalRev, oepoll.individualRev)
            for op in ops:
                if op.revision == -1 and op.param2 != None:
                    oepoll.globalRev = int(op.param2.split("\x1e")[0])
                if op.revision == -1 and op.param1 != None:
                   oepoll.individualRev = int(op.param1.split("\x1e")[0])
                oepoll.localRev = max(op.revision, oepoll.localRev)
                t1 = threading.Thread(target=executeOp(op,))
                t1.start()
                t1.join()
        except Exception as e:
            e = traceback.format_exc()
            if "EOFError" in e:pass
            elif "ShouldSyncException" in e or "LOG_OUT" in e:
                python3 = sys.executable
                os.execl(python3, python3, *sys.argv)
            else:
               traceback.print_exc()

if __name__ == '__main__':
    print ('##---- RUNNING PROGRAM -----##')
    runningProgram()