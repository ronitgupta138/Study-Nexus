.PHONY: help install test demo clean

help:
	@echo "Study-Nexus - Autonomous CS Socratic Study Room on Switch"
	@echo "Commands:"
	@echo "  make install - Install required dependencies"
	@echo "  make test    - Run automated active recall & note archival test"
	@echo "  make demo    - Run interactive rich terminal study simulation"

install:
	pip install -r requirements.txt

test:
	python3 test_nexus_flow.py

demo:
	python3 demo_simulation.py

clean:
	rm -rf __pycache__ .pytest_cache notes/*.md
