NAME_ORIGINAL = 106bombyx.py

NAME_COPY = 106bombyx

all :   $(NAME_COPY)

$(NAME_COPY):
	cp -f $(NAME_ORIGINAL) $(NAME_COPY)
	chmod +x $(NAME_COPY)

clean :
	rm -f $(NAME_COPY)

fclean :    clean
	rm -f $(NAME_COPY)

re: fclean all
