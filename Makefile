ispell:
	hunspell -d en_GB,en_US -H -p words $$(find -name '*.md')

