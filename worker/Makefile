CC		:= g++
C_FLAGS := -std=c++17 -Wall -Wextra

BIN		:= bin
SRC		:= src
INCLUDE	:= include -Isrc
LIB_DIR := lib
LIB		:= -lwsock32 -lWs2_32

LIBRARIES	:= src/lib/command_executor/*.cpp src/lib/network/*.cpp src/core/*.cpp

ifeq ($(OS),Windows_NT)
EXECUTABLE	:= main.exe
else
EXECUTABLE	:= main
endif

all: $(BIN)/$(EXECUTABLE)

clean:
	$(RM) $(BIN)/$(EXECUTABLE)

run: all
	./$(BIN)/$(EXECUTABLE)

$(BIN)/$(EXECUTABLE): $(SRC)/**.cpp
	$(CC) $(C_FLAGS) -I$(INCLUDE) $^ -o $@ $(LIBRARIES) $(LIB)