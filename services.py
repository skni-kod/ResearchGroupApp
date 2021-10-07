import abc
import dataclasses

from kivy.network.urlrequest import UrlRequest


class BaseService(abc.ABC):
    BASE_URL = "https://kod.prz.edu.pl/backend/api"

    def get(self, endpoint_path, on_success=None, on_redirect=None, on_failure=None, on_error=None,
                 on_progress=None):
        return UrlRequest(self.BASE_URL + endpoint_path, on_success, on_redirect, on_failure, on_error,
                 on_progress, verify=False)


class ArticleService(BaseService):
    def get_articles(self, on_success=None, on_redirect=None, on_failure=None, on_error=None,
                 on_progress=None):
        return self.get("/articles/", on_success, on_redirect, on_failure, on_error,
                 on_progress)

    def get_article(self, article_id, on_success=None, on_redirect=None, on_failure=None, on_error=None,
                 on_progress=None):
        return self.get("/articles/%d/" % article_id, on_success, on_redirect, on_failure, on_error,
                 on_progress)


class ProjectsService(BaseService):
    def get_projects(self, on_success=None, on_redirect=None, on_failure=None, on_error=None,
                 on_progress=None):
        return self.get("/projects/", on_success, on_redirect, on_failure, on_error,
                 on_progress)

    def get_project(self, project_id, on_success=None, on_redirect=None, on_failure=None, on_error=None,
                 on_progress=None):
        return self.get("/projects/%d/" % project_id, on_success, on_redirect, on_failure, on_error,
                 on_progress)