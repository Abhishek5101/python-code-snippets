def html(tag):

    def wrap_text(msg):
        print(' <{0}> {1} <{0}>'.format(tag, msg))

    return wrap_text


var = html('h1')         # var = log_message
var("HEADLINE 1")                        # multiline comment = ' ctrl + / '
var("HEADLINE 2")
var("HEADLINE 3")

var2 = html('h2')
var2("HEADLINE 1 v1")
var2("HEADLINE 1 v2")
var2("HEADLINE 1 v3")
