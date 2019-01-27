from utils import get_response
from requests.exceptions import RequestException


class BaseHelper(object):

    @staticmethod
    def get_site_status(url):
        try:
            response = get_response(url)
            return {"code": response.status_code}
        except RequestException:
            return {"code": None}
