from observability_mtl_instrument.logs.builders.fullLogConfig import FullLogConfig
from dotenv import load_dotenv
import os

log_config = FullLogConfig(
    service_name="todo-app", loki_url=os.getenv("LOKI_URL")
).get_log_config()

logger = log_config.logger