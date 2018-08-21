package com.yabuo.chatbot;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class ChatMessageServiceImpl implements ChatMessageService {
	private final ChatMessageRepository chatMessageRepository;

	@Autowired
	public ChatMessageServiceImpl(ChatMessageRepository chatMessageRepository) {
		this.chatMessageRepository = chatMessageRepository;
	}

	@Override
	public ChatMessage save(ChatMessage chatMessage) {
		return chatMessageRepository.save(chatMessage);
	}

	@Override
	public Optional<ChatMessage> findOne(String id) {
		return chatMessageRepository.findById(id);
	}

	@Override
	public Iterable<ChatMessage> findAll() {
		return chatMessageRepository.findAll();
	}

	@Override
	public Page<ChatMessage> findByPhrase(String phrase, PageRequest pageRequest) {
		return chatMessageRepository.findByPhrase(phrase, pageRequest);
	}

	@Override
	public Page<ChatMessage> findByPhraseUsingCustomQuery(String phrase, PageRequest pageRequest) {
		return chatMessageRepository.findByPhraseUsingCustomQuery(phrase, pageRequest);
	}

	@Override
	public void delete(ChatMessage chatMessage) {
		chatMessageRepository.delete(chatMessage);
	}
}
