const {errorResponse}=require('./response')
class CustError extends Error
{
    constructor(statusCode,message){
        super(message);
        this.statusCode=statusCode
    }
    
};

 const errorHandler=(err,req,res,next)=>
{
    let response="";
    if(err instanceof CustError){
        response=errorResponse(err);
    }
    res.send(response);
}
module.exports={CustError,errorHandler};