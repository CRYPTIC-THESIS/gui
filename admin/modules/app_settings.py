
class MainSettings():
    # APP SETTINGS
    # ///////////////////////////////////////////////////////////////
    ENABLE_CUSTOM_TITLE_BAR = True
    MENU_WIDTH = 240
    LEFT_BOX_WIDTH = 240
    RIGHT_BOX_WIDTH = 240
    TIME_ANIMATION = 500

    # BTNS LEFT AND RIGHT BOX COLORS
    BTN_LEFT_BOX_COLOR = "background-color: rgb(44, 49, 58);"
    BTN_RIGHT_BOX_COLOR = "background-color: #ff79c6;"

    # MENU SELECTED STYLESHEET
    MENU_SELECTED_STYLESHEET = """
    border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 #2AB7CA, stop:0.5 rgba(85, 170, 255, 0));
    background-color: rgb(40, 44, 52);
    """

    # CRYPTO SELECTED STYLESHEET
    CRYPTO_SELECTED_STYLESHEET = """
    background-color: transparent;
    width: 43px;
    height: 43px;
    border: 5px solid;
    border-color: #2AB7CA;
    """

    PRICE_SELECTED_STYLESHEET = """
    background: 'white';
	border-color: 'white';
    """

    CURRPRICE_SELECTED_STYLESHEET = """
    background: #21252B;
    border-radius: 10px;
    color: #2AB7CA;
    """

    HISTODAY_SELECTED_STYLESHEET = """
    background: #8C88BF;
    """

class LoginSettings():
    # APP SETTINGS
    # ///////////////////////////////////////////////////////////////
    ENABLE_CUSTOM_TITLE_BAR = True
    MENU_WIDTH = 240
    LEFT_BOX_WIDTH = 240
    RIGHT_BOX_WIDTH = 240
    TIME_ANIMATION = 500