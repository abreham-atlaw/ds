#include <string>

#include <httplib/httplib.h>

#include <lib/network/client.hpp>
#include <lib/network/response.hpp>

#include "models.hpp"
#include "requests.hpp"


#ifndef API_CLNT

#define API_CLNT
class api_client: public client{

	public:
	api_client(std::string api_url);

	command_request get_command();

	void submit_results(command_result result);


};
#endif
