BLACK			=	"\033[0;30m"
RED				=	"\033[0;31m"
GREEN			=	"\033[0;32m"
YELLOW			=	"\033[0;33m"
CYAN			=	"\033[0;35m"
BLUE			=	"\033[0;34m"
WHITE			=	"\033[0;37m"
END				=	"\033[0;0m"
# Files

DIR				= $(shell echo $(PWD))
RM				= rm -rf


# Directories

NAME			= ./.portaudio
OUT				= pa.tgz
all : $(NAME)
	@echo $(RED)"Up to Date!"$(END)
$(NAME):
	@curl http://files.portaudio.com/archives/pa_stable_v190700_20210406.tgz -o $(OUT)
	@gunzip -c pa.tgz | tar xopf -
	@/bin/sh -c "cd portaudio && ./configure && make && sudo make install && export LD_LIBRARY_PATH=/usr/local/lib"
	@rm -rf $(OUT)
	@mkdir $(NAME)
	@clear
	@$(shell /usr/local/bin/pip install -r requirements.txt)

clean : 
	@echo $(RED)">- Deleting portaudio..." $(END)
	@$(RM) ./portaudio $(NAME) $(OUT)
	@echo $(BLUE)">- Successfully! [$(NAME)]" $(END)

re : clean all

.PHONY: all  clean re
