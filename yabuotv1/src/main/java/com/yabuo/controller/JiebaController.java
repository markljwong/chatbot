package com.yabuo.controller;

import com.huaban.analysis.jieba.JiebaSegmenter;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;

@RestController
public class JiebaController {
	JiebaSegmenter segmenter = new JiebaSegmenter();

	@RequestMapping("/jieba")
	public ModelAndView jieba(HttpServletRequest request) {
		if(request.getParameter("mode").equals("Index")) {
			return new ModelAndView("main", "jieba", segmenter.process(request.getParameter("phrase"), JiebaSegmenter.SegMode.INDEX).toString());
		} else {
			return new ModelAndView("main", "jieba", segmenter.process(request.getParameter("phrase"), JiebaSegmenter.SegMode.SEARCH).toString());
		}
	}}
