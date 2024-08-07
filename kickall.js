const thrift = require('thrift-http');
const LineService = require('./LibJS/NewTalkService');
//const Cryptr = require('cryptr');
//const vm = require('vm');
const {Message,DeleteOtherFromChatRequest,GetChatsRequest,AcceptChatInvitationByTicketRequest,CancelChatInvitationRequest,FindChatByTicketRequest} = require('./LibJS/NewTalkService_types');
//cryptr = new Cryptr("Kyuza");
var _client = '';
var gid = '';
var type = '';
var kick = [];
var cancel = [];
var token = ''; 
var app = '';
var apps = '';
var ua = '';
var helper = '';
var ticket = '';
var promiseArray = [];

process.argv.forEach(function (val) {
  if(val.includes('gid=')){
    gid = val.split('gid=').pop();
  }else if(val.includes('type=')){
	  type = val.split('type=').pop(); 
  }else if(val.includes('token=')){
	  token = val.split('token=').pop();
  }else if(val.includes('helper=')){
	  helper = val.split('helper=').pop();
  } else if(val.includes('app=')) {
    apps = val.split('app=').pop();
  } else if(val.includes("uid=")) {
    kick.push(val.split("uid=").pop());
  } else if(val.includes('uik=')) {
    cancel.push(val.split("uik=").pop());
  } else if(val.includes('ticket=')) {
    ticket = val.split("ticket=").pop();
  }
});

if(helper == "yes") {
  app = "ANDROIDLITE\t2.16.0\tAndroid\t11";
  ua="Line/2.16.0"
}

if (apps.toLowerCase() == "chrome") {
  app = "CHROMEOS\t2.4.1\tChrome OS\t1";
  ua = "Line/2.4.1"
} else if (apps.toLowerCase() == "desktopwin") {
  app = "DESKTOPWIN\t6.7.1\tWindows\t10";
  ua = "Line/6.7.1";
}

function setTHttpClient(options) {
    var connection =
      thrift.createHttpConnection('legy-jp.line.naver.jp', 443, options);
    connection.on('error', (err) => {
      console.log('err',err);
      return err;
    });
    _client = thrift.createHttpClient(LineService, connection);
  }
  
  
setTHttpClient(options={
    protocol: thrift.TCompactProtocol,
    transport: thrift.TBufferedTransport,
    headers: {'User-Agent':ua,'X-Line-Application':app,'X-Line-Access':token},
    path: '/S4',
    https: true
    });

let sandbox = {
  Message,
  _client,
}

//var text = `4c00634e1bc6ea46ff6c7747830300fb9bb0221956d73febea4ff260ca4bb2357b159f9a4b6ba18798ed62e0d67ad7ba90ef70d321e0940a9e60f584d1252e1c932c3b2b8a87c5705781f533181b3ab36ccd1a7822a11a547305ca52abd34f1271e2c68517346be5c1974e9d278b390d34563ca722ed86218c26c9aaf99f3c29399f2d0fbab9c5c4dcf5eda0a5b705d00ceb6308d3ab38a7343a1d9f615420bed6a975e70c72d444652cb323c9ca3bb82a97ba88c96d18e15aa6eedc220edb79ffc42295db78f772e906b3dc928bb86678033230f3e9abcb040bbb11cf2bb9b4eab55fa3af123cfb61c4ae84d05e1c760e1af2e662c51c0566744c3a85df9baa201af80c39220bf71c9a2b7632a050c3c15c33485d0a75f152ac40faa641f28eed91eb670fe1b88b77dfb26913998315b4881be767f397e3cb377ae96fd469bfa1715adb8f934421c4bfab9a4430ef6647e0b13b2060151352806f4e189046c0b948c3ad061fc9acc687a421e2e283b668f13a09902b680f2aceddc40319491ba5807daf4dd5d15cb2d849c67897170244b9b0f0de645c7e277f5c6afeeaca4433b8e68bca60022a32fdad985a03bad1deaaf1a156bcf1b847e640c2b60e654eae47131236dab491f0`
//var decs = cryptr.decrypt(text)
//vm.runInNewContext(decs,sandbox);


async function findChatByTicket(ticketId) {
  var req = new FindChatByTicketRequest();
  req.ticketId = ticketId;
  return await _client.findChatByTicket(req)
}

async function acceptChatInvitationByTicket(ticketId,groupId) {
  var res = new AcceptChatInvitationByTicketRequest();
  res.reqSeq = 0;
  res.chatMid = groupId;
  res.ticketId = ticketId;
  var result = await _client.acceptChatInvitationByTicket(res);
  return result;
}

async function getChats(groupId) {
  var req = new GetChatsRequest();
  req.chatMids = [groupId];
  req.withMembers = true;
  req.withInvitees = true;
  var result = await _client.getChats(req);
  return result;
}

// async function getGroupTicket(){
//   var req = new GetChatsRequest();
//   req.chatMids = [gid];
//   req.withMembers = true;
//   req.withInvitees = true;
//   var result = _client.getChats(req);
//   for (var res in result.chats[0].extra.groupExtra.memberMids) {
//     kick.push(res)
//   }
//   for (var ress in result.chat[0].extra.groupExtra.inviteeMids) {
//     cancel.push(ress);
//   }
// }

if(ticket != "") {
  findChatByTicket(ticket).then(val=>{
    gid = val.chat.chatMid
    acceptChatInvitationByTicket(ticket,val.chat.chatMid).then(res=>{
      console.log(`Success join group ${val.chat.chatName}`);
      getChats(gid).then(val=>{
        for (var res in val.chats[0].extra.groupExtra.memberMids) {
          if (res != "ub04637c2c85095ab5e2f5ed3756223c9") {
            kick.push(res);
          }
        }
        for (var ress in val.chats[0].extra.groupExtra.inviteeMids) {
          if (res != "ub04637c2c85095ab5e2f5ed3756223c9") {
            cancel.push(ress);
          }
        }
        if (type == "kick") {
          for (var i in kick) {
            var data = new DeleteOtherFromChatRequest()
            data.reqSeq = 0
            data.chatMid = gid
            data.targetUserMids = [kick[i]]
            _client.deleteOtherFromChat(data)
          }
          console.log("SUCCESS KICKALL")
        } else if (type == "cancel") {
          for(var i in cancel) {
            var data = new CancelChatInvitationRequest()
            data.reqSeq = 0
            data.chatMid = gid
            data.targetUserMids = [cancel[i]]
            _client.cancelChatInvitation(data)
          }
          console.log("SUCCESS CANCELALL")
        } else if (type == "dual") {
          for(var i in cancel) {
            var data = new CancelChatInvitationRequest()
            data.reqSeq = 0
            data.chatMid = gid
            data.targetUserMids = [cancel[i]]
            _client.cancelChatInvitation(data)
          }
          for(var i in kick) {
            var data = new DeleteOtherFromChatRequest()
            data.reqSeq = 0
            data.chatMid = gid
            data.targetUserMids = [kick[i]]
            _client.deleteOtherFromChat(data)
          }
        }
      })
    })
  })
} else {
  if (type == "kick") {
    for(var i in kick) {
      var data = new DeleteOtherFromChatRequest()
      data.reqSeq = 0
      data.chatMid = gid
      data.targetUserMids = [kick[i]]
      _client.deleteOtherFromChat(data)
    }
    console.log("SUCCESS KICKALL")
  } else if (type == "cancel") {
    for(var i in cancel) {
      var data = new CancelChatInvitationRequest()
      data.reqSeq = 0
      data.chatMid = gid
      data.targetUserMids = [cancel[i]]
      _client.cancelChatInvitation(data)
    }
    console.log("SUCCESS CANCELALL")
  } else if (type == "dual") {
    for(var i in kick) {
      var data = new DeleteOtherFromChatRequest()
      data.reqSeq = 0
      data.chatMid = gid
      data.targetUserMids = [kick[i]]
      _client.deleteOtherFromChat(data)
    }
    for(var i in cancel) {
      var data = new CancelChatInvitationRequest()
      data.reqSeq = 0
      data.chatMid = gid
      data.targetUserMids = [cancel[i]]
      _client.cancelChatInvitation(data)
    }
    console.log("SUCCESS BYPASS")
  }
}