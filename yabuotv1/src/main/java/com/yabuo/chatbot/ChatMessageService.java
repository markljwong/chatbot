package com.yabuo.chatbot;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;

import java.util.Optional;

public interface ChatMessageService {
	ChatMessage save(ChatMessage chatMessage);

	Optional<ChatMessage> findOne(String id);

	Iterable<ChatMessage> findAll();

	Page<ChatMessage> findByPhrase(String phrase, PageRequest pageRequest);

	Page<ChatMessage> findByPhraseUsingCustomQuery(String phrase, PageRequest pageRequest);

	void delete(ChatMessage chatMessage);
}
