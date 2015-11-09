
import logging
import logging.handlers

# Non Rotating
formatter = logging.Formatter("[%(asctime)s] %(levelname)-5s [%(name)s] [%(filename)s:%(lineno)d:%(funcName)s] %(message)s")
log_file = "/tmp/deqin_data.log"
log_fh = logging.FileHandler(log_file)
log_fh.setFormatter(formatter)

flog = logging.getLogger("deqin_data");
flog.setLevel(logging.INFO)
flog.addHandler(log_fh)
