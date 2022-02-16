#include "core/api_client.hpp"
#include <lib/command_executor/command_executor.hpp>


#ifndef MN_APP

#define MN_APP
class main_application{

	public:

	main_application();
	void start();

	private:
	api_client client;
	command_executor executor;

	void fetch_and_execute_command();
	void loop();
};
#endif
