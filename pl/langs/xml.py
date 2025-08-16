from ..lex import (
    Lexer as AbstractLexer,
    Token,
    Equals,
    Identifier,
    Source,
)


class Xml:
    OpenXmlDeclaration: type[Token] = Token.define("Open Xml Declaration", r"<\?xml")
    CloseXmlDeclaration: type[Token] = Token.define("Close Xml Declaration", r"\?>")
    String: type[Token] = Token.define(
        "String",
        "|".join(
            [
                r"'[^']*'",
                r'"[^"]*"',
            ]
        ),
    )
    TagName: type[Token] = Token.define("Tag Name", r"[A-Za-z0-9][A-Za-z0-9_.-]*")
    Comment: type[Token] = Token.define("Comment", r"<!--.*-->")
    Cdata: type[Token] = Token.define("CDATA", r"<!\[CDATA\[[^\]]*\]\]>")
    OpenTag: type[Token] = Token.define("Open Tag", r"<")
    OpenSelfClosingTag: type[Token] = Token.define("Open Self-closing Tag", r"</")
    CloseOpeningTag: type[Token] = Token.define("Close Opening Tag", r">")
    CloseClosingTag: type[Token] = Token.define("Close Closing Tag", r"/>")
    Text: type[Token] = Token.define(
        "Text",
        r"[!\"#$%&'()*+,\-./0-9:;=>?@A-Z\[\\\]^_`a-z{|}~]"
        r"[ !\"#$%&'()*+,\-./0-9:;=>?@A-Z\[\\\]^_`a-z{|}~]*"
        r"[^ \t<]",
    )

    token_types_excluding_text: list[type[Token]] = [
        OpenXmlDeclaration,
        CloseXmlDeclaration,
        TagName,
        Identifier,
        Equals,
        String,
        Comment,
        Cdata,
        OpenTag,
        OpenSelfClosingTag,
        CloseOpeningTag,
        CloseClosingTag,
    ]
    token_types: list[type[Token]] = token_types_excluding_text + [Text]

    class Lexer(AbstractLexer):
        def __init__(self):
            class Instance(AbstractLexer.Instance):
                def __init__(self, src: Source):
                    super().__init__(src)

                def lex(self) -> list[Token]:
                    result: list[Token] = []
                    self.skip_whitespace()
                    while self.src[self.pos] != "eof":
                        if result:
                            print(result[-1])
                        if result and result[-1].token_type() == "Close Opening Tag":
                            result.append(self.parse_token(Xml.token_types))
                        else:
                            result.append(
                                self.parse_token(Xml.token_types_excluding_text)
                            )
                    return result

            self.Instance: type[AbstractLexer.Instance] = Instance
