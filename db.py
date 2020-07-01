# https://github.com/jpsca/sqla-wrapper/blob/master/tests/conftest.py
import sys

sys.path.append("C:/Users/dustinchu/Desktop/mysql/sqlWrapper/")


from sqlWrapper.main import SQLAlchemy

db=SQLAlchemy("mysql+pymysql://root:xS346@Dc01@127.0.0.1:3306/goodboydb",encoding='utf-8', echo=False)


# import pytest

# from sqla_wrapper import SQLAlchemy


# @pytest.fixture(scope="session")
# def uri1():
#     return "sqlite://"


# @pytest.fixture(scope="session")
# def uri2():
#     return "sqlite://"


# @pytest.fixture
# def db(uri1):
# return SQLAlchemy(uri1)