#include <string>
#include <json/json.hpp>


#ifndef RSPNS

#define RSPNS

class response{

	public:

	response(std::string body, int status){
		this->body = body;
		this->status = status;
	}

	nlohmann::json json(){
		return nlohmann::json::parse(this->body);
	}

	std::string get_body(){
		return this->body;
	}

	int get_status(){
		return this->status;
	}

	bool is_successfull(){
		return (this->status >= 200 && this->status < 300);
	}

	private:
	std::string body;
	int status;


};
#endif
