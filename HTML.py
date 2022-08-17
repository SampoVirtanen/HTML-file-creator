import subprocess
name=input("Input a name: ")
name=(name+".html")
path="C:/Output/" + name
f = open(path, "x")
f.write('''<!doctype html>

<html lang="fi">
<head>
	<meta charset="utf-8">
	<title> </title>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap-theme.min.css">
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>
<body>
 
</body>
</html>''')
f.close
path=path.replace('/', '\\')
subprocess.Popen(r'explorer /select,"'+path+'"')