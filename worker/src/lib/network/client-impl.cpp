#include <string>
#include <iostream> //TODO REMOVE
#include <httplib/httplib.h>

#include "request.hpp"
#include "response.hpp"
#include "client.hpp"



client::client(std::string base_url): clt(base_url){
	this->base_url = base_url;
}

response client::call(request req){
	try{
		response rsp = to_response(
			httplib::Result(
				(req.get_method() == method::POST) ? this->post(req) : this->get(req)
			)
		);
		return rsp;
	}
	catch(const std::exception& ex){
		throw -1;
	}

}

httplib::Result client::get(request req){
	return clt.Get(req.get_url().c_str());
}

httplib::Result client::post(request req){
	return clt.Post(
		req.get_url().c_str(),
		req.get_params()
	);
}

response client::to_response(httplib::Result res){
	if(res.error() == httplib::Error::Success){
		return response(
			res->body,
			res->status
		);
	}
	return response("", -1);
}
