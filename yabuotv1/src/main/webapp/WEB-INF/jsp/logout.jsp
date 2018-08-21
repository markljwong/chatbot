<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
        <title>Welcome</title>
    </head>
    <body>
        <table>
        	<tr>
        		<td>You have logged out of account: ${user.userName}</td>
        	</tr>
        	<tr>
        		<td>
       				<form action="/index" method="post">
        				<input type="submit" value="Return to Login"/>
        			</form>
        		</td>
        	</tr>
        </table>
    </body>
</html>