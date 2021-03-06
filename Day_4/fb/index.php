<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Facebook - Log In or Sign Up</title>
<link rel="stylesheet" type="text/css" href="style.css">
</head>

<body>
<div id="bodyWrapper">
	<div id="headerWrapper">
    	<div id="title">facebook</div>
        <div id="login">
            <form id="loginForm">
                <table id="loginTable" width="50" border="0" cellspacing="2">
                  <tbody>
                    <tr>
                      <th scope="col" align="left">Email or Phone</th>
                      <th scope="col" align="left">Password</th>
                      <th scope="col">&nbsp;</th>
                    </tr>
                    <tr>
                      <td><input type="text" id="email" name="email"></td>
                      <td><input type="password" id="password" name="password"></td>
                      <td><input type="submit" name="login" value="Log In"></td>
                    </tr>
                    <tr>
                      <td>&nbsp;</td>
                      <td align="left"><a href="">Forgotten Account?</a></td>
                      <td>&nbsp;</td>
                    </tr>
                  </tbody>
                </table>
               </form>
        </div>
    </div>
    <div id="contentWrapper">
    	<div id="leftWrapper">
        	<div id="recentMsgWrapper" class="centerElement">
                <div id="recent_msg">Recent logins</div>
                <div id="recent_Pic" class="centerElement"></div>
                <div id="recent_name" class="centerElement">Mustafa</div>
            </div>
        </div>
        <div id="rightWrapper">
            <div id="signUp">
            	<form id="signUpForm">
                	<table id="signUpTable" width="470" border="0" cellspacing="10">
                      <tbody>
                      <tr>
                          <td colspan="2" id="msg"><b>Create a new account</b></td>
                        </tr>
                        <tr>
                          <td colspan="2">It's free and always will be.</td>
                        </tr>
                        <tr>
                          <td class="names"><input type="text" id="firstname" name="fname" placeholder="First name"></td>
                          <td class="names"><input type="text" id="lastname" name="lname" placeholder="Surname"></td>
                        </tr>
                        <tr>
                          <td colspan="2" class="longText"><input type="text" id="email" name="email" placeholder="Mobile number or email address"></td>
                        </tr>
                        <tr>
                          <td colspan="2" class="longText"><input type="text" id="password" name="password" placeholder="New Password"></td>
                        </tr>
                        <tr>
                          <td><b>Birthday</b></td>
                        </tr>
                        <tr>
                          <td>
                              <select>
                              	<option>Day</option>
                              </select>
                              <select>
                              	<option>Month</option>
                              </select>
                              <select>
                              	<option>Year</option>
                              </select>
                          </td>
                          <td #signUpForm><a href="#">Why do i need to provide my <br>date of birth</a></td>
                        </tr>
                        <tr>
                          <td>
                              <div id="radiobtn">
                              	<input type="radio" name="gender">Female 
                                <input type="radio" name="gender">Male
                              </div>
                          </td>
                          <td>&nbsp;</td>
                        </tr>
                        <tr>
                          <td colspan="2" class="text">By Clicking Sign Up, you agree to our <a href="#">Terms</a> and confirm that you <br> have read our <a href="#">Data Policy</a>, including <a href="#">Cookie Use Policy</a>. You <br> may receive SMS message notification from Facebook and can <br> opt out at any time.</td>
                        </tr>
                        <tr>
                          <td colspan="2"><input type="submit" id="signUp" name="signUp" value="Sign Up"></td>
                        </tr>
                        <tr>
                          <td colspan="2">
                              <div id="horizontal">
                              </div>
                          </td>
                        </tr>
                        <tr>
                          <td colspan="2"><a href="#">Create a Page</a> for a celebrity, band or business</td>
                        </tr>
                      </tbody>
                    </table>
                </form>
            </div>
        </div>
    </div>
                          

    <div id="footerWrapper"></div>
</div>
</body>
</html>