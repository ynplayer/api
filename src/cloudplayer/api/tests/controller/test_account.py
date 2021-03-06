import pytest

from cloudplayer.api.controller.account import AccountController


@pytest.mark.gen_test
def test_controller_should_redirect_alias_to_current_user(db, current_user):
    controller = AccountController(db, current_user)
    account = yield controller.read({'id': 'me', 'provider_id': 'cloudplayer'})
    assert account.id == current_user['cloudplayer']
