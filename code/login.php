<!DOCTYPE html>
<html>
  <head>
    <title>User login/registraton </title>
	<link rel="stylesheet" type="text/css" href="style.css">
	<link rel="stylesheet" type="text/css" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" >
  </head>
  
    <body>
      <div class="container">
	  <div class="login-box">
	    <div class="row">
	     <div class="col-md-6">
		   <h2 style="color:white"> Login here </h2>
		   <form action="validation.php" method="post">
		     <div class="form-group">
			    <label style="color:white">Username</label>
				<input type="text" name="user" class="form-control" required>
			 </div>
			 <div class="form-group">
			    <label style="color:white">Password</label>
				<input type="password" name="password" placeholder="password" class="form-control" required>
			 </div>
			 <button type="submit" class="btn btn-primary">Login </button>
		   </form>
		</div>
		<div class="col-md-6">
		   <h2 style="color:white"> Register here </h2>
		   <form action="registration.php" method="post">
		     <div class="form-group">
			    <label style="color:white">Username</label>
				<input type="text" name="user" class="form-control" required>
			 </div>
			 <div class="form-group">
			    <label style="color:white">Password</label>
				<input type="password" name="password" placeholder="password" class="form-control" required>
			 </div>
			 <div class="form-group">
			    <label style="color:white">Email</label>
				<input type="email" name="email" class="form-control" required>
			 </div>
			 <button type="submit" class="btn btn-primary">Register </button>
		   </form>
		</div>
		</div>
	  </div>
    </body>
</html>