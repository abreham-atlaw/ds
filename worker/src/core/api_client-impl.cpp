#include <string>
#include <json/json.hpp>


#include <lib/network/response.hpp>

#include "api_client.hpp"
#include "models.hpp"
#include "requests.hpp"


api_client::api_client(std::string api_url): client(api_url){

}

command_request api_client::get_command(){
	response res = this->call(
		get_command_request()
	);

	if(!res.is_successfull())
		throw -1;

	nlohmann::json jsn = res.json();
	return command_request(
		jsn["id"].get<std::string>(),
		jsn["command"].get<std::string>()
	);


}

void api_client::submit_results(command_result result){

	response res = this->call(
		submit_results_request(result)
	);

	if(!res.is_successfull())
		throw -1;

}
