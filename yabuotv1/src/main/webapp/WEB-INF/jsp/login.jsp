<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<html>
	<head>
		<title>Login</title>
	</head>
	<body>
		<c:if test="${!empty error}">
        	<font color="red"><c:out value="${error}"/></font>
        </c:if>
		<form action="/loginCheck" method="post">
			<fieldset>
				<legend><b>Please log in for access</b></legend>
				<table>
					<tr>
						<td>Username: </td>
						<td><input type="text" name="userName"></td>
					</tr>
					<tr>
						<td>Password:</td>
						<td><input type="password" name="password"></td>
					</tr>
					<tr>
						<td><input type="submit" value="Login" />
						<input type="reset" value="Clear" /></td>
					</tr>
				</table>
			</fieldset>
		</form>
	</body>
</html>
