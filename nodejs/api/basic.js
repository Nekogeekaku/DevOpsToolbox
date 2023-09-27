var router = require('express').Router();




router.get('/',function(req,res,next){
    return res.json({message:'Success'});
});


module.exports = router;
