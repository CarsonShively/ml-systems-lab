.PHONY: lock auto-ai front-end back-end

VENV := .venv
PY := $(VENV)/bin/python
UV := $(VENV)/bin/uv
SL := $(VENV)/bin/streamlit
STAMP := $(VENV)/installed
UVI := $(VENV)/bin/uvicorn

$(PY):
	python3 -m venv $(VENV) 

$(UV): $(PY)
	$(PY) -m pip install uv

$(STAMP): uv.lock $(UV)
	$(UV) sync
	touch $(STAMP)

lock: $(UV)
	$(UV) lock

front-end: $(STAMP)
	$(SL) run auto_ai.py

back-end: $(STAMP)
	$(UVI) api:api --reload

