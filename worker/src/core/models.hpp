#include <string>


#ifndef MDLS

#define MDLS
class command_request{

	public:
	std::string id;
	std::string command;
	
	command_request(std::string id, std::string command){
		this->id = id;
		this->command = command;
	}

};


class command_result{

	public:
	std::string id;
	std::string value;

	command_result(std::string id, std::string value){
		this->id = id;
		this->value = value;
	}

};

#endif