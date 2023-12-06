NAME = its-right-here

build:
	docker build -f Dockerfile -t $(NAME) ..

run: build
	docker run -d -p 34522:22 --name $(NAME) $(NAME)

stop:
	docker stop $(NAME)

clean: stop
	docker rm $(NAME)

.PHONY: build run stop clean
