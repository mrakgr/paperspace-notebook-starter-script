from gradient import NotebooksClient, ResourceFetchingError
from multiprocessing import Lock, Process
from datetime import datetime
from plyer import notification

def start_machine(lock,machine_type,id,api_key):
    notebooks_client = NotebooksClient(api_key)
    n = datetime.now()
    while True:
        try:
            notebooks_client.start(id=id,machine_type=machine_type,shutdown_timeout=6)
            msg = f'{id} - The {machine_type} machine has been acquired for Paperspace Gradient Notebook.'
            with lock: 
                print(f"The time it took to complete the request is {datetime.now() - n}")
                print(msg)
            notification.notify('Paperspace Gradient Notebook Script', msg)
            return
        except ResourceFetchingError as e:
            if str(e).find('out of capacity') != -1:
                with lock: print(f"{id} - {machine_type}: {e}")
            else:
                with lock: print(f"Aborting {id} - {machine_type}: {e}")
                return
        
        
if __name__ == "__main__":
    lock = Lock()
    api_key = "" # The API key of your Paperspace account.
    machine_types = ['Free-A4000','Free-RTX5000']
    id = '' # The id of the Gradient notebook.
    for machine_type in machine_types:
        Process(target=start_machine,args=(lock,machine_type,id,api_key)).start()