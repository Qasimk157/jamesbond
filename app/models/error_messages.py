from enum import Enum


class ErrorMessages(Enum):
    
    server_error = "Internal Server Error."
    connection_error = "Data API connection not established."
    server_busy_error = "Server is too busy at the moment, please retry in 15 minutes."
    rbac_connection_error = "API connection not established."
    record_not_found = "Record not found."
 