from sqlalchemy.exc import IntegrityError
import pytest

from lti.models import ApplicationInstance


class TestApplicationInstance(object):
    def test_it_persists_application_instance(self,
        db_session):
      db_session.add(
        ApplicationInstance(
          consumer_key="TEST_CONSUMER_KEY",
          shared_secret="TEST_SHARED_SECRET",
          lms_url="TEST_LMS_URL",
        )
      )

      persisted = db_session.query(ApplicationInstance).one()

      assert persisted.consumer_key == "TEST_CONSUMER_KEY"
      assert persisted.shared_secret == "TEST_SHARED_SECRET"
      assert persisted.lms_url == "TEST_LMS_URL"


