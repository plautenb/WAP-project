import pytest
from pages.twitch_page import TwitchPage
from fixtures.fixtures import driver

class TestsStreamers:

    @pytest.mark.parametrize("game_name", ["StarCraft II", "Leauge of Legends"],
                             ids=["StarCraft II", "Leauge of Legends"])
    def test_open_game_streamer(self, driver, game_name):
        twitch_page = TwitchPage(driver=driver)
        twitch_page.search_game(game_name=game_name)
        twitch_page.switch_to_channels_tab()
        twitch_page.perform_scroll(times=2)
        twitch_page.select_streamer_first_available_streamer(game_name=game_name)
