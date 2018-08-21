package com.yabuo.controller;

import com.yabuo.model.ChatMessage;
import com.yabuo.dao.ChatMessageDao;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/ChatMessages")
public class ChatMessageController {
	private ChatMessageDao chatMessageDao;

	@Autowired
	public ChatMessageController(ChatMessageDao chatMessageDao) {
		this.chatMessageDao = chatMessageDao;
	}

	@PostMapping
	public ChatMessage insertChatMessage(@RequestBody ChatMessage chatMessage) throws Exception {
		return chatMessageDao.insertChatMessage(chatMessage);
	}

	@GetMapping("/{id}")
	public Map<String, Object> getChatMessageById(@PathVariable String id) {
		return chatMessageDao.getChatMessageById(id);
	}

	@PutMapping("/{id}")
	public Map<String, Object> updateChatMessageById(@RequestBody ChatMessage chatMessage, @PathVariable String id) {
		return chatMessageDao.updateChatMessageById(id, chatMessage);
	}

	@DeleteMapping("/{id}")
	public void deleteChatMessageById(@PathVariable String id) {
		chatMessageDao.deleteChatMessageById(id);
	}
}
