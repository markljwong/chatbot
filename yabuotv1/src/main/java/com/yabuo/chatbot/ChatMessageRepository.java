package com.yabuo.chatbot;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.elasticsearch.annotations.Query;
import org.springframework.data.elasticsearch.repository.ElasticsearchRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ChatMessageRepository extends ElasticsearchRepository<ChatMessage, String> {
	Page<ChatMessage> findByPhrase(String phrase, Pageable pageable);

	@Query("{\"bool\": {\"must\": [{\"match\": {\"phrase\": \"?0\"}}]}}")
	Page<ChatMessage> findByPhraseUsingCustomQuery(String phrase, Pageable pageable);
}
