#include<string>
#include<stdio.h>

#include "command_executor.hpp"


command_executor::command_executor(){
	
}

std::string command_executor::execute(std::string command){
	std::string result = "";
	FILE *pipe = popen(command.append(" 2>&1").c_str(), "r");

	if(pipe == NULL)
		throw -1;
	
	int ch;
	while((ch=fgetc(pipe)) != EOF)
		result += ch;
	
	
	return result;

}