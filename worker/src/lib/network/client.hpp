#include <string>

#include <httplib/httplib.h>

#include "request.hpp"
#include "response.hpp"


#ifndef CLNT

#define CLNT
class client{

	public:

	client(std::string base_url);

	response call(request req);

	private:
	std::string base_url;
	httplib::Client clt;

	httplib::Result get(request req);

	httplib::Result post(request req);

	response to_response(httplib::Result res);

};
#endif
