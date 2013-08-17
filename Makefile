MAKEFILES_DIR=makefiles
DB_FILE=db/vehicle_reg_prefix.db

db:
	> $(DB_FILE)
	sqlite3 $(DB_FILE) < $(MAKEFILES_DIR)/tables.sql
	python $(MAKEFILES_DIR)/counties.py $(DB_FILE)
	python $(MAKEFILES_DIR)/areas.py $(DB_FILE)
	python $(MAKEFILES_DIR)/prefixes.py $(DB_FILE)
	@echo "db made"

clean:
	find . -name '*.pyc' | xargs rm
