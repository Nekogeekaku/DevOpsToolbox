var express = require('express')
var bodyParser = require('body-parser');
var ejs= require('ejs');
var engine = require('ejs-mate');


var app = express()




app.use( bodyParser.json() );       // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
 extended: true
}));
// ---------------------- Middlewares
app.use(express.static(__dirname+'/public'));
app.use( bodyParser.json() );       // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
 extended: true
}));



// ---------------------- Engine
app.engine('ejs', engine);
app.set('view engine', 'ejs');
// ---------------------- Routes
var basic = require('./api/basic');
app.use('/basic',basic);
var gilab_basic = require('./api/gitlab/gitlab_basics');
app.use('/gitlab',gilab_basic);


app.get('/', function (req, res) {
    res.send('Hello World')
  })
  


app.set('port', process.env.PORT ||3000);
app.listen(app.get('port'), function(err){
 if (err) throw err;
 console.log("Server is running on port "+app.get('port')+".");
});
