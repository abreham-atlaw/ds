#include <string>

#ifndef CMD_EXTR

#define CMD_EXTR

class command_executor{

	public:
	command_executor();
	std::string execute(std::string command);

};

#endif