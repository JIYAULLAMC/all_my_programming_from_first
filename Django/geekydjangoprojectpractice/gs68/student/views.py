from django.shortcuts import render

# Create your views here.


def setcookie(request):
    response =  render(request, 'student/setcookie.html')   
    data = """    
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body {
            padding: 0px;
            margin: 0px;
            width: 400px;
        }
        .div {
            background-color: aquamarine;
            color:aqua;
            width: 380px;
        }
        h1, h2 {
            color:green
        }

        p {
            color:black

        }
    </style>
</head>
<body>
    <div>
        <h1>this is the cookies </h1>
        <h2>this is your cookies </h2>
        <table>
            <tr>
                <td>name</td>
                <td>
                    <p>
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Id ad iusto hic harum quidem magnam nesciunt nisi minima consequuntur nostrum?
                    </p>
                </td>
            </tr>
            <tr>
                <td>name</td>
                <td>
                    <p>
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Id ad iusto hic harum quidem magnam nesciunt nisi minima consequuntur nostrum?
                    </p>
                </td>
            </tr>
            <tr>
                <td>name</td>
                <td>
                    <p>
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Id ad iusto hic harum quidem magnam nesciunt nisi minima consequuntur nostrum?
                    </p>
                </td>
            </tr>
        </table>
    </div>
</body>
</html>
    """
    response.set_cookie('name', data ,max_age=30)   
    return response


def getcookie(request):
    # name = request.COOKIES['name']
    name = request.COOKIES.get('name', "Guest")
    return render(request, 'student/getcookie.html', {'name':name})


def delcookie(request):
    response = render(request, "student/delcookie.html")
    response.delete_cookie('name')
    return response