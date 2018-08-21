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
    	<div>
        	<h2>Welcome to the test page ${user.userName}. Your current points are:
        	${user.credits}</h2>
       	</div>

       	<div>
       	 	<form action="/logout" method="post">
            	<input type="submit" value="Logout" />
        	</form>
        </div>

        <div>
        	<table>
        		<tr>
					<td><p>This website currently only hosts the Jieba segmenter by user fxsjy
					on Github designed for the Chinese language. This is a java version
					maintained by huaban on Github.</p></td>
				</tr>
				<tr>
					<td><p>There are currently <b>two</b> options</p></td>
				</tr>
				<tr>
					<td>
                		<ul>
							<li><b>Index</b>: Returns all the possible concepts/words
							from a phrase</li>
							<li><b>Search</b>: Attempts to returns only most logical segmentation
							of phrase into concepts/words for a logical sentence</li>
						</ul>
					</td>
				</tr>
			</table>
		</div>
			<i>Input a Chinese phrase below and click Segment to see the output.</i>
			<form action="/jieba" method="post">
				<fieldset>
					<legend>Input Text</legend>
					<textarea name="phrase" rows = "10" cols="100">Enter phrase here</textarea>
					<table>
						<tr>
							<td><input type="radio" name="mode" value="Index" checked></td>
							<td>Index</td>
						</tr>
						<tr>
							<td><input type="radio" name="mode" value="Search"></td>
							<td>Search</td>
						</tr>
					</table>
					<input type="submit" name="Segment">
				</fieldset>
			</form>
        </div>

        <div>
        	<i>Alternatively: Upload a text file and click Segment File. Wait for completion then download file.</i>
         	<form action="/fileUpload" method="post" enctype="multipart/form-data">
         		<fieldset>
         			<legend>Upload file</legend>
         			<table>
         				<tr>
         					<td>File to upload: </td>
         					<td><input type="file" name="file"/></td>
         				</tr>
         				<tr>
         					<td></td>
         					<td><input type="submit" value="Upload"/></td>
         				</tr>
         			</table>
         			<c:if test="${!empty message}">
						<font color="blue"><c:out value="${message}"/></font>
					</c:if>
         		</fieldset>
         	</form>
        </div>

        <div>
        	<i>Past uploaded files:</i>
        	<ul>
        		<c:forEach var="file" items="${files}">
        			<li>"${file}"</li>
        		</c:forEach>
        	</ul>
        </div>

       	<div>
       		<table>
       			<tr>
       				<td><i>Segmented Text</i></td>
       			</tr>
       			<tr>
       				<td>
						<c:if test="${!empty jieba}">
							<font color="green"><c:out value="${jieba}"/></font>
						</c:if>
					</td>
				</tr>
			</table>
        </div>

    </body>
</html>