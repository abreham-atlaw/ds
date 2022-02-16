#include <string>

#include <httplib/httplib.h>

#include <lib/network/request.hpp>
#include "models.hpp"


#ifndef RQSTS

#define RQSTS
class get_command_request : public request{

	public:
	get_command_request(): request("/requests/", method::GET){

	}

};


class submit_results_request : public request{

	public:
	submit_results_request(command_result result): request("/requests/", method::POST){
		this->set_params(
			this->setup_params(result)
		);
	}


	private:
	httplib::Params setup_params(command_result result){

		httplib::Params params;
		params.emplace("id", result.id);
		params.emplace("value", result.value);
		
		return params;
	}


};
#endif
