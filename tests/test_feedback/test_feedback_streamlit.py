import pytest

from trubrics.integrations.streamlit import FeedbackCollector


def test_feedback_collector_raises():
    with pytest.raises(ValueError):
        FeedbackCollector(trubrics_platform_auth="something")


def test_st_auth_raises():
    collector = FeedbackCollector()
    with pytest.raises(ValueError):
        collector.st_trubrics_auth()


@pytest.mark.parametrize(
    "kwargs",
    [
        ({"feedback_type": "custom"}),
        ({"feedback_type": "random"}),
        ({"feedback_type": "issue", "user_response": {"test": "test"}}),
        ({"feedback_type": "issue", "open_feedback_label": "test"}),
        ({"feedback_type": "faces", "user_response": "desc"}),
        ({"feedback_type": "thumbs", "user_response": "desc"}),
    ],
)
def test_st_feedback_raises(kwargs):
    collector = FeedbackCollector()
    with pytest.raises(ValueError):
        collector.st_feedback(**kwargs)
