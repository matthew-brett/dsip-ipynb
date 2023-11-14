BUILD_DIR=_build/html

html:
	jupyter-book build -W .

github: html
	ghp-import -n _build/html -p -f

clean:
	rm -rf _build

rm-ipynb:
	rm -rf */*.ipynb
