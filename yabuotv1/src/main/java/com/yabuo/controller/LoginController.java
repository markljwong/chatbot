package com.yabuo.controller;

import com.yabuo.login.User;
import com.yabuo.login.UserService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;
import java.util.Date;

@RestController
public class LoginController {
	private UserService userService;

	@RequestMapping({"/", "/index"})
	public ModelAndView loginPage() {
		return new ModelAndView("login");
	}

	@RequestMapping(value = "/logout")
	public ModelAndView logout(){
		return new ModelAndView("logout");
	}

	@RequestMapping("/loginCheck")
	public ModelAndView loginCheck(HttpServletRequest request) {
		boolean isValidUser =  userService.hasMatchUser(request.getParameter("userName"),
				request.getParameter("password"));
		if (!isValidUser) {
			return new ModelAndView("login", "error", "Username or Password is wrong.");
		} else {
			User user = userService.findUserByUserName(request.getParameter("userName"));
			user.setLastIp(request.getLocalAddr());
			user.setLastVisit(new Date());
			userService.loginSuccess(user);
			request.getSession().setAttribute("user", user);
			return new ModelAndView("main");
		}
	}

	@Autowired
	public void setUserService(UserService userService) {
		this.userService = userService;
	}
}
