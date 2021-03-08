# AUTOGENERATED! DO NOT EDIT! File to edit: 00_api.ipynb (unless otherwise specified).

__all__ = ['parse_pdf', 'logger']

# Cell
import logging
from pathlib import Path
from typing import Optional, Dict, Any

import requests

logger = logging.getLogger(__name__)

def parse_pdf(server_address: str, file_path: Path, port: Optional[str], timeout: int = 60
              ) -> Optional[Dict[str, Any]]:
    '''
    This function if successful returns the JSON output of the
    science parse server as a dictionary. Else if a Timeout Exception
    or any other Exception occurs it will return None. If any of the
    exceptions do occur they will be logged as an error.

    1. **server_address**: Address of the server e.g. `http://127.0.0.1`
    2. **file_path**: Path to the pdf file to be processed.
    3. **port**: The port to the server e.g. 8080
    4. **timeout**: The amount of time to allow the request to take.

    **returns** A dictionary with the following keys:
    ```python
    ['abstractText', 'authors', 'id', 'references', 'sections', 'title', 'year']
    ```

    **Note** not all of these dictionary keys will always exist if science parse
    cannot detect the relevant information e.g. if it cannot find any references
    then there will be no reference key.

    **Note** See the example on the main page of the documentation for a
    detailed example of this method.
    '''

    endpoint = "/v1"
    if port:
        url = f'{server_address}:{port}{endpoint}'
    else:
        url = f'{server_address}{endpoint}'
    file_name = file_path.name
    files = {'data-binary': (file_name, file_path.open('rb'), 'application/pdf',
                             {'Expires': '0'})}
    try:
        response = requests.post(url, files=files,
                                 headers={'Accept': 'application/json'},
                                 timeout=timeout)
        status_code = response.status_code
        if status_code != 200:
            error_message = (f'URL: {url}. {file_name} failed with a '
                             f'status code: {status_code}')
            logger.error(error_message)
            return None
        return response.json()
    except requests.exceptions.Timeout:
        error_message = (f'URL: {url}. {file_name} failed due to a timeout.')
        logger.error(error_message)
    except Exception as e:
        error_message = f'URL: {url}. {file_name} failed due to the following error:'
        logger.error(error_message, exc_info=True)
    return None
