print('Status: 200 OK')
print('Content-type: text/html')
print('')
header = '''<head runat="server">
    <title></title>
    <script language="javascript" type="text/javascript">
// <![CDATA[

        function Button2_onclick() {
            alert(Text1.value);
        }

// ]]>
    </script>
</head>'''
print(header)
print('<h1>This is a header</h1>')
print('<input id="Text1" type="text" />')
button = '''<input id="Button2" type="button" value="button"
        onclick="return Button2_onclick()"/>'''
print(button)
print('<p>note:this is only a test.</p>')
