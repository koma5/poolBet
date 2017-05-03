var https = require('https');
var util = require('util');

var options = {
  hostname : 'blockchain.info',
  port: 443,
  method: 'GET',
  path: '/en/latestblock',
};

var req = https.request(options, function(res) {
  var body = '';
  //console.log(res.statusCode);

  res.on('data', function(chunk) {
    body += chunk;
  })

  res.on('end', function(){
    var latestBlock = JSON.parse(body)

    var date = new Date(latestBlock.time*1000)

    console.log(util.format("index:\t%s\nheight:\t%s\ntime:\t%s",
    latestBlock.block_index,
    latestBlock.height,
    date));
    })

});

req.end()
