#include <string>

#include <httplib/httplib.h>


#ifndef RQST

#define RQST
enum method{
	GET=1, POST=2
};

class request{

	public:

	request(std::string url){
		this->url = url;
	}

	request(std::string url, method mthd){
		this->url = url;
		this->mthd = mthd;
	}

	void set_method(method mthd){
		this->mthd = mthd;
	}

	void set_params(httplib::Params params){
		this->params = params;
	}

	std::string get_url(){
		return this->url;
	}

	method get_method(){
		return this->mthd;
	}

	httplib::Params get_params(){
		return this->params;
	}



	private:
	
	std::string url;
	httplib::Params params;
	method mthd;


	

};
#endif
