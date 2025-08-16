from pl.lex import (
    Asterisk,
    Character,
    GenericLexer,
    LeftParenthesis,
    Pipe,
    Plus,
    RightParenthesis,
    Source,
    Token,
    Question,
)
from pl.langs import Xml


def test_0():
    token_types: list[type[Token]] = [
        Asterisk,
        Character,
        LeftParenthesis,
        Pipe,
        Plus,
        RightParenthesis,
        Question,
    ]
    test_str: str = "a*b+(c|d)?"
    test_result: list[Token] = GenericLexer(token_types).lex(Source(test_str))
    expected_lexemes: list[str] = ["a", "*", "b", "+", "(", "c", "|", "d", ")", "?"]

    print(test_result)
    for token, expected_lexeme in zip(test_result, expected_lexemes):
        assert token.lexeme == expected_lexeme


def test_1():
    test_str: str = """
    <?xml version="1.0" encoding="UTF-8"?>
        <!-- Sample XML for lexer testing -->
        <note>
            <to>Tove</to>
            <from>Jani</from>
            <heading reminder="true">Reminder</heading>
            <body>
                Don't forget me this weekend!
                <![CDATA[Some <unescaped> content]]>
            </body>
            <empty-tag attr="value" />
    </note>
    """
    test_result: list[Token] = Xml.Lexer().lex(Source(test_str))
    expected_lexemes: list[str] = [
        "<?xml",
        "version",
        "=",
        '"1.0"',
        "encoding",
        "=",
        '"UTF-8"',
        "?>",
        "<!-- Sample XML for lexer testing -->",
        "<",
        "note",
        ">",
        "<",
        "to",
        ">",
        "Tove",
        "</",
        "to",
        ">",
        "<",
        "from",
        ">",
        "Jani",
        "</",
        "from",
        ">",
        "<",
        "heading",
        "reminder",
        "=",
        '"true"',
        ">",
        "Reminder",
        "</",
        "heading",
        ">",
        "<",
        "body",
        ">",
        "Don't forget me this weekend!",
        "<![CDATA[Some <unescaped> content]]>",
        "</",
        "body",
        ">",
        "<",
        "empty-tag",
        "attr",
        "=",
        '"value"',
        "/>",
        "</",
        "note",
        ">",
    ]

    print(test_result)
    for token, expected_lexeme in zip(test_result, expected_lexemes):
        assert (
            token.lexeme == expected_lexeme
        ), f"expecting lexeme '{expected_lexeme}', got: {token}"
