from click_battle.template_generation import generate_main_page


def test_main_page():
    main_page = generate_main_page(1, 2)
    expected = (
        "<!DOCTYPE html>\n"
        '<html lang="en">\n'
        "<head>\n"
        '    <meta charset="UTF-8">\n'
        "    <title>Click battle</title>\n"
        "</head>\n"
        "<body>\n"
        '<div class="content">\n'
        '    <div class="left_element">\n'
        '        <form action="/score_left" method="post">\n'
        "            <p>Left</p>\n"
        '            <input type="submit" value="Submit">\n'
        "        </form>\n"
        "    </div>\n"
        '    <div class="score">\n'
        "        <p>1:2</p>\n"
        "    </div>\n"
        '    <div class="right_element">\n'
        '        <form action="/score_right" method="post">\n'
        "            <p>Right</p>\n"
        '            <input type="submit" value="Submit">\n'
        "        </form>\n"
        "    </div>\n"
        "</div>\n"
        "</body>\n"
        "</html>"
    )

    assert main_page == expected
