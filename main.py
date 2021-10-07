import asyncio

import kivy
from kivy import Logger
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.screen import MDScreen

import services

kivy.require('2.0.0')
Builder.load_file("widgets/MainScreen.kv")
Builder.load_file("widgets/ArticleListScreen.kv")


class ArticleListItem(TwoLineListItem):
    def __init__(self, **kwargs):
        self.article_id = kwargs.pop("article_id", None)
        super().__init__(**kwargs)


class ArticleListScreen(MDScreen):
    def on_enter(self, *args):
        self.ids.loading_spinner.active = True
        self.ids.article_list.active = False
        article_serivce = services.ArticleService()
        req = article_serivce.get_articles(on_success=self.on_fetch_success, on_failure=self.on_fetch_failed, on_error=self.on_fetch_error)

    def on_fetch_success(self, request, result):
        if type(result) is list:
            self.ids.article_list.clear_widgets()
            for article in result:
                self.ids.article_list.add_widget(ArticleListItem(article_id=article['id'], text=article['title'], secondary_text=article['text'].split("---readmore---")[0]))
        self.ids.loading_spinner.active = False
        self.ids.article_list.active = True

    def on_fetch_failed(self, request, result):
        print("FAILED")
        print(request)
        print(result)

    def on_fetch_error(self, request, result):
        print("ERROR")
        print(request)
        print(result)


class ArticleDetailScreen(MDScreen):
    article_id = NumericProperty(0)

    def on_enter(self, *args):
        article_serivce = services.ArticleService()
        print(self.article_id)
        req = article_serivce.get_article(article_id=self.article_id, on_success=self.on_fetch_success, on_failure=self.on_fetch_failed,
                                           on_error=self.on_fetch_error)

    def on_fetch_success(self, request, result):
        print(result)

    def on_fetch_failed(self, request, result):
        print("FAILED")
        print(request)
        print(result)

    def on_fetch_error(self, request, result):
        print("ERROR")
        print(request)
        print(result)


class SectionScreen(MDScreen):
    pass


class ProjectListScreen(MDScreen):
    pass


class ProjectDetailScreen(MDScreen):
    pass


class PartnerList(MDScreen):
    pass

    def on_fetch_error(self, request, result):
        print("ERROR")
        print(request)
        print(result)

class MainScreen(MDScreen):
    pass


class MainApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(ArticleListScreen(name='article_list'))
        sm.add_widget(ArticleDetailScreen(name='article_detail'))
        return sm


mainApp = MainApp()
loop = asyncio.get_event_loop()
loop.run_until_complete(
    mainApp.async_run(async_lib='asyncio'))
loop.close()
