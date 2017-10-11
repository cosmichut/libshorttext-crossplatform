
all: code 

code: stemmer learner

stemmer:
	make -C libshorttext/converter/stemmer

learner:
	make -C libshorttext/classifier/learner

clean:
	rm -rf *.svm *.converter *.model *.config *.out *.pyc
	make -C doc clean
