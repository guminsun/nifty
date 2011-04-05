.PHONY: all
all: setup clean

.PHONY:	clean
clean:
	rm -rf bin/*

.PHONY: setup
setup:
	mkdir -p bin
