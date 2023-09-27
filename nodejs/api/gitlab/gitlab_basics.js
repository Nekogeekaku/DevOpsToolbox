var router = require('express').Router();

var axios = require('axios');
var secrets = require('../../config/secrets');
var https = require('https')

router.get('/',function(req,res,next){
    return res.json({message:'Success'});
});
router.get('/listprojectsingroup',function(req,res,next){
axios({
    method:'get',
    headers:{'PRIVATE-TOKEN':secrets.gitlabapitoken},
    url:secrets.gitlab_base_url+'/api/v4/namespaces/'+secrets.Group_ID,
    httpsAgent: new https.Agent({rejectUnauthorized:false})
}).then(function(response){
    return res.json({message:response.data});
})
});


module.exports = router;
